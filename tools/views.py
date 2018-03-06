from __future__ import absolute_import, unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from .tasks import hello_world
# Create your views here.

def test_hello(request):
    r = hello_world.delay(1, 2)
    result = 'task done: {}'.format(r.get())
    return HttpResponse(result)
