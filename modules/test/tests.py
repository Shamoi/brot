from modules.test import get, check

test_message = [{"time" : 1424717809, "sender" : 91670994,
        "chat-id" : 136, "id-of-message" : 198504,
        "text" : "!тест"}]

def tests():
    result = "Test: " # Test for "check"

    isChecking = check.check("!тест") == True and check.check("тест") == False
    if isChecking:
        result += "Чекинг - успешно, "
    else:
        result += "Чекинг - провалено, "

    result += "завершено."
    return result
