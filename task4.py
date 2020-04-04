import random


def cached(function):
    memo = {}  # like memory

    def wrapper(*args):
        if args in memo:
            return memo[args]
        else:
            out_value = function(*args)
            memo[args] = out_value
            return out_value

    return wrapper


@cached
def f(x):
    return random.randint(1, 100) * x


a = f(1)
b = f(1)
if a == b:
    print("They are equal")
else:
    print("NOT equal: a=", a, "   b=", b)

print("\nSECOND TRY\n")
b = f(2)
if a == b:
    print("They are equal")
else:
    print("NOT equal: a=", a, "   b=", b)
