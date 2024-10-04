from ib111 import week_03  # noqa

# hodnotit: ne/ano (umažte „ne/“ pro hodnocení kvality tohoto řešení)


# V tomto domácím úkolu si naprogramujete zjednodušenou variantu hry «2048¹».
# Na rozdíl od původní hry budeme uvažovat jen jednorozměrný hrací plán,
# tj. jeden řádek.
#
# ¹ ‹https://play2048.co/›
#
# Hrací plán budeme reprezentovat pomocí seznamu nezáporných celých čísel;
# nuly budou představovat prázdná místa.
# Například seznam ‹[2, 0, 0, 2, 4, 8, 0]› reprezentuje následující situaci:
#
#  ┌───┬───┬───┬───┬───┬───┬───┐
#  │ 2 │   │   │ 2 │ 4 │ 8 │   │
#  └───┴───┴───┴───┴───┴───┴───┘
#
# Základním krokem hry je posun doleva nebo doprava. Při posunu se všechna
# čísla „sesypou“ v zadaném směru, přičemž dvojice stejných číslic se sečtou.
# Posunem doleva se tedy uvedený seznam změní na ‹[4, 4, 8, 0, 0, 0, 0]›.
#
# Abyste si hru mohli vyzkoušet (poté, co úlohu vyřešíte), je vám k dispozici
# soubor ‹game_2048.py›, který vložte do stejného adresáře, jako je soubor
# s vaším řešením, případně jej upravte dle komentářů na jeho začátku
# a spusťte. Hra se ovládá šipkami doleva a doprava, ‹R› hru resetuje
# a ‹Q› ukončí.
#
# Napište proceduru ‹slide›, která provede posun řádku reprezentovaného
# seznamem ‹row›, a to buď doleva (pokud má parametr ‹to_left› hodnotu ‹True›)
# nebo doprava (pokud má parametr ‹to_left› hodnotu ‹False›). Procedura přímo
# modifikuje parametr ‹row› a vrací ‹True›, pokud posunem došlo k nějaké
# změně; v opačném případě vrací ‹False›.

def slide(row, to_left):
    changed = False

    if to_left:
        my_range = range(len(row) - 1)
        add = 1
    else:
        my_range = range(len(row) - 1, 0, -1)
        add = -1

    for i in my_range:
        next = i + add
        while 0 < next < len(row) - 1 and row[next] == 0:
            next += add
        if row[i] == row[next] and row[i] != 0:
            row[i] *= 2
            row[next] = 0
            changed = True

    for i in my_range:
        next = i + add
        while 0 < next < len(row) - 1 and row[next] == 0:
            next += add
        if row[i] == 0 and row[next] != 0:
            row[i] = row[next]
            row[next] = 0
            changed = True

    return changed


def main():
    row = [0, 2, 2, 0]
    assert slide(row, True)
    assert row == [4, 0, 0, 0]

    row = [2, 2, 2, 2, 2]
    assert slide(row, False)
    assert row == [0, 0, 2, 4, 4]

    row = [2, 0, 0, 2, 4, 2, 2, 2]
    assert slide(row, True)
    assert row == [4, 4, 4, 2, 0, 0, 0, 0]

    row = [3, 0, 6, 3, 3, 3, 6, 0, 6]
    assert slide(row, False)
    assert row == [0, 0, 0, 0, 3, 6, 3, 6, 12]

    row = [16, 8, 4, 2, 0, 0, 0]
    assert not slide(row, True)
    assert row == [16, 8, 4, 2, 0, 0, 0]


if __name__ == '__main__':
    main()
