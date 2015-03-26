from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.conf import settings

# Import Redis if enabled
if settings.REDIS_ENABLED: 
    import redis
    r = redis.Redis(unix_socket_path=settings.REDIS_SOCK)

import slacklog

def index(request):
    return redirect(settings.SLACKRANDOM_URL_GITHUB)
    

def stats(request):
    responseData = {}
    
    if settings.REDIS_ENABLED: 
        try:
            responseData['bytesGenerated'] = r.get(settings.REDIS_BYTES_GENERATED)
            responseData['requestCount'] = r.get(settings.REDIS_REQUEST_COUNT)
        except Exception, e:
            slacklog.error("stats", e)

    return JsonResponse(responseData)