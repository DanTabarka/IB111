from ib111 import week_05  # noqa

# Známky studentů z jednoho předmětu jsou uloženy ve slovníku, kde
# klíčem je UČO studenta a hodnotou je známka zadaná jako písmeno.
# Možná hodnocení jsou 'A' až 'F', dále, 'N', 'P', 'X', 'Z' a '-'.

# Napište čistou funkci ‹modus›, jejímž vstupem bude slovník známek
# a výstupem bude jejich modus, tedy nejčastější hodnota.
# Předpokládejte, že známek se stejnou četností může být více, takže
# funkce bude vždy vracet množinu známek, a to i v případě, že je
# nejčastější hodnota určena jednoznačně. V případě, že je vstupní
# slovník prázdný, bude výstupem prázdná množina.


def modus(marks: dict[int, str]) -> set[str]:
    d: dict[str, int] = {}

    for _, mark in marks.items():
        d[mark] = d.get(mark, 0) + 1

    max_count = max(d.values()) if d else 0

    most_frequent = [mark for mark, c in d.items() if c == max_count]

    return set(most_frequent)


# Dále napište predikát ‹check›, který ověří, že známky jsou
# smysluplné, tedy že odpovídají buďto předmětu ukončenému zkouškou
# (známky 'A' - 'F', nebo 'X'), kolokviem (známky 'P' nebo 'N'),
# anebo zápočtem (známky 'Z' nebo 'N'). Hodnocení '-' je možné
# u jakéhokoliv způsobu hodnocení. Klasifikované zápočty
# neuvažujeme.

def exam(marks: set[str]) -> bool:
    return {"A", "B", "C", "D", "E", "F", "X"} >= marks


def kolokviem(marks: set[str]) -> bool:
    return {"P", "N"} >= marks


def credit(marks: set[str]) -> bool:
    return {"Z", "N", "-"} >= marks


def check(marks: dict[int, str]) -> bool:
    marks_set = set(marks.values())

    return exam(marks_set) or kolokviem(marks_set) or credit(marks_set)


def main() -> None:
    assert modus({}) == set()
    assert modus({100000: 'P'}) == {'P'}
    assert modus({100000: 'A', 100001: 'B', 100002: 'A'}) == {'A'}
    assert modus({100000: 'A', 100001: 'B', 100002: 'A', 100003: 'B'}) \
           == {'A', 'B'}
    assert check({})
    assert check({100000: 'P'})
    assert check({100000: '-'})
    assert check({100000: 'A', 100001: 'B', 100002: 'A'})
    assert check({100000: 'A', 100001: 'B', 100002: 'A', 100003: 'B'})
    assert not check({100000: 'A', 100001: 'B', 100002: 'A', 100003: 'N'})
    assert not check({100000: 'P', 100001: 'N', 100002: 'Z', 100003: '-'})


if __name__ == "__main__":
    main()
