import logging
import redis
from django.conf import settings

log = logging.getLogger('slackrandom.info')
r = redis.Redis(unix_socket_path=settings.REDIS_SOCK)

def info(source, message):
    log.info(source + "\t" + str(message))
    bytes_generated(str(message))

def bytes_generated(message):
    if not settings.REDIS_ENABLED: return
    
    r.incrby(settings.REDIS_BYTES_GENERATED, len(message.replace(" ", "")))