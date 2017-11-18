(function () {
    'use strict';

    angular
        .module('frontendApp.verify')
        .controller('VerifyController', VerifyController);

    VerifyController.$inject = [
        '$state',
        '$stateParams',
        '$scope',
        '$rootScope',
        '$log',
        'LTS',
    'NotificationHandler'];

    function VerifyController($state, $stateParams, $scope, $rootScope, $log, LTS, NotificationHandler ) {
        var vm = this;
        $rootScope.pageTitle = "";

        vm.fileAddress = $stateParams.address;


        vm.explorerUrl = "https://www.blocktrail.com/tBTC"; //https://blockchain.info/

        var promise = LTS.verify(vm.fileAddress);
        promise.success(function (result) {
            vm.fileInfo = result;
            if (vm.fileInfo.status === "confirmed" && vm.fileInfo.confirmations >= 6) {
                vm.fileInfo.message = "Strong Confirmation";
                vm.fileInfo.status = "strong confirmed";
            } else if (vm.fileInfo.status === "confirmed") {
                vm.fileInfo.message = "Confirmed";
            } else if (vm.fileInfo.status === "unconfirmed") {
                vm.fileInfo.message = "Pending Confirmation";
            } else if (vm.fileInfo.status === "unknown") {
                vm.fileInfo.message = "File Not Timestamped";
            } else {
                vm.fileInfo.message = "Unknown Error";
            }
        }).error(function (error) {
            NotificationHandler.error(error);
        });

        /*
        vm.fileInfo = {
            status: "unconfirmed",
            taddress: vm.fileAddress,
            txid: "fc12dfcb4723715a456c6984e298e00c479706067da81be969e8085544b0ba08",
            confirmations: 10,
            received: 1508257515,
            confirmed: 1508257515,
            block_height: 400000,
            block_hash: "000000000000000004ec466ce4732fe6f1ed1cddc2ed4b328fff5224276e3f6f"
        };
        */

        vm.back = function () {
            $state.go('main.timestamp');
        };


        vm.timestamp = function() {
            console.log("timestamping")
            var promise = LTS.timestamp(vm.fileAddress);
            promise.success(function (result) {
                $state.reload();
            }).error(function (error) {
                NotificationHandler.error(error);
            });
        };

    }
})();
