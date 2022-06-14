import datetime
import logging


def new_gen(old_fun):
    def new_fun(n):
        print('Дата и время: ', datetime.datetime.now())
        print('Имя функции: ', old_fun)
        print('Аргументы при вызове: ', n)
        print('Возвращаемое значение: ')
        result = old_fun(n)
        logging.basicConfig(filename='exlog.log', level=logging.INFO)
        logging.info('writiing in the log')
        return result
    return new_fun

@new_gen
def flat_generator(n):
    for item in n:
        for i in item:
            yield i

nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None],
]

for item in flat_generator(nested_list):
    print(item)
