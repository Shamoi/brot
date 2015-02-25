import json
import re

commands = json.loads(open('modules/staticcmds/files/commands.json').read())
add_command = re.compile('".+" *- *".+"')

def get(message):
    if add_command.match(message["text"].lower()):
        commands_adding_file = open('modules/staticcmds/files/commands.json', 'w')
        question = message["text"].split('"')[1]
        answer = message["text"].split('"')[3]
        commands.update({question.lower() : {"text" : answer, "photo" : ""}})
        commands_adding_file.write(json.dumps(commands))
        commands_adding_file.close()
        return {"text" : ["Готово, команда добавлена"], "photos" : []}
    else:
        print (commands[message["text"].lower()]["photo"])
        return {"text" : [commands[message["text"].lower()]["text"]], "photos" : [commands[message["text"].lower()]["photo"]]}
