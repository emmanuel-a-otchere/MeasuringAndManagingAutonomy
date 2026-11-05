/*
 * Measuring & Managing Autonomy — scoring engine (shared by the static site
 * and the Node self-test). Mirrors the rules of docs/maturity-model.md and
 * docs/assessment.md, and tools/autonomy_score.py.
 *
 * Exposes (browser: window.Autonomy; CommonJS: module.exports):
 *   DIMENSIONS, LEVELS, QUESTIONS,
 *   scoreDimension(answers) -> 0..5,
 *   safeLevel(scores) -> 0..5            (weakest-link rule: min D3, D4, D6)
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

  // Index 0 is the Submarine Line: no autonomy at all (v2.0.0 scale).
  var LEVEL_NAMES = ["Submarine Line", "Ask", "Inform-after", "Guardrailed", "Supervised", "Accountable"];
  var WEAKEST_LINK = ["D3", "D4", "D6"];
  var CLEAN_CYCLES_TO_EXPAND = 2;

  // Semantic version of the scoring ruleset (docs/versioning.md).
  // Kept identical to tools/autonomy_score.py; parity asserted by both
  // self-tests. MAJOR = re-scoring; MINOR = additive/clarification; PATCH = no
  // change to scored outputs.
  // 2.0.0: MAJOR re-baseline — definitive levels L1..L5, L0 = Submarine Line.
  var RULESET_VERSION = "2.0.0";

  // Question items per (dimension, level), from docs/assessment.md.
  // A dimension scores at level n if all items for levels <= n are true.
  // L1 items describe the Ask arrangement (analyze and recommend, everything
  // approved); a dimension with none of them true scores 0 — the Submarine
  // Line: no autonomy at all in this dimension.
  var QUESTIONS = {
    D1: {
      1: "The unit knows which decisions it may analyze and recommend here, and that every decision requires approval",
      2: "The unit can produce a list of decisions it currently makes",
      3: "A written inventory names the decision classes, their level and limits, updated in the last quarter",
      4: "Thresholds, exceptions and edge cases are codified and versioned",
      5: "The unit redesigned its own decision inventory in the last two cycles, by negotiation not discovery"
    },
    D2: {
      1: "The unit can produce a sound analysis or recommendation in this domain, even if slowly or with rework",
      2: "Decisions are sound but slow, with heavy reliance on one person",
      3: "Playbooks exist and any member can make a routine decision to the same standard",
      4: "At least one genuine exception was handled without escalation and without harm",
      5: "The unit has taught this domain to another unit or set an org-wide standard"
    },
    D3: {
      1: "Every decision is gated: nothing acts without the grantor's explicit approval",
      2: "There are stated limits at all — even verbal",
      3: "Limits are written and checked (checklist, reviewer, manual gate)",
      4: "Limits are automated (budgets, gates, auto-rollback) and were exercised in the last two quarters",
      5: "The unit designed its own guardrails, monitors them, and stress-tests them"
    },
    D4: {
      1: "The grantor sees each decision as part of approving it",
      2: "A bad decision in this domain would be noticed by someone within a quarter",
      3: "Standard dashboards exist and are reviewed by the unit at a fixed cadence",
      4: "Signals are near-real-time and breach alerts reach the grantor automatically",
      5: "The unit has demonstrated catching and correcting drift before anyone external noticed"
    },
    D5: {
      1: "Each decision is visible to the grantor at approval time",
      2: "The grantor can get a summary of recent decisions on request",
      3: "A decision log stakeholders can find without asking anyone",
      4: "Every consequential decision has a written, linkable rationale",
      5: "An external auditor could reconstruct the decision history and reasoning end-to-end"
    },
    D6: {
      1: "Ownership is explicit at approval: the grantor owns what they approve",
      2: "After the last failure, ownership was assigned to the unit (not deflected)",
      3: "The unit reviews its own outcomes on a fixed cadence; the escalation path is written down",
      4: "The escalation path has been exercised at least once; post-incident learning is routine",
      5: "The unit published a failure analysis that another unit has reused"
    }
  };

  function scoreDimension(code, answers) {
    // answers: {level: bool} for levels 1..5 of this dimension.
    // Score = the highest level whose items for ALL levels <= it are true;
    // 0 (Submarine Line) when even the L1 item is false.
    var level = 0;
    for (var n = 1; n <= 5; n++) {
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
      if (weakest === 0) {
        return "submarine: no autonomy is safe to grant yet — build " +
          "guardrails, telemetry, and accountability before any contract";
      }
      return "formalize: write a contract at the safe level before any change";
    }
    if (current === 0) {
      if (weakest === 0) {
        return "hold at the Submarine Line (L0): no autonomy is safe to " +
          "grant yet; build guardrails, telemetry, and accountability";
      }
      return "formalize: write the first contract at the safe level (L" + weakest + ")";
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
      if (current === 0) {
        notes.push("no formal grant (Submarine Line): nothing has been delegated in this domain");
      }
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
      rulesetVersion: RULESET_VERSION,
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
    RULESET_VERSION: RULESET_VERSION,
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
