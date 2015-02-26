from modules.weather import get, check

test_message = [{"time" : 1424717809, "sender" : 91670994,
        "chat-id" : 136, "id-of-message" : 198504,
        "text" : "время"}]

def tests():
    result = "MDK: "

    # Test for "check"
    isChecking = check.check("мдк") == True and check.check("чтк") == False
    if isChecking:
        result += "Чекинг - успешно, "
    else:
        result += "Чекинг - провалено, "

    result += "завершено."
    return result
