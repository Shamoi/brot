from modules.time import tests #from each module taking tests

def doTests():
    results = ["Тестирование"]
    results.append(tests.tests())
    return results

if __name__ == '__main__':
    results = doTests()
    for result in results:
        print(result)
