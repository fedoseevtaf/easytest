# Russian language comments


# Функция - пример объекта класса function
def none(*args, **keyargs):
    return None


# Класс для тестирования функций по кейсам тестирования
class test():
    # Метод для инициализации нового стэка кейсов тестирования функции по ней
    def __init__(self, func, *skipArgs , **skipKeyargs):
        # Защита от пользователей неправильно задающих аргументы
        errorTest1 = type(func) != type(none)
        if not errorTest1:

            # Чистая функция создания нового теста
            test__init__(self, func, message)
            
        else:
            errorMessage = 'Type of test function is not function!'
            raise TypeError(errorMessage)
            

    # Метод для добавления нового кейса тестирования 
    def case(self, inputData = (0, {}), outputData = 0, *skipArgs, sep = 0, **skipKeyargs):
        # Защита от пользователей неправильно задающих аргументы
        errorTest1 = type(inputData) not in {tuple, list}
        errorTest2 = type(sep) != (int)
        if (not errorTest1) and (not errorTest2):

            # Чистая функция создания в тесте кейса тестирования
            testcase(self, inputData, outputData, sep)

        elif errorTest1:
            errorMessage = 'Type of case input data is not tuple or list!'
            raise TypeError(errorMessage)
        elif errorTest2:
            errorMessage = 'Type of separator is not int!'
            raise TypeError(errorMessage)
            
    # Метод для выполнения кейсов тестирования из теста
    def todo(self, *skipArgs, **skipKeyargs):
        # Заготовка под будующие аргументы
        if True:

            # Чистая функция для выполнения кейсов
            testtodo(self)

        else:
            pass


# Чистые функции без защиты от неправильных аргументов
# !!! НЕ ТРОГАТЬ ЭТИ ФУНКЦИИ !!!
# !!! DON'T TOUCH THIS FUNCTIONS !!!
def test__init__(self, func):
    self.func = func

    self.input = []
    self.output = []


def testcase(self, inputData, outputData, sep):
    self.input.insert(sep, inputData)
    self.output.insert(sep, outputData)


def testtodo(self):
    for key in range(len(self.input)):
        arguments = self.input[key][0:-1]
        keyarguments = self.input[key][-1]
        
        result = self.func(*arguments, **keyarguments)
        
        try:
            assert result == self.output[key]

            message = ':input:{}: :result:{}: :output:{}:'.format(self.input[key], result, self.output[key])
            print('OK    {}'.format(message))

        except:
            errorMessage = ':input:{}: :result:{}: :output:{}:'.format(self.input[key], result, self.output[key])
            print('FAIL    {}}'.format(errorMessage))
        
