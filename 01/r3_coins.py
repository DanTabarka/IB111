from ib111 import week_01  # noqa


# Uvažme, že chceme přesně zaplatit sumu ‹value›, přičemž máme
# k dispozici pouze mince denominací 1, 2 a 5 korun.
# Spočtěte, kolik nejméně mincí potřebujeme.

def coins(value):
    coins = 0

    coins += value // 5
    value %= 5

    coins += value // 2
    value %= 2
    
    coins += value
    
    return coins


def main():
    assert coins(10) == 2
    assert coins(23) == 6
    assert coins(48) == 11
    assert coins(92) == 19
    assert coins(314) == 64
    assert coins(1043) == 210


if __name__ == "__main__":
    main()
