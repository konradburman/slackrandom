import json
import logging
import random
import uuid
from datetime import datetime
from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

import slacklog

random255 = lambda: random.SystemRandom().randint(0,255)

@csrf_exempt
def slackrandom(request):
    responseData = ""
    statusCode = 200

    try:
        requestData = {}

        requestData['token'] = str(request.POST['token'])
        requestData['team_id'] = str(request.POST['team_id'])
        requestData['team_domain'] = str(request.POST['team_domain'])
        requestData['channel_id'] = str(request.POST['channel_id'])
        requestData['channel_name'] = str(request.POST['channel_name'])
        requestData['user_id'] = str(request.POST['user_id'])
        requestData['user_name'] = str(request.POST['user_name'])
        requestData['command'] = str(request.POST['command'])
        requestData['text'] = str(request.POST['text'])

        slacklog.request(requestData)

        requestWords = requestData['text'].split()

        if len(requestWords) == 0:
            responseData = generate_randomint(0, 100)
        elif len(requestWords) == 1:
            responseData = process_single(requestWords)
        elif len(requestWords) == 2:
            responseData = process_double(requestWords)
        elif len(requestWords) == 3:
            responseData = process_triple(requestWords)
    except Exception, e:
        statusCode = 500
        slacklog.error("slackrandom", e)

    return HttpResponse(responseData, status = statusCode)

def process_single(words):
    word = words[0].lower()

    try:
        word = int(word)
    except Exception, e:
        pass

    if word == "uuid":
        return generate_uuid()
    elif word == "coin":
        return generate_coin(1)
    elif word == "dice":
        return generate_dice(1)
    elif word == "color" or word == "colour":
        return generate_colour()
    elif isinstance(word, int):
        return generate_randomint(0, word)

    return ""

def process_double(words):
    try:
        words[0] = words[0].lower()
        words[0] = int(words[0])
    except Exception, e:
        pass

    try:
        words[1] = words[1].lower()
        words[1] = int(words[1])
    except Exception, e:
        pass

    if isinstance(words[0], int) and isinstance(words[1], int):
        return generate_randomint(words[0], words[1])
    elif words[0] == "coin":
        return generate_coin(cap_integer(words[1], 0, 100))
    elif words[0] == "dice":
        return generate_dice(cap_integer(words[1], 0, 100))
    elif words[0] == "byte":
        if words[1] == "hex":
            return generate_byte_hex(1)
        elif words[1] == "octal":
            return generate_byte_octal(1)
        elif words[1] == "binary":
            return generate_byte_binary(1)

    return ""

def process_triple(words):
    try:
        words[0] = words[0].lower()
        words[0] = int(words[0])
    except Exception, e:
        pass

    try:
        words[1] = words[1].lower()
        words[1] = int(words[1])
    except Exception, e:
        pass

    try:
        words[2] = cap_integer(int(words[2].lower()), 0, 10000)
    except Exception, e:
        pass

    if words[0] == "byte":
        if words[1] == "hex":
            return generate_byte_hex(words[2])
        elif words[1] == "octal":
            return generate_byte_octal(words[2])
        elif words[1] == "binary":
            return generate_byte_binary(words[2])

    return ""

def generate_randomint(a, b):
    integer = random.SystemRandom().randint(a, b)
    
    slacklog.info("generate_randomint", integer)

    return integer

def generate_uuid():
    genuuid = str(uuid.uuid4())

    slacklog.info("generate_uuid", genuuid)

    return genuuid

def generate_coin(coin):
    gen_coin = generate_coin_recursive("", coin)

    slacklog.info("generate_coin", gen_coin)

    return gen_coin

def generate_coin_recursive(gen_coin, coin):
    if coin == 0: return gen_coin

    return generate_coin_recursive(("Heads" if random.SystemRandom().randint(0, 1) == 1 else "Tails") + " " + gen_coin, coin - 1).strip()

def generate_dice(dice):
    gen_dice = generate_dice_recursive("", dice)

    slacklog.info("generate_dice", gen_dice)

    return gen_dice

def generate_dice_recursive(gen_dice, dice):
    if dice == 0: return gen_dice

    return generate_dice_recursive(str(random.SystemRandom().randint(1, 6)) + " " + gen_dice, dice - 1).strip()

def generate_colour():
    gen_colour = '#{:02x}{:02x}{:02x}'.format(random255(), random255(), random255())

    slacklog.info("generate_colour", gen_colour)

    return gen_colour

def generate_byte_hex(hex):
    gen_hex = ""

    for i in xrange(hex):
        gen_hex = '{:s}{:02x} '.format(gen_hex, random255())

    slacklog.info("generate_byte_hex", gen_hex)

    return gen_hex

def generate_byte_octal(octal):
    gen_octal = ""

    for i in xrange(octal):
        gen_octal = '{:s}{:03o} '.format(gen_octal, random255())

    slacklog.info("generate_byte_octal", gen_octal)

    return gen_octal

def generate_byte_binary(binary):
    gen_binary = ""

    for i in xrange(binary):
        gen_binary = '{:s}{:08b} '.format(gen_binary, random255())

    slacklog.info("generate_byte_binary", gen_binary)

    return gen_binary

def cap_integer(value, lower, upper):
    value = upper if value > upper else value
    value = lower if value < lower else value

    return value