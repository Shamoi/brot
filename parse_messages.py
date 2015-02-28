import modules.time.check as time_check #import each module
import modules.time.get as time_get

import modules.test.check as test_check
import modules.test.get as test_get

import modules.staticcmds.check as staticcmds_check
import modules.staticcmds.get as staticcmds_get

import modules.wiki.check as wiki_check
import modules.wiki.get as wiki_get

import modules.when.check as when_check
import modules.when.get as when_get

import modules.weather.check as weather_check
import modules.weather.get as weather_get

import modules.mdk.check as mdk_check
import modules.mdk.get as mdk_get

import modules.sur.check as sur_check
import modules.sur.get as sur_get

import modules.night.check as night_check
import modules.night.get as night_get


def parse(message):
    if time_check.check(message["text"]):
        return time_get.get(message)
    elif test_check.check(message["text"]):
        return test_get.get(message)
    elif mdk_check.check(message["text"]):
        return mdk_get.get(message)
    elif night_check.check(message["text"]):
        return night_get.get(message)
    elif sur_check.check(message["text"]):
        return sur_get.get(message)
    elif when_check.check(message["text"]):
        return when_get.get(message)
    elif weather_check.check(message["text"]):
        return weather_get.get(message)
    elif staticcmds_check.check(message["text"]):
        return staticcmds_get.get(message)
    elif wiki_check.check(message["text"]):
        return wiki_get.get(message)
    else:
        return {"text" : ["Я не могут ответить на это, мне нужно уточнить в офисе"], "photos" : []}
