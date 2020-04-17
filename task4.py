def cached(function):
    memo = {}  # like memory

    def wrapper(*args, **kwargs):
        # key - input
        # result - output

        key = args
        if kwargs:
            for item in sorted(kwargs.items()): #sorted оебспечивает устойчивость
                key += item

        # ==
        if key in memo:
            result = memo[key]
        else:
            result = function(*args, **kwargs)
            memo[key] = result

        return result

    return wrapper


@cached
def foo(*args, **kwargs):
    out_str = ''  # output str

    # args
    if args:# если args вообще был передан
        out_str = str(sum(n for n in args))

    # kwargs
    if kwargs:  # если kwargs вообще был передан
        for key in sorted(kwargs.keys()):
            out_str += str( kwargs[key] )


    return out_str


print("result: ", foo(1, 2, 3) == foo(1, 2, 3))  # позиционные аргументы
print("\n")
print("result: ", foo(bar=42, spam="eggs") == foo(spam="eggs", bar=42))
