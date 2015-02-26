from modules.weather import get, check

test_message = [{"time" : 1424717809, "sender" : 91670994,
        "chat-id" : 136, "id-of-message" : 198504,
        "text" : "время"}]

def tests():
    result = "Weather: "

    # Test for "check"
    isChecking = check.check("погода") == True and check.check("пагада") == False
    if isChecking:
        result += "Чекинг - успешно, "
    else:
        result += "Чекинг - провалено, "

    result += "завершено."
    return result
