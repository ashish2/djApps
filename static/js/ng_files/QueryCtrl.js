// AngularJs Needed
// Works on top of AngularJs

app.controller("QueryCtrl", function($scope, $http){
	$scope.selectedPerson = 0;
	$scope.selectedGenre = null;
	$scope.search_results = [];
	$scope.people = [
		{
			id: 0,
			name: 'Leon',
			music: [
				'Rock',
				'Metal',
				'Dubstep',
				'Electro'
			]
		},
		{
			id: 1,
			name: 'Chris',
			music: [
				'Indie',
				'Drumstep',
				'Dubstep',
				'Electro'
			]
		},
		{
			id: 2,
			name: 'Harry',
			music: [
				'Rock',
				'Metal',
				'Thrash Metal',
				'Heavy Metal'
			]
		},
		{
			id: 3,
			name: 'Allyce',
			music: [
				'Pop',
				'RnB',
				'Hip Hop'
			]
		}
	];
	
	// Filter by, on selecting `No` will remove the key of Languages from params, else, it will set key Languages with the id
	$scope.params = {
		format: "json",
		offset: 0,
		//limit: 1,
		// Filters
		//languages: 0,
		//categories: 0,
		// Sorting
		//order_by: "length",
	};
	
	$scope.prepareFilter = function(e) {
		params = $scope.params;
		$scope.sanitizeParams();
		// Serialize params
		// Send params_str
		$scope.init();
	};
	
	$scope.sanitizeParams = function() {
		// FTM
		if ($scope.params.languages == "")
			delete $scope.params.languages;
		if ($scope.params.categories == "")
			delete $scope.params.categories;
	};
	
	// Speech
	var recognition;
	$scope.initSpeech = function() {
		recognition = new webkitSpeechRecognition();
	};
	
	$scope.speechRecordingStart = function() {
		recognition.onresult = $scope.speechResult;
		recognition.start();
	};
	
	$scope.speechResult = function(ev) {
		res = ev.results[0][0].transcript;
		console.log("res");
		console.log(res);
	};
	
	// Speech-
	
	$scope.stripHtml = function(str) {
		return str.replace(/<\/?[^>]+(>|$)/g, "");
	};
	
	$scope.init = function() {
		//$scope.sanitizeParams();
		//params = $.param($scope.params);
		//params = decodeURIComponent(params);
		////console.log("params", params);
		//url = '/api/v1/movies/?'+	params;
		//$http.get(url)
		//.success(function(data){
			//$scope.res = data;
			//$scope.movies = $scope.res.objects;
		//});
	};
	
	
});


