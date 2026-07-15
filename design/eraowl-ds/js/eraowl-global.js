/**
 * EraOwl Design System (EODS) — Global JavaScript Utilities
 * Version: 1.0.0
 * Target: React 19 + FastAPI + Tailwind CSS 4
 * Dependencies: None (vanilla JS, ES2020+, no jQuery)
 * Namespace: eods
 *
 * Usage:
 *   eods.notify.success('Record saved');
 *   eods.modal.open('modal_confirm');
 *   eods.theme.toggle();
 */

(function (global) {
  'use strict';

  const EODS_NS = 'eods';
  const EODS_PREFIX = 'eods';

  // ==========================================================================
  // Internal Helpers
  // ==========================================================================

  function $(selector, context) {
    return (context || document).querySelector(selector);
  }

  function $$(selector, context) {
    return Array.from((context || document).querySelectorAll(selector));
  }

  function createElement(tag, attrs, children) {
    const el = document.createElement(tag);
    if (attrs) {
      Object.entries(attrs).forEach(function (entry) {
        var key = entry[0], value = entry[1];
        if (key === 'className') { el.className = value; }
        else if (key === 'innerHTML') { el.innerHTML = value; }
        else if (key === 'textContent') { el.textContent = value; }
        else if (key.startsWith('on')) { el.addEventListener(key.slice(2).toLowerCase(), value); }
        else if (key === 'style' && typeof value === 'object') { Object.assign(el.style, value); }
        else { el.setAttribute(key, value); }
      });
    }
    if (children) {
      children.forEach(function (child) {
        if (typeof child === 'string') { el.appendChild(document.createTextNode(child)); }
        else if (child) { el.appendChild(child); }
      });
    }
    return el;
  }

  function getApexItem(itemName) {
    if (typeof apex !== 'undefined' && apex.item) {
      return apex.item(itemName);
    }
    return {
      getValue: function () {
        var el = document.getElementById(itemName) ||
                 document.querySelector('[name="' + itemName + '"]');
        return el ? el.value : null;
      },
      setValue: function (val) {
        var el = document.getElementById(itemName) ||
                 document.querySelector('[name="' + itemName + '"]');
        if (el) { el.value = val; }
      }
    };
  }

  function dispatchCustomEvent(name, detail) {
    document.dispatchEvent(new CustomEvent(name, { detail: detail || {}, bubbles: true }));
  }

  // ==========================================================================
  // Module: Notifications
  // ==========================================================================

  var notificationQueue = [];
  var notificationTimer = null;

  var notify = {
    _container: null,

    _getContainer: function () {
      if (!notify._container) {
        notify._container = createElement('div', {
          className: EODS_PREFIX + '-toast-container',
          id: EODS_PREFIX + '-toast-container'
        });
        document.body.appendChild(notify._container);
      }
      return notify._container;
    },

    /**
     * Show a toast notification.
     * @param {string} message - Notification message
     * @param {string} type - success, warning, danger, info, loading
     * @param {object} options - { position, duration, dismissible, icon }
     */
    show: function (message, type, options) {
      type = type || 'info';
      options = options || {};
      var duration = options.duration !== undefined ? options.duration : 5000;
      var position = options.position || 'top-right';

      var container = notify._getContainer();
      container.className = EODS_PREFIX + '-toast-container ' +
        EODS_PREFIX + '-toast-container--' + position;

      var iconMap = {
        success: 'fa-check-circle',
        warning: 'fa-exclamation-triangle',
        danger: 'fa-times-circle',
        info: 'fa-info-circle',
        loading: 'fa-spinner ' + EODS_PREFIX + '-spinner ' + EODS_PREFIX + '-spinner--sm'
      };

      var toast = createElement('div', {
        className: EODS_PREFIX + '-toast ' + EODS_PREFIX + '-toast--' + type,
        role: 'status',
        'aria-live': 'polite'
      });

      if (options.icon !== false) {
        var icon = createElement('span', {
          className: EODS_PREFIX + '-toast__icon fa ' + (iconMap[type] || iconMap.info),
          'aria-hidden': 'true'
        });
        toast.appendChild(icon);
      }

      var text = createElement('span', {
        className: EODS_PREFIX + '-toast__text',
        textContent: message
      });
      toast.appendChild(text);

      if (options.dismissible !== false) {
        var dismiss = createElement('button', {
          className: EODS_PREFIX + '-toast__dismiss',
          'aria-label': 'Dismiss notification',
          onClick: function () { notify.dismiss(toast); }
        }, ['\u00D7']);
        toast.appendChild(dismiss);
      }

      container.appendChild(toast);

      // Animate in
      requestAnimationFrame(function () {
        toast.classList.add(EODS_PREFIX + '-toast--visible');
      });

      // Auto dismiss
      if (duration > 0) {
        setTimeout(function () {
          notify.dismiss(toast);
        }, duration);
      }

      return toast;
    },

    dismiss: function (toast) {
      toast.classList.remove(EODS_PREFIX + '-toast--visible');
      toast.addEventListener('transitionend', function handler() {
        toast.removeEventListener('transitionend', handler);
        if (toast.parentNode) {
          toast.parentNode.removeChild(toast);
        }
      });
      // Fallback if transition doesn't fire
      setTimeout(function () {
        if (toast.parentNode) {
          toast.parentNode.removeChild(toast);
        }
      }, 400);
    },

    success: function (message, options) { return notify.show(message, 'success', options); },
    warning: function (message, options) { return notify.show(message, 'warning', options); },
    danger: function (message, options) { return notify.show(message, 'danger', options); },
    error: function (message, options) { return notify.show(message, 'danger', options); },
    info: function (message, options) { return notify.show(message, 'info', options); },
    loading: function (message, options) { return notify.show(message, 'loading', options); },

    /**
     * Dismiss all visible toasts.
     */
    dismissAll: function () {
      var container = notify._getContainer();
      $$('.' + EODS_PREFIX + '-toast', container).forEach(function (t) {
        notify.dismiss(t);
      });
    },

    /**
     * Show an inline form field error.
     * @param {string} fieldId - Field element ID or APEX item name
     * @param {string} message - Error message
     */
    inlineError: function (fieldId, message) {
      var el = document.getElementById(fieldId) ||
               document.querySelector('[name="' + fieldId + '"]');
      if (!el) return;

      var group = el.closest('.' + EODS_PREFIX + '-form__group');
      if (group) {
        group.classList.add(EODS_PREFIX + '-form__group--error');
      } else {
        el.classList.add(EODS_PREFIX + '-form__control--error');
      }

      var errorEl = group
        ? $('.' + EODS_PREFIX + '-form__error', group)
        : el.nextElementSibling;
      if (errorEl) {
        errorEl.textContent = message;
        errorEl.style.display = 'block';
        errorEl.setAttribute('role', 'alert');
      }
    },

    /**
     * Clear inline errors on a field.
     * @param {string} fieldId - Field element ID
     */
    clearInlineError: function (fieldId) {
      var el = document.getElementById(fieldId) ||
               document.querySelector('[name="' + fieldId + '"]');
      if (!el) return;

      var group = el.closest('.' + EODS_PREFIX + '-form__group');
      if (group) {
        group.classList.remove(EODS_PREFIX + '-form__group--error');
      } else {
        el.classList.remove(EODS_PREFIX + '-form__control--error');
      }

      var errorEl = group
        ? $('.' + EODS_PREFIX + '-form__error', group)
        : el.nextElementSibling;
      if (errorEl) {
        errorEl.style.display = 'none';
        errorEl.textContent = '';
      }
    },

    /**
     * Show a confirmation dialog using browser confirm or custom.
     */
    confirm: function (message, options) {
      options = options || {};
      return new Promise(function (resolve) {
        if (options.useCustom !== false && typeof eods !== 'undefined' && eods.modal) {
          eods.modal.confirm(message, options).then(resolve);
        } else {
          resolve(window.confirm(message));
        }
      });
    }
  };

  // ==========================================================================
  // Module: Modal / Dialog
  // ==========================================================================

  var modal = {
    _activeModal: null,
    _backdrop: null,
    _previousFocus: null,

    _getBackdrop: function () {
      if (!modal._backdrop) {
        modal._backdrop = createElement('div', {
          className: EODS_PREFIX + '-dialog-backdrop',
          onClick: function () {
            if (modal._activeModal && modal._activeModal.dataset.closeBackdrop !== 'false') {
              modal.close(modal._activeModal);
            }
          }
        });
        document.body.appendChild(modal._backdrop);
      }
      return modal._backdrop;
    },

    /**
     * Open a modal dialog by element or ID.
     * @param {string|HTMLElement} target - Dialog element or ID
     */
    open: function (target) {
      var el = typeof target === 'string' ? document.getElementById(target) : target;
      if (!el) {
        console.error('[eods.modal] Dialog not found:', target);
        return null;
      }

      // Close existing
      if (modal._activeModal) {
        modal.close(modal._activeModal);
      }

      modal._previousFocus = document.activeElement;
      modal._activeModal = el;

      var backdrop = modal._getBackdrop();
      backdrop.classList.add(EODS_PREFIX + '-dialog-backdrop--visible');

      el.classList.add(EODS_PREFIX + '-dialog--visible');
      el.setAttribute('aria-hidden', 'false');

      // Focus trap
      modal._trapFocus(el);

      // ESC key
      el._escHandler = function (e) {
        if (e.key === 'Escape' && el.dataset.closeEsc !== 'false') {
          modal.close(el);
        }
      };
      document.addEventListener('keydown', el._escHandler);

      dispatchCustomEvent(EODS_PREFIX + ':dialog:open', { dialog: el });

      return el;
    },

    /**
     * Close a modal dialog.
     */
    close: function (el) {
      if (!el) el = modal._activeModal;
      if (!el) return;

      el.classList.remove(EODS_PREFIX + '-dialog--visible');
      el.setAttribute('aria-hidden', 'true');

      var backdrop = modal._getBackdrop();
      // Only hide backdrop if no other modals
      if (modal._activeModal === el) {
        backdrop.classList.remove(EODS_PREFIX + '-dialog-backdrop--visible');
        modal._activeModal = null;
      }

      // Remove ESC handler
      if (el._escHandler) {
        document.removeEventListener('keydown', el._escHandler);
        delete el._escHandler;
      }

      // Restore focus
      if (modal._previousFocus && typeof modal._previousFocus.focus === 'function') {
        setTimeout(function () { modal._previousFocus.focus(); }, 100);
      }

      dispatchCustomEvent(EODS_PREFIX + ':dialog:close', { dialog: el });

      // Call onClose callback
      if (typeof el._onClose === 'function') {
        el._onClose();
        delete el._onClose;
      }
    },

    /**
     * Set dialog to loading state.
     */
    setLoading: function (el, isLoading) {
      if (!el) el = modal._activeModal;
      if (!el) return;

      var body = $('.' + EODS_PREFIX + '-dialog__body', el);
      if (!body) return;

      if (isLoading) {
        body.setAttribute('data-eods-loading', 'true');
        var loadingEl = createElement('div', {
          className: EODS_PREFIX + '-dialog__loading'
        }, [
          createElement('div', { className: EODS_PREFIX + '-spinner ' + EODS_PREFIX + '-spinner--lg', role: 'status' }),
          createElement('p', { textContent: 'Loading...' })
        ]);
        body.innerHTML = '';
        body.appendChild(loadingEl);
      } else {
        body.removeAttribute('data-eods-loading');
      }
    },

    /**
     * Create and show a confirmation dialog.
     */
    confirm: function (message, options) {
      options = options || {};
      return new Promise(function (resolve) {
        var dialog = createElement('div', {
          className: EODS_PREFIX + '-dialog ' + EODS_PREFIX + '-dialog--sm ' +
                     EODS_PREFIX + '-dialog--visible ' + EODS_PREFIX + '-dialog--confirm',
          role: 'alertdialog',
          'aria-modal': 'true',
          'aria-labelledby': EODS_PREFIX + '-confirm-title'
        });

        var iconType = options.type || 'warning';
        var iconMap = {
          danger: 'fa-times-circle ' + EODS_PREFIX + '-dialog__alert-icon--danger',
          warning: 'fa-exclamation-triangle ' + EODS_PREFIX + '-dialog__alert-icon--warning',
          info: 'fa-info-circle ' + EODS_PREFIX + '-dialog__alert-icon--info',
          success: 'fa-check-circle ' + EODS_PREFIX + '-dialog__alert-icon--success'
        };

        var headerContent = [
          createElement('h2', {
            id: EODS_PREFIX + '-confirm-title',
            className: EODS_PREFIX + '-dialog__title',
            textContent: options.title || 'Confirm'
          })
        ];

        if (options.showClose !== false) {
          headerContent.push(createElement('button', {
            className: EODS_PREFIX + '-dialog__close',
            'aria-label': 'Close',
            onClick: function () { modal.close(dialog); resolve(false); }
          }, ['\u00D7']));
        }

        var header = createElement('div', {
          className: EODS_PREFIX + '-dialog__header'
        }, headerContent);

        var body = createElement('div', {
          className: EODS_PREFIX + '-dialog__body'
        }, [
          createElement('div', { className: EODS_PREFIX + '-dialog__alert-icon fa ' + (iconMap[iconType] || iconMap.warning), 'aria-hidden': 'true' }),
          createElement('p', { textContent: message || 'Are you sure?' })
        ]);

        var confirmText = options.confirmText || 'Confirm';
        var cancelText = options.cancelText || 'Cancel';

        var footer = createElement('div', {
          className: EODS_PREFIX + '-dialog__footer'
        }, [
          createElement('button', {
            className: EODS_PREFIX + '-btn ' + EODS_PREFIX + '-btn--secondary ' + EODS_PREFIX + '-btn--md',
            textContent: cancelText,
            onClick: function () { modal.close(dialog); resolve(false); }
          }),
          createElement('button', {
            className: EODS_PREFIX + '-btn ' + EODS_PREFIX + '-btn--' +
                       (options.type === 'danger' ? 'danger' : 'primary') + ' ' + EODS_PREFIX + '-btn--md',
            textContent: confirmText,
            onClick: function () { modal.close(dialog); resolve(true); }
          })
        ]);

        dialog.appendChild(header);
        dialog.appendChild(body);
        dialog.appendChild(footer);

        document.body.appendChild(dialog);
        modal.open(dialog);

        // Clean up after close
        var origClose = dialog._onClose;
        dialog._onClose = function () {
          if (dialog.parentNode) {
            dialog.parentNode.removeChild(dialog);
          }
        };
      });
    },

    /**
     * Alert dialog (single OK button).
     */
    alert: function (message, options) {
      options = options || {};
      return new Promise(function (resolve) {
        var dialog = createElement('div', {
          className: EODS_PREFIX + '-dialog ' + EODS_PREFIX + '-dialog--sm ' +
                     EODS_PREFIX + '-dialog--visible ' + EODS_PREFIX + '-dialog--alert',
          role: 'alertdialog', 'aria-modal': 'true'
        });

        var iconType = options.type || 'info';
        var iconMap = {
          danger: 'fa-times-circle ' + EODS_PREFIX + '-dialog__alert-icon--danger',
          warning: 'fa-exclamation-triangle ' + EODS_PREFIX + '-dialog__alert-icon--warning',
          info: 'fa-info-circle ' + EODS_PREFIX + '-dialog__alert-icon--info',
          success: 'fa-check-circle ' + EODS_PREFIX + '-dialog__alert-icon--success'
        };

        dialog.appendChild(createElement('div', { className: EODS_PREFIX + '-dialog__header' }, [
          createElement('h2', { className: EODS_PREFIX + '-dialog__title', textContent: options.title || 'Notice' }),
          createElement('button', { className: EODS_PREFIX + '-dialog__close', 'aria-label': 'Close',
            onClick: function () { modal.close(dialog); resolve(); } }, ['\u00D7'])
        ]));

        dialog.appendChild(createElement('div', { className: EODS_PREFIX + '-dialog__body' }, [
          createElement('div', { className: EODS_PREFIX + '-dialog__alert-icon fa ' + (iconMap[iconType] || iconMap.info), 'aria-hidden': 'true' }),
          createElement('p', { textContent: message || '' })
        ]));

        dialog.appendChild(createElement('div', { className: EODS_PREFIX + '-dialog__footer' }, [
          createElement('button', {
            className: EODS_PREFIX + '-btn ' + EODS_PREFIX + '-btn--primary ' + EODS_PREFIX + '-btn--md',
            textContent: 'OK',
            onClick: function () { modal.close(dialog); resolve(); }
          })
        ]));

        document.body.appendChild(dialog);
        modal.open(dialog);

        dialog._onClose = function () {
          if (dialog.parentNode) dialog.parentNode.removeChild(dialog);
          resolve();
        };
      });
    },

    _trapFocus: function (el) {
      var focusable = $$(
        'a[href], button:not([disabled]), textarea:not([disabled]), input:not([disabled]), ' +
        'select:not([disabled]), [tabindex]:not([tabindex="-1"])', el
      );
      if (focusable.length === 0) return;

      var first = focusable[0];
      var last = focusable[focusable.length - 1];

      el._focusTrap = function (e) {
        if (e.key !== 'Tab') return;
        if (e.shiftKey && document.activeElement === first) {
          e.preventDefault();
          last.focus();
        } else if (!e.shiftKey && document.activeElement === last) {
          e.preventDefault();
          first.focus();
        }
      };

      document.addEventListener('keydown', el._focusTrap);
      first.focus();
    }
  };

  // ==========================================================================
  // Module: Loading Overlay
  // ==========================================================================

  var loadingOverlay = null;

  var loading = {
    /**
     * Show loading overlay over an element or full page.
     * @param {string|HTMLElement} target - Target element or 'page'
     * @param {string} message - Loading message
     */
    show: function (target, message) {
      loading.hide();

      if (!target || target === 'page' || target === 'body') {
        target = document.body;
      } else if (typeof target === 'string') {
        target = document.getElementById(target);
      }
      if (!target) return;

      loadingOverlay = createElement('div', {
        className: EODS_PREFIX + '-loading-overlay',
        role: 'status',
        'aria-label': message || 'Loading'
      }, [
        createElement('div', { className: EODS_PREFIX + '-loading-overlay__content' }, [
          createElement('div', { className: EODS_PREFIX + '-spinner ' + EODS_PREFIX + '-spinner--lg ' +
            EODS_PREFIX + '-spinner--light', role: 'status' }),
          message ? createElement('p', { className: EODS_PREFIX + '-loading-overlay__text', textContent: message }) : null
        ])
      ]);

      var position = window.getComputedStyle(target).position;
      if (position === 'static') {
        target.style.position = 'relative';
      }

      target.appendChild(loadingOverlay);
      return loadingOverlay;
    },

    hide: function () {
      if (loadingOverlay && loadingOverlay.parentNode) {
        loadingOverlay.parentNode.removeChild(loadingOverlay);
      }
      loadingOverlay = null;
    }
  };

  // ==========================================================================
  // Module: AJAX
  // ==========================================================================

  var ajax = {
    _defaultTimeout: 30000,
    _maxRetries: 2,

    /**
     * Make an APEX AJAX call (on-demand process).
     * @param {string} process - AJAX callback process name
     * @param {object} data - Key-value pairs to send
     * @param {object} options - { timeout, retries, silent }
     * @returns {Promise}
     */
    call: function (process, data, options) {
      options = options || {};
      var timeout = options.timeout || ajax._defaultTimeout;

      return new Promise(function (resolve, reject) {
        if (typeof apex === 'undefined' || !apex.server || !apex.server.process) {
          reject(new Error('[eods.ajax] APEX server API not available'));
          return;
        }

        var controller = new AbortController();
        var timeoutId = setTimeout(function () {
          controller.abort();
          reject(new Error('[eods.ajax] Request timeout: ' + process));
        }, timeout);

        apex.server.process(process, data || {}, {
          success: function (result) {
            clearTimeout(timeoutId);
            resolve(result);
          },
          error: function (jqXHR, textStatus, errorThrown) {
            clearTimeout(timeoutId);
            var err = new Error(errorThrown || textStatus || 'AJAX error');
            err.status = jqXHR ? jqXHR.status : undefined;
            err.process = process;
            reject(err);
          },
          dataType: options.dataType || 'json'
        });
      });
    },

    /**
     * Convenience: GET-like APEX callback.
     */
    get: function (process, data, options) {
      return ajax.call(process, data, options);
    },

    /**
     * Convenience: POST-like APEX callback.
     */
    post: function (process, data, options) {
      return ajax.call(process, data, options);
    },

    /**
     * Fetch wrapper with error handling (for non-APEX endpoints).
     * @param {string} url - URL to fetch
     * @param {object} options - Fetch options + { retries, silent }
     */
    fetch: function (url, options) {
      options = options || {};
      var retries = options.retries !== undefined ? options.retries : 0;
      var silent = options.silent || false;

      return fetch(url, {
        method: options.method || 'GET',
        headers: Object.assign({
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        }, options.headers || {}),
        body: options.body ? JSON.stringify(options.body) : undefined,
        signal: options.signal
      })
      .then(function (response) {
        if (!response.ok) {
          throw new Error('HTTP ' + response.status + ': ' + response.statusText);
        }
        var contentType = response.headers.get('content-type') || '';
        if (contentType.includes('application/json')) {
          return response.json();
        }
        return response.text();
      })
      .catch(function (err) {
        if (retries > 0) {
          return ajax.fetch(url, Object.assign({}, options, { retries: retries - 1 }));
        }
        if (!silent) {
          errorHandler.handle(err, { source: 'fetch', url: url });
        }
        throw err;
      });
    },

    /**
     * Submit page items and optionally branch.
     * Uses APEX native submit if available.
     */
    submit: function (request) {
      if (typeof apex !== 'undefined' && apex.page && apex.page.submit) {
        apex.page.submit(request);
      } else if (typeof apex !== 'undefined' && apex.submit) {
        apex.submit(request);
      } else {
        console.warn('[eods.ajax] APEX submit API not available');
      }
    }
  };

  // ==========================================================================
  // Module: Interactive Grid Helper
  // ==========================================================================

  var ig = {
    /**
     * Get Interactive Grid widget by static ID.
     * @param {string} staticId - IG static ID
     * @returns {object|null}
     */
    get: function (staticId) {
      if (typeof apex !== 'undefined' && apex.region) {
        return apex.region(staticId);
      }
      return null;
    },

    /**
     * Get selected records from an IG.
     */
    getSelectedRecords: function (staticId) {
      var region = ig.get(staticId);
      if (!region || !region.widget) return [];

      try {
        var view = region.widget().interactiveGrid('getViews', 'grid');
        var model = view.model;
        var selected = view.getSelectedRecords();
        if (!selected || selected.length === 0) return [];

        return selected.map(function (rec) {
          var obj = {};
          model.getRecordFields(rec).forEach(function (field) {
            obj[field] = model.getValue(rec, field);
          });
          return obj;
        });
      } catch (e) {
        console.error('[eods.ig] Error getting selected records:', e);
        return [];
      }
    },

    /**
     * Refresh an Interactive Grid.
     */
    refresh: function (staticId) {
      var region = ig.get(staticId);
      if (region && region.widget) {
        try {
          region.widget().interactiveGrid('getActions').invoke('refresh');
        } catch (e) {
          console.error('[eods.ig] Error refreshing grid:', e);
        }
      }
    },

    /**
     * Add a new row to an editable IG.
     */
    addRow: function (staticId) {
      var region = ig.get(staticId);
      if (!region || !region.widget) return;

      try {
        var widget = region.widget();
        widget.interactiveGrid('getActions').invoke('selection-add-row');
      } catch (e) {
        console.error('[eods.ig] Error adding row:', e);
      }
    },

    /**
     * Delete selected rows in an IG.
     */
    deleteSelectedRows: function (staticId) {
      var region = ig.get(staticId);
      if (!region || !region.widget) return;

      try {
        var widget = region.widget();
        widget.interactiveGrid('getActions').invoke('selection-delete');
      } catch (e) {
        console.error('[eods.ig] Error deleting rows:', e);
      }
    },

    /**
     * Save all changes in an editable IG.
     */
    save: function (staticId) {
      var region = ig.get(staticId);
      if (!region || !region.widget) return;

      try {
        var widget = region.widget();
        widget.interactiveGrid('getActions').invoke('save');
      } catch (e) {
        console.error('[eods.ig] Error saving grid:', e);
      }
    },

    /**
     * Set a filter on an IG column.
     */
    setFilter: function (staticId, columnName, value) {
      var region = ig.get(staticId);
      if (!region || !region.widget) return;

      try {
        var widget = region.widget();
        var views = widget.interactiveGrid('getViews');
        var model = views.grid.model;
        var filter = model.getFilters();
        filter.add(columnName, value, 'EQ');
      } catch (e) {
        console.error('[eods.ig] Error setting filter:', e);
      }
    },

    /**
     * Clear all filters in an IG.
     */
    clearFilters: function (staticId) {
      var region = ig.get(staticId);
      if (!region || !region.widget) return;

      try {
        var widget = region.widget();
        var views = widget.interactiveGrid('getViews');
        var model = views.grid.model;
        var filter = model.getFilters();
        filter.clear();
      } catch (e) {
        console.error('[eods.ig] Error clearing filters:', e);
      }
    }
  };

  // ==========================================================================
  // Module: Validation
  // ==========================================================================

  var validation = {
    /**
     * Validate a single form field.
     * @param {string} fieldId - Field ID or name
     * @param {object} rules - { required, minLength, maxLength, pattern, email, custom }
     * @returns {boolean}
     */
    validateField: function (fieldId, rules) {
      rules = rules || {};
      var val = (getApexItem(fieldId).getValue() || '').toString().trim();
      var errors = [];

      if (rules.required && val.length === 0) {
        errors.push(rules.requiredMessage || 'This field is required.');
      }

      if (rules.minLength && val.length < rules.minLength) {
        errors.push(rules.minLengthMessage || 'Minimum ' + rules.minLength + ' characters required.');
      }

      if (rules.maxLength && val.length > rules.maxLength) {
        errors.push(rules.maxLengthMessage || 'Maximum ' + rules.maxLength + ' characters allowed.');
      }

      if (rules.pattern && val.length > 0) {
        var re = new RegExp(rules.pattern);
        if (!re.test(val)) {
          errors.push(rules.patternMessage || 'Invalid format.');
        }
      }

      if (rules.email && val.length > 0) {
        var emailRe = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRe.test(val)) {
          errors.push(rules.emailMessage || 'Please enter a valid email address.');
        }
      }

      if (rules.custom && typeof rules.custom === 'function') {
        var customResult = rules.custom(val);
        if (customResult !== true) {
          errors.push(customResult || 'Validation failed.');
        }
      }

      if (errors.length > 0) {
        notify.inlineError(fieldId, errors[0]);
        return false;
      }

      notify.clearInlineError(fieldId);
      return true;
    },

    /**
     * Validate all fields in a form.
     * @param {string} formId - Form element ID
     * @param {object} fieldRules - { fieldName: { rules } }
     * @returns {boolean}
     */
    validateForm: function (formId, fieldRules) {
      fieldRules = fieldRules || {};
      var valid = true;

      Object.keys(fieldRules).forEach(function (fieldId) {
        if (!validation.validateField(fieldId, fieldRules[fieldId])) {
          valid = false;
        }
      });

      return valid;
    }
  };

  // ==========================================================================
  // Module: Button
  // ==========================================================================

  var btn = {
    setLoading: function (el, isLoading) {
      if (typeof el === 'string') el = document.getElementById(el);
      if (!el) return;

      if (isLoading) {
        el.classList.add(EODS_PREFIX + '-btn--loading');
        el.disabled = true;
      } else {
        el.classList.remove(EODS_PREFIX + '-btn--loading');
        el.disabled = false;
      }
    },

    disable: function (el) {
      if (typeof el === 'string') el = document.getElementById(el);
      if (!el) return;
      el.classList.add(EODS_PREFIX + '-btn--disabled');
      el.disabled = true;
    },

    enable: function (el) {
      if (typeof el === 'string') el = document.getElementById(el);
      if (!el) return;
      el.classList.remove(EODS_PREFIX + '-btn--disabled');
      el.disabled = false;
    },

    confirm: function (el, options) {
      if (typeof el === 'string') el = document.getElementById(el);
      if (!el) return Promise.resolve(false);

      options = options || {};
      return modal.confirm(options.message || 'Are you sure?', options);
    }
  };

  // ==========================================================================
  // Module: Date Helper
  // ==========================================================================

  var dateHelper = {
    /**
     * Format a date.
     * @param {Date|string|number} date - Date to format
     * @param {string} format - 'iso', 'short', 'long', 'time', 'datetime', 'relative' or custom
     * @returns {string}
     */
    format: function (date, format) {
      var d = date instanceof Date ? date : new Date(date);
      if (isNaN(d.getTime())) return '';

      format = format || 'iso';

      var pad = function (n) { return String(n).padStart(2, '0'); };

      var formatters = {
        iso: function () {
          return d.getFullYear() + '-' + pad(d.getMonth() + 1) + '-' + pad(d.getDate());
        },
        short: function () {
          return pad(d.getMonth() + 1) + '/' + pad(d.getDate()) + '/' + d.getFullYear().toString().slice(-2);
        },
        long: function () {
          var months = ['January','February','March','April','May','June',
                        'July','August','September','October','November','December'];
          return months[d.getMonth()] + ' ' + d.getDate() + ', ' + d.getFullYear();
        },
        time: function () {
          var h = d.getHours();
          var ampm = h >= 12 ? 'PM' : 'AM';
          h = h % 12 || 12;
          return h + ':' + pad(d.getMinutes()) + ' ' + ampm;
        },
        datetime: function () {
          return dateHelper.format(d, 'short') + ' ' + dateHelper.format(d, 'time');
        },
        relative: function () {
          var now = new Date();
          var diff = now - d;
          var seconds = Math.floor(diff / 1000);
          var minutes = Math.floor(seconds / 60);
          var hours = Math.floor(minutes / 60);
          var days = Math.floor(hours / 24);
          var months = Math.floor(days / 30);
          var years = Math.floor(days / 365);

          if (seconds < 60) return 'Just now';
          if (minutes < 60) return minutes + 'm ago';
          if (hours < 24) return hours + 'h ago';
          if (days < 7) return days + 'd ago';
          if (days < 30) return Math.floor(days / 7) + 'w ago';
          if (months < 12) return months + 'mo ago';
          return years + 'y ago';
        }
      };

      return (formatters[format] || function () { return d.toString(); })();
    },

    /**
     * Parse a date string.
     */
    parse: function (str) {
      var d = new Date(str);
      return isNaN(d.getTime()) ? null : d;
    }
  };

  // ==========================================================================
  // Module: Session Helper
  // ==========================================================================

  var session = {
    /**
     * Get a value from session storage.
     */
    get: function (key, defaultValue) {
      try {
        var val = sessionStorage.getItem(EODS_PREFIX + '_' + key);
        if (val === null) return defaultValue;
        try { return JSON.parse(val); } catch (e) { return val; }
      } catch (e) {
        return defaultValue;
      }
    },

    /**
     * Set a value in session storage.
     */
    set: function (key, value) {
      try {
        sessionStorage.setItem(EODS_PREFIX + '_' + key, JSON.stringify(value));
      } catch (e) {
        console.warn('[eods.session] Storage full or unavailable');
      }
    },

    /**
     * Remove a value from session storage.
     */
    remove: function (key) {
      try {
        sessionStorage.removeItem(EODS_PREFIX + '_' + key);
      } catch (e) { /* ignore */ }
    },

    /**
     * Clear all EODS session storage.
     */
    clear: function () {
      try {
        Object.keys(sessionStorage).forEach(function (k) {
          if (k.startsWith(EODS_PREFIX + '_')) {
            sessionStorage.removeItem(k);
          }
        });
      } catch (e) { /* ignore */ }
    }
  };

  // ==========================================================================
  // Module: Local Storage (persistent)
  // ==========================================================================

  var storage = {
    get: function (key, defaultValue) {
      try {
        var val = localStorage.getItem(EODS_PREFIX + '_' + key);
        if (val === null) return defaultValue;
        try { return JSON.parse(val); } catch (e) { return val; }
      } catch (e) { return defaultValue; }
    },

    set: function (key, value) {
      try {
        localStorage.setItem(EODS_PREFIX + '_' + key, JSON.stringify(value));
      } catch (e) {
        console.warn('[eods.storage] Storage full or unavailable');
      }
    },

    remove: function (key) {
      try {
        localStorage.removeItem(EODS_PREFIX + '_' + key);
      } catch (e) { /* ignore */ }
    }
  };

  // ==========================================================================
  // Module: Error Handler
  // ==========================================================================

  var errorHandler = {
    _listeners: [],

    /**
     * Handle an error — log and optionally display.
     */
    handle: function (err, context) {
      context = context || {};
      var message = err instanceof Error ? err.message : String(err);

      // Log to console
      console.error('[eods.error]', message, context, err);

      // Dispatch event for custom listeners
      dispatchCustomEvent(EODS_PREFIX + ':error', {
        message: message,
        error: err,
        context: context
      });

      // Call registered listeners
      errorHandler._listeners.forEach(function (fn) {
        try { fn(err, context); } catch (e) { /* prevent cascading */ }
      });

      // APEX debug if available
      if (typeof apex !== 'undefined' && apex.debug && apex.debug.error) {
        try { apex.debug.error(message); } catch (e) { /* ignore */ }
      }
    },

    /**
     * Register a global error listener.
     */
    onError: function (fn) {
      if (typeof fn === 'function') {
        errorHandler._listeners.push(fn);
      }
    },

    /**
     * Global unhandled error capture.
     */
    init: function () {
      window.addEventListener('error', function (e) {
        errorHandler.handle(e.error || e.message, {
          source: 'window.onerror',
          filename: e.filename,
          lineno: e.lineno,
          colno: e.colno
        });
      });

      window.addEventListener('unhandledrejection', function (e) {
        errorHandler.handle(e.reason, { source: 'unhandledrejection' });
      });
    }
  };

  // ==========================================================================
  // Module: Theme / Dark Mode
  // ==========================================================================

  var theme = {
    /**
     * Get current theme ('light', 'dark', 'auto').
     */
    get: function () {
      return document.documentElement.getAttribute('data-theme') || storage.get('theme', 'auto');
    },

    /**
     * Set theme.
     * @param {string} mode - 'light', 'dark', or 'auto'
     */
    set: function (mode) {
      if (mode === 'auto') {
        document.documentElement.removeAttribute('data-theme');
        storage.remove('theme');
      } else {
        document.documentElement.setAttribute('data-theme', mode);
        storage.set('theme', mode);
      }
      dispatchCustomEvent(EODS_PREFIX + ':theme:change', { theme: mode });
    },

    /**
     * Toggle between light and dark.
     */
    toggle: function () {
      var current = theme.get();
      theme.set(current === 'dark' ? 'light' : 'dark');
    },

    /**
     * Initialize theme from storage.
     */
    init: function () {
      var saved = storage.get('theme', 'auto');
      if (saved !== 'auto') {
        document.documentElement.setAttribute('data-theme', saved);
      }
    }
  };

  // ==========================================================================
  // Module: DOM Utilities
  // ==========================================================================

  var dom = {
    /**
     * Get element(s).
     */
    get: function (selector, context) { return $(selector, context); },
    getAll: function (selector, context) { return $$(selector, context); },

    /**
     * Create an element.
     */
    create: function (tag, attrs, children) { return createElement(tag, attrs, children); },

    /**
     * Add a class.
     */
    addClass: function (el, className) {
      if (typeof el === 'string') el = $(el);
      if (el) el.classList.add(className);
    },

    /**
     * Remove a class.
     */
    removeClass: function (el, className) {
      if (typeof el === 'string') el = $(el);
      if (el) el.classList.remove(className);
    },

    /**
     * Toggle a class.
     */
    toggleClass: function (el, className, force) {
      if (typeof el === 'string') el = $(el);
      if (el) el.classList.toggle(className, force);
    },

    /**
     * Check if element has a class.
     */
    hasClass: function (el, className) {
      if (typeof el === 'string') el = $(el);
      return el ? el.classList.contains(className) : false;
    },

    /**
     * Fade element in.
     */
    fadeIn: function (el, duration) {
      if (typeof el === 'string') el = $(el);
      if (!el) return;
      el.style.opacity = '0';
      el.style.display = '';
      el.style.transition = 'opacity ' + (duration || 250) + 'ms ease';
      requestAnimationFrame(function () {
        el.style.opacity = '1';
      });
    },

    /**
     * Fade element out.
     */
    fadeOut: function (el, duration) {
      if (typeof el === 'string') el = $(el);
      if (!el) return;
      el.style.transition = 'opacity ' + (duration || 250) + 'ms ease';
      el.style.opacity = '0';
      el.addEventListener('transitionend', function handler() {
        el.removeEventListener('transitionend', handler);
        el.style.display = 'none';
      });
    }
  };

  // ==========================================================================
  // Module: Debounce / Throttle
  // ==========================================================================

  var util = {
    /**
     * Debounce a function.
     */
    debounce: function (fn, delay) {
      delay = delay || 300;
      var timer;
      return function () {
        var context = this, args = arguments;
        clearTimeout(timer);
        timer = setTimeout(function () { fn.apply(context, args); }, delay);
      };
    },

    /**
     * Throttle a function.
     */
    throttle: function (fn, limit) {
      limit = limit || 300;
      var inThrottle = false;
      return function () {
        if (!inThrottle) {
          fn.apply(this, arguments);
          inThrottle = true;
          setTimeout(function () { inThrottle = false; }, limit);
        }
      };
    },

    /**
     * Generate a unique ID with optional prefix.
     */
    uid: function (prefix) {
      return (prefix || EODS_PREFIX) + '-' + Date.now().toString(36) + '-' +
             Math.random().toString(36).substring(2, 9);
    },

    /**
     * Escape HTML to prevent XSS.
     */
    escapeHtml: function (str) {
      var div = document.createElement('div');
      div.appendChild(document.createTextNode(str));
      return div.innerHTML;
    },

    /**
     * Copy text to clipboard.
     */
    copyToClipboard: function (text) {
      return navigator.clipboard.writeText(text).catch(function (err) {
        console.warn('[eods.util] Clipboard write failed:', err);
      });
    }
  };

  // ==========================================================================
  // Module: Dynamic Action Helpers
  // ==========================================================================

  var da = {
    /**
     * Manually trigger a dynamic action on an element.
     */
    trigger: function (eventName, elementId) {
      var el = document.getElementById(elementId);
      if (el) {
        el.dispatchEvent(new Event(eventName, { bubbles: true }));
      }
    },

    /**
     * Get the dynamic action context if available.
     */
    getContext: function () {
      if (typeof apex !== 'undefined' && apex.da && apex.da.getContext) {
        return apex.da.getContext();
      }
      return null;
    }
  };

  // ==========================================================================
  // Auto-Initialization
  // ==========================================================================

  function autoInit() {
    // Init theme
    theme.init();

    // Init global error handling
    errorHandler.init();

    // Add toast container styles if not present
    if (!document.getElementById(EODS_PREFIX + '-toast-styles')) {
      var styleEl = document.createElement('style');
      styleEl.id = EODS_PREFIX + '-toast-styles';
      styleEl.textContent = [
        '.' + EODS_PREFIX + '-toast-container { position: fixed; z-index: ' +
          'var(--z-toast, 1080); display: flex; flex-direction: column; gap: var(--space-2, 0.5rem); ' +
          'pointer-events: none; max-width: 380px; width: 100%; }',
        '.' + EODS_PREFIX + '-toast-container--top-right { top: var(--space-4, 1rem); right: var(--space-4, 1rem); }',
        '.' + EODS_PREFIX + '-toast-container--top-left { top: var(--space-4, 1rem); left: var(--space-4, 1rem); }',
        '.' + EODS_PREFIX + '-toast-container--bottom-right { bottom: var(--space-4, 1rem); right: var(--space-4, 1rem); }',
        '.' + EODS_PREFIX + '-toast-container--bottom-left { bottom: var(--space-4, 1rem); left: var(--space-4, 1rem); }',
        '.' + EODS_PREFIX + '-toast-container--top-center { top: var(--space-4, 1rem); left: 50%; ' +
          'transform: translateX(-50%); }',
        '.' + EODS_PREFIX + '-toast-container--bottom-center { bottom: var(--space-4, 1rem); left: 50%; ' +
          'transform: translateX(-50%); }',
        '.' + EODS_PREFIX + '-toast { display: flex; align-items: flex-start; gap: var(--space-2, 0.5rem); ' +
          'padding: var(--space-3, 0.75rem) var(--space-4, 1rem); background-color: var(--color-surface-overlay, #fff); ' +
          'border: 1px solid var(--border-color-default, #e2e8f0); border-radius: var(--radius-md, 0.5rem); ' +
          'box-shadow: var(--shadow-lg, 0 10px 15px rgba(0,0,0,0.1)); pointer-events: auto; ' +
          'transform: translateY(-10px); opacity: 0; transition: transform var(--transition-base, 250ms ease), ' +
          'opacity var(--transition-base, 250ms ease); }',
        '.' + EODS_PREFIX + '-toast--visible { transform: translateY(0); opacity: 1; }',
        '.' + EODS_PREFIX + '-toast__icon { flex-shrink: 0; font-size: 1.125rem; }',
        '.' + EODS_PREFIX + '-toast--success .' + EODS_PREFIX + '-toast__icon { color: var(--color-success-500); }',
        '.' + EODS_PREFIX + '-toast--warning .' + EODS_PREFIX + '-toast__icon { color: var(--color-warning-500); }',
        '.' + EODS_PREFIX + '-toast--danger .' + EODS_PREFIX + '-toast__icon { color: var(--color-danger-500); }',
        '.' + EODS_PREFIX + '-toast--info .' + EODS_PREFIX + '-toast__icon { color: var(--color-info-500); }',
        '.' + EODS_PREFIX + '-toast__text { flex: 1; font-size: var(--font-size-sm, 0.875rem); ' +
          'color: var(--eods-text-primary); }',
        '.' + EODS_PREFIX + '-toast__dismiss { flex-shrink: 0; background: none; border: none; cursor: pointer; ' +
          'font-size: 1.25rem; color: var(--color-neutral-400); padding: 0; line-height: 1; }',
        '.' + EODS_PREFIX + '-toast__dismiss:hover { color: var(--color-neutral-600); }',
        '.' + EODS_PREFIX + '-loading-overlay { position: absolute; inset: 0; display: flex; align-items: center; ' +
          'justify-content: center; background-color: rgba(255,255,255,0.7); z-index: var(--z-dropdown, 1000); ' +
          'border-radius: inherit; }',
        '.' + EODS_PREFIX + '-loading-overlay__content { display: flex; flex-direction: column; align-items: center; ' +
          'gap: var(--space-4, 1rem); }',
        '.' + EODS_PREFIX + '-loading-overlay__text { font-size: var(--font-size-sm, 0.875rem); ' +
          'color: var(--color-neutral-500); margin: 0; }'
      ].join('\n');
      document.head.appendChild(styleEl);
    }
  }

  // Initialize on DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', autoInit);
  } else {
    autoInit();
  }

  // ==========================================================================
  // Public API
  // ==========================================================================

  var api = {
    notify: notify,
    modal: modal,
    loading: loading,
    ajax: ajax,
    ig: ig,
    validation: validation,
    btn: btn,
    date: dateHelper,
    session: session,
    storage: storage,
    error: errorHandler,
    theme: theme,
    dom: dom,
    util: util,
    da: da
  };

  // Expose to global scope
  global[EODS_NS] = api;

  // AMD support
  if (typeof define === 'function' && define.amd) {
    define(function () { return api; });
  }

})(typeof window !== 'undefined' ? window : this);
