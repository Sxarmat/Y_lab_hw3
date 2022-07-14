from functools import wraps
from time import sleep
from math import pow


def iterator(call_count, start_sleep_time, factor, border_sleep_time):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            time_sleep = start_sleep_time
            print('Кол-во запусков = {}'.format(call_count), 'Начало работы', sep='\n')
            for i in range(1, call_count + 1):
                sleep(time_sleep)
                result = func(*args, **kwargs)
                print('Запуск номер {}. Ожидание: {} секунд. Результат декорируемой функции = {}.'.format(i, time_sleep,
                                                                                                          result))
                next_sleep = time_sleep * pow(2, factor)
                time_sleep = next_sleep if next_sleep < border_sleep_time else border_sleep_time
            return result
        return wrapper
    return decorator


