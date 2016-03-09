// AngularJs Needed
// Works on top of AngularJs

var app = angular.module("MyApp", []);
app.config(function($interpolateProvider) {
	$interpolateProvider.startSymbol('{$');
	$interpolateProvider.endSymbol('$}');
});

// Filters
//app.filter('strip', function() {
	//
	//function stripHtml(input) {
		//return str.replace(/<\/?[^>]+(>|$)/g, "");
	//}
	//
//});



// Filters-
