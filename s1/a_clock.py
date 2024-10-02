from ib111 import week_00  # noqa
from turtle import done, forward, right, left, backward, penup, pendown
from math import pi, sin

# hodnotit: ne/ano (umažte „ne/“ pro hodnocení kvality tohoto řešení)


# Napište proceduru ‹clock›, která pomocí želví grafiky vykreslí ciferník
# hodin s ručičkami v následující podobě:
#
# • ciferník má tvar dvanáctiúhelníku postaveného „na špičku“ s délkou
#   strany rovnou ‹side›, vrcholy dvanáctiúhelníku tedy odpovídají číslicím;
# • ručičky ukazují čas zadaný ve formátu UNIX Epoch Time, tj. jako
#   počet sekund od 1. 1. 1970, 0.00:00, v parametru ‹epoch_time›;
# • sekundová ručička je znázorněna čarou o délce 1,8násobku ‹side›;
# • minutová ručička je znázorněna prázdným obdélníkem o délce
#   1,6násobku ‹side› a šířce dvacetiny ‹side›;
# • hodinová ručička je znázorněna prázdným obdélníkem o délce
#   1,4násobku ‹side› a šířce desetiny ‹side›;
# • pro ručičky ve tvaru obdélníku platí, že vzdálenost mezi středem ciferníku
#   a kratší stranou obdélníku je polovina jeho šířky.
#
# Parametr ‹epoch_time› je vždy celé číslo, parametr ‹side› je kladné „reálné“
# číslo (typu ‹float›).
#
# Minutová a hodinová ručička se neposunují skokově, ale (v rámci možností)
# spojitě, tj. například v čase 13.30:00 je hodinová ručička přesně
# v polovině úhlu mezi jedničkou a dvojkou.
#
# Testovací prostředí želví grafiky podporuje pouze procedury ‹forward›,
# ‹backward›, ‹right›, ‹left›, ‹penup›, ‹pendown›, ‹setheading›.
# Použití procedur ‹speed›, ‹delay› a ‹done› se sice nepovažuje za chybu,
# ale budou v testech ignorovány, tj. «nebudou mít žádný efekt».


def polygon(length):
    r = length / (2 * sin(pi / 12))
    forward(r)
    right(90 + 360 / 24)
    pendown()
    for _ in range(12):
        forward(length)
        right(360 / 12)

    penup()
    right(90 - 360 / 24)
    forward(r)
    right(180)
    penup()


def draw_rectangle(multiple_a, multiple_b, side):
    pendown()
    left(90)
    forward(multiple_a * side / 2)
    for _ in range(2):
        right(90)
        forward(multiple_b * side)
        right(90)
        forward(multiple_a * side)

    backward(multiple_a * side / 2)
    right(90)

    penup()


def clock(epoch_time, side):
    penup()
    left(90)
    seconds = epoch_time % 60
    seconds_angle = 360 * (seconds / 60.0)
    minutes = epoch_time // 60 % (60)
    minutes_angle = 360 * (minutes / 60.0) + seconds_angle / 60.0
    hours = epoch_time // 3600 % (12)
    hours_angle = 360 * (hours / 12.0) + minutes_angle / 12.0

    polygon(side)

    right(seconds_angle)
    draw_rectangle(0, 1.8, side)
    right(360 - seconds_angle + minutes_angle)
    draw_rectangle(0.05, 1.6, side)
    right(360 - minutes_angle + hours_angle)
    draw_rectangle(0.1, 1.4, side)
    left(hours_angle)


def main():
    clock(1661081862, 150.0)
    done()


if __name__ == '__main__':
    main()
