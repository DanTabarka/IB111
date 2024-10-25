from ib111 import week_05  # noqa

# hodnotit: ne/ano (umažte „ne/“ pro hodnocení kvality tohoto řešení)


# «Connect Four¹» je hra pro dva hráče, v češtině někdy nazývaná Cestovní nebo
# Padající piškvorky. Každý hráč má žetony v jedné barvě; vyhrává ten, kdo jako
# první vytvoří nepřerušenou řadu «přesně čtyř» svých žetonů (horizontální,
# vertikální, diagonální). Hrací deska je přitom postavena vertikálně tak, že
# žetony padají směrem dolů, dokud nenarazí na jiný žeton nebo spodní rám
# desky. Hráč si tedy při svém tahu volí pouze sloupec, do nějž žeton hodí.
# (Na rozdíl od klasických piškvorek, kde si hráč volí přesné souřadnice
# a nic nikam nepadá.)
#
# ¹ ‹https://en.wikipedia.org/wiki/Connect_Four›
#
# Pro reprezentaci žetonů hráčů budeme v tomto úkolu používat znaky ‹X› a ‹O›.
# Hrací desku bude představovat seznam seznamů žetonů – vnitřní seznamy jsou
# postupně jednotlivé sloupce desky seřazené zdola nahoru. Tedy např. seznam
# ‹[['X'], [], ['O', 'X'], [], ['X', 'O', 'O'], [], []]›
# popisuje následující situaci:
#
#  ┌───┬───┬───┬───┬───┬───┬───┐
#  │   │   │   │   │ O │   │   │
#  ├───┼───┼───┼───┼───┼───┼───┤
#  │   │   │ X │   │ O │   │   │
#  ├───┼───┼───┼───┼───┼───┼───┤
#  │ X │   │ O │   │ X │   │   │
#  └───┴───┴───┴───┴───┴───┴───┘
#    0   1   2   3   4   5   6
#
# V naší reprezentaci přitom nemáme žádnou maximální výšku. Do sloupce
# s indexem 4 tedy je možno přidat další žeton a celá herní deska se tak
# nadstaví o další řádek.
#
# Pro hrací desku používáme typový alias ‹Grid›.

Grid = list[list[str]]


# Herní desku budeme chtít v průběhu hry (textově) vykreslovat. Samotná
# vykreslovací procedura je připravená v dodaném souboru (viz níže), ale abyste
# jí usnadnili práci, implementuje nejprve čistou funkci ‹to_matrix›, která
# zadanou herní desku ‹grid› zkonvertuje do podoby 2D matice (reprezentované
# seznamem seznamů jako na přednášce). Matice bude mít přesně tolik řádků,
# kolik je potřeba. (Matice s nula řádky je prázdný seznam.)
# Prvky matice budou jednoznakové řetězce ‹" "› (prázdné místo), ‹"X"›, ‹"O"›.
#
# Pro desku z výše uvedené situaci tedy funkce ‹to_matrix› vrátí tento seznam:
# ‹[[" ", " ", " ", " ", "O", " ", " "],
#   [" ", " ", "X", " ", "O", " ", " "],
#   ["X", " ", "O", " ", "X", " ", " "]]›

def to_matrix(grid: Grid) -> list[list[str]]:
    pass


# Dále pak implementujte proceduru ‹play›, která provede do zadané herní desky
# ‹grid› vhození žetonu hráče ‹player› do sloupce ‹column›. Předpokládejte
# přitom, že herní deska je ve stavu, kdy ještě nikdo nevyhrál, ‹player› je
# buďto ‹'X'› nebo ‹'O'› a ‹column› je validní index sloupce. Procedura vrátí
# ‹True›, pokud tímto tahem hráč vyhrál; ‹False› jinak.
#
# Pro jistotu připomínáme, že za výhru považujeme pouze situaci, kdy má některý
# z hráčů nepřerušenou řadu «přesně čtyř» svých žetonů. Pokud tedy vhozením
# žetonu vznikne nepřerušená řada více než čtyř žetonů, o výhru se nejedná.

def play(grid: Grid, player: str, column: int) -> bool:
    pass


# Pro (textovou) vizualizaci je vám k dispozici soubor ‹game_connect_four.py›,
# který vložte do stejného adresáře, jako je soubor s vaším řešením a spusťte.
# Počet sloupců herní desky nastavíte jako globální konstantu ‹SIZE›.


def main() -> None:
    grid: Grid = [['X'], [], ['O', 'X'], [], ['X', 'O', 'O'], [], []]
    assert to_matrix(grid) == [
        [" ", " ", " ", " ", "O", " ", " "],
        [" ", " ", "X", " ", "O", " ", " "],
        ["X", " ", "O", " ", "X", " ", " "],
    ]

    assert not play(grid, 'X', 3)
    assert grid == [['X'], [], ['O', 'X'], ['X'], ['X', 'O', 'O'], [], []]

    assert not play(grid, 'O', 3)
    assert grid == [['X'], [], ['O', 'X'], ['X', 'O'], ['X', 'O', 'O'], [], []]

    assert not play(grid, 'X', 5)
    assert grid \
        == [['X'], [], ['O', 'X'], ['X', 'O'], ['X', 'O', 'O'], ['X'], []]

    assert not play(grid, 'O', 5)
    assert grid \
        == [['X'], [], ['O', 'X'], ['X', 'O'], ['X', 'O', 'O'], ['X', 'O'], []]

    assert not play(grid, 'X', 5)
    assert grid \
        == [['X'], [], ['O', 'X'], ['X', 'O'],
            ['X', 'O', 'O'], ['X', 'O', 'X'], []]

    assert play(grid, 'O', 5)
    assert grid \
        == [['X'], [], ['O', 'X'], ['X', 'O'],
            ['X', 'O', 'O'], ['X', 'O', 'X', 'O'], []]


if __name__ == '__main__':
    main()
