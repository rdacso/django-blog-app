# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http.response import HttpResponse
from django.template import Context, loader
from .models import Tag

def homepage(request):
    tag_list = Tag.objects.all()
    template = loader.get_template('organizer/tag_list.html')
    context = {'tag_list':tag_list}
    output = template.render(context)
    return HttpResponse(output)
