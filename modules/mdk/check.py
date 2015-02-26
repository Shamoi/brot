import re

mdk = re.compile('мдк|mdk')

def check(message):
    if mdk.match(message.lower()):
        return True
    else:
        return False
