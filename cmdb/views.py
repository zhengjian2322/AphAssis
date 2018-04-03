# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import random

from PIL import Image
from django.http import HttpResponse
from django.shortcuts import HttpResponse
from django.shortcuts import render

# Create your views here.
from cmdb import models
from cmdb.models import IMG


def upload_file(request):
    ctx = {}
    i=0
    if request.method == 'POST':
        for key, value in request.FILES.iteritems():

           img = Image.open(value)

           a=value
           img.save(value.name)
           print key
    return render(request, "upload_file.html", ctx)
    '''my_form = FileUploadForm(request.POST, request.FILES)
        if my_form.is_valid():
            f = my_form.cleaned_data['my_file']
            handle_uploaded_file(f)
        return HttpResponse('Upload Success')
    else: my_form = FileUploadForm()
    return render(request, 'upload_file.html', {'form': my_form})

def handle_uploaded_file(f):
        with open(f.name, 'wb+') as destination:
            for chunk in f.chunks(): destination.write(chunk) '''

