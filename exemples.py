from easytest import *


# Exemple 1
def X2(value, *skipArgs, **skipKeyargs):
    return value * 2

x2 = test(X2)

# Correct cases
x2.case((2, {}), 4)
x2.case((17.8, {}), 35.6)
x2.case(('qwertypassword', {}), 'qwertypassword' * 2)
x2.case(([0, 1, 2, 3], {}), [0, 1, 2, 3] * 2)
x2.case((*(('trash',) * 10), {'trash' : 'trash'}), 'trash' * 2)

# Error cases
x2.case(({'q' : 'q'}, {}), error = True)
x2.case(({},), error = True)

x2.todo()



# Exemple 2
def getitem(*values, key = 0, **skipKeyargs):
    return values[key]

gettest = test(getitem)

# Correct cases
mylist = [0, 1, [0, 1], {'0' : '1'}, '01', False, True]
for key in range(len(mylist)):
    gettest.case((*mylist, {'key' : key}), mylist[key])

# Error cases
gettest.case(({'key' : 753},), error = True)
for key in range(0, 4):
    gettest.case((*mylist, {'key' : key + 0.5}), error = True)

gettest.todo()



# Exemple 3
def Sum(num = 1, *skipArgs, unevenSum = False, **skipKeyargs):
    errorTest1 = type(num) != int
    errorTest2 = num < 1
    if (not errorTest1) and (not errorTest2):

        if not unevenSum:
            return ((num + 1) * num) / 2
        else:
            return ((num + 1) / 2) ** 2

    elif errorTest1:
        raise TypeError('Type of num is not int!')
    elif errorTest2:
        raise ValueError('Num < 1')

sumtest = test(Sum)

# Correct cases
for num in range(1, 6):
    sumtest.case((num, {}),  ((num + 1) * num) / 2)

for num in range(1, 6):
    sumtest.case((num, {'unevenSum' : True}), ((num + 1) / 2) ** 2)

# Error cases
for num in range(0, -6, -1):
    sumtest.case((num, {}), error = True)

uncorrectTypes = [[0, 1], {'0' : '1'}, '01', False, True]
for num in uncorrectTypes:
    sumtest.case((num, {}), error = True)

sumtest.todo()
