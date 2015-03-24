from loop import parse_message
import re

message = {
    'text': '!тест',
    'attachments': [],
    'id': 215865,
    'sender_id': 91670994,
    'type': 'user',
    'chat': None
}

testing_commands = {
    '!тест': 'Тест пройден',
    'время': 'Московское время - (\d+:\d+), воткинское - (\d+:\d+)',
    'что такое гораздо?': '(.+) — (.+)',
    'кто такая Ким Кардашьян': '(.+) — (.+)',
    'кто такой Амараап Ппагугу?': 'Я не знаю',
    'пинг': 'понг',
    '"пинг" - "понг"': 'Команда "пинг" добавлена'
}

# Basic tests
for command in testing_commands:
    expression = re.compile(testing_commands[command])
    message['text'] = command
    assert expression.match(parse_message(message)['text'])