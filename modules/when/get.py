import time
import random
def get(message):
    if random.randint(1, 50) == 13:
        return {"text" : ["Никогда"], "photos" : []}
    return {"text" : ["Это будет " + str(random.randint(1, 31)) + "." +
    str(random.randint(1, 12)) + "." + str(random.randint(2015, 2018))], "photos" : []}
