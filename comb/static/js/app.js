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
	$('#pdf-button').text("OCR'ing");
	$('#pdf-button').css('background', '#ea8557');
	$('#change-pdf').hide();
	$('.loading').show();
}

function changePDF() {
	$('#pdf-button').attr('onclick', 'chooseFile();');
	$('#pdf-button').click();
}
