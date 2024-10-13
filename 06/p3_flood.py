from ib111 import week_06  # noqa

# «Flood fill» je algoritmus z oblasti rastrové grafiky, který
# vyplní souvislou jednobarevnou plochu nějakou jinou barvou.
# Postupuje tak, že nejdříve na novou barvu obarví pozici, na které
# začíná, dále se pokusí obarvit její sousedy (pozice jiné než
# cílové barvy se neobarvují), a podobně pokračuje se sousedy těchto
# sousedů, atd. Zastaví se, dojde-li na okraj obrázku, nebo narazí
# na pixel, který nemá žádné nové stejnobarevné sousedy.
#
# Sousední pixely uvažujeme pouze ve čtyřech směrech, tj. ne diagonálně.

# Napište proceduru, která na vstupu dostane plochu reprezentovanou
# obdélníkovým seznamem seznamů (délky všech vnitřních seznamů jsou
# stejné), počáteční pozici (je zaručeno, že se bude jednat o platné
# souřadnice), a cílovou barvu, na kterou mají být vybrané pozice
# přebarveny.

Position = tuple[int, int]
Area = list[list[int]]


def flood_fill(area: Area, start: Position, colour: int) -> None:
    stack = [start]
    row, col = start
    colour_to_fill = area[row][col]
    row_count = len(area)
    col_count = len(area[0])

    while stack:
        row, col = stack.pop()
        area[row][col] = colour

        # up
        if row - 1 >= 0 and area[row - 1][col] == colour_to_fill:
            stack.append((row - 1, col))
        # down
        if row + 1 < row_count and area[row + 1][col] == colour_to_fill:
            stack.append((row + 1, col))
        # left
        if col - 1 >= 0 and area[row][col - 1] == colour_to_fill:
            stack.append((row, col - 1))
        # right
        if col + 1 < col_count and area[row][col + 1] == colour_to_fill:
            stack.append((row, col + 1))


def main() -> None:
    check_flood([[0]], (0, 0), 1, [[1]])
    check_flood([[0, 0, 1, 1, 1, 0]], (0, 3), 2, [[0, 0, 2, 2, 2, 0]])
    check_flood([[0, 0, 1, 1, 1, 0]], (0, 0), 2, [[2, 2, 1, 1, 1, 0]])
    check_flood([[1, 2, 3, 4], [1, 1, 1, 1], [2, 2, 2, 1], [5, 5, 1, 1]],
                (1, 1), 8,
                [[8, 2, 3, 4], [8, 8, 8, 8], [2, 2, 2, 8], [5, 5, 8, 8]])
    check_flood([[1, 2, 3, 4], [1, 1, 1, 1], [2, 2, 2, 1], [1, 5, 1, 1]],
                (1, 1), 8,
                [[8, 2, 3, 4], [8, 8, 8, 8], [2, 2, 2, 8], [1, 5, 8, 8]])


def check_flood(area: Area, start: Position,
                new_colour: int, expected_result: Area) -> None:
    flood_fill(area, start, new_colour)
    assert area == expected_result


if __name__ == '__main__':
    main()
