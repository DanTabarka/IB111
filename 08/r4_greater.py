from ib111 import week_08  # noqa


# † Napište funkci ‹next_greater›, která vrátí nejmenší větší číslo
# se stejnými ciframi jaké má číslo ‹number›. Pokud větší číslo
# neexistuje, funkce vrací ‹None›. Nezkoušejte všechny permutace
# cifer, existuje efektivnejší řešení.

def next_greater(number: int) -> int | None:
    pass


def main() -> None:
    assert next_greater(12) == 21
    assert next_greater(513) == 531
    assert next_greater(2017) == 2071
    assert next_greater(9) is None
    assert next_greater(111) is None
    assert next_greater(531) is None
    assert next_greater(351) == 513


if __name__ == "__main__":
    main()
