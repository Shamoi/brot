from modules.time import tests as time_tests #from each module taking tests
from modules.test import tests as test_tests
from modules.staticcmds import tests as staticcmds_tests
from modules.wiki import tests as wiki_tests
import vk_api
import json
import time #for generation nubmer (anti flood control)

def doCommandsTests():
    results = ["Тестирование команд:"]
    results.append(time_tests.tests())
    results.append(test_tests.tests())
    results.append(staticcmds_tests.tests())
    results.append(wiki_tests.tests())
    return results

def doMessagesTests():
    results = ["Тестирование отправки:"]
    config = json.loads(open('config.json').read())
    try:
        vk_test = vk_api.VkApi(config["vk-login"], config["vk-password"])
        response = vk_test.method('messages.send',
                                  {"user_id" : 91670994, "message" : "Test message" + str(time.time())})
    except Exception as error_msg:
        results.append("Отправка сообщения - провалено({})".format(error_msg))
    else:
        results.append("Отправка сообщения - успешно")
    return results

def doTests():
    results = []
    results += doMessagesTests()
    results += doCommandsTests()
    return results

def printTests():
    results = doTests()
    for result in results:
        print(result)
    return 0

if __name__ == '__main__':
    printTests()
