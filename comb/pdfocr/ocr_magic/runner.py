import subprocess
import os
from os import listdir
from os.path import isfile, join
from pytesser import *
import shutil
import time

def pdf_to_png(pdf_path, out_name):
        subprocess.check_output(['echo', '\n***** Converting from PDF to PNG *****'])
        subprocess.check_output(['echo', '***** PNGs temporarily saved in ' + out_name + ' *****'])
        subprocess.check_output(['convert', '-verbose', '-density',  '200', pdf_path, '-quality', '100', '-sharpen',  '0x1.0', out_name])

def get_path(filename):
	path = '/home/ubuntu/Comb/comb/media/' + filename 
        return normalize_path(path)

def normalize_path(path):
        if path[-4:] == '.pdf':
                return path
        else:
                print 'No pdf extension detected, adding .pdf extension to path...'
                return path + '.pdf'

def png_to_text(png_dir):
        print '\n***** Converting all PNGs in "' + png_dir + '" to text *****'

        only_png_filepaths = [ os.path.abspath(png_dir + os.path.sep + f) for f in listdir(png_dir) if isfile(join(png_dir, f)) and f.endswith('.png')]
        
        text_files = map(ocr, only_png_filepaths)
        return text_files

################################### Streaming jazz

def get_png_filepaths(png_dir):
        only_png_filepaths = [ os.path.abspath(png_dir + os.path.sep + f) for f in listdir(png_dir) if isfile(join(png_dir, f)) and f.endswith('.png')]
        return only_png_filepaths

def pdf_to_pnglist(filename):
        path = get_path(filename) 
       
        if os.path.isfile(path):
                # TODO: namespace pdfs and pngs (temp files?)
                out_temp_dir = os.path.dirname(path) + '/comb_images'
                if not os.path.exists(out_temp_dir):
                        os.makedirs(out_temp_dir)

                out_png = out_temp_dir + os.path.sep + os.path.basename(path)[:-4] + '.png'

                pdf_to_png(path, out_png)
                png_filepaths = get_png_filepaths(out_temp_dir)
                return png_filepaths
        else:
                print path + ' is not a valid path. Try again.'
                return None

###################################

def ocr(png_file_path):
        print "OCR'ing " + png_file_path
        return image_file_to_string(png_file_path, graceful_errors=True)

def remove_files(path):
        print 'Removing images in ' + os.path.abspath(path)
        shutil.rmtree(path)
       
def pdf_to_text(filename):
	path = get_path(filename) 
       
        if os.path.isfile(path):
		# TODO: namespace pdfs and pngs (temp files?)
                millis = int(round(time.time() * 1000))
                out_temp_dir = os.path.dirname(path) + '/comb_images/' + str(millis)
                if not os.path.exists(out_temp_dir):
                        os.makedirs(out_temp_dir)

                out_png = out_temp_dir + os.path.sep + os.path.basename(path)[:-4] + '.png'

                print 'out_temp_dir: ' + str(out_temp_dir)
                print 'out_png' + str(out_png)

                pdf_to_png(path, out_png)
                text_files = png_to_text(out_temp_dir)
                remove_files(out_temp_dir)
		return text_files
        else:
                print path + ' is not a valid path. Try again.'
                return None
