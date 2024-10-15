from ib111 import week_03  # noqa


# Napište (čistou) funkci, která pro zadaný seznam nezáporných čísel
# ‹data› vrátí nový seznam obsahující dvojice – číslo a jeho
# četnost. Výstupní seznam musí být seřazený vzestupně dle první
# složky. Můžete předpokládat, že v ‹data› se nachází pouze celá
# čísla z rozsahu [0, 100] (včetně).

def histogram(data):
    c = [0 for _ in range(100)]
    for number in data:
        c[number] += 1
    pairs = [(i, c[i]) for i in range(100) if c[i] > 0]
    return pairs


def main() -> None:
    assert histogram([1, 2, 3, 2, 1]) == [(1, 2), (2, 2), (3, 1)]
    assert histogram([7, 1, 7, 1, 5]) == [(1, 2), (5, 1), (7, 2)]
    assert histogram([1, 1, 1]) == [(1, 3)]
    assert histogram([]) == []


if __name__ == "__main__":
    main()
