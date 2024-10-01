from ib111 import week_01  # noqa
from math import sqrt, ceil


# Napište funkci, která pro zadané celé číslo ‹number›
# najde nejbližší větší číslo, které je násobke kladného
# celého čísla ‹k›.

def next_multiple(number, k):
    return number + k - (number % k)


# Dále napište funkci, která pro zadané kladné celé číslo
# ‹number› najde nejbližší větší prvočíslo.

def next_prime(number):
    if number == 1:
        return 2

    number += 1 + number % 2

    while not is_prime(number):
        number += 2

    return number


def is_prime(number):
    if number % 2 == 0:
        return False

    for i in range(3, ceil(sqrt(number))):
        if number % i == 0:
            return False
    return True


def main():
    assert next_multiple(1, 2) == 2
    assert next_multiple(10, 7) == 14
    assert next_multiple(10, 5) == 15
    assert next_multiple(54, 6) == 60
    assert next_multiple(131, 29) == 145
    assert next_multiple(123, 112) == 224
    assert next_multiple(423, 90) == 450

    assert next_prime(1) == 2
    assert next_prime(2) == 3
    assert next_prime(3) == 5
    assert next_prime(4) == 5
    assert next_prime(11) == 13
    assert next_prime(12) == 13
    assert next_prime(13) == 17


if __name__ == "__main__":
    main()
