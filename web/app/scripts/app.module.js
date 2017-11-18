(function () {
    'use strict';
    /**
     * @ngdoc overview
     * @name frontend
     * @description
     * # frontend
     *
     * Main module of the application.
     */
    angular
        .module('frontendApp', [

            // bower and dependencies
            'ngAnimate',
            'ngCookies',
            'ngResource',
            'ngRoute',
            'ngSanitize',
            'ngTouch',
            'ui.router',
            'angular.filter',
            'toaster',
            'ngDialog',
            'ui.bootstrap',
            'ngWebSocket',
            'ngFileUpload',


            // config
            'frontendApp.config',

            // rest

            'frontendApp.rest',

            // own modules
            'frontendApp.timestamp',
            'frontendApp.verify',
            'frontendApp.notification'




        ])
    ;

})();


