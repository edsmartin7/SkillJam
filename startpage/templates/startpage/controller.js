angular.module('app').controller('ctrl', function($scope){
})

var app = angular.module('app', []);
app.controller('formControl', function($scope){
   $scope.username = "The User";
   $scope.password = "The Password";
});

