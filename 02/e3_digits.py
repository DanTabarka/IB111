from ib111 import week_02  # noqa


# Napište funkci ‹count_digit_in_sequence›, která spočte kolikrát se
# cifra ‹digit› vyskytuje v číslech v rozmezí od čísla ‹low› po
# číslo ‹high› včetně. Například cifra 1 se na intervalu od 0 po 13
# vyskytuje šestkrát, konkrétně v číslech: 1 10 11 12 13.

def count_digit_in_sequence(digit, low, high):
    count = 0
    if low == 0 and digit == 0:
        count += 1
    
    for num in range(low, high + 1):
        while num > 0:
            if num % 10 == digit:
                count += 1
            num //= 10

    return count


def main():
    assert count_digit_in_sequence(1, 0, 13) == 6
    assert count_digit_in_sequence(0, 10, 20) == 2
    assert count_digit_in_sequence(0, 0, 10) == 2
    assert count_digit_in_sequence(4, 15, 23) == 0
    assert count_digit_in_sequence(5, 20, 120) == 20
    assert count_digit_in_sequence(0, 10, 100) == 11
    assert count_digit_in_sequence(2, 111, 1000) == 279


if __name__ == "__main__":
    main()
