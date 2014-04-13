from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import condition
from ocr_magic import runner

# Create your views here.
def index(request):
	return render(request, 'pdfocr/index.html')

@csrf_exempt
def upload(request):
	if request.method == 'POST':
		file_contents = request.FILES
		pdf_name = str(file_contents['user-pdf'])
		
		text_array = runner.pdf_to_text(pdf_name)	
		print 'text_array: ' + str(text_array)
		text = ''.join(text_array)
		context = { 'text': text }

		# png_filepaths = runner.pdf_to_pnglist(pdf_name)
		# return StreamingHttpResponse(request, png_filepaths)
		# return stream_response(request)
		
	
		if file_contents:
			return render(request, 'pdfocr/results.html', context)
		else:
		 	# TODO: Graceful failure
		 	return HttpResponse('Failed to upload file. Try again.')



#def stream_response(request, png_filepaths):
 #   return StreamingHttpResponse(stream_response_generator(png_filepaths))

#def stream_response_generator(png_filepaths):
#	print 'HERE2'
#	yield "<html><body>\n"
#	for index, path in enumerate(png_filepaths):
#		text = runner.ocr(path)
#		print 'CONVERTED ' + text
#		yield "<div>------ PAGE {}------\n{}\n</div>".format(index, text)
#		time.sleep(1)
#	yield "</body></html>\n"


#@condition(etag_func=None)
#def stream_response(request):
#    resp = HttpResponse( stream_response_generator(), mimetype='text/html')
 #   return resp
#
#def stream_response_generator():
 #   yield "<html><body>\n"
  #  for x in range(1,11):
   #     yield "<div>%s</div>\n" % x
    #    yield " " * 1024  # Encourage browser to render incrementally
     #   time.sleep(1)
    #yield "</body></html>\n"
