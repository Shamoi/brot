import json

commands = json.loads(open('modules/staticcmds/files/commands.json').read())

def check(message):
    if message.lower() in commands:
        return True
    else:
        return False
