import random


def cached(function):
    memo = {}  # like memory

    def wrapper(*args, **kwargs):
        out_arr = []  # output dictionary
        temp_arr = [] # for kwargs

        #args
        assert isinstance(args, tuple) # args to tuple
        if args.__len__() != 0:
            if args in memo:
                out_arr = memo[args]
            else:
                for x in args:
                    out_arr.append(function(x))
                memo[args] = out_arr

        # kwargs
        if kwargs.__len__() !=0:  # если словарь вообще был передан
            temp = list(kwargs.items())  # делаем список из элементов словоря
            kwarg_content = tuple(temp)  # кортеж


            if kwarg_content in memo:
                temp_arr = memo[kwarg_content]
                for i in temp_arr:  # merging lists of arg and kwarg results
                    out_arr.append(i)
            else:
                for key in kwargs.keys(): #выписываем значения по ключам в список для вывода
                    temp_arr.append(kwargs[key])

                memo[kwarg_content] = temp_arr  # 'кортеж' = значения элементов кортежа

                if len(temp_arr) != 0: # kwargs were not given
                    for i in temp_arr:  # merging lists of arg and kwarg results
                        out_arr.append(i)

        return out_arr

    return wrapper


@cached
def func(arg):
    return random.randint(1, 100) * arg


print("result: ", func(1, 2, 3) == func(1, 2, 3))  # позиционные аргументы
print("\n")
print("result: ", func(Hi=100, Me=200) == func(Hi=100, Me=200))

