angular.module('POA', ['ngResource']);
function GameCtrl($scope, $resource) {
    var GameService = $resource('../game');
    function fill() {
        $scope.games = GameService.get();
    }
    fill();
    setInterval(fill, 5000);
}


