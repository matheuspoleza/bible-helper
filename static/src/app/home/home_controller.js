define(['app'], function (app) {
  app.controller('HomeController', function ($scope, $http) {
    $scope.message = 'Home Page';
    $http.get('/api').then(function(res){
      $scope.message = res.data;
    })
  });
});
