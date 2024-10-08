from ib111 import week_01  # noqa


# Napište funkci ‹nested›, která spočítá ‹n›-tý člen posloupnosti
# (počítáno od 0), která vznikne napojením postupně se
# prodlužujících prefixů přirozených čísel.
#
# Nechť ⟦Aᵢ⟧ je posloupnost čísel ⟦1⟧ až ⟦i⟧:
#
#  ⟦ A₁ → 1
#    A₂ → 1, 2
#    A₃ → 1, 2, 3
#    A₄ → 1, 2, 3, 4
#    A₅ → 1, 2, 3, 4, 5 ⟧
#
# Hledaná posloupnost ⟦B⟧ vznikne napojením posloupností ⟦A₁⟧, ⟦A₂⟧,
# ⟦A₃⟧ … (do nekonečna) za sebe:
#
#  ⟦ B  → 1, 1, 2, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 4, 5, 1, 2, … ⟧
#         1  2  3  4  5  6  7  8  9  10 11 12 13 14 15
# Vaším úkolem je najít ‹n›-tý prvek posloupnosti ⟦B⟧.

def nested(n):
    index_of_one = 0
    plus = 1
    while index_of_one < n:
        index_of_one += plus
        plus += 1
    if index_of_one == n:
        return 1
    return n - (index_of_one - plus)    # (index - plus) => index of prev one


# Dále napište funkci ‹nested_sum›, která spočítá sumu prvních ‹n› členů
# této posloupnosti.

def nested_sum(n):
    summary = 0
    plus = 1
    upper_bound = 1
    for _ in range(n):
        summary += plus
        plus += 1
        if upper_bound == plus - 1:
            plus = 1
            upper_bound += 1

    return summary


def main():
    assert nested(0) == 1
    assert nested(1) == 1
    assert nested(2) == 2
    assert nested(8) == 3
    assert nested(9) == 4
    assert nested(25) == 5
    assert nested(130) == 11

    assert nested_sum(2) == 2
    assert nested_sum(5) == 7
    assert nested_sum(13) == 26
    assert nested_sum(30) == 87
    assert nested_sum(100) == 500


if __name__ == "__main__":
    main()
