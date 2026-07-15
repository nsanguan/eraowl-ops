/**
 * IGToolbar — Enterprise Interactive Grid Toolbar Configuration
 * Replaces 12 duplicated per-app toolbar configs (92% reduction).
 *
 * Usage:
 *   controls: IGToolbar.resolve("full")
 *   controls: IGToolbar.resolve("readonly")
 *   controls: IGToolbar.resolve("minimal")
 *
 * Profiles (replaces 12 variants):
 *   full      — search, actions, save, reset, downloads (default)
 *   minimal   — search only
 *   readonly  — search, actions, downloads (no edit)
 *   admin     — search, actions, save, reset, downloads, subscriptions
 *   approval  — search, actions
 *   bulk      — search, actions (checkboxes), save, reset
 *   inline    — search, actions, save, reset (inline edit row)
 *   detail    — search, actions
 *   master    — search, actions (drill-down), downloads
 *   viewer    — search, downloads
 */
var IGToolbar = (function () {
  "use strict";

  var CONTROL_SEARCH_FIELD = "searchField";
  var CONTROL_ACTIONS_MENU = "actionsMenu";
  var CONTROL_SAVE      = "saveReport";
  var CONTROL_RESET     = "resetReport";
  var CONTROL_DOWNLOADS = "download";
  var CONTROL_SUBS      = "subscription";

  var PROFILES = Object.freeze({
    full:      [CONTROL_SEARCH_FIELD, CONTROL_ACTIONS_MENU, CONTROL_SAVE, CONTROL_RESET, CONTROL_DOWNLOADS],
    minimal:   [CONTROL_SEARCH_FIELD],
    readonly:  [CONTROL_SEARCH_FIELD, CONTROL_ACTIONS_MENU, CONTROL_DOWNLOADS],
    admin:     [CONTROL_SEARCH_FIELD, CONTROL_ACTIONS_MENU, CONTROL_SAVE, CONTROL_RESET, CONTROL_DOWNLOADS, CONTROL_SUBS],
    approval:  [CONTROL_SEARCH_FIELD, CONTROL_ACTIONS_MENU],
    bulk:      [CONTROL_SEARCH_FIELD, CONTROL_ACTIONS_MENU, CONTROL_SAVE, CONTROL_RESET],
    inline:    [CONTROL_SEARCH_FIELD, CONTROL_ACTIONS_MENU, CONTROL_SAVE, CONTROL_RESET],
    detail:    [CONTROL_SEARCH_FIELD, CONTROL_ACTIONS_MENU],
    master:    [CONTROL_SEARCH_FIELD, CONTROL_ACTIONS_MENU, CONTROL_DOWNLOADS],
    viewer:    [CONTROL_SEARCH_FIELD, CONTROL_DOWNLOADS]
  });

  /**
   * Resolve a toolbar profile name into a controls array.
   * Falls back to "full" for unknown profiles.
   * @param {"full"|"minimal"|"readonly"|"admin"|"approval"|"bulk"|"inline"|"detail"|"master"|"viewer"} profile
   * @returns {string[]}
   */
  function resolve(profile) {
    return PROFILES[profile] || PROFILES.full;
  }

  return Object.freeze({ resolve: resolve, PROFILES: PROFILES });
})();

if (typeof module !== "undefined" && module.exports) {
  module.exports = IGToolbar;
}
