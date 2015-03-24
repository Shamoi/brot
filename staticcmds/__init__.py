import re
import redis
import json

static_cmds = redis.StrictRedis(host='localhost', port=6379, db=0)
expression = re.compile('"(.+)" ?- ?"(.*)"', re.IGNORECASE)

delete_symbols = ['?', '.', ',', '!']


def get(message):
    read_command = static_cmds.get(prepare_command(message['text'].lower()))
    if read_command:
        read_command = json.loads(read_command.decode('utf-8'))
        return {
            'text': read_command['text'],
            'attachments': read_command['attachments']
        }
    else:
        adding_command = expression.search(message['text'])
        if adding_command:
            static_cmds.set(
                adding_command.group(1).lower(),
                json.dumps(
                    {
                        'text': prepare_command(adding_command.group(2)),
                        'attachments': message['attachments']
                    })
            )
            return {'text': 'Команда "{}" добавлена'.format(adding_command.group(1)),
                    'attachments': []}
        else:
            return None


def prepare_command(command):
    for sym in delete_symbols:
        command.replace(sym, '')
    return command
