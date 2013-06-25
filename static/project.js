angular.module('POA', ['ngResource']);
function TodoCtrl($scope, $resource) {
    $scope.todos = $resource('../game').query();
}

