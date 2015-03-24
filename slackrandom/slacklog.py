import logging

log = logging.getLogger('slackrandom.info')

def info(source, message):
    log.info(source + "\t" + str(message))