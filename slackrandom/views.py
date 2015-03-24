import redis
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

r = redis.Redis(unix_socket_path=settings.REDIS_SOCK)

def index(request):
    bytes_generated = r.get(settings.REDIS_BYTES_GENERATED)
	return HttpResponse(bytes_generated);
