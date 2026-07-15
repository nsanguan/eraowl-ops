/**
 * IGColumnDefaults — Enterprise defaults for Interactive Grid columns.
 *
 * Eliminates per-column repetition of the same 4 filter operators
 * for every text column in every grid across every app.
 *
 * Usage:
 *   IGColumnDefaults.filterOperators()  → defaults for text columns
 *   IGColumnDefaults.filterOperators("strict") → contains + equal only
 */

var IGColumnDefaults = (function () {
  "use strict";

  var FILTER_PROFILES = Object.freeze({
    standard: ["contains", "startsWith", "caseInsensitive", "regexp"],
    strict:   ["equal", "contains"],
    numeric:  ["equal", "greaterThan", "lessThan", "between"],
    date:     ["equal", "greaterThan", "lessThan", "between", "isNull"],
    id:       ["equal"]
  });

  /**
   * @param {"standard"|"strict"|"numeric"|"date"|"id"} profile
   * @returns {string[]}
   */
  function filterOperators(profile) {
    return FILTER_PROFILES[profile] || FILTER_PROFILES["standard"];
  }

  return Object.freeze({ filterOperators: filterOperators, FILTER_PROFILES: FILTER_PROFILES });
})();
