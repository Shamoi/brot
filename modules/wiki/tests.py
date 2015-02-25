from modules.wiki import get, check

test_message = {"time" : 1424717809, "sender" : 91670994,
        "chat-id" : 136, "id-of-message" : 198504,
        "text" : "что такое нью-йорк"}

def tests():
    result = "Wiki: "

    # Test for "get"
    isWorking = "Нью-Йо́рк" in get.get(test_message)["text"][0]
    if isWorking:
        result += "Работоспособность - успешно, "
    else:
        result += "Работоспособность - провалено, "

    # Test for "check"
    isChecking = check.check("кто такой школьник") == True and check.check("кто такая лвлававдламл") == False
    if isChecking:
        result += "чекинг - успешно, "
    else:
        result += "чекинг - провалено, "

    result += "завершено."
    return result
