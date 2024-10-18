from ib111 import week_04  # noqa
from math import sqrt, sin, cos, radians, acos, pi, isclose

# V této úloze bude Vašim úkolem rozšířit a otypovat implementaci
# z ukázky ‹02/triangle.py›.
#
# Strany trojúhelníku značíme ⟦a, b, c⟧. Úhel mezi ⟦a⟧ a ⟦b⟧ je ⟦γ⟧
# (‹gamma›), mezi ‹b› a ‹c› je ⟦α⟧ (‹alpha›) a mezi ⟦c⟧ a
# ⟦a⟧ je úhel ⟦β⟧ (‹beta›):
#
#           ● A
#          ╱ ╲
#         ╱ α ╲
#        ╱     ╲
#     c ╱       ╲ b
#      ╱         ╲
#     ╱           ╲
#    ╱ β         γ ╲
# B ●───────────────● C
#           a
#
# 1. Prvním úkolem bude implementovat obecnou funkci ‹perimeter›, která má
#    volitelné parametry tří stran a tří úhlů trojúhelníku. Je-li to možné
#    z předaných parametrů, funkce spočítá obvod trojúhelníku jednou z metod
#    «SSS», «ASA», «SAS», jinak vrátí ‹None›.
#
# 2. Druhým úkolem bude otypovat zbytek pomocných funkcí tak, aby Vám prošla
#    typová kontrola. Typ funkce ‹perimeter› neměňte.


def is_one_none(x: float | None, y: float | None, z: float | None) -> bool:
    return x is None or y is None or z is None


def perimeter(a: float | None,
              b: float | None,
              c: float | None,
              alpha: float | None,
              beta: float | None,
              gamma: float | None) -> float | None:
    if not is_one_none(a, b, c):
        assert a is not None and b is not None and c is not None
        return perimeter_sss(a, b, c)

    if not is_one_none(a, gamma, b):
        assert a is not None and b is not None and gamma is not None
        return perimeter_sas(a, gamma, b)
    if not is_one_none(a, beta, c):
        assert a is not None and beta is not None and c is not None
        return perimeter_sas(a, beta, c)
    if not is_one_none(b, alpha, c):
        assert alpha is not None and b is not None and c is not None
        return perimeter_sas(b, alpha, c)

    if not is_one_none(beta, a, gamma):
        assert a is not None and beta is not None and gamma is not None
        return perimeter_asa(beta, a, gamma)
    if not is_one_none(alpha, b, gamma):
        assert alpha is not None and b is not None and gamma is not None
        return perimeter_asa(alpha, b, gamma)
    if not is_one_none(alpha, c, beta):
        assert alpha is not None and beta is not None and c is not None
        return perimeter_asa(alpha, c, beta)

    return None


# Funkce ‹perimeter_sss› spočte obvod trojúhelníku zadaného třemi stranami.

def perimeter_sss(a: float, b: float, c: float) -> float:
    return a + b + c


# Funkce ‹perimeter_sas› spočte obvod trojúhelníku zadaného dvěma stranami a
# nimi sevřeným úhlem.

def perimeter_sas(a: float, angle: float, b: float) -> float:
    c = sqrt(a ** 2 + b ** 2 - 2 * a * b * cos(radians(angle)))
    return perimeter_sss(a, b, c)


# Funkce ‹perimeter_asa› spočte obvod trojúhelníku zadaného stranou a jí
# přilehlých úhlů.

def perimeter_asa(alpha: float, c: float, beta: float) -> float:
    gamma = radians(180 - alpha - beta)
    alpha = radians(alpha)
    beta = radians(beta)
    a = c * sin(alpha) / sin(gamma)
    b = c * sin(beta) / sin(gamma)
    return perimeter_sss(a, b, c)


def main() -> None:
    for a in range(1, 6):
        for b in range(1, 6):
            for c in range(max(abs(a - b) + 1, 1), a + b):
                check_triangle(float(a), float(b), float(c))


# Pomocné funkce pro testy, které spočítají úhel ze zadaných stran.

def get_alpha(a: float, b: float, c: float) -> float:
    return acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)) * 180 / pi


def get_beta(a: float, b: float, c: float) -> float:
    return acos((a ** 2 + c ** 2 - b ** 2) / (2 * a * c)) * 180 / pi


def check_triangle(a: float, b: float, c: float) -> None:
    alpha = get_alpha(a, b, c)
    beta = get_beta(a, b, c)
    gamma = 180 - alpha - beta

    res = perimeter(a, b, c, alpha, beta, gamma)
    assert res is not None and isclose(res, a + b + c)
    res = perimeter(None, b, c, alpha, beta, gamma)
    assert res is not None and isclose(res, a + b + c)
    res = perimeter(a, None, c, alpha, beta, gamma)
    assert res is not None and isclose(res, a + b + c)
    res = perimeter(a, b, None, alpha, beta, gamma)
    assert res is not None and isclose(res, a + b + c)
    res = perimeter(a, b, c, None, beta, gamma)
    assert res is not None and isclose(res, a + b + c)
    res = perimeter(a, b, c, None, None, None)
    assert res is not None and isclose(res, a + b + c)
    res = perimeter(a, b, None, None, None, gamma)
    assert res is not None and isclose(res, a + b + c)
    res = perimeter(None, b, c, alpha, None, None)
    assert res is not None and isclose(res, a + b + c)
    res = perimeter(a, None, c, None, beta, None)
    assert res is not None and isclose(res, a + b + c)
    res = perimeter(None, b, None, alpha, None, gamma)
    assert res is not None and isclose(res, a + b + c)
    res = perimeter(a, None, None, None, beta, gamma)
    assert res is not None and isclose(res, a + b + c)
    res = perimeter(None, None, c, alpha, beta, None)
    assert res is not None and isclose(res, a + b + c)
    res = perimeter(a, b, c, alpha, beta, gamma)
    assert res is not None and isclose(res, a + b + c)

    assert perimeter(None, None, None, None, None, None) is None
    assert perimeter(a, b, None, None, None, None) is None
    assert perimeter(a, None, c, None, None, None) is None
    assert perimeter(None, None, None, alpha, beta, gamma) is None
    assert perimeter(None, b, None, None, None, gamma) is None
    assert perimeter(None, None, c, None, None, gamma) is None
    assert perimeter(None, b, c, None, None, gamma) is None


if __name__ == '__main__':
    main()
