(function () {
    'use strict';

    angular
        .module('frontendApp.timestamp')
        .controller('TimestampController', TimestampController);

    TimestampController.$inject = [
        '$state',
        '$scope',
        '$rootScope',
        '$log',
        '$filter',
        'LTS',
        'NotificationHandler'];
    function TimestampController($state, $scope, $rootScope, $log, $filter, LTS, NotificationHandler) {
        var vm = this;
        $rootScope.pageTitle = "Legal Timestamps (Demo)";

        vm.file = null;

        $scope.onFileSelect = function(files) {
            vm.file = files[0];
            $log.info(vm.file)
        };

        vm.timestamp = function() {
            var reader = new FileReader();
            reader.onload = function(e) {
                    $scope.$apply(function () {
                        var fileContents = reader.result;
                        var fileAddr = hashAndConvertToAddress(fileContents);

                        var promise = LTS.timestamp(fileAddr);
                        promise.success(function (result) {
                            $state.go('main.verify',{address:fileAddr});
                        }).error(function (error) {
                            NotificationHandler.error(error);
                        });

                    });
            };
            reader.readAsBinaryString(vm.file);
        };


        vm.verify = function(){
            var reader = new FileReader();
            reader.onload = function(e) {
                $scope.$apply(function () {
                    var fileContents = reader.result;
                    var fileAddr = hashAndConvertToAddress(fileContents);
                    console.log(fileAddr);

                    var promise = LTS.verify(fileAddr);
                    promise.success(function (result) {
                        $state.go('main.verify',{address:fileAddr});
                    }).error(function (error) {
                        NotificationHandler.error(error);
                    });

                });
            };
            reader.readAsBinaryString(vm.file);
        }


        /**
         * This function calculates the sha256 hash of the given file
         * and uses the result to generate a valid Bitcoin address (base58 ripemd160)
         * @param fileContents
         * @returns {*}
         */
        function hashAndConvertToAddress(fileContents) {
            var sha256 = lib.hashalg('sha256');
            var ripemd160 = lib.hashalg('rmd160');
            var address = lib.bitcoin.address;
            sha256.update(fileContents);
            ripemd160.update(sha256.digest());
            return address.toBase58Check(ripemd160.digest(), 0x6f);// 0x00 for mainnet; 0x6f for testnet
        }
    }
})();
