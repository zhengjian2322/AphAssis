from django.shortcuts import render
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
import random
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from upload.models import Ques, guide
from django.http import HttpResponse, JsonResponse
# Create your views here.

def makeSet(request):
	return render(request,'makeSet/makeSet.html')

@csrf_exempt
def get_all(request):
	questions = list(Ques.objects.all())
	length = len(questions)
	question = questions[number]
	ans = {}
	ans.update("length": length)	
	for i in range(length):
		ques = str(question.question)
		imageA = str(question.imageA)
		DesA = str(question.DesA)
		imageB = str(question.imageB)
		DesB = str(question.DesB)
		imageC = str(question.imageC)
		DesC = str(question.DesC)
		imageD = str(question.imageD)
		DesD = str(question.DesD)
		voice = str(question.voice)
		ans.update(str(i): {"namee":ques, "imageA":imageA, "DesA":DesA,
						 "imageB":imageB, "DesB":DesB, "imageC":imageC,
						 "DesC":DesC, "imageD":imageD, "DesD":DesD,
						 "voice":voice})	
		
	return JsonResponse(ans)

