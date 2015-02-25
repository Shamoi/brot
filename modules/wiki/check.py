import re
import wikipedia

wikipedia.set_lang("ru")
wikipedia_message = re.compile('(к|ч)то так(ая|ое|ой|ие) .+\??')

def check(message):
    if wikipedia_message.match(message.lower()):
        try:
            wikipedia_is_in = wikipedia.summary(message.replace("?", "")[10:], sentences = 1)
        except wikipedia.exceptions.DisambiguationError as e:
            return True
        except Exception as error:
            return False
        else:
            return True
    else:
        return False
