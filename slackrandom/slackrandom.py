import json
import redis
from datetime import datetime
from django.http import JsonResponse, Http404
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def slackrandom(request):
    responseData = {}
    responseData["text"] = "DONE"

    print request.POST['token']
    print request.POST['team_id']
    print request.POST['team_domain']
    print request.POST['channel_id']
    print request.POST['channel_name']
    print request.POST['user_id']
    print request.POST['user_name']
    print request.POST['command']
    print request.POST['text']

    return JsonResponse(responseData)