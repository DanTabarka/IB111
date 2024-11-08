from ib111 import week_03  # noqa


# Naprogramujte (čistou) funkci, která ze dvou vzestupně seřazených
# seznamů čísel ‹a›, ‹b› vytvoří nový vzestupně seřazený seznam,
# který bude obsahovat všechny prvky z ‹a› i ‹b›. Nezapomeňte, že
# nesmíte modifikovat vstupní seznamy (jinak by funkce nebyla
# čistá). Pokuste se funkci naprogramovat «efektivně».

def merge(a, b):
    ptr_a = 0
    ptr_b = 0
    merged = []

    while ptr_a < len(a) and ptr_b < len(b):
        if a[ptr_a] < b[ptr_b]:
            merged.append(a[ptr_a])
            ptr_a += 1
        else:
            merged.append(b[ptr_b])
            ptr_b += 1

    for i in range(ptr_a, len(a)):  # remainder of A
        merged.append(a[i])

    for i in range(ptr_b, len(b)):  # remainder of B
        merged.append(b[i])

    return merged


def main():
    assert merge([1, 2, 3], [1, 2, 3]) == [1, 1, 2, 2, 3, 3]
    assert merge([0, 2, 4, 6, 8], [1, 3, 5, 7, 9]) \
        == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert merge([], []) == []
    assert merge([], [1, 2]) == [1, 2]
    assert merge([1, 2], []) == [1, 2]
    assert merge([1, 5, 10], [-1, 2, 3, 4, 6, 10, 11]) \
        == [-1, 1, 2, 3, 4, 5, 6, 10, 10, 11]


if __name__ == "__main__":
    main()
