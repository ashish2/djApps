// AngularJs Needed
// Works on top of AngularJs

var app = angular.module("MyApp", []);
app.config(function($interpolateProvider) {
	$interpolateProvider.startSymbol('{$');
	$interpolateProvider.endSymbol('$}');
});

