# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse,Http404, HttpResponseRedirect
from Records.forms import *
from Records.models import *

# Create your views here.
def index(request):
    """
    displays index page
    :param request: http request
    :return: http request
    """
    return render(request, 'index.html' )




def create(request):

    if request.method == 'POST':
        form = RecordsForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data

            newRecord = Records.objects.create(name = cd['name'], emailAdd= cd['email'])
            newRecord.save()

            return HttpResponseRedirect('/create/success/')

    else:
        form = RecordsForm()

    return render(request, 'create.html', {'form':form })

# once record is successfully created
def create_success(request):

    return render(request, 'success.html')


def listRecords(request):

    recordsList = Records.objects.all()

    return render( request, 'list.html', {'recList':recordsList})

