from django.http import HttpResponse

from . import api

def event_handler(request):
    print(request)
    print(request.POST)
    print(request.GET)
    print(request.body)
    return HttpResponse('Hello, World!')
