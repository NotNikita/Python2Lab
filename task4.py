import random


def cached(function):
    memo = {}  # like memory

    def wrapper(*args, **kwargs):
        out_arr = {} # output dictionary

        for num in args: # for each arg in *args
            if num in memo:
                    out_arr[num] = memo[num]
            else:
                    value_for_num = function(num)
                    out_arr[num] = value_for_num
                    memo[num] = value_for_num

        for word in kwargs.keys():
            if word in memo:
                out_arr[word] = memo[word]
            else:
                value_for_num = kwargs[word] # how to get second value??
                out_arr[word] = value_for_num
                memo[word] = value_for_num
        return out_arr

    return wrapper


@cached
def func(arg):
    return random.randint(1, 100) * arg



func(1,2,3, Hi = 100, Me = 200)  # позиционные аргументы
func(1,2)
func('Hi')
