(function () {
  'use strict';

  angular
    .module('frontendApp')
    .run(frontendRun);

  frontendRun.$inject = ['$rootScope', '$log', '$state', '$cookies'];
  function frontendRun($rootScope, $log, $state, $cookies) {
  }
})();
