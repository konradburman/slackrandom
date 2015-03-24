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

    try:
        word = int(word)
    except Exception, e:
        pass

    if word == "uuid":
        return generate_uuid()
    elif word == "coin":
        return generate_coin()
    elif word == "dice":
        return generate_dice("", 1)
    elif isinstance(word, int):
        return generate_randomint(0, word)

    return ""

def process_double(words):
    try:
        words[0] = int(words[0])
    except Exception, e:
        pass

    try:
        words[1] = int(words[1])
    except Exception, e:
        pass

    if isinstance(words[0], int) and isinstance(words[1], int):
        return generate_randomint(words[0], words[1])
    elif words[0] == "dice" and words[1] >= 1:
        return generate_dice("", words[1])

    return ""

def generate_randomint(a, b):
    integer = random.SystemRandom().randint(a, b)
    
    slacklog.info("generate_randomint", integer)

    return integer

def generate_uuid():
    genuuid = str(uuid.uuid4())

    slacklog.info("generate_uuid", genuuid)

    return genuuid

def generate_coin():
    coin = "Heads" if random.SystemRandom().randint(0, 1) == 1 else "Tails"

    slacklog.info("generate_coin", coin)

    return coin

def generate_dice(gen_dice, dice):
    if dice != 0 or dice == "": gen_dice = generate_dice(str(random.SystemRandom().randint(1, 6)) + " " + gen_dice, dice - 1).strip()

    slacklog.info("generate_dice", gen_dice)

    return gen_dice