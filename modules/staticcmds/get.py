import json
import re

blocked = ["сева", "сева.", "!сева"]
commands = json.loads(open('modules/staticcmds/files/commands.json').read())
add_command = re.compile('".+" *- *".+"')

def get(message):
    if add_command.match(message["text"].lower()):
        return addCommand(message)
    else:
        return getCommand(message)


def addCommand(message):
    commands_adding_file = open('modules/staticcmds/files/commands.json', 'w')
    question = message["text"].split('"')[1].replace("?", "")
    answer = message["text"].split('"')[3]

    if question.lower() in blocked:
        commands_adding_file.write(json.dumps(commands))
        commands_adding_file.close()
        return {"text" : ["Команду нельзя изменять"], "photos" : []}

    commands.update({question.lower() : {"text" : answer, "photo" : message["attachment"]}})
    commands_adding_file.write(json.dumps(commands))
    commands_adding_file.close()
    return {"text" : ['Готово, команда "' + question + '" добавлена'], "photos" : []}

def getCommand(message):
    return {"text" : [commands[message["text"].lower().replace("?", "")]["text"]],
            "photos" : [commands[message["text"].lower().replace("?", "")]["photo"]]}
