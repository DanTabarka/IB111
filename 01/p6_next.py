from ib111 import week_01  # noqa


# Napište funkci, která pro zadané celé číslo ‹number›
# najde nejbližší větší číslo, které je násobke kladného
# celého čísla ‹k›.

def next_multiple(number, k):
    for i in range(number + 1, number + k + 1):
        if i % k == 0:
            return i
    return -1


# Dále napište funkci, která pro zadané kladné celé číslo
# ‹number› najde nejbližší větší prvočíslo.

def next_prime(number):
    number += 1
    while not is_prime(number):
        number += 1

    return number


def is_prime(number):
    for i in range(2, number):
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
