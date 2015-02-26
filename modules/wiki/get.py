import wikipedia

wikipedia.set_lang("ru")

def get(message):
    try:
        wikipedia_is_in = wikipedia.summary(message["text"][10:], sentences = 1)
    except wikipedia.exceptions.DisambiguationError as e:
        message["text"] = "что такое " +  e.options[0]
    except wikipedia.exceptions.WikipediaException:
        pass
    try:
        message["text"] = message["text"].replace("?", "")
        return {"text" : [wikipedia.summary(message["text"][10:])],
                "photos" : []}
    except Exception as e:
        return {"text" : ["Ошибочка: " + str(e)], "photos" : []}
