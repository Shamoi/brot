from modules.time import check, get as time #import each module

def parse(message):
    if time.check(message):
        return time.get(messages)
