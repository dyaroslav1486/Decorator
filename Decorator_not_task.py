
from datetime import datetime as dtime


def logger(old_function):
    def new_function(*args, **kwargs):
        oldname = old_function.__name__
        time = str(dtime.now())
        path = oldname + '.log'
        with open (path, 'a', encoding='utf-8') as f:
            time = str(dtime.now())
            f.write(f'Название функции "{oldname}"\n')
            f.write(f'Аргументы функции {oldname} - {args}{kwargs}\n')
            time = str(dtime.now())
            f.write(f'Время начала работы функции {time}\n')
            result = old_function(*args, **kwargs)
            time = str(dtime.now())
            f.write(f'Время конца работы функции {time}\n')
            f.write(f'Результат - {result}\n\n')
        return result
    return new_function



def summator(a,b,c):
    return a+b+c

loggers_sum = logger(summator)
loggers_sum(45, 19, 213)
