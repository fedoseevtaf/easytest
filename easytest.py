# Russian language comments


# Функция - пример объекта класса function
def none(*skipArgs, **skipKeyargs):
    return None

def normalizeIndex(index, length):
    if index < 0:
        return length + index + (index < 0)
    else:
        return index


# Класс нужен для объединения кейсов тестированя в один объект
class test():
    
    # Метод используется для создания нового набота кейсов тестирования функции
    def __init__(self, func = none, *skipArgs , **skipKeyargs):
        
        # Для защиты от некорректных аргументов функция обёрнута в тесты типов
        errorTest1 = type(func) not in {type(none), type(sum)}
        if not errorTest1:

            # Чистая функция создания нового теста
            test__init__(self, func)

        # Вызов ошибок при некорректных аргументах
        elif errorTeat1:
            errorMessage = 'Type of test function is not function!'
            raise TypeError(errorMessage)
            

    # Метод используется для добавления кейса тестирования
    def case(self, inputData = (None, {}), outputData = None, *skipArgs, key = -1, **skipKeyargs):
        
        # Для защиты от некорректных аргументов функция обёрнута в тесты
        errorTest1 = type(inputData) not in {tuple, list}
        errorTest2 = type(key) != (int)
        if (not errorTest1) and (not errorTest2):

            # Чистая функция создания кейса тестирования
            testcase(self, inputData, outputData, key)

        # Вызов ошибок при некорректных аргументах
        elif errorTest1:
            errorMessage = 'Type of case input data is not tuple or list!'
            raise TypeError(errorMessage)
        elif errorTest2:
            errorMessage = 'Type of key is not int!'
            raise TypeError(errorMessage)
            
    # Метод для выполнения кейсов тестирования из теста
    def todo(self, *skipArgs, **skipKeyargs):
        
        if True:

            # Чистая функция для выполнения кейсов
            testtodo(self)

        elif True:
            pass


# Чистые функции без защиты от некорректных аргументов
# Они предназначены для работы с тестами
# !!! НЕ ТРОГАТЬ ЭТИ ФУНКЦИИ !!!
# !!! DON'T TOUCH THIS FUNCTIONS !!!
def test__init__(self, func):
    self.func = func

    self.input = []
    self.output = []


def testcase(self, inputData, outputData, key):
    key = normalizeIndex(key, len(self.input))
    
    self.input.insert(key, inputData)
    self.output.insert(key, outputData)


def testtodo(self):
    for key in range(len(self.input)):
        arguments = self.input[key][0:-1]
        keyarguments = self.input[key][-1]
        
        result = self.func(*arguments, **keyarguments)
        
        try:
            assert result == self.output[key]

            message = ('OK\ninput:{}\nresult:{}'.format(self.input[key], result))
            print(message)

        except:
            errorMessage = 'FAIL\ninput:{}\nresult:{}\noutput:{}'.format(self.input[key], result, self.output[key])
            print(errorMessage)
        
