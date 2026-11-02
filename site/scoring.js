/*
 * Measuring & Managing Autonomy — scoring engine (shared by the static site
 * and the Node self-test). Mirrors the rules of docs/maturity-model.md and
 * docs/assessment.md, and tools/autonomy_score.py.
 *
 * Exposes (browser: window.Autonomy; CommonJS: module.exports):
 *   DIMENSIONS, LEVELS, QUESTIONS,
 *   scoreDimension(answers) -> 0..4,
 *   safeLevel(scores) -> 0..4            (weakest-link rule: min D3, D4, D6)
 *   gapNotes(scores, current) -> [string]
 *   recommendedMove(scores, current) -> string
 *   assess(scores, current) -> object
 */
(function (global) {
  "use strict";

  var DIMENSIONS = [
    { code: "D1", name: "decision clarity" },
    { code: "D2", name: "capability" },
    { code: "D3", name: "guardrails" },
    { code: "D4", name: "telemetry" },
    { code: "D5", name: "transparency" },
    { code: "D6", name: "accountability" }
  ];

  var LEVEL_NAMES = ["Ask", "Inform-after", "Guardrailed", "Supervised", "Accountable"];
  var WEAKEST_LINK = ["D3", "D4", "D6"];
  var CLEAN_CYCLES_TO_EXPAND = 2;

  // Question items per (dimension, level), from docs/assessment.md.
  // A dimension scores at level n if all items for levels <= n are true.
  var QUESTIONS = {
    D1: {
      1: "The unit can produce a list of decisions it currently makes",
      2: "A written inventory names the decision classes, their level and limits, updated in the last quarter",
      3: "Thresholds, exceptions and edge cases are codified and versioned",
      4: "The unit redesigned its own decision inventory in the last two cycles, by negotiation not discovery"
    },
    D2: {
      1: "No materially wrong or reversed decisions in this domain last quarter",
      2: "Playbooks exist and any member can make a routine decision to the same standard",
      3: "At least one genuine exception was handled without escalation and without harm",
      4: "The unit has taught this domain to another unit or set an org-wide standard"
    },
    D3: {
      1: "There are stated limits at all — even verbal",
      2: "Limits are written and checked (checklist, reviewer, manual gate)",
      3: "Limits are automated (budgets, gates, auto-rollback) and were exercised in the last two quarters",
      4: "The unit designed its own guardrails, monitors them, and stress-tests them"
    },
    D4: {
      1: "A bad decision in this domain would be noticed by someone within a quarter",
      2: "Standard dashboards exist and are reviewed by the unit at a fixed cadence",
      3: "Signals are near-real-time and breach alerts reach the grantor automatically",
      4: "The unit has demonstrated catching and correcting drift before anyone external noticed"
    },
    D5: {
      1: "The grantor can get a summary of recent decisions on request",
      2: "A decision log stakeholders can find without asking anyone",
      3: "Every consequential decision has a written, linkable rationale",
      4: "An external auditor could reconstruct the decision history and reasoning end-to-end"
    },
    D6: {
      1: "After the last failure, ownership was assigned to the unit (not deflected)",
      2: "The unit reviews its own outcomes on a fixed cadence; the escalation path is written down",
      3: "The escalation path has been exercised at least once; post-incident learning is routine",
      4: "The unit published a failure analysis that another unit has reused"
    }
  };

  function scoreDimension(code, answers) {
    // answers: {level: bool} for levels 1..4 of this dimension.
    // Score = the highest level whose items for ALL levels <= it are true.
    var level = 0;
    for (var n = 1; n <= 4; n++) {
      var allTrue = true;
      for (var k = 1; k <= n; k++) {
        if (!answers[k]) { allTrue = false; break; }
      }
      if (allTrue) { level = n; }
    }
    return level;
  }

  function safeLevel(scores) {
    return Math.min.apply(null, WEAKEST_LINK.map(function (d) { return scores[d]; }));
  }

  function recommendedMove(scores, current) {
    var weakest = safeLevel(scores);
    if (current === null || current === undefined) {
      return "formalize: write a contract at the safe level before any change";
    }
    if (weakest < current) {
      return "contract or re-shape: safety dimensions lag the grant";
    }
    if (weakest > current) {
      return "expand (after " + CLEAN_CYCLES_TO_EXPAND +
        " clean cycles): raise one level or widen scope in the strongest dimension";
    }
    if (Math.min(scores.D1, scores.D2) < weakest) {
      return "hold and coach: capability/clarity lag; keep the grant";
    }
    return "hold: stable at the current level; re-review next horizon";
  }

  function gapNotes(scores, current) {
    var notes = [];
    var weakest = safeLevel(scores);
    var coaching = ["D1", "D2"].filter(function (d) { return scores[d] < weakest; });
    if (coaching.length) {
      notes.push("coaching signal: " + coaching.join(", ") +
        " below the safety floor — invest in clarity/capability; do not revoke for this");
    }
    if (current !== null && current !== undefined) {
      var headroom = safeLevel(scores) - current;
      if (headroom > 0) {
        notes.push("headroom: safe level exceeds granted level by " + headroom +
          "; expand after " + CLEAN_CYCLES_TO_EXPAND + " clean review cycles");
      } else if (headroom < 0) {
        notes.push("over-grant: granted level exceeds safe level by " + (-headroom) +
          "; fix guardrails/telemetry/accountability or step down");
      } else {
        notes.push("granted level matches safe level: hold and review");
      }
    }
    return notes;
  }

  function assess(scores, current) {
    return {
      scores: scores,
      safeGrantLevel: safeLevel(scores),
      grantedLevel: current === undefined ? null : current,
      notes: gapNotes(scores, current),
      recommendedMove: recommendedMove(scores, current)
    };
  }

  var api = {
    DIMENSIONS: DIMENSIONS,
    LEVEL_NAMES: LEVEL_NAMES,
    WEAKEST_LINK: WEAKEST_LINK,
    QUESTIONS: QUESTIONS,
    scoreDimension: scoreDimension,
    safeLevel: safeLevel,
    gapNotes: gapNotes,
    recommendedMove: recommendedMove,
    assess: assess
  };

  if (typeof module !== "undefined" && module.exports) {
    module.exports = api;
  } else {
    global.Autonomy = api;
  }
})(typeof window !== "undefined" ? window : this);
