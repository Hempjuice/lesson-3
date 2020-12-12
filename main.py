from time import time
from functools import wraps


EVEN_NUMBERS = 0
ODD_NUMBERS = 1
PRIME_NUMBERS = 2


def exponentiation(numbers, degree=2):
    """ Функция возводит переданный список числел в степень degree и возвращает результат """
    result = []

    for n in numbers:
        result.append(pow(n, degree))

    return result


def is_prime(number):
    """ Функция возвращает True, если переданное число простое """
    count = 0

    for i in range(1, number + 1):
        if number % i == 0:
            count += 1

    return count == 2


def time_call(func):
    @wraps(func)
    def wrapper(n, f):
        start = time()
        res = func(n, f)
        end = time()
        time_taken = end - start
        print(f'Времени затречено: {time_taken:.10f}')
        return res

    return wrapper


@time_call
def filter_numbers(numbers, flt):
    """ Функция отфильтровывает переданный список чисел по заданному отбору (четные, нечетные, простые) """
    if flt == EVEN_NUMBERS:
        func = lambda n: n % 2 == 0
    elif flt == ODD_NUMBERS:
        func = lambda n: n % 2 == 1
    else:
        func = is_prime

    return list(filter(func, numbers))


def fibonacci(n):
    """ Функция вычисляет n число Фибоначчи """
    if n <= 0:
        return None

    result = 1

    if n > 2:
        result = fibonacci(n - 1) + fibonacci(n - 2)

    return result


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    print('Квадраты чисел', numbers, ':', exponentiation(numbers))
    print('Только четные числа из списка', numbers, ':', filter_numbers(numbers, EVEN_NUMBERS))
    print('Только нечетные числа из списка', numbers, ':', filter_numbers(numbers, ODD_NUMBERS))
    print('Только простые числа из списка', numbers, ':', filter_numbers(numbers, PRIME_NUMBERS))

    fib_number = 10
    print(fib_number, 'число Фибоначчи:', fibonacci(fib_number))