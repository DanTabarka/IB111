from ib111 import week_08  # noqa

# Implementujte čistou funkci ‹frequency_sort›, která podle
# frekvencí výskytu seřadí hodnoty v seznamu ‹values›. Hodnoty se
# stejnou frekvencí výskytu nechť jsou seřazeny vzestupně podle
# hodnoty samotné. Výsledný seznam bude obsahovat každou hodnotu
# právě jednou.


def frequency_sort(values: list[int]) -> list[int]:
    values_count: dict[int, int] = {}
    for val in values:                              # get count
        values_count[val] = values_count.get(val, 0) + 1

    grouped_by_count: dict[int, list[int]] = {}     # group by frequency
    for key, val in values_count.items():
        if val not in grouped_by_count:
            grouped_by_count[val] = []
        grouped_by_count[val].append(key)

    sorted_by_frequency: list[int] = []
    for count in sorted(grouped_by_count.keys()):
        sorted_elements = sorted(grouped_by_count[count])
        sorted_by_frequency = sorted_elements + sorted_by_frequency

    return sorted_by_frequency


def main() -> None:
    assert frequency_sort([]) == []
    assert frequency_sort([1]) == [1]
    assert frequency_sort([1, 3, 2, 4]) == [1, 2, 3, 4]
    assert frequency_sort([5, 6, 2, 5, 3, 3, 6, 5, 5, 6, 5]) == [5, 6, 3, 2]
    assert frequency_sort([1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 5, 5,
                           5, 4, 4, 4, 4, 4, 4]) == [4, 3, 2, 5, 1]
    records = [1, 2, 2, 2, 3, 3]
    assert frequency_sort(records) == [2, 3, 1]
    assert records == [1, 2, 2, 2, 3, 3]


if __name__ == "__main__":
    main()
