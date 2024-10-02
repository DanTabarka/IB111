from ib111 import week_01  # noqa
from math import ceil, sqrt
# hodnotit: ano (umažte „ne/“ pro hodnocení kvality tohoto řešení)


# Napište čistou funkci ‹nth_smallest_prime_divisor›, která vrátí ‹index›-té
# nejmenší prvočíslo vyskytující se v prvočíselném rozkladu čísla ‹num›.
# Pokud se v rozkladu vyskytuje některé prvočíslo vícekrát, počítáme všechny
# jeho výskyty, tedy např. v čísle ⟦2 · 2 · 3 · 3 · 3 · 5 = 540⟧ je třetím
# nejmenším prvočíslem číslo 3. Pokud má ‹num› méně než ‹index› prvočísel
# v rozkladu, funkce vrátí ‹None›.
#
# Předpokládejte, že ‹num› i ‹index› jsou kladná celá čísla.
# Zde indexujeme od 1, tedy první prvočíslo v rozkladu má ‹index› 1.
#
# Je potřeba, aby vaše funkce fungovala rozumně rychle i pro velmi velká
# čísla, u nichž je hledané prvočíslo malé. (Není třeba vymýšlet zvláště
# chytrá řešení, jen je třeba nedělat zbytečnou práci navíc.)

def is_prime(number):
    if number % 2 == 0 or number % 3 == 0:
        return False

    # jump by 6 and check 6 + 0 and 6 + 2, (6 + 4 | 3) ->
    # 5 + 6 => check 11 and 13, 15 is % 3 and so on...
    for i in range(5, ceil(sqrt(number)), 6):
        if number % i == 0 or number % (i + 2) == 0:
            return False
    return True


def next_prime(number):
    if number == 2:
        return 3

    number += 1 + number % 2    # now it is odd number

    while not is_prime(number):
        number += 2

    return number


def find_next_prime(num, prime):
    while num % prime != 0:
        prime = next_prime(prime)
        if prime > num:
            return None
    return prime


def nth_smallest_prime_divisor(num, index):
    prime = 2

    for _ in range(index - 1):
        if num % prime != 0:
            prime = find_next_prime(num, prime)
            if prime is None:
                return None
        num //= prime

    if num != 1 and is_prime(num):  # last iteration should be very high prime
        return num

    return find_next_prime(num, prime)  # last iteration


def main():
    assert nth_smallest_prime_divisor(20, 1) == 2
    assert nth_smallest_prime_divisor(42350, 2) == 5
    assert nth_smallest_prime_divisor(42350, 3) == 5
    assert nth_smallest_prime_divisor(42350, 4) == 7
    assert nth_smallest_prime_divisor(42350, 7) is None
    assert nth_smallest_prime_divisor(4039636, 3) == 1009909
    print(nth_smallest_prime_divisor(4039636, 3))
    print(nth_smallest_prime_divisor(9699690, 4))
    print(nth_smallest_prime_divisor(9699690, 5))
    print(nth_smallest_prime_divisor(9699690, 6))
    print(nth_smallest_prime_divisor(9699690, 7))
    print(nth_smallest_prime_divisor(9699690, 8))
    print(nth_smallest_prime_divisor(9699690, 9))
    print(nth_smallest_prime_divisor(4127911259, 1))
    print(nth_smallest_prime_divisor(4127911259, 2))


if __name__ == '__main__':
    main()
