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

def parse(message):
    if time_check.check(message["text"]):
        return time_get.get(message)
    elif test_check.check(message["text"]):
        return test_get.get(message)
    elif when_check.check(message["text"]):
        return when_get.get(message)
    elif staticcmds_check.check(message["text"]):
        return staticcmds_get.get(message)
    elif wiki_check.check(message["text"]):
        return wiki_get.get(message)
    else:
        return None
