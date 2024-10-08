from ib111 import week_03  # noqa
from math import isclose, sqrt


# Napište čistou funkci, která dostane na vstup seznam bodů v rovině
# (tj. seznam dvojic čísel) a vrátí délku lomené čáry, která těmito
# body prochází (tzn. takové, která vznikne spojením každých dvou
# sousedních bodů seznamu úsečkou). Souřadnice i délky
# reprezentujeme čísly s plovoucí desetinnou čárkou (typ ‹float›).

# Například seznam ‹[(0, 0), (1, 0), (1, 1), (2, 1)]› definuje tuto
# lomenou čáru:
#
#       (1, 1) ┌───▶(2, 1)
#              │
#    (0, 0)╶───┘(1, 0)
#
# složenou ze tří segmentů (úseček) velikosti 1. Její délka je 3.


def point_distance(a, b):
    ax, ay = a
    bx, by = b
    return sqrt((ax - bx) ** 2 + (ay - by) ** 2)


def length(points):
    if len(points) <= 1:
        return 0.0

    res = 0.0
    for i in range(len(points) - 1):
        res += point_distance(points[i], points[i + 1])

    return res


def main():
    assert isclose(point_distance((0.0, 0.0), (1.0, 0.0)), 1.0)
    assert isclose(point_distance((3.0, 0.0), (0.0, 4.0)), 5.0)
    assert isclose(length([(0.0, 1.0), (1.0, 1.0), (1.0, 2.0)]), 2.0)
    assert isclose(length([(0.0, 0.0)]), 0.0)
    assert isclose(length([]), 0.0)
    assert isclose(length([(3.0, 5.0), (3.0, 15.0), (4.0, 15.0),
                           (4.0, 0.0), (0.0, 0.0)]), 30.0)
    assert isclose(length([(0.0, 0.0), (3.0, 4.0)]), 5.0)
    assert isclose(length([(0.0, 0.0), (3.0, 4.0), (3.0, 7.0)]), 8.0)


if __name__ == "__main__":
    main()
