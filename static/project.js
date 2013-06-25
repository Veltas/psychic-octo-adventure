angular.module('POA', ['ngResource']);
function GameCtrl($scope, $resource) {
    var GameService = $resource('../game');
    $scope.fill = function() {
        $scope.games = GameService.get();
    }
    $scope.fill();
    setInterval($scope.fill, 5000);
}


