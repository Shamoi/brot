import re

sur = re.compile('сур|((хочу )?упороться)')

def check(message):
    if sur.match(message.lower()):
        return True
    else:
        return False
