# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from upload.models import Ques
# Create your views here.

def show(request):
	all_ques = Ques.objects.all()
	questions = list(all_ques)
	question = questions[0]
	return render(request,'show/showImg.html',{"question":question})
