angular.module('ListServices', ['ngResource']).
factory('ListItems', function($resource) {
    return $resource(
        '/backlift/data/itemlist/:id',  // URL template
        {id: '@id'},                    // default values
        {
            create: {method: 'POST'},
            update: {method: 'PUT'}
        }
    );
});

function TodoCtrl($scope) {
  $scope.todos = [
    {text:'learn angular', done:true},
    {text:'build an angular app', done:false}];

  $scope.addTodo = function() {
    $scope.todos.push({text:$scope.todoText, done:false});
    $scope.todoText = '';
  };

  $scope.remaining = function() {
    var count = 0;
    angular.forEach($scope.todos, function(todo) {
      count += todo.done ? 0 : 1;
    });
    return count;
  };

  $scope.archive = function() {
    var oldTodos = $scope.todos;
    $scope.todos = [];
    angular.forEach(oldTodos, function(todo) {
      if (!todo.done) $scope.todos.push(todo);
    });
  };
}

