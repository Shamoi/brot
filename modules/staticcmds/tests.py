from modules.staticcmds import get, check

test_message = {"time" : 1424717809, "sender" : 91670994,
        "chat-id" : 136, "id-of-message" : 198504,
        "text" : "тест1"}

def tests():
    result = "Staticcmds: "

    # Test for "get"
    isWorking = "ответ" in get.get(test_message)["text"][0]
    if isWorking:
        result += "Работоспособность - успешно, "
    else:
        result += "Работоспособность - провалено, "

    # Test for "check"
    isChecking = check.check("тест1") == True and check.check("!тест") == False
    if isChecking:
        result += "чекинг - успешно, "
    else:
        result += "чекинг - провалено, "

    result += "завершено."
    return result
