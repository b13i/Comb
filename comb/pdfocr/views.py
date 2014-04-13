from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from ocr_magic import runner

# Create your views here.
def index(request):
	return render(request, 'pdfocr/index.html')

@csrf_exempt
def upload(request):
	if request.method == 'POST':
		print 'Received a POST to upload/'
		file_contents = request.FILES
		pdf_name = str(file_contents['user-pdf'])
		print 'File: ' + str(file_contents)
		print 'user-pdf: ' + str(file_contents['user-pdf'])	
		print 'pdf_to_text: ' + str(runner.pdf_to_text)
		
		text_array = runner.pdf_to_text(pdf_name)	
		text = ''.join(text_array)
		context = { 'text': text }
	
		if file_contents:
			return render(request, 'pdfocr/results.html', context)
		else:
			# TODO: Graceful failure
			return HttpResponse('Failed to upload file. Try again.')
