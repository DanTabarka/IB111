from ib111 import week_01  # noqa


# Napište funkci ‹largest_triple›, která najde pythagorejskou
# trojici ⟦(a, b, c)⟧ – totiž takovou, že ⟦a⟧, ⟦b⟧ a ⟦c⟧ jsou
# přirozená čísla a platí ⟦a² + b² = c²⟧ (tzn. tvoří pravoúhlý
# trojúhelník). Hledáme trojici, která:
#
#  1. má největší možný součet ⟦a + b + c⟧,
#  2. hodnoty ⟦a⟧, ⟦b⟧ jsou menší než ‹max_side›.
#
# Výsledkem funkce bude součet ⟦a + b + c⟧, tedy největší možný
# obvod pravoúhlého trojúhelníku, jsou-li obě jeho odvěsny kratší
# než ‹max_side›.

def largest_triple(max_side):
    biggest_sum = 0
    for a in range(max_side - 1, 0, -1):
        for b in range(max_side - 1, 0, -1):
            c = max_side // 2
            while c ** 2 < a ** 2 + b ** 2:
                c += 1
            if c ** 2 == a ** 2 + b ** 2 and a + b + c > biggest_sum:
                biggest_sum = a + b + c
                break

    return biggest_sum


def main():
    print(largest_triple(6))
    assert largest_triple(10) == 24
    assert largest_triple(25) == 72
    assert largest_triple(100) == 288
    print(100)
    assert largest_triple(150) == 490
    print(150)
    assert largest_triple(1000) == 3290


if __name__ == "__main__":
    main()
