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
    if number % 2 == 0:
        return False

    for i in range(3, ceil(sqrt(number)), 2):
        if number % i == 0:
            return False
    return True


def next_prime(number):
    if number == 1:
        return 2

    number += 1 + number % 2

    while not is_prime(number):
        number += 2
        while number % 3 == 0 or number % 5 == 0:
            number += 2

    return number


def nth_smallest_prime_divisor(num, index):
    prime = 2

    for _ in range(index):
        if num % prime != 0:
            while num % prime != 0:
                prime = next_prime(prime)
                if prime > num:
                    return None
        num //= prime

    return prime


def main():
    assert nth_smallest_prime_divisor(20, 1) == 2
    assert nth_smallest_prime_divisor(42350, 2) == 5
    assert nth_smallest_prime_divisor(42350, 3) == 5
    assert nth_smallest_prime_divisor(42350, 4) == 7
    assert nth_smallest_prime_divisor(42350, 7) is None


if __name__ == '__main__':
    main()
