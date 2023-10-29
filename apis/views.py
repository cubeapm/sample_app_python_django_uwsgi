import requests
from django.core.cache import cache
from django.http import HttpResponse
from apis.models import User


def index(request):
    return HttpResponse("Hello")


def param(request, param):
    return HttpResponse("Got param {}".format(param))


def exception(request):
    raise Exception("Sample exception")


def api(request):
    requests.get('http://localhost:8000/apis/')
    return HttpResponse("API called")


def redis(request):
    cache.set('foo', 'bar')
    return HttpResponse("Redis called")


def mysql(request):
    return HttpResponse(User.objects.all())
