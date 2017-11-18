(function(angular, undefined) {
  "use strict";

  angular.module('frontendApp.config', [])

    .constant('BACKEND_API', 'http://128.131.169.35:8080/')

      //.constant('BACKEND_API', 'http://localhost:5000/')
    .constant('VERSION_INFO', {version: '0.0.1', build: 'test build'})

    .constant('DEBUG', true)

  ;
})(angular);
