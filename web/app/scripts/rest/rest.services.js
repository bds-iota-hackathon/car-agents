(function (angular, undefined) {
    'use strict';
    angular.module('frontendApp.rest', [])

        .service('LTS', function($http, $rootScope, BACKEND_API){
            var vm = this;

            vm.timestamp = function (addr) {
                return $http({
                    method: 'GET',
                    url: BACKEND_API + "ts/" + addr,
                    isArray: false
                });
            };

            vm.verify = function (addr) {
                return $http({
                    method: 'GET',
                    url: BACKEND_API + "vf/" + addr,
                    isArray: false
                });
            };

            vm.blockheight = function () {
                return $http({
                    method: 'GET',
                    url: "https://blockchain.info/q/getblockcount"
                });
            };
        });


})(angular);
