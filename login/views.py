from django.contrib.auth import authenticate
import json
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template.loader import get_template

from login.models import register

def nregister(request):
    if request.method == 'POST':
        type = request.POST.get('type', None)
        if (type =="1" ):
            res_username = request.POST.get('res_username', None)
            res_password = request.POST.get('res_password', None)
            res_email = request.POST.get('res_email', None)
            a = register.objects.filter(Q(res_username=res_username))
            flag = 0
            for e in a:
                flag = 1
                break
            if (flag == 1):
                return HttpResponse("failed")
            else:
                new_register = register(
                    res_username=res_username,
                    res_password=res_password,
                    res_email=res_email
                )
                new_register.save()
                return HttpResponse("success")
        elif (type == "2"):
            username = request.POST.get('username', None)
            password = request.POST.get('password', None)
            m = register.objects.filter(res_username=username, res_password=password)
            if m:
                resp = {'status':'failed' , 'reason': '登录成功'}
                t = get_template('/AphAssis-master/templates/index.html')
                return render('index.html')
            else:
                resp = {'status': 'failed', 'reason': '用户名或密码错误'}
                return HttpResponse(json.dumps(resp), content_type="application/json")
    return render(request, 'login/register.html')