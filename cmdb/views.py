# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.shortcuts import HttpResponse
from django.shortcuts import render

# Create your views here.
from cmdb import models


def index(request):
    #return HttpResponse("hello world")
    print "sdfsgv"
    if request.method == 'POST':
        a = request.POST.get('image')
        models.imageModel.objects.create(image_key="1", image_value=" ")
        print (a)

    return render(request,"index.html",)
