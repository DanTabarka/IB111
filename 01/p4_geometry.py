from ib111 import week_01  # noqa


# Napište predikát (tj. čistou funkci, která vrací pravdivostní
# hodnotu – boolean), který je pravdivý, je-li možno vytvořit
# pravoúhlý trojúhelník ze stran o délkách zadaných kladnými
# celými čísly ‹a›, ‹b› a ‹c›.

def is_right(a, b, c):
    return (a ** 2 == b ** 2 + c ** 2) or \
            (b ** 2 == a ** 2 + c ** 2) or \
            (c ** 2 == b ** 2 + a ** 2)


# Dále napište predikát, který je pravdivý, popisují-li parametry
# ‹a›, ‹b› a ‹c› rovnostranný trojúhelník.

def is_equilateral(a, b, c):
    return a == b and b == c


# Konečně napište predikát, který je pravdivý, popisují-li parametry
# ‹a›, ‹b› a ‹c› rovnoramenný trojúhelník.

def is_isosceles(a, b, c):
    return (a == b or c == b or a == c) and \
            (a + b > c and a + c > b and b + c > a)


def main():
    assert is_right(3, 4, 5)
    assert is_right(4, 3, 5)
    assert is_right(5, 4, 3)
    assert is_right(17, 15, 8)
    assert not is_right(1, 1, 1)
    assert not is_right(2, 5, 5)
    assert not is_right(10, 3, 7)
    assert not is_right(3, 2, 1)

    assert is_equilateral(1, 1, 1)
    assert not is_equilateral(2, 1, 3)

    assert is_isosceles(1, 1, 1)
    assert is_isosceles(2, 2, 1)
    assert is_isosceles(1, 3, 3)
    assert is_isosceles(2, 1, 2)
    assert not is_isosceles(1, 4, 7)
    assert not is_isosceles(3, 1, 7)
    assert not is_isosceles(1, 1, 4)
    assert not is_isosceles(1, 4, 1)
    assert not is_isosceles(4, 1, 1)


if __name__ == "__main__":
    main()
