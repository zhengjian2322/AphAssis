# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from django.shortcuts import render
from upload.models import Ques
# Create your views here.

index = 0

def show(request):
	index = 0
	all_ques = Ques.objects.all()
	questions = list(all_ques)
	number = len(questions)
	question = questions[index]
	return render(request,'show/showImg.html',{"Question":question})


def index(request):
	return render(request,'show/index.html')

def get_next(request):
	index += 1
	return HttpResponse("Success")



