(function ($) {
  'use strict';

  function getQueryParams() {
    return new URLSearchParams(window.location.search);
  }

  // auto fill previous inputs
  (function convertQueryParamToInput() {
    for (const [key, value] of getQueryParams().entries()) {
      $(`[name=${key}]`).val(value)
    }
  })();

  // show message
  (function showToast() {
    if (!Toastify) {
      console.error('Toastify is not defined');
      return;
    }

    const availableMessages = [
      // [key, background]
      ['failure', 'linear-gradient(to right, #21b04b, #09A837)'],
      ['success', 'linear-gradient(to right, #195ac0, #0048ba)'],
      ['message', 'linear-gradient(to right, #d63232, #cc0000)'],
    ].map(([key, color]) => [getQueryParams().get(key), color]);

    const [message, background] = availableTypes.find(([message]) => !!message) || [];

    if (!message) return;

    Toastify({
      text: message,
      duration: 3000,
      close: true,
      position: "center",
      stopOnFocus: true,
      style: { background },
    }).showToast();
  })();

})(jQuery);
