from modules.time import get

def tests():
    result = "Time: "
    isWorking = "Текущее время" in get.get()[0]
    if isWorking:
        result += "Работоспособность - успешно, "
    else:
        result += "Работоспособность - провалено, "

    result += "завершено без фатальных ошибок."
    return result
