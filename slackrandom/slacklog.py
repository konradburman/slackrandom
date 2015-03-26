import logging
from django.conf import settings

# Import Redis if enabled
if settings.REDIS_ENABLED: 
    import redis
    r = redis.Redis(unix_socket_path=settings.REDIS_SOCK)

log = logging.getLogger('slackrandom.info')
log_error = logging.getLogger('slackrandom.error')
log_request = logging.getLogger('slackrandom.request')

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

def request(data):
    if not data: return

    log_request.info(data)