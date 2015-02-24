import json

commands = json.loads(open('modules/staticcmds/files/commands.json').read())

def get(message):
    return {"text" : [commands[message["text"].lower()]["text"]], "photos" : []}
