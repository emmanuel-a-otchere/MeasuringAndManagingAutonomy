// Self-test for site/scoring.js — mirrors the Python tool's tests.
// Run with: node tools/site_selftest.js  (exit 0 = OK)
"use strict";

const A = require("../site/scoring.js");

let failures = 0;
function check(name, cond) {
  if (cond) { console.log("ok - " + name); }
  else { failures++; console.error("FAIL - " + name); }
}

// scoreDimension: all levels <= n must be true
check("L0 (Submarine Line) when nothing checked",
  A.scoreDimension("D1", {}) === 0);
check("L1 when only the Ask-arrangement item is true",
  A.scoreDimension("D1", { 1: true }) === 1);
check("L3 requires L1..L3 items",
  A.scoreDimension("D1", { 1: true, 2: true, 3: true }) === 3);
check("gap in ladder caps score (L1+L3 true but not L2)",
  A.scoreDimension("D1", { 1: true, 2: false, 3: true }) === 1);
check("all true -> L5",
  A.scoreDimension("D6", { 1: true, 2: true, 3: true, 4: true, 5: true }) === 5);

// weakest-link rule
check("weakest link is min over D3/D4/D6",
  A.safeLevel({ D1: 5, D2: 5, D3: 3, D4: 4, D5: 5, D6: 5 }) === 3);
check("weakest link ignores D1/D2/D5",
  A.safeLevel({ D1: 0, D2: 0, D3: 4, D4: 4, D5: 0, D6: 4 }) === 4);
check("Submarine Line: a zero safety dimension grounds the grant at L0",
  A.safeLevel({ D1: 5, D2: 5, D3: 5, D4: 0, D5: 5, D6: 5 }) === 0);

// worked example (examples/README.md): scores D1..D6 = 2 4 3 3 2 2, no formal grant
const ex = A.assess({ D1: 2, D2: 4, D3: 3, D4: 3, D5: 2, D6: 2 }, null);
check("worked example safe level = 2", ex.safeGrantLevel === 2);
check("worked example move = formalize", ex.recommendedMove.startsWith("formalize"));
check("submarine: all-zero vector grounds at L0",
  A.assess({ D1: 0, D2: 0, D3: 0, D4: 0, D5: 0, D6: 0 }, null).recommendedMove.startsWith("submarine"));

// coaching signal
const coach = A.assess({ D1: 1, D2: 2, D3: 4, D4: 4, D5: 4, D6: 4 }, 4);
check("coaching note fires", coach.notes.some(n => n.includes("coaching")));
check("coaching move = hold and coach", coach.recommendedMove.startsWith("hold and coach"));

// over-grant
const over = A.assess({ D1: 5, D2: 5, D3: 2, D4: 5, D5: 5, D6: 5 }, 4);
check("over-grant note fires", over.notes.some(n => n.includes("over-grant")));
check("over-grant move = contract", over.recommendedMove.startsWith("contract"));

// headroom
const head = A.assess({ D1: 5, D2: 5, D3: 4, D4: 4, D5: 5, D6: 4 }, 3);
check("headroom move = expand", head.recommendedMove.startsWith("expand"));

// hold
const hold = A.assess({ D1: 4, D2: 4, D3: 4, D4: 4, D5: 4, D6: 4 }, 4);
check("stable at level = hold", hold.recommendedMove.startsWith("hold: stable"));

// parity with the Python tool on the worked example
// (python3 tools/autonomy_score.py 2 4 3 3 2 2 -> safe level 2, formalize)

// ruleset versioning (docs/versioning.md): stamp present in every assessment,
// and identical to the Python implementation -- cross-implementation drift is
// a release blocker
check("ruleset version is 2.0.0", A.RULESET_VERSION === "2.0.0");
check("assess() records ruleset version",
  A.assess({ D1: 2, D2: 2, D3: 2, D4: 2, D5: 2, D6: 2 }, 2).rulesetVersion === "2.0.0");
const fs = require("fs");
const py = fs.readFileSync(__dirname + "/../src/measuring_autonomy/score.py", "utf8");
const pyVer = (py.match(/RULESET_VERSION = "([^"]+)"/) || [])[1];
check("version parity with autonomy_score.py",
  pyVer !== undefined && pyVer === A.RULESET_VERSION);

check("question set covers all six dimensions with L1..L5 items",
  Object.keys(A.QUESTIONS).length === 6 &&
  A.DIMENSIONS.every(d => A.QUESTIONS[d.code] &&
    Object.keys(A.QUESTIONS[d.code]).length === 5 &&
    [1, 2, 3, 4, 5].every(l => A.QUESTIONS[d.code][l])));

if (failures) {
  console.error(failures + " failure(s)");
  process.exit(1);
}
console.log("self-test: OK");
