from functools import lru_cache


@lru_cache
def fibonacci(n: int) -> int:
    if n <= 0:
        return 0
    elif n <= 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def my_fibonacci(n: int, my_dict: dict = {}) -> int:
    try:
        return my_dict[n]
    except KeyError:
        if n <= 0:
            my_dict[n] = 0
        elif n <= 2:
            my_dict[n] = 1
        else:
            my_dict[n] = my_fibonacci(n - 1, my_dict) + my_fibonacci(n - 2, my_dict)
    return my_dict[n]


if __name__ == '__main__':
    print(fibonacci(500))
    print(my_fibonacci(500))
