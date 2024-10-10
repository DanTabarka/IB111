from ib111 import week_05  # noqa


# V tomto příkladu dostanete dva seznamy obsahující celá čísla.
# Vaším úkolem je napsat čistou funkci ‹largest_common_sublist_sum›,
# která najde takový společný podseznam seznamů ‹left› a ‹right›,
# který má největší celkový součet, a tento součet vrátí.

# Podseznamem seznamu ‹S› myslíme takový seznam ‹T›, pro který
# existuje číslo ‹k› takové, že platí ‹S[k + i] == T[i]› pro všechna
# ‹i› taková, že ⟦0 ≤ i < len(T)⟧. Například seznam ‹[1, 2]› je
# podseznamem seznamu ‹[0, 1, 2, 3]›, kde ‹k = 1›.

# Složitost smí být v nejhorším případě až kubická vzhledem k délce
# delšího vstupního seznamu.

def largest_common_sublist_sum(left: list[int], right: list[int]) -> int:
    largest_sum = 0
    tmp_sum = 0

    idx_left = 0
    idx_right = 0

    while idx_left < len(left) and idx_right < len(right):
        if left[idx_left] == right[idx_right]:
            tmp_sum += left[idx_left]
            idx_left += 1
            idx_right += 1

        else:
            if tmp_sum > largest_sum:
                largest_sum = tmp_sum
            tmp_sum = 0

            if left[idx_left] > right[idx_right]:
                idx_right += 1
            elif left[idx_left] < right[idx_right]:
                idx_left += 1
    return largest_sum
        



def main() -> None:
    l1: list[int] = []
    l2 = [1, 2, 3, 4, 5]
    l3 = [2, 3, 4, 6, 7, 9, 10]
    l4 = [1, 2, 3, 8, 9]

    assert largest_common_sublist_sum(l1, l2) == 0
    assert largest_common_sublist_sum(l2, l3) == 9
    assert largest_common_sublist_sum(l2, l4) == 6
    assert largest_common_sublist_sum(l3, l4) == 9


if __name__ == "__main__":
    main()
