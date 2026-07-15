/**
 * eops-ig — Enterprise Interactive Grid JavaScript Utilities
 * Version: 2.0
 * Dependencies: apex (APEX JS API), eods (global design system)
 * Zero jQuery. ES2020+. CSP-safe.
 *
 * Usage (ES module):
 *   import { IGController, IGColumnFormatter, IGExportHelper,
 *            IGRowHighlight, IGKeyboardNav, IGMasterDetail } from "./eops-ig.js";
 *
 *   const ig = new IGController("employees_grid");
 *   ig.refresh();
 *   ig.getSelectedRows();
 */

(function () {
  "use strict";

  /**
   * Safely resolve an APEX region's interactiveGrid widget.
   * @param {string} staticId
   * @returns {object|null}
   */
  function _getIgWidget(staticId) {
    if (typeof apex === "undefined" || !apex.region) {
      console.warn("[eops-ig] APEX JS API not available");
      return null;
    }
    var region = apex.region(staticId);
    if (!region || !region.widget) {
      console.warn("[eops-ig] Region not found or no widget: " + staticId);
      return null;
    }
    try {
      var widget = region.widget();
      return widget.interactiveGrid ? widget : null;
    } catch (e) {
      console.error("[eops-ig] Error accessing widget for " + staticId, e);
      return null;
    }
  }

  /**
   * Safely get the grid view model from a widget.
   * @param {object} widget — APEX Interactive Grid widget
   * @returns {{view: object, model: object}|null}
   */
  function _getViewModel(widget) {
    try {
      var view = widget.interactiveGrid("getViews", "grid");
      if (!view) return null;
      return { view: view, model: view.model };
    } catch (e) {
      console.error("[eops-ig] Error getting view model", e);
      return null;
    }
  }

  /**
   * Wrap a value in a Promise if it is not already thenable.
   * @param {*} val
   * @returns {Promise}
   */
  function _toPromise(val) {
    if (val && typeof val.then === "function") return val;
    return Promise.resolve(val);
  }

  // ==========================================================================
  // Module 1: IGController
  // ==========================================================================

  /**
   * Primary controller for an Interactive Grid instance.
   */
  function IGController(staticId) {
    this.staticId = staticId;
    this._rowSelectCallbacks = [];
    this._highlightRules = [];
  }

  /**
   * Get the underlying APEX Interactive Grid widget.
   * @returns {object|null}
   */
  IGController.prototype.getWidget = function () {
    return _getIgWidget(this.staticId);
  };

  /**
   * Get the grid view and model.
   * @returns {{view: object, model: object}|null}
   */
  IGController.prototype.getViewModel = function () {
    var widget = this.getWidget();
    if (!widget) return null;
    return _getViewModel(widget);
  };

  /**
   * Refresh the Interactive Grid.
   * @returns {Promise<void>}
   */
  IGController.prototype.refresh = function () {
    var widget = this.getWidget();
    if (!widget) return Promise.resolve();
    try {
      widget.interactiveGrid("getActions").invoke("refresh");
      return Promise.resolve();
    } catch (e) {
      console.error("[eops-ig] Error refreshing " + this.staticId, e);
      return Promise.reject(e);
    }
  };

  /**
   * Get all selected rows as plain objects.
   * @returns {object[]}
   */
  IGController.prototype.getSelectedRows = function () {
    var vm = this.getViewModel();
    if (!vm) return [];

    try {
      var selectedRecords = vm.view.getSelectedRecords();
      if (!selectedRecords || selectedRecords.length === 0) return [];

      var model = vm.model;
      var results = [];
      var fields = null;

      for (var i = 0; i < selectedRecords.length; i++) {
        var rec = selectedRecords[i];
        if (fields === null) {
          fields = model.getRecordFields(rec);
        }
        var row = {};
        for (var j = 0; j < fields.length; j++) {
          row[fields[j]] = model.getValue(rec, fields[j]);
        }
        results.push(row);
      }
      return results;
    } catch (e) {
      console.error("[eops-ig] Error getting selected rows for " + this.staticId, e);
      return [];
    }
  };

  /**
   * Get all rows (visible in grid view) as plain objects.
   * @returns {object[]}
   */
  IGController.prototype.getAllRows = function () {
    var vm = this.getViewModel();
    if (!vm) return [];

    try {
      var totalRecords = vm.model.getRecordCount();
      if (!totalRecords) return [];

      var results = [];
      var fields = null;

      for (var i = 0; i < totalRecords; i++) {
        var rec = vm.view.getRecordByIndex(i);
        if (!rec) continue;
        if (fields === null) {
          fields = vm.model.getRecordFields(rec);
        }
        var row = {};
        for (var j = 0; j < fields.length; j++) {
          row[fields[j]] = vm.model.getValue(rec, fields[j]);
        }
        results.push(row);
      }
      return results;
    } catch (e) {
      console.error("[eops-ig] Error getting all rows for " + this.staticId, e);
      return [];
    }
  };

  /**
   * Get a single cell value by record ID and column name.
   * @param {string} recordId
   * @param {string} columnName
   * @returns {*}
   */
  IGController.prototype.getCellValue = function (recordId, columnName) {
    var vm = this.getViewModel();
    if (!vm) return null;

    try {
      var rec = vm.model.getRecord(recordId);
      if (!rec) return null;
      return vm.model.getValue(rec, columnName);
    } catch (e) {
      console.error("[eops-ig] Error getting cell value for " + this.staticId, e);
      return null;
    }
  };

  /**
   * Set a single cell value by record ID and column name.
   * @param {string} recordId
   * @param {string} columnName
   * @param {*} value
   */
  IGController.prototype.setCellValue = function (recordId, columnName, value) {
    var vm = this.getViewModel();
    if (!vm) return;

    try {
      var rec = vm.model.getRecord(recordId);
      if (!rec) return;
      vm.model.setValue(rec, columnName, value);
    } catch (e) {
      console.error("[eops-ig] Error setting cell value for " + this.staticId, e);
    }
  };

  /**
   * Add a new empty row to an editable grid.
   * @param {object|undefined} defaultValues — optional default values keyed by column name
   */
  IGController.prototype.addRow = function (defaultValues) {
    var widget = this.getWidget();
    if (!widget) return;

    try {
      widget.interactiveGrid("getActions").invoke("selection-add-row");

      if (defaultValues && typeof defaultValues === "object") {
        var vm = _getViewModel(widget);
        if (vm) {
          var totalRecords = vm.model.getRecordCount();
          if (totalRecords > 0) {
            var newRec = vm.model.getRecord(totalRecords - 1);
            if (newRec) {
              var keys = Object.keys(defaultValues);
              for (var i = 0; i < keys.length; i++) {
                try {
                  vm.model.setValue(newRec, keys[i], defaultValues[keys[i]]);
                } catch (e) {
                  console.warn("[eops-ig] Could not set default for column " + keys[i], e);
                }
              }
            }
          }
        }
      }
    } catch (e) {
      console.error("[eops-ig] Error adding row to " + this.staticId, e);
    }
  };

  /**
   * Delete the currently selected rows from an editable grid.
   */
  IGController.prototype.deleteSelectedRows = function () {
    var widget = this.getWidget();
    if (!widget) return;

    try {
      widget.interactiveGrid("getActions").invoke("selection-delete");
    } catch (e) {
      console.error("[eops-ig] Error deleting rows from " + this.staticId, e);
    }
  };

  /**
   * Save all pending changes in an editable grid.
   * @returns {Promise<void>}
   */
  IGController.prototype.saveAll = function () {
    var widget = this.getWidget();
    if (!widget) return Promise.resolve();

    try {
      widget.interactiveGrid("getActions").invoke("save");
      return Promise.resolve();
    } catch (e) {
      console.error("[eops-ig] Error saving " + this.staticId, e);
      return Promise.reject(e);
    }
  };

  /**
   * Set a filter on a column programmatically.
   * @param {string} columnName
   * @param {*} value
   * @param {string} operator — e.g. "EQ", "GT", "LT", "CONTAINS" (default "EQ")
   */
  IGController.prototype.setFilter = function (columnName, value, operator) {
    operator = operator || "EQ";
    var vm = this.getViewModel();
    if (!vm) return;

    try {
      vm.model.getFilters().add(columnName, value, operator);
    } catch (e) {
      console.error("[eops-ig] Error setting filter on " + this.staticId + "." + columnName, e);
    }
  };

  /**
   * Clear all filters on the grid.
   */
  IGController.prototype.clearFilters = function () {
    var vm = this.getViewModel();
    if (!vm) return;

    try {
      vm.model.getFilters().clear();
    } catch (e) {
      console.error("[eops-ig] Error clearing filters for " + this.staticId, e);
    }
  };

  /**
   * Register a callback for row selection changes.
   * @param {function} callback — receives the selected row object
   */
  IGController.prototype.onRowSelect = function (callback) {
    if (typeof callback !== "function") return;
    this._rowSelectCallbacks.push(callback);
  };

  /**
   * Manually fire row-select callbacks (e.g., from a dynamic action).
   * Called by the initJavaScriptFunction when row selection changes.
   */
  IGController.prototype._fireRowSelect = function () {
    var selected = this.getSelectedRows();
    if (selected.length === 0) return;

    var row = selected[0];
    for (var i = 0; i < this._rowSelectCallbacks.length; i++) {
      try {
        this._rowSelectCallbacks[i](row, selected);
      } catch (e) {
        console.error("[eops-ig] Error in row-select callback", e);
      }
    }
  };

  /**
   * Apply conditional highlighting rules to the grid.
   * @param {Array<{column: string, operator: string, value: *, className: string}>} rules
   *
   * Supported operators: "=", "!=", ">", "<", ">=", "<=", "contains", "startsWith", "isNull", "isNotNull"
   */
  IGController.prototype.applyHighlight = function (rules) {
    this._highlightRules = rules || [];

    try {
      var widget = this.getWidget();
      if (!widget) return;

      var gridEl = widget[0] || widget;
      var container;
      if (gridEl && gridEl.nodeType) {
        container = gridEl;
      } else {
        container = document.getElementById(this.staticId);
      }
      if (!container) return;

      this._walkGridRows(container, this._highlightRules);
    } catch (e) {
      console.error("[eops-ig] Error applying highlight for " + this.staticId, e);
    }
  };

  /**
   * Walk the grid DOM and apply highlight classes to matching cells/rows.
   * @param {HTMLElement} container
   * @param {Array} rules
   */
  IGController.prototype._walkGridRows = function (container, rules) {
    var self = this;
    if (!rules || rules.length === 0) return;

    var vm = this.getViewModel();
    if (!vm) return;

    var model = vm.model;
    var totalRecords = model.getRecordCount();
    if (!totalRecords) return;

    var cells = container.querySelectorAll(".eops-ig--cell, td[headers], .a-GV-cell");

    for (var c = 0; c < cells.length; c++) {
      var cell = cells[c];
      var headers = cell.getAttribute("headers");
      if (!headers) continue;

      var rowIndex = self._getRowIndex(cell);
      if (rowIndex === null || rowIndex >= totalRecords) continue;

      try {
        var rec = model.getRecord(rowIndex);
        if (!rec) continue;

        for (var r = 0; r < rules.length; r++) {
          var rule = rules[r];
          var cellValue = model.getValue(rec, rule.column);
          if (self._evalRule(cellValue, rule)) {
            cell.classList.add(rule.className);
          }
        }
      } catch (e) {
        // skip individual cell errors
      }
    }
  };

  /**
   * Evaluate a single highlighting rule against a value.
   * @param {*} cellValue
   * @param {{operator: string, value: *, className: string}} rule
   * @returns {boolean}
   */
  IGController.prototype._evalRule = function (cellValue, rule) {
    var val = rule.value;
    var op = (rule.operator || "=").toString();

    switch (op) {
      case "=":
      case "==":
      case "equal":
        return String(cellValue) === String(val);
      case "!=":
      case "notEqual":
        return String(cellValue) !== String(val);
      case ">":
      case "greaterThan":
        return Number(cellValue) > Number(val);
      case "<":
      case "lessThan":
        return Number(cellValue) < Number(val);
      case ">=":
      case "greaterThanOrEqual":
        return Number(cellValue) >= Number(val);
      case "<=":
      case "lessThanOrEqual":
        return Number(cellValue) <= Number(val);
      case "contains":
        return String(cellValue).toLowerCase().indexOf(String(val).toLowerCase()) !== -1;
      case "startsWith":
        return String(cellValue).toLowerCase().indexOf(String(val).toLowerCase()) === 0;
      case "isNull":
        return cellValue === null || cellValue === undefined || cellValue === "";
      case "isNotNull":
        return cellValue !== null && cellValue !== undefined && cellValue !== "";
      default:
        return false;
    }
  };

  /**
   * Attempt to derive row index from a cell DOM element.
   * @param {HTMLElement} cell
   * @returns {number|null}
   */
  IGController.prototype._getRowIndex = function (cell) {
    var tr = cell.closest("tr, .eops-ig--body-row, [role='row']");
    if (!tr) return null;

    var idxAttr = tr.getAttribute("data-row-index") || tr.getAttribute("data-idx");
    if (idxAttr !== null) return parseInt(idxAttr, 10);

    var parent = tr.parentNode;
    if (!parent) return null;
    var rows = parent.querySelectorAll("tr, .eops-ig--body-row, [role='row']");
    for (var i = 0; i < rows.length; i++) {
      if (rows[i] === tr) return i;
    }
    return null;
  };

  /**
   * Programmatically trigger an export.
   * @param {string} format — "csv", "excel", "pdf"
   */
  IGController.prototype.exportData = function (format) {
    format = format || "csv";
    var widget = this.getWidget();
    if (!widget) return;

    try {
      widget.interactiveGrid("getActions").invoke("download", { format: format });
    } catch (e) {
      console.error("[eops-ig] Error exporting " + this.staticId + " as " + format, e);
    }
  };

  /**
   * Export grid data as CSV with a custom filename.
   * Uses APEX download action with a filename hint.
   * @param {{filename: string}} options
   */
  IGController.prototype.exportCSV = function (options) {
    options = options || {};
    var widget = this.getWidget();
    if (!widget) return;

    try {
      var config = { format: "csv" };
      if (options.filename) {
        config.filename = options.filename;
      }
      widget.interactiveGrid("getActions").invoke("download", config);
    } catch (e) {
      console.error("[eops-ig] Error exporting CSV for " + this.staticId, e);
    }
  };

  // ==========================================================================
  // Module 2: IGColumnFormatter
  // ==========================================================================

  var IGColumnFormatter = {
    /**
     * Format a numeric value as localized currency.
     * @param {number|string} value
     * @param {{locale: string, currency: string, decimals: number}} options
     * @returns {string}
     */
    currency: function (value, options) {
      options = options || {};
      var locale = options.locale || "en-US";
      var currency = options.currency || "USD";
      var decimals = options.decimals !== undefined ? options.decimals : 2;

      var num = typeof value === "string" ? parseFloat(value) : value;
      if (isNaN(num)) return "";

      try {
        return new Intl.NumberFormat(locale, {
          style: "currency",
          currency: currency,
          minimumFractionDigits: decimals,
          maximumFractionDigits: decimals
        }).format(num);
      } catch (e) {
        return currency + " " + num.toFixed(decimals);
      }
    },

    /**
     * Format a date value using the global date helper or locale string.
     * @param {Date|string} value
     * @param {{locale: string, format: string}} options
     * @returns {string}
     */
    date: function (value, options) {
      options = options || {};
      var locale = options.locale || "en-US";
      var format = options.format || "shortDate";

      if (value === null || value === undefined || value === "") return "";

      var d = value instanceof Date ? value : new Date(value);
      if (isNaN(d.getTime())) return "";

      if (typeof eods !== "undefined" && eods.date) {
        return eods.date.format(d, format);
      }

      try {
        var opts = {};
        if (format === "shortDate") {
          opts = { year: "numeric", month: "2-digit", day: "2-digit" };
        } else if (format === "longDate") {
          opts = { year: "numeric", month: "long", day: "numeric" };
        } else if (format === "dateTime") {
          opts = { year: "numeric", month: "2-digit", day: "2-digit",
                   hour: "2-digit", minute: "2-digit" };
        }
        return d.toLocaleDateString(locale, opts);
      } catch (e) {
        return d.toISOString().split("T")[0];
      }
    },

    /**
     * Format a value as a percentage.
     * @param {number} value — e.g. 0.25 for 25%
     * @param {number} decimals
     * @returns {string}
     */
    percentage: function (value, decimals) {
      decimals = decimals !== undefined ? decimals : 1;
      var num = typeof value === "string" ? parseFloat(value) : value;
      if (isNaN(num)) return "";
      return (num * 100).toFixed(decimals) + "%";
    },

    /**
     * Format a value as a status badge with inline CSS classes.
     * @param {string} value — status text
     * @param {{approved: string, pending: string, rejected: string, default: string}} mappings
     * @returns {string} — HTML string
     */
    statusBadge: function (value, mappings) {
      mappings = mappings || {};
      if (value === null || value === undefined) {
        value = "";
      }

      var normalized = String(value).toLowerCase().trim();
      var display = String(value);
      var badgeClass = "eops-ig--highlight-info";

      if (normalized === "approved" || normalized === "complete" || normalized === "active") {
        badgeClass = "eops-ig--highlight-success";
        display = mappings.approved || display;
      } else if (normalized === "pending" || normalized === "in progress" || normalized === "review") {
        badgeClass = "eops-ig--highlight-warning";
        display = mappings.pending || display;
      } else if (normalized === "rejected" || normalized === "cancelled" || normalized === "inactive") {
        badgeClass = "eops-ig--highlight-danger";
        display = mappings.rejected || display;
      }

      return '<span class="' + badgeClass + '">' + display + '</span>';
    }
  };

  // ==========================================================================
  // Module 3: IGExportHelper
  // ==========================================================================

  var IGExportHelper = {
    /**
     * Trigger a download on an IG.
     * @param {string} staticId
     * @param {string} format — "csv", "excel", "pdf"
     */
    triggerDownload: function (staticId, format) {
      format = format || "csv";
      var widget = _getIgWidget(staticId);
      if (!widget) return;

      try {
        widget.interactiveGrid("getActions").invoke("download", { format: format });
      } catch (e) {
        console.error("[eops-ig] Download failed for " + staticId, e);
      }
    },

    /**
     * Generate a filename from a grid name and current date.
     * @param {string} gridName — human-readable grid name
     * @param {string} format — file extension
     * @returns {string}
     */
    generateFilename: function (gridName, format) {
      var now = new Date();
      var datePart = now.getFullYear() +
        String(now.getMonth() + 1).padStart(2, "0") +
        String(now.getDate()).padStart(2, "0") + "_" +
        String(now.getHours()).padStart(2, "0") +
        String(now.getMinutes()).padStart(2, "0") +
        String(now.getSeconds()).padStart(2, "0");

      var safe = (gridName || "export")
        .replace(/[^a-zA-Z0-9_-]/g, "_")
        .replace(/_+/g, "_")
        .replace(/^_|_$/g, "")
        .toLowerCase();

      return safe + "_" + datePart + "." + (format || "csv");
    }
  };

  // ==========================================================================
  // Module 4: IGRowHighlight
  // ==========================================================================

  var IGRowHighlight = {
    /**
     * Apply declarative highlight rules to an IG by static ID.
     * @param {string} staticId
     * @param {Array<{column: string, operator: string, value: *, className: string, rowLevel: boolean}>} rules
     *
     * Each rule specifies:
     *   column    — column name to evaluate
     *   operator  — "=", "!=", ">", "<", ">=", "<=", "contains", "startsWith", "isNull", "isNotNull"
     *   value     — threshold value
     *   className — CSS class to apply (e.g. "eops-ig--highlight-danger")
     *   rowLevel  — if true, applies the class to the entire row instead of the cell
     */
    apply: function (staticId, rules) {
      if (!rules || !rules.length) return;

      var widget = _getIgWidget(staticId);
      if (!widget) return;

      var vm = _getViewModel(widget);
      if (!vm) return;

      var model = vm.model;
      var totalRecords = model.getRecordCount();
      if (!totalRecords) return;

      var container = widget[0] || widget;
      if (!container || !container.nodeType) {
        container = document.getElementById(staticId);
      }
      if (!container) return;

      var self = this;

      var cells = container.querySelectorAll(
        ".eops-ig--cell, " +
        "td[headers], " +
        ".a-GV-cell, " +
        "[role='gridcell']"
      );

      for (var c = 0; c < cells.length; c++) {
        var cell = cells[c];
        var rowIndex = self._resolveRowIndex(cell);
        if (rowIndex === null || rowIndex >= totalRecords) continue;

        try {
          var rec = model.getRecord(rowIndex);
          if (!rec) continue;

          for (var r = 0; r < rules.length; r++) {
            var rule = rules[r];

            if (rule.column) {
              var cellValue = model.getValue(rec, rule.column);
              if (!self._evaluate(cellValue, rule)) continue;
            }

            if (rule.rowLevel) {
              var row = cell.closest("tr, .eops-ig--body-row, [role='row']");
              if (row) {
                row.classList.add(rule.className);
              }
            } else {
              cell.classList.add(rule.className);
            }
          }
        } catch (e) {
          // skip individual row/cell errors
        }
      }
    },

    /**
     * Clear all highlight classes from a grid.
     * @param {string} staticId
     */
    clear: function (staticId) {
      var widget = _getIgWidget(staticId);
      if (!widget) return;

      var container = widget[0] || widget;
      if (!container || !container.nodeType) {
        container = document.getElementById(staticId);
      }
      if (!container) return;

      var highlightClasses = [
        "eops-ig--highlight-success",
        "eops-ig--highlight-warning",
        "eops-ig--highlight-danger",
        "eops-ig--highlight-info",
        "eops-ig--highlight-row-success",
        "eops-ig--highlight-row-warning",
        "eops-ig--highlight-row-danger",
        "eops-ig--highlight-row-info"
      ];

      for (var h = 0; h < highlightClasses.length; h++) {
        var els = container.querySelectorAll("." + highlightClasses[h]);
        for (var e = 0; e < els.length; e++) {
          els[e].classList.remove(highlightClasses[h]);
        }
      }
    },

    /**
     * @param {HTMLElement} cell
     * @returns {number|null}
     */
    _resolveRowIndex: function (cell) {
      var tr = cell.closest("tr, .eops-ig--body-row, [role='row']");
      if (!tr) return null;

      var idx = tr.getAttribute("data-row-index") ||
                tr.getAttribute("data-idx") ||
                tr.getAttribute("data-rid");
      if (idx !== null) return parseInt(idx, 10);

      var parent = tr.parentNode;
      if (!parent) return null;
      var rows = parent.querySelectorAll("tr, .eops-ig--body-row, [role='row']");
      for (var i = 0; i < rows.length; i++) {
        if (rows[i] === tr) return i;
      }
      return null;
    },

    /**
     * Evaluate a rule operator against a cell value.
     * @param {*} cellValue
     * @param {{operator: string, value: *}} rule
     * @returns {boolean}
     */
    _evaluate: function (cellValue, rule) {
      var val = rule.value;
      var op = (rule.operator || "=").toString();

      switch (op) {
        case "=":
        case "==":
        case "equal":
          return String(cellValue) === String(val);
        case "!=":
        case "notEqual":
          return String(cellValue) !== String(val);
        case ">":
        case "greaterThan":
          return Number(cellValue) > Number(val);
        case "<":
        case "lessThan":
          return Number(cellValue) < Number(val);
        case ">=":
        case "greaterThanOrEqual":
          return Number(cellValue) >= Number(val);
        case "<=":
        case "lessThanOrEqual":
          return Number(cellValue) <= Number(val);
        case "contains":
          return String(cellValue).toLowerCase().indexOf(String(val).toLowerCase()) !== -1;
        case "startsWith":
          return String(cellValue).toLowerCase().indexOf(String(val).toLowerCase()) === 0;
        case "isNull":
          return cellValue === null || cellValue === undefined || cellValue === "";
        case "isNotNull":
          return cellValue !== null && cellValue !== undefined && cellValue !== "";
        default:
          return false;
      }
    }
  };

  // ==========================================================================
  // Module 5: IGKeyboardNav
  // ==========================================================================

  var IGKeyboardNav = {
    /**
     * Initialize keyboard navigation on a grid container.
     * Enables: Arrow keys (cell-to-cell), Enter (edit mode), Escape (cancel edit)
     * @param {string} staticId
     * @param {{autoInit: boolean}} options
     * @returns {{dispose: function}|null}
     */
    init: function (staticId, options) {
      options = options || {};
      var widget = _getIgWidget(staticId);
      if (!widget) return null;

      var container = widget[0] || widget;
      if (!container || !container.nodeType) {
        container = document.getElementById(staticId);
      }
      if (!container) return null;

      var grid = container.querySelector(".eops-ig--grid, table, .a-GV");
      if (!grid) return null;

      var self = this;
      var activeIndex = { row: 0, col: 0 };

      function getCells(rowEl) {
        if (!rowEl) return [];
        return Array.from(rowEl.querySelectorAll(
          ".eops-ig--cell, " +
          "td[headers], " +
          ".a-GV-cell, " +
          "[role='gridcell']"
        ));
      }

      function getRows() {
        return Array.from(grid.querySelectorAll(
          ".eops-ig--body-row, " +
          "tr.a-GV-row, " +
          "[role='row']:not([role='row'][aria-label])"
        ));
      }

      function focusCell(row, col) {
        var rows = getRows();
        if (row >= rows.length) row = rows.length - 1;
        if (row < 0) row = 0;

        var rowEl = rows[row];
        if (!rowEl) return;

        var cells = getCells(rowEl);
        if (col >= cells.length) col = cells.length - 1;
        if (col < 0) col = 0;

        var cell = cells[col];
        if (!cell) return;

        activeIndex = { row: row, col: col };

        var input = cell.querySelector("input, select, textarea");
        if (input) {
          input.focus();
        } else {
          cell.setAttribute("tabindex", "0");
          cell.focus();
        }
      }

      function onKeyDown(e) {
        switch (e.key) {
          case "ArrowUp":
            e.preventDefault();
            focusCell(activeIndex.row - 1, activeIndex.col);
            break;
          case "ArrowDown":
            e.preventDefault();
            focusCell(activeIndex.row + 1, activeIndex.col);
            break;
          case "ArrowLeft":
            e.preventDefault();
            focusCell(activeIndex.row, activeIndex.col - 1);
            break;
          case "ArrowRight":
            e.preventDefault();
            focusCell(activeIndex.row, activeIndex.col + 1);
            break;
          case "Enter":
            e.preventDefault();
            var focused = document.activeElement;
            if (focused) {
              var input = focused.querySelector("input, select, textarea");
              if (input && focused !== input) {
                input.focus();
              }
            }
            break;
          case "Escape":
            document.activeElement.blur();
            grid.focus();
            break;
          case "Tab":
            // Allow native tab behavior
            break;
          default:
            break;
        }
      }

      function onCellClick(e) {
        var cell = e.target.closest(
          ".eops-ig--cell, td[headers], .a-GV-cell, [role='gridcell']"
        );
        if (!cell) return;

        var rows = getRows();
        var rowEl = cell.closest("tr, .eops-ig--body-row, [role='row']");
        var cells = getCells(rowEl);

        if (rowEl) {
          activeIndex.row = rows.indexOf(rowEl);
        }
        activeIndex.col = cells.indexOf(cell);
      }

      grid.addEventListener("keydown", onKeyDown);
      grid.addEventListener("click", onCellClick);
      grid.setAttribute("tabindex", "0");

      if (options.autoInit !== false) {
        setTimeout(function () {
          focusCell(0, 0);
        }, 100);
      }

      return {
        dispose: function () {
          grid.removeEventListener("keydown", onKeyDown);
          grid.removeEventListener("click", onCellClick);
          grid.removeAttribute("tabindex");
        }
      };
    }
  };

  // ==========================================================================
  // Module 6: IGMasterDetail
  // ==========================================================================

  var IGMasterDetail = {
    /**
     * Wire up master-detail linking between a master IG and detail regions.
     *
     * When a row in the master grid is clicked, the detail region is
     * refreshed via AJAX using the selected row's key value(s).
     *
     * @param {string} masterStaticId — static ID of the master IG
     * @param {Array<{detailRegionId: string, keys: Array<{sourceColumn: string, targetItem: string}>}>} details
     *
     * Example:
     *   IGMasterDetail.link("emp_grid", [
     *     {
     *       detailRegionId: "emp_detail",
     *       keys: [
     *         { sourceColumn: "EMPLOYEE_ID", targetItem: "P1_EMP_ID" }
     *       ]
     *     }
     *   ]);
     *
     * @returns {{dispose: function}|null}
     */
    link: function (masterStaticId, details) {
      if (!details || !details.length) return null;

      var widget = _getIgWidget(masterStaticId);
      if (!widget) return null;

      var container = widget[0] || widget;
      if (!container || !container.nodeType) {
        container = document.getElementById(masterStaticId);
      }
      if (!container) return null;

      var grid = container.querySelector(".eops-ig--grid, table, .a-GV");
      if (!grid) return null;

      var self = this;

      function onRowClicked(e) {
        var row = e.target.closest("tr, .eops-ig--body-row, [role='row']");
        if (!row) return;

        self._syncDetail(masterStaticId, details);
      }

      grid.addEventListener("click", onRowClicked);

      // Also register via APEX IG selection-change event if available
      if (typeof apex !== "undefined" && apex.jQuery) {
        var $grid = apex.jQuery("#" + masterStaticId + " .a-GV, " +
                                "#" + masterStaticId + "_ig");
        if ($grid.length) {
          $grid.on("selectionchange", function () {
            self._syncDetail(masterStaticId, details);
          });
        }
      }

      return {
        dispose: function () {
          grid.removeEventListener("click", onRowClicked);
          if (typeof apex !== "undefined" && apex.jQuery) {
            var $grid = apex.jQuery("#" + masterStaticId + " .a-GV, " +
                                    "#" + masterStaticId + "_ig");
            if ($grid.length) {
              $grid.off("selectionchange");
            }
          }
        }
      };
    },

    /**
     * Synchronize detail regions with the currently selected row.
     * @param {string} masterStaticId
     * @param {Array} details
     */
    _syncDetail: function (masterStaticId, details) {
      var vm = _getViewModel(_getIgWidget(masterStaticId));
      if (!vm) return;

      var selected = _getSelectedRecords(vm);
      if (selected.length === 0) return;

      var row = selected[0];
      var model = vm.model;

      for (var d = 0; d < details.length; d++) {
        var detail = details[d];
        var keys = detail.keys;
        if (!keys || !keys.length) continue;

        for (var k = 0; k < keys.length; k++) {
          var key = keys[k];
          var val = model.getValue(row, key.sourceColumn);

          if (key.targetItem) {
            IGMasterDetail._setPageItem(key.targetItem, val);
          }
        }

        if (detail.detailRegionId) {
          IGMasterDetail._refreshRegion(detail.detailRegionId);
        }
      }
    },

    /**
     * Set an APEX page item value.
     * @param {string} itemName
     * @param {*} value
     */
    _setPageItem: function (itemName, value) {
      if (typeof apex !== "undefined" && apex.item) {
        try {
          apex.item(itemName).setValue(value);
        } catch (e) {
          // Fallback: set DOM element directly
          var el = document.getElementById(itemName) ||
                   document.querySelector('[name="' + itemName + '"]');
          if (el) {
            el.value = value;
            el.dispatchEvent(new Event("change", { bubbles: true }));
          }
        }
      }
    },

    /**
     * Refresh an APEX region.
     * @param {string} regionStaticId
     */
    _refreshRegion: function (regionStaticId) {
      if (typeof apex !== "undefined" && apex.region) {
        try {
          apex.region(regionStaticId).refresh();
        } catch (e) {
          console.error("[eops-ig] Error refreshing detail region " + regionStaticId, e);
        }
      }
    }
  };

  /**
   * Helper: get selected records from a view model.
   */
  function _getSelectedRecords(vm) {
    try {
      return vm.view.getSelectedRecords() || [];
    } catch (e) {
      return [];
    }
  }

  // ==========================================================================
  // Exports — ES Module + Global
  // ==========================================================================

  var exports = {
    IGController: IGController,
    IGColumnFormatter: IGColumnFormatter,
    IGExportHelper: IGExportHelper,
    IGRowHighlight: IGRowHighlight,
    IGKeyboardNav: IGKeyboardNav,
    IGMasterDetail: IGMasterDetail
  };

  // ES Module export
  if (typeof module !== "undefined" && module.exports) {
    module.exports = exports;
  }

  // Global namespace under eods (if available) or standalone window.EOPS_IG
  if (typeof window !== "undefined") {
    if (typeof eods !== "undefined") {
      eods.ig2 = exports;
    } else {
      window.EOPS_IG = exports;
    }
  }

  // AMD support
  if (typeof define === "function" && define.amd) {
    define(function () { return exports; });
  }
})();
