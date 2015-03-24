import json
import logging
import random
import uuid
from datetime import datetime
from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

from slackrandom import slacklog

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

    if requestText == "":
        responseData = generate_randomint(0, 100)
    elif requestText == "uuid":
        responseData = generate_uuid()

    return HttpResponse(responseData)

def generate_randomint(min, max):
    integer = random.SystemRandom().randint(0, 100)
    
    slacklog.info("generate_randomint", integer)

    return integer

def generate_uuid():
    genuuid = str(uuid.uuid4())

    slacklog.info("generate_uuid", genuuid)

    return genuuid