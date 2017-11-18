(function() {
  'use strict';

  angular
    .module('frontendApp')
    .config(frontendConfig)
  ;

  frontendConfig.$inject = [ '$httpProvider'];
  function frontendConfig($httpProvider) {


    // --- add postData to DELETE
    $httpProvider.defaults.headers.delete = { "Content-Type": "application/json;charset=utf-8" };
  }

})();
