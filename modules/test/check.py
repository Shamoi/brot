import re

test = re.compile('!(тест|test)')

def check(message):
    if test.match(message.lower()):
        return True
    else:
        return False
