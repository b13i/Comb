from django.db import models
from django import forms

# Create your models here.
class OcrWrapper(models.Model):
	pdf = models.FileField(upload_to='media/')

class UploadFileForm(forms.Form):
	file = forms.FileField()
	
