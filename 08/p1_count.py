from ib111 import week_08  # noqa


# Implementujte čistou funkci ‹count_in_sorted›, která ve vzestupně
# seřazeném seznamu ‹records› co nejefektivněji spočte počet výskytů
# hodnoty ‹value›. K hodnotám v ‹records› přistupujte použitím
# metody ‹get›: např. ‹records.get(7)› vrátí hodnotu na indexu 7.
# Délku seznamu získáte voláním ‹records.size()›.
# Dobré řešení úlohy je logaritmické časové složitosti.
def get_index_of_first_near(records: 'CountingList', value: int, low: int, high: int) -> int:
    is_bigger = (low == 0)          # to find bigger or smaller than value
    index = (high + low) // 2
    size = records.size()
    step = size // 2
    
    while low < high:
        if is_bigger:
            index += step
        else:
            index -= step

        if index < low or index > high:
            step //= (-2)
            continue
        current = records.get(index)
        if is_bigger and current > value:
            step //= (-2)
        elif not is_bigger and current < value:
            step //= (-2)

    return 0


def count_in_sorted(records: 'CountingList', value: int) -> int:

    low, high = 0, records.size()
    size = records.size()
    count = 0

    while low < high:
        mid = (low + high) // 2
        mid_value = records.get(mid)

        if mid_value == value:
            count += 1
            get_index_of_first_near(records, value, mid, size)
            get_index_of_first_near(records, value, 0, mid)
            return count

        if mid_value < value:
            low = mid + 1
        elif mid_value > value:
            high = mid

    return 0


def main() -> None:
    assert count_in_sorted(CountingList([1, 2, 2, 5]), 2) == 2
    assert count_in_sorted(CountingList([1, 2, 2, 5]), 1) == 1
    assert count_in_sorted(CountingList([1, 2, 2, 2, 2]), 2) == 4
    assert count_in_sorted(CountingList([2, 2, 2, 3]), 2) == 3
    assert count_in_sorted(CountingList([1, 2, 2, 5]), 10) == 0
    big_1 = CountingList([x // 3 for x in range(1000)])
    big_2 = CountingList([x // 7 for x in range(1000)])
    assert count_in_sorted(big_1, 180) == 3
    assert big_1.access_count() < 100
    assert count_in_sorted(big_2, 90) == 7
    assert big_2.access_count() < 100
    big_3 = CountingList([1, 1] + [2 for i in range(1000)] + [3, 3])
    assert count_in_sorted(big_3, 2) == 1000
    print(big_3.access_count())
    assert big_3.access_count() < 100


class CountingList:

    def __init__(self, items: list[int]):
        self.__items = items
        self.__count = 0

    def get(self, index: int) -> int:
        self.__count += 1
        return self.__items[index]

    def size(self) -> int:
        return len(self.__items)

    def access_count(self) -> int:
        return self.__count


if __name__ == "__main__":
    main()
