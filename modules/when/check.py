import re

when_text = re.compile('когда .+')

def check(message):
    if when_text.match(message.lower()):
        return True
    else:
        return False
