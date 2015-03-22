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
                'object': __import__(name=module[0]),
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
    global last_message_id

    while True:
        message = get_message(
            last_message_id=last_message_id
        )
        if message is not None:
            last_message_id = message['id']
            answer = parse_message(message)
            if answer is not None:
                send_message(message=answer['text'],
                             attachments=answer['attachments'],
                             type=message['type'],
                             send_to=message['chat'] if message['type'] == 'chat'
                             else message['sender_id']
                )


def parse_message(message):
    for parsing_module in imported_modules:
        if imported_modules[parsing_module]['regexp'].match(message['text']):
            return imported_modules[parsing_module]['object'].get(message)
    else:
        return None


loop()  # Starting loop