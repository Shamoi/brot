from modules.time import get, check

def tests():
    result = "Time: "

    # Test for "get"
    isWorking = "Текущее время" in get.get()[0]
    if isWorking:
        result += "Работоспособность - успешно, "
    else:
        result += "Работоспособность - провалено, "

    # Test for "check"
    isChecking = check.check("время") == True and check.check("бремя") == False
    if isChecking:
        result += "Чекинг - успешно, "
    else:
        result += "Чекинг - провалено, "

    result += "завершено."
    return result
