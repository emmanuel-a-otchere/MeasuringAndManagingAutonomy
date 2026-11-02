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
check("L0 when nothing checked",
  A.scoreDimension("D1", {}) === 0);
check("L2 requires L1 and L2 items",
  A.scoreDimension("D1", { 1: true, 2: true }) === 2);
check("gap in ladder caps score (L1+L3 true but not L2)",
  A.scoreDimension("D1", { 1: true, 2: false, 3: true }) === 1);
check("all true -> L4",
  A.scoreDimension("D6", { 1: true, 2: true, 3: true, 4: true }) === 4);

// weakest-link rule
check("weakest link is min over D3/D4/D6",
  A.safeLevel({ D1: 4, D2: 4, D3: 2, D4: 3, D5: 4, D6: 4 }) === 2);
check("weakest link ignores D1/D2/D5",
  A.safeLevel({ D1: 0, D2: 0, D3: 3, D4: 3, D5: 0, D6: 3 }) === 3);

// worked example (examples/README.md): scores D1..D6 = 1 3 2 2 1 1, no formal grant
const ex = A.assess({ D1: 1, D2: 3, D3: 2, D4: 2, D5: 1, D6: 1 }, null);
check("worked example safe level = 1", ex.safeGrantLevel === 1);
check("worked example move = formalize", ex.recommendedMove.startsWith("formalize"));

// coaching signal
const coach = A.assess({ D1: 0, D2: 1, D3: 3, D4: 3, D5: 3, D6: 3 }, 3);
check("coaching note fires", coach.notes.some(n => n.includes("coaching")));
check("coaching move = hold and coach", coach.recommendedMove.startsWith("hold and coach"));

// over-grant
const over = A.assess({ D1: 4, D2: 4, D3: 1, D4: 4, D5: 4, D6: 4 }, 3);
check("over-grant note fires", over.notes.some(n => n.includes("over-grant")));
check("over-grant move = contract", over.recommendedMove.startsWith("contract"));

// headroom
const head = A.assess({ D1: 4, D2: 4, D3: 3, D4: 3, D5: 4, D6: 3 }, 2);
check("headroom move = expand", head.recommendedMove.startsWith("expand"));

// hold
const hold = A.assess({ D1: 3, D2: 3, D3: 3, D4: 3, D5: 3, D6: 3 }, 3);
check("stable at level = hold", hold.recommendedMove.startsWith("hold: stable"));

// parity with the Python tool on the worked example
// (python3 tools/autonomy_score.py 1 3 2 2 1 1 -> safe level 1, formalize)

// ruleset versioning (docs/versioning.md): stamp present in every assessment,
// and identical to the Python implementation -- cross-implementation drift is
// a release blocker
check("ruleset version is 1.0.0", A.RULESET_VERSION === "1.0.0");
check("assess() records ruleset version",
  A.assess({ D1: 1, D2: 1, D3: 1, D4: 1, D5: 1, D6: 1 }, 1).rulesetVersion === "1.0.0");
const fs = require("fs");
const py = fs.readFileSync(__dirname + "/../tools/autonomy_score.py", "utf8");
const pyVer = (py.match(/RULESET_VERSION = "([^"]+)"/) || [])[1];
check("version parity with autonomy_score.py",
  pyVer !== undefined && pyVer === A.RULESET_VERSION);

check("question set covers all six dimensions",
  Object.keys(A.QUESTIONS).length === 6 &&
  A.DIMENSIONS.every(d => A.QUESTIONS[d.code] &&
    Object.keys(A.QUESTIONS[d.code]).length === 4));

if (failures) {
  console.error(failures + " failure(s)");
  process.exit(1);
}
console.log("self-test: OK");
