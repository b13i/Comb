var app = angular.module('app', []);

app.controller('MainCtrl', function($scope) {
	console.log('Current controller: MainCtrl');

	$scope.submitFile = function(files) {
	    var fd = new FormData();
	    // Take the first selected file
	    fd.append("file", files[0]);

	    $http.post('/upload/', fd, {
	        withCredentials: true,
	        headers: {'Content-Type': undefined },
	        transformRequest: angular.identity
	    }).success(function(data, status, headers, config) {
	    	console.log("SUCCESS");
	    }).error(function() {
	    	console.log("ERROR")
	    });

	    $('.header').addClass('shrink');
		$('#pdf-button').addClass('shrink');
		$('span').addClass('shrink');

		$('#submit-pdf').click();
		$('#pdf-button').text('Cancel');
		$('#pdf-button').css('background', '#ea8557');
		$('#change-pdf').hide();
	};

	$scope.chooseFile = function() {
		$('#choose-pdf').change(function() {
			// File has now been selected
			$('#pdf-button').text('Convert to Text')
			$('#pdf-button').attr('onclick', 'submitFile();')
			$('#change-pdf').show();
		})
		$("#choose-pdf").click();
	}

	// $scope.submitFile = function() {
	// 	$('.header').addClass('shrink');
	// 	$('#pdf-button').addClass('shrink');
	// 	$('span').addClass('shrink');

	// 	$('#submit-pdf').click();
	// 	$('#pdf-button').text('Cancel');
	// 	$('#pdf-button').css('background', '#ea8557');
	// 	$('#change-pdf').hide();
	// }

	$scope.changePDF = function() {
		$('#pdf-button').attr('onclick', 'chooseFile();');
		$('#pdf-button').click();
	}
});

app.config(function($routeProvider) {
	$routeProvider.when('/', {
		controller: 'MainCtrl'
	});
});

