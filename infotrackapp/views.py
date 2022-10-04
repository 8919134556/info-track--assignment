from asyncio.windows_events import NULL
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404,reverse
from django.http import HttpResponse
from django.conf import settings
from django.template import loader
from django.shortcuts import render
from . models import *
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist




def home(request):
    data = Select_data.objects.all()
    demo = data.count()
    su = list(Select_data.objects.values_list('header5', flat=True))
    s = '| '.join(str(x) for x in su)
    if demo == 0:
        if request.method == 'POST':
            no = request.POST['no']
            header1 = request.POST['header1']
            header2 = request.POST['header2']
            header3 = request.POST['header3']
            header4 = request.POST['header4']
            header5 = request.POST['header5']
            header6 = request.POST['header6']
            data1 = Select_data.objects.create(no=no,header1=header1,header2=header2,header3=header3,
            header4=header4,header5=header5,header6=header6)
            data1.save()
            return redirect('home')
    elif request.method == 'POST':
        num = request.POST['no']
        obj = Select_data.objects.filter(no=num)
        if obj.exists():
            messages.error (request, "Already selected")
        else:
            if request.method == 'POST':
                no = request.POST['no']
                header1 = request.POST['header1']
                header2 = request.POST['header2']
                header3 = request.POST['header3']
                header4 = request.POST['header4']
                header5 = request.POST['header5']
                header6 = request.POST['header6']
                data1 = Select_data.objects.create(no=no,header1=header1,header2=header2,header3=header3,
                header4=header4,header5=header5,header6=header6)
                data1.save()
                return redirect('home')
    return render (request, './index.html', {'view' : data, 'view1' : demo, 'view2':s})


def delete(request, id):
    try:
        data = Select_data.objects.get(no=id)
        data.delete()
    except ObjectDoesNotExist:
        messages.error (request, "Please select correct one")
    return redirect('home')