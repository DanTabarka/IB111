from ib111 import week_09  # noqa


# Pro účely tohoto cvičení musíme trochu pozměnit zápis stromu do
# tříd. Protože budeme strom měnit „na místě“, musí být prázdný i
# neprázdný strom reprezentován stejným typem. Proto si jej
# rozdělíme na třídy ‹Node› a ‹Tree›, které budou hrát podobnou roli
# jako jejich protějšky v zřetězeném seznamu. Tyto třídy nijak
# nemodifikujte.

class Node:
    def __init__(self, value: int,
                 left: 'Node | None',
                 right: 'Node | None'):
        self.value = value
        self.left = left
        self.right = right


def leaf(value: int) -> Node:
    return Node(value, None, None)


class Tree:
    def __init__(self, root: Node | None):
        self.root = root


# Napište proceduru, která na vstupu dostane instanci výše popsaného
# stromu ‹tree› a množinu celých čísel ‹keep› a ze stromu ‹tree›
# odstraní všechny vrcholy (uzly), kterých hodnota v množině ‹keep›
# chybí. Spolu s vrcholem odstraňte i celý podstrom, který v něm
# začíná. Správné řešení má složitost lineární vůči počtu uzlů
# původního stromu.

def prune(tree: Tree, keep: set[int]) -> None:
    if tree is None or tree.root is None:
        return
    
    head = tree.root

    if head.value not in keep:
        tree.root = None

    recursive(head, keep)


def recursive(node: Node | None, keep: set[int]) -> None:
    if node is None:
        return
    if node.left is not None and node.left.value not in keep:
        node.left = None
    if node.right is not None and node.right.value not in keep:
        node.right = None

    recursive(node.left, keep)
    recursive(node.right, keep)


def main() -> None:
    t1 = Tree(leaf(5))
    prune(t1, {5})
    assert t1.root is not None
    assert t1.root.left is None
    assert t1.root.right is None

    keep = {1, 2, 3, 4}
    prune(t1, keep)
    assert t1.root is None
    assert keep == {1, 2, 3, 4}

    t2 = Tree(leaf(5))
    t2.root.left = leaf(6)
    t2.root.right = leaf(7)
    prune(t2, {5, 6})
    assert t2.root is not None
    assert t2.root.left is not None
    assert t2.root.right is None
    assert t2.root.left.left is None
    assert t2.root.left.right is None

    prune(t2, set())
    assert t2.root is None

    t3 = Tree(leaf(5))
    t3.root.left = leaf(5)
    t3.root.right = leaf(6)
    t3.root.right.left = leaf(5)
    prune(t3, {5})
    assert t3.root is not None
    assert t3.root.left is not None
    assert t3.root.right is None


if __name__ == '__main__':
    main()
