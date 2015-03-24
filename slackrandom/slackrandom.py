import json
import random
from datetime import datetime
from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def slackrandom(request):
    responseData = ""
    requestToken = request.POST['token']
    requestTeamId = request.POST['team_id']
    requestTeamDomain = request.POST['team_domain']
    requestChannelId = request.POST['channel_id']
    requestChannelName = request.POST['channel_name']
    requestUserId = request.POST['user_id']
    requestUserName = request.POST['user_name']
    requestCommand = request.POST['command']
    requestText = request.POST['text']
    systemRandom = random.SystemRandom()

    responseData = systemRandom.randomint(0, 100)


    return HttpResponse(responseData)