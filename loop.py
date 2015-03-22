from vk_functions import get_message, send_message
import re

last_message_id = get_message()['id']

modules = [
    ('test', re.compile('!(тест|test)'))
]

imported_modules = {}
for module in modules:
    try:
        imported_modules.update({
            module[0]: {
                'object': __import__('modules.{name}'.format(name=module[0])),
                'regexp': module[1]
            }
        })
    except ImportError as error:
        print('Не удается импортировать модуль "{module}"'.format(
            module=module[0]
        ))
        print(error)
        continue


def loop():
    while True:
        message = get_message(
            last_message_id=last_message_id
        )
        if message is not None:
            answer = parse_message(message)
            send_message(message=answer['text'],
                         attachments=answer['attachments'],
                         type=message['type'],
                         send_to=message['chat'] if message['type'] == 'chat'
                         else message['sender_id']
            )


def parse_message(message):
    for parsing_module in imported_modules:
        print(message['text'])
        if imported_modules[parsing_module]['regexp'].match(message['text']):
            return imported_modules[parsing_module]['object'].get()


loop()  # Starting loop