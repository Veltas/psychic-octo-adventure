angular.module('POA', ['ngResource']);
function GameCtrl($scope, $resource) {
    var GameService = $resource('../game/:gameId');
    $scope.fill = function() {
        $scope.games = GameService.get();
    }
    $scope.fill();
    setInterval($scope.fill, 5000);

    $scope.removeGame = function(id) {
        GameService.delete({'gameId': id});
        $scope.fill();
    }
}



