from ib111 import week_05  # noqa


# Binární relací nad danou množinou je množina dvojic prvků z této
# množiny. Daná relace se pak nazývá tranzitivní, platí-li pro
# všechny dvojice ⟦(a, b), (b, c)⟧ z této relace, že se v relaci
# nachází i dvojice ⟦(a, c)⟧. V této úloze budeme pracovat
# s relacemi nad celými čísly.

# Napište predikát, který rozhodne, je-li zadaná relace tranzitivní.

def is_transitive(relation: set[tuple[int, int]]) -> bool:
    pass


def main() -> None:
    assert is_transitive({(1, 2)})
    assert is_transitive(set())
    assert is_transitive({(1, 2), (2, 1), (1, 1), (2, 2)})
    assert is_transitive({(1, 2), (2, 3), (1, 3)})

    assert not is_transitive({(1, 2), (2, 3)})
    assert not is_transitive({(1, 2), (2, 1)})
    assert not is_transitive({(1, 2), (2, 5), (5, 1)})
    assert not is_transitive({(1, 5), (5, 6), (6, 1)})


if __name__ == '__main__':
    main()
