from modules.time import tests #from each module taking tests
import vk_api
import json
import time #for generation nubmer (anti flood contro;)

def doCommandsTests():
    results = ["Тестирование команд:"]
    results.append(tests.tests())
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

if __name__ == '__main__':
    results = []
    results += doMessagesTests()
    results += doCommandsTests()
    for result in results:
        print(result)
