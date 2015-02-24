from modules.time import tests #from each module taking tests

def doCommandsTests():
    results = ["Тестирование команд:"]
    results.append(tests.tests())
    return results

if __name__ == '__main__':
    results = doCommandsTests()
    for result in results:
        print(result)
