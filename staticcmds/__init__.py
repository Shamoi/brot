import re
import redis
import json

static_cmds = redis.StrictRedis(host='localhost', port=6379, db=0)
expression = re.compile('"(.+)" ?- ?"(.+)"', re.IGNORECASE)

def get(message):
    read_command = static_cmds.get(message['text'].lower())
    if read_command:
        read_command = read_command.decode('utf-8')
        return {
            'text': json.loads(read_command)['text'],
            'attachments': json.loads(read_command)['attachments']
        }
    else:
        adding_command = expression.search(message['text'])
        if adding_command:
            static_cmds.set(
                adding_command.group(1).lower(),
                json.dumps({
                    'text': adding_command.group(2),
                    'attachments': message['attachments']
                })
            )
            return {'text': 'Команда "{}" добавлена'.format(adding_command.group(1)),
                    'attachments': []}
        else:
            return None

