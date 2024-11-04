from ib111 import week_09  # noqa

# V tomto příkladu budeme pracovat se stromy, které reprezentují
# aritmetické výrazy. Tyto mají následující strukturu:
#
#  • konstantu reprezentuje strom, který má oba podstromy prázdné,
#  • složený výraz je reprezentován stromem, který má v kořenu
#    uložen operátor (‹+› nebo ‹*›) a jeho neprázdné podstromy
#    reprezentují operandy.
#
# Žádné jiné uzly ve stromě přítomny nebudou.


class Tree:
    def __init__(self, value: str | int,
                 left: 'Tree | None',
                 right: 'Tree | None'):
        self.value = value
        self.left = left
        self.right = right


def leaf(value: int) -> Tree:
    return Tree(value, None, None)


# Napište čistou funkci, která na vstupu dostane instanci výše
# popsaného stromu a vrátí výsledek vyhodnocení výrazu, který
# tento strom reprezentuje.


def evaluate(tree: Tree) -> int:
    assert tree is not None
    if isinstance(tree.value, str):
        assert tree.left is not None and tree.right is not None
        op = tree.value
        assert op is not None
        if op == "+":
            return evaluate(tree.left) + evaluate(tree.right)
        return evaluate(tree.left) * evaluate(tree.right)

    return tree.value if isinstance(tree.value, int) else 0


def main() -> None:
    t1 = leaf(5)
    t2 = Tree("+", leaf(2), leaf(4))
    t3 = Tree("*", t1, t2)
    t4 = Tree("*", leaf(0), t3)

    assert evaluate(t1) == 5
    assert evaluate(t2) == 6
    assert evaluate(t3) == 30
    assert evaluate(t4) == 0


if __name__ == '__main__':
    main()
