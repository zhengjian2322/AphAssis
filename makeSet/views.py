# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
import random
from copy import deepcopy
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
	#toList = []
	#toList.append(length)
	ans = {}
	ans["length"] = length
	for i in range(length):
		ans["ques" + str(i)] = str(questions[i].question)
		ans["imageA" + str(i)] = str(questions[i].imageA)
		ans["DesA" + str(i)] = str(questions[i].DesA)
		ans["imageB" + str(i)] = str(questions[i].imageB)
		ans["DesB" + str(i)] = str(questions[i].DesB)
		ans["imageC" + str(i)] = str(questions[i].imageC)
		ans["DesC" + str(i)] = str(questions[i].DesC)
		ans["imageD" + str(i)] = str(questions[i].imageD)
		ans["DesD" + str(i)] = str(questions[i].DesD)
		ans["voice" + str(i)] = str(questions[i].voice)
		#toList.append(deepcopy(ans))	
		
	return JsonResponse(ans)

