from ib111 import week_03  # noqa


# Napište (čistou) funkci, která pro zadaný seznam nezáporných čísel
# ‹data› vrátí nový seznam obsahující dvojice – číslo a jeho
# četnost. Výstupní seznam musí být seřazený vzestupně dle první
# složky. Můžete předpokládat, že v ‹data› se nachází pouze celá
# čísla z rozsahu [0, 100] (včetně).
def get_index(arr, number):
    for i, num in enumerate(arr):
        if num == number:
            return i
    return -1


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def histogram(data):
    bubble_sort(data)
    numbers = []
    frequency = []

    for num in data:
        index = get_index(numbers, num)
        if index == -1:
            numbers.append(num)
            frequency.append(1)
        else:
            frequency[index] += 1

    pairs = []
    for i in range(len(numbers)):
        pairs.append((numbers[i], frequency[i]))

    return pairs


def main() -> None:
    assert histogram([1, 2, 3, 2, 1]) == [(1, 2), (2, 2), (3, 1)]
    assert histogram([7, 1, 7, 1, 5]) == [(1, 2), (5, 1), (7, 2)]
    assert histogram([1, 1, 1]) == [(1, 3)]
    assert histogram([]) == []


if __name__ == "__main__":
    main()
