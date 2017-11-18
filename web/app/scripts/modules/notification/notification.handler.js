(function() {
    'use strict';

    angular.module('frontendApp.notification')
        .service('NotificationHandler', NotificationHandler);

    NotificationHandler.$inject = ['toaster', '$filter', '$log'];
    function NotificationHandler(toaster, $filter, $log) {
        var vm = this;

        vm.success = success;
        vm.info = info;
        vm.warn = warn;
        vm.error = error;

        function success(message) {
            $log.log("SUCCESS: " + message);
            toaster.pop({
                type:    'success',
                title:   'SUCCESS',
                body:    message,
                timeout: 3000
            });
        }

        function info(message) {
            $log.info("INFO: " + message);
            toaster.pop({
                type:    'info',
                title:   'INFO',
                body:    message,
                timeout: 3000
            });
        }

        function warn(message) {
            $log.warn("WARN: " + message);
            toaster.pop({
                type:    'warning',
                title:   'WARNING',
                body:    message,
                timeout: 3000
            });
        }

        function error(error) {
            var message = '';

            // if error.data, then errorMessage from backend
            if (error.data) { message = error.statusText; }
            // if answer not from backend
            else { message = error; }

            $log.error("ERROR: " + error);
            toaster.pop({
                type:    'error',
                title:   'ERROR',
                body:    message,
                timeout: 5000
            });
        }
    }
})();

