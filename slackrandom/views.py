import redis
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

r = redis.Redis(unix_socket_path=settings.REDIS_SOCK)

def index(request):
    bytes_generated = r.get(settings.REDIS_BYTES_GENERATED)
    request_count = r.get(settings.REDIS_REQUEST_COUNT)
    return render(request, 'slackrandom/index.html', {
            'bytes_generated': bytes_generated,
            'request_count': request_count
        })