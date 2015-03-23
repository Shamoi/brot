import wikipedia
import re

wikipedia.set_lang('ru')
expression = re.compile('(ч|к)то так(ой|ая|ое|ие) ([^?]+)\??', re.IGNORECASE)


def get(message):
    query = expression.search(message['text']).group(3)
    try:
        wiki_answer = wikipedia.summary(query, 5)
    except wikipedia.exceptions.DisambiguationError as error:
        wiki_answer = wikipedia.summary(error.options[0], 5)
    except wikipedia.PageError:
        return {'text': "Я не знаю.", 'attachments': []}
    return {'text': wiki_answer, 'attachments': []}