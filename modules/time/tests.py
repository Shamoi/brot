from modules.time import get, check

test_message = [{"time" : 1424717809, "sender" : 91670994,
        "chat-id" : 136, "id-of-message" : 198504,
        "text" : "время"}]

def tests():
    result = "Time: "

    # Test for "get"
    isWorking = "Текущее время" in get.get(test_message)[0]
    if isWorking:
        result += "Работоспособность - успешно, "
    else:
        result += "Работоспособность - провалено, "

    # Test for "check"
    isChecking = check.check("время") == True and check.check("бремя") == False
    if isChecking:
        result += "чекинг - успешно, "
    else:
        result += "чекинг - провалено, "

    result += "завершено."
    return result
