import modules.time.check as time_check #import each module
import modules.time.get as time_get
def parse(message):
    if time_check.check(message[0]["text"]):
        return time_get.get(message)
