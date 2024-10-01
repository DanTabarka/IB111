from ib111 import week_01  # noqa


# † Napište predikát, který určí, jsou-li 2 čísla spřátelená
# (amicable). Spřátelená čísla jsou dvě přirozená čísla taková,
# že součet všech vlastních dělitelů jednoho čísla se rovná
# druhému číslu, a naopak – součet všech vlastních dělitelů
# druhého čísla se rovná prvnímu.
#
# Za vlastní dělitele čísla považujeme všechny jeho kladné
# dělitele s výjimkou čísla samotného; např. vlastní dělitelé
# čísla 12 jsou 1, 2, 3, 4, 6.

def get_dividers_sum(number):
    summ = 0

    for i in range(1, number // 2 + 1):
        if number % i == 0:
            summ += i

    return summ


def amicable(a, b):
    return get_dividers_sum(a) == b and  get_dividers_sum(b) == a


def main():
    assert not amicable(136, 241)
    assert not amicable(1, 1)
    assert amicable(220, 284)
    assert amicable(1184, 1210)
    assert amicable(2620, 2924)
    assert not amicable(1190, 1212)
    assert not amicable(349, 234)


if __name__ == "__main__":
    main()
