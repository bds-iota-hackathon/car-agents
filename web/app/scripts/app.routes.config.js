(function () {
    'use strict';

    angular
        .module('frontendApp')
        .config(frontendRouteConfig)
    ;

    frontendRouteConfig.$inject = ['$urlRouterProvider', '$stateProvider'];
    function frontendRouteConfig($urlRouterProvider, $stateProvider) {

        $urlRouterProvider.otherwise('/timestamp');

        $stateProvider
            .state('main', {
                url: '/',
                abstract: true,
                templateUrl: 'views/main/main.html',
                controllerAs: 'vm'
            })
            .state('main.timestamp', {
                templateUrl: 'views/timestamp/timestamp.html',
                url: 'timestamp',
                controller: 'TimestampController',
                controllerAs: 'vm'
            })
            .state('main.verify', {
                templateUrl: 'views/verify/verify.html',
                url: 'verify/:address',
                controller: 'VerifyController',
                controllerAs: 'vm'
            });
    }

})();
