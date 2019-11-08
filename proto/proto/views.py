from django.http import HttpResponse


def event_handler(request):
    return HttpResponse('Hello, World!')
