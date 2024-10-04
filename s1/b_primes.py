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

def nth_smallest_prime_divisor(num, index):
    upper_bound = ceil(sqrt(num))

    for divisor in range(2, upper_bound + 1):
        while index > 0 and num % divisor == 0:
            num //= divisor
            index -= 1
        if index == 0:
            return divisor
    if index == 1 and num != 1:
        return num
    return None


def main():
    assert nth_smallest_prime_divisor(20, 1) == 2
    assert nth_smallest_prime_divisor(25, 1) == 5
    assert nth_smallest_prime_divisor(25, 1) == 5
    assert nth_smallest_prime_divisor(25, 1) == 5
    assert nth_smallest_prime_divisor(25, 1) == 5
    assert nth_smallest_prime_divisor(25, 2) == 5
    assert nth_smallest_prime_divisor(42350, 2) == 5
    assert nth_smallest_prime_divisor(42350, 3) == 5
    assert nth_smallest_prime_divisor(42350, 4) == 7
    assert nth_smallest_prime_divisor(42350, 7) is None
    assert nth_smallest_prime_divisor(4039636, 3) == 1009909
    # print(nth_smallest_prime_divisor(4039636, 3))
    # print(nth_smallest_prime_divisor(9699690, 4))
    # print(nth_smallest_prime_divisor(9699690, 5))
    # print(nth_smallest_prime_divisor(9699690, 6))
    # print(nth_smallest_prime_divisor(9699690, 7))
    # print(nth_smallest_prime_divisor(9699690, 8))
    # print(nth_smallest_prime_divisor(9699690, 9))
    # print(nth_smallest_prime_divisor(4127911259, 1))
    # print(nth_smallest_prime_divisor(4127911259, 2))


if __name__ == '__main__':
    main()
