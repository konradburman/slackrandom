import logging
import redis
from django.conf import settings

log = logging.getLogger('slackrandom.info')
log_error = logging.getLogger('slackrandomerror.info')
r = redis.Redis(unix_socket_path=settings.REDIS_SOCK)

def info(source, message):
    log.info(source + "\t" + str(message))
    bytes_generated(str(message))

def error(source, message):
    log_error.error(source + "\t" + str(message))

def bytes_generated(message):
    if not settings.REDIS_ENABLED: return

    pipe = r.pipeline()
    pipe.incrby(settings.REDIS_BYTES_GENERATED, len(message.replace(" ", "")))
    pipe.incrby(settings.REDIS_REQUEST_COUNT, 1)
    pipe.execute()