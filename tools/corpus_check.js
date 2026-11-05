// Shared scoring corpus checker (JavaScript implementation).
// Runs every case in tests/corpus.json through site/scoring.js and fails on
// any drift from the expected values. The corpus is the single test fixture
// shared by all scoring implementations (see tools/corpus_check.py for the
// Python engine); CI runs both and blocks release on drift.
//
// Run with: node tools/corpus_check.js   (exit 0 = OK)
"use strict";

const fs = require("fs");
const path = require("path");

const A = require("../site/scoring.js");
const corpus = JSON.parse(
  fs.readFileSync(path.join(__dirname, "..", "tests", "corpus.json"), "utf8")
);

if (corpus.ruleset_version !== A.RULESET_VERSION) {
  console.error(
    `error: corpus targets ruleset ${corpus.ruleset_version} but the engine ` +
      `is ${A.RULESET_VERSION} — update tests/corpus.json with the scoring change`
  );
  process.exit(2);
}

let failures = 0;
for (const c of corpus.cases) {
  const r = A.assess(c.scores, c.current);
  if (r.safeGrantLevel !== c.expect.safe_grant_level) {
    failures++;
    console.error(`FAIL - ${c.name}: safeGrantLevel ${r.safeGrantLevel} != ${c.expect.safe_grant_level}`);
  }
  if (r.recommendedMove !== c.expect.recommended_move) {
    failures++;
    console.error(`FAIL - ${c.name}: recommendedMove ${JSON.stringify(r.recommendedMove)} != ${JSON.stringify(c.expect.recommended_move)}`);
  }
  for (const needle of c.expect.notes_contain || []) {
    if (!r.notes.some((n) => n.includes(needle))) {
      failures++;
      console.error(`FAIL - ${c.name}: no note containing ${JSON.stringify(needle)}`);
    }
  }
}

if (failures) {
  console.error(`corpus (javascript): ${failures} failure(s)`);
  process.exit(1);
}
console.log(`corpus (javascript): ${corpus.cases.length} cases OK against ruleset ${A.RULESET_VERSION}`);
