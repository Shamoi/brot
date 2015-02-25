import json
import re

add_command = re.compile('".+" *- *".+"') #Regular expression for adding command

def check(message):
    commands = json.loads(open('modules/staticcmds/files/commands.json').read())
    if (message.lower() in commands) or add_command.match(message.lower()):
        return True
    else:
        return False
