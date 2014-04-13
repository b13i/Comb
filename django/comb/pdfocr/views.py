from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
	return render(request, 'pdfocr/index.html')

@csrf_exempt
def upload(request):
	if request.method == 'POST':
		print 'Received a POST to upload/'
		file_contents = request.FILES
		print 'File: ' + str(file_contents)
		if file_contents:
			return HttpResponse('Successfully uploaded file!')
		else:
			return HttpResponse('Failed to upload file. Try again.')
	if request.method == 'GET':
		return HttpResponse('Yo my brotha this is a get')
