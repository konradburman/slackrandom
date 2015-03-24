import json
import logging
import random
import uuid
from datetime import datetime
from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

import slacklog

@csrf_exempt
def slackrandom(request):
    responseData = ""

    try:
        requestToken = request.POST['token']
        requestTeamId = request.POST['team_id']
        requestTeamDomain = request.POST['team_domain']
        requestChannelId = request.POST['channel_id']
        requestChannelName = request.POST['channel_name']
        requestUserId = request.POST['user_id']
        requestUserName = request.POST['user_name']
        requestCommand = request.POST['command']
        requestText = request.POST['text']
        requestWords = requestText.split()

        if len(requestWords) == 0:
            responseData = generate_randomint(0, 100)
        elif len(requestWords) == 1:
            responseData = process_single(requestWords)
        elif len(requestWords) == 2:
            responseData = process_double(requestWords)
    except Exception, e:
        pass

    return HttpResponse(responseData)

def process_single(words):
    word = words[0]

    if word == "uuid":
        return generate_uuid()
    elif isinstance(word, int):
        return generate_randomint(0, word)

    return ""

def process_double(words):
    if isinstance(words[0], int) and isinstance(words[1], int):
        return generate_randomint(words[0], words[1])

    return ""

def generate_randomint(min, max):
    integer = random.SystemRandom().randint(0, 100)
    
    slacklog.info("generate_randomint", integer)

    return integer

def generate_uuid():
    genuuid = str(uuid.uuid4())

    slacklog.info("generate_uuid", genuuid)

    return genuuid