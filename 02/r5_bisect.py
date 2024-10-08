from ib111 import week_02  # noqa
from math import sqrt


# † Napište funkci ‹bisect›, která aproximuje kořen spojité funkce
# ⟦f⟧ (předané parametrem ‹fun›) s chybou menší než ‹epsilon› na
# zadaném intervalu od ‹low› po ‹high› včetně. Algoritmus bisekce
# předpokládá, že v zadaném intervalu se nachází právě jedno řešení.
#
# Při hledání řešení postupujte následovně:
#
#  1. spočtěte hodnotu funkce pro bod uprostřed intervalu, a je-li
#     výsledek v rozsahu povolené chyby, vraťte tento bod,
#  2. jinak spočtěte hodnoty funkce v hraničních bodech intervalu
#     a zjistěte, ve které polovině má funkce kořen,
#  3. opakujte výpočet s vybranou polovinou jako s novým intervalem.
#
# Chybu ⟦e⟧ spočtete v bodě ⟦x⟧ jako ⟦e = |f(x)|⟧.
#
# Poznámka: funkci předanou parametrem můžete v Pythonu normálně
# volat jako libovolnou jinou funkci.

def bisect(fun, low, high, eps):
    mid = (low + high) / 2

    mid_value = fun(mid)

    if abs(mid_value) < eps:
        return mid
    
    if fun(low) * mid_value < 0:    # low -> mid change of sign
        return bisect(fun, low, mid, eps) 
    return bisect(fun, mid, high, eps)  # mid -> high change of sign



def fun_a(x):
    return x ** 2 - 3


def fun_b(x):
    return x ** 3 - x - 1


def fun_c(x):
    return sqrt(x) / x - x ** 3 + 5


def main():
    assert abs(fun_a(bisect(fun_a, 1.0, 2.0, 0.01))) < 0.01
    assert abs(fun_a(bisect(fun_a, 1.0, 2.0, 0.0001))) < 0.0001
    assert abs(fun_b(bisect(fun_b, 1.0, 5.0, 0.001))) < 0.001
    assert abs(fun_c(bisect(fun_c, 1.0, 10.0, 0.001))) < 0.001


if __name__ == "__main__":
    main()
