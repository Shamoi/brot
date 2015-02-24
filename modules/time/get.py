import time

def get(message):
    return {"text" : [time.strftime("Текущее время - %H:%M")], "photos" : []}
