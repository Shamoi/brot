from modules.weather import get, check

test_message = [{"time" : 1424717809, "sender" : 91670994,
        "chat-id" : 136, "id-of-message" : 198504,
        "text" : "время"}]

def tests():
    result = "Night: "

    # Test for "check"
    isChecking = check.check("тьма") == True and check.check("темень") == False
    if isChecking:
        result += "Чекинг - успешно, "
    else:
        result += "Чекинг - провалено, "

    result += "завершено."
    return result
