import re

night = re.compile('тьма')

def check(message):
    if night.match(message.lower()):
        return True
    else:
        return False
