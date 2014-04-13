var app = angular.module('compApp', []);

app.controller('MainCtrl', function($scope) {
	console.log('Current controller: MainCtrl');

	function chooseFile() {
		$('#choose-pdf').change(function() {
			// File has now been selected
			$('#pdf-button').text('Convert to Text')
			$('#pdf-button').attr('onclick', 'submitFile();')
			$('#change-pdf').show();
		})
		$("#choose-pdf").click();
	}

	function submitFile() {
		$('.header').addClass('shrink');
		$('#pdf-button').addClass('shrink');
		$('span').addClass('shrink');

		$('#submit-pdf').click();
		$('#pdf-button').text('Cancel');
		$('#pdf-button').css('background', '#ea8557');
		$('#change-pdf').hide();
	}

	function changePDF() {
		$('#pdf-button').attr('onclick', 'chooseFile();');
		$('#pdf-button').click();
	}
});

app.config(function($routeProvider) {
	$routeProvider.when('/', {
		controller: 'MainCtrl',
		templateUrl: '/partials/pdf_upload.html'
	});
})

