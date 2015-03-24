import unittest
import time
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

class BrotModuleTests(unittest.TestCase):
    def setUp(self):
        global message
        self.message = message

    def test_test_module(self):
        self.message['text'] = '!тест'
        answer = parse_message(self.message)
        self.assertEqual(answer['text'], 'Тест пройден')
        self.assertTrue(answer['attachments'] != [])

    def test_like_module(self):
        self.message['text'] = 'лайк на фотографию'
        answer = parse_message(self.message)
        self.assertEqual(answer['text'], 'Готово')

    def test_time_module(self):
        expression = re.compile('Московское время - (\d+:\d+), воткинское - (\d+:\d+)')
        self.message['text'] = 'время'
        answer = parse_message(self.message)
        self.assertTrue(expression.search(answer['text']))


if __name__ == '__main__':
    unittest.main()
