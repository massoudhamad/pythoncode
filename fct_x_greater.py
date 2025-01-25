import math


def fct_x_greater(x, y):
    return ((y**2) / x) + math.sqrt(x) * y


def fct_x_less(x, y):
    return (x + 2) ** 3 + y


def first_if_func(x, y):
    if x > 0:
        return fct_x_greater(x, y)
    elif x < 0:
        return fct_x_less(x, y)
    else:
        return x


print(first_if_func(0, 5))
