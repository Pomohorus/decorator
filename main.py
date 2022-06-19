import datetime
import logging

def par_der(nested):
    def new_gen(old_fun):
        def new_fun(*args, **kwars):
            print('Дата и время: ', datetime.datetime.now())
            print('Имя функции: ', old_fun)
            print('Аргументы при вызове: ', nested)
            print('Возвращаемое значение: ')
            result = old_fun(nested)
            logging.basicConfig(filename='exlog.log', level=logging.INFO)
            logging.info('writiing in the log')
            return result
        return new_fun
    return new_gen

nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None],
]

@par_der(nested=nested_list)
def flat_generator(n):
    for item in n:
        for i in item:
            yield i



for item in flat_generator():
    print(item)
