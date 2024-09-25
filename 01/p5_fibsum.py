from ib111 import week_01  # noqa


# Napište funkci, která spočítá sumu prvních ‹n› «sudých» členů
# Fibonacciho posloupnosti (tj. členů, které jsou sudé, nikoliv
# těch, které mají sudé indexy). Například volání ‹fibsum(3) = 44 =
# 2 + 8 + 34›.

def fibsum(n):
    first = 1
    second = 1
    summary = 0
    while n > 0:
        tmp = second
        second += first
        first = tmp
        if second % 2 == 0:
            n -= 1
            summary += second

    return summary


def main():
    assert fibsum(0) == 0
    assert fibsum(1) == 2
    assert fibsum(2) == 10
    assert fibsum(3) == 44
    assert fibsum(4) == 188
    assert fibsum(5) == 798
    assert fibsum(10) == 1089154


if __name__ == "__main__":
    main()
