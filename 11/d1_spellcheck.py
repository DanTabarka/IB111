from ib111 import week_11  # noqa

# V této ukázce načteme seznam slov uložených v komprimovaném
# souboru (ve formátu ‹gzip›) a použijeme jej k implementaci (velmi
# zjednodušené) kontroly pravopisu. K načtení souboru použijeme
# standardní modul ‹gzip›.

import gzip


# Načtení slovníku realizujeme jednoduchým podprogramem
# ‹read_dictionary›, který soubor dekomprimuje a slova uloží do
# množiny (množina proto, abychom dokázali slova rychle vyhledávat).
# Výstup dekompresního algoritmu budeme «číst» (písmenko ‹r›
# v parametru ‹mode›) v «textovém režimu» (písmenko ‹t›).
# Dekomprimovaná data pak již čteme stejně jako libovolný jiný
# soubor, třeba iterací, která postupně vrací jednotlivé řádky.
# Protože slova jsou v souboru uložena ve formátu 1 řádek = 1 slovo,
# bude nám právě tento režim vyhovovat. K odstranění znaků konce
# řádku použijeme metodu ‹strip›.

def read_dictionary(path: str) -> set[str]:
    out: set[str] = set()
    with gzip.open(path, 'rt') as data:
        for word in data:
            out.add(word.strip())
    return out


# Samotnou kontrolu provede čistá funkce ‹spellcheck›. Vstupem je
# množina přípustných slov (obsah seznamu slov načteného výše) a
# text, který chceme zkontrolovat. Výstupem je pak krom samotných
# neznámých slov také seznam čísel řádků, na kterých se ve vstupu
# objevují. K reprezentaci použijeme slovník, kde klíčem je špatně
# napsané slovo a hodnotou zmiňovaný seznam.

# Abychom se alespoň trochu přiblížili realitě, budeme se chtít
# vypořádat s některými problémy:
#
#  • slova nejsou vždy oddělena mezerami: často se objevují čárky,
#    tečky, uvozovky, závorky a podobně,
#  • na velikosti písmen občas záleží, ale ne vždy:
#    ◦ slovo, které ve slovníku obsahuje velká písmena, je,
#      napíšeme-li jej malými písmeny, typicky chybou (třeba
#      „Jean-Pierre“)
#    ◦ naopak, slovo, které je ve slovníku malými písmeny, může
#      v textu stát na začátku věty, nebo obsahovat velká písmena
#      z jiného důvodu, a typicky to chyba není.
#
# Skutečné programy pro kontrolu pravopisu jsou obvykle mnohem
# složitější, nám ale bude tato úroveň realizmu stačit. Metody,
# které neznáte, si dohledejte v dokumentaci: i to je důležitá
# součást programování.

def spellcheck(dictionary: set[str], text: str) -> dict[str, list[int]]:
    problems: dict[str, list[int]] = {}
    to_erase = {',', '.', '!', '?', '(', ')', '"'}
    for lineno, line in enumerate(text.split('\n')):
        processed = ''
        for char in line:
            processed += ' ' if char in to_erase else char
        for word in processed.split():
            if word not in dictionary and \
               word.lower() not in dictionary:
                if word not in problems:
                    problems[word] = []
                problems[word].append(lineno + 1)
    return problems


# Celý program otestujeme na několika jednoduchých vstupech. Slovník
# naleznete v souboru ‹zz.words.gz› (na stroji ‹aisa› si jej můžete
# prohlédnout třeba příkazem ‹zless›).

def main() -> None:  # demo
    dictionary = read_dictionary('zz.words.gz')
    assert len(spellcheck(dictionary, 'hello world')) == 0
    assert len(spellcheck(dictionary, 'hello, world!')) == 0
    assert len(spellcheck(dictionary, 'hello, borld!')) == 1
    bad = spellcheck(dictionary, 'Hello, borld!\nErr, I mean'
                     '"world". Truely.')
    assert bad == {'borld': [1], 'Truely': [2]}, str(bad)


if __name__ == '__main__':
    main()
