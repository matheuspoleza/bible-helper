define(['app'], function(app){
  app.controller('FirstPageController', function($scope, $http){
    $scope.message = 'Tema: Namoro';
    $http.get('/api/namoro').then(function(res){
      $scope.message = res.data;
    });
  });
});
