# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render



def index(request):
    context = {'title': 'Mon super titre'}
    return render(request, 'market/index.html', context)
    