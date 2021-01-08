# Russian language comments


# Функция - пример объекта класса function
def none(*skipArgs, **skipKeyargs):
    return None

def normalizeIndex(index, length):
    if index < 0:
        return length + index + 1
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
    def case(self, inputData = (None, {}), outputData = None, *skipArgs, key = -1, error = False, **skipKeyargs):
        
        # Для защиты от некорректных аргументов функция обёрнута в тесты
        errorTest1 = type(inputData) not in {tuple, list}
        errorTest2 = type(key) != (int)
        errorTest3 = type(inputData[-1]) != (dict)
        if (not errorTest1) and (not errorTest2) and (not errorTest3):

            # Чистая функция создания кейса тестирования
            testcase(self, inputData, outputData, key, error)

        # Вызов ошибок при некорректных аргументах
        elif errorTest1:
            errorMessage = 'Type of case input data is not tuple or list!'
            raise TypeError(errorMessage)
        elif errorTest2:
            errorMessage = 'Type of key is not int!'
            raise TypeError(errorMessage)
        elif errorTest3:
            errorMessage = 'In inputData is not dict of key arguments!'
            
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
    self.error = []


def testcase(self, inputData, outputData, key, error):
    key = normalizeIndex(key, len(self.input))
    
    self.input.insert(key, inputData)
    self.output.insert(key, outputData)
    self.error.insert(key, error)


def testtodo(self):
    for key in range(len(self.input)):
        arguments = self.input[key][0:-1]
        keyarguments = self.input[key][-1]
        
        testing(self, key, arguments, keyarguments)
                
            

def testing(self, key, arguments, keyarguments):
    try:
        result = self.func(*arguments, **keyarguments)
        assert result == self.output[key]

        okResult(self, key, result)
            
    except AssertionError:
        failResult(self, key, result)
            
    except Exception as error:
            
        if self.error[key]:
            okError(self, key, error)
                
        else:
            failError(self, key, error)


                
def okResult(self, key, result):
    message = ('OK\ninput:{}\nresult:{}'.format(self.input[key], result))
    print(message)

def failResult(self, key, result):
    errorMessage = 'FAIL\ninput:{}\nresult:{}\noutput:{}'.format(self.input[key], result, self.output[key])
    print(errorMessage)

def okError(self, key, error):
    message = 'OK\ninput:{}\nerror:{}'.format(self.input[key], type(error))
    print(message)

def failError(self, key, error):
    errorMessage = 'FAIL\ninput:{}\nerror:{}'.format(self.input[key], type(error))
    print(errorMessage)


    
