from ib111 import week_12  # noqa


class Tree:
    def __init__(self, value: int, left: 'Tree | None',
                 right: 'Tree | None') -> None:
        self.value = value
        self.left = left
        self.right = right


def leaf(value: int) -> Tree:
    return Tree(value, None, None)


# Napište čistou funkci ‹get_bounds›, která nalezne minimální a
# maximální hodnotu v zadaném neprázdném stromě.

def get_bounds(tree: Tree) -> tuple[int, int]:
    pass


def main() -> None:
    assert get_bounds(leaf(1)) == (1, 1)
    assert get_bounds(Tree(1, leaf(2), leaf(3))) == (1, 3)
    assert get_bounds(Tree(-1, leaf(2), leaf(-3))) == (-3, 2)
    assert get_bounds(
        Tree(0, Tree(-1, Tree(-19, leaf(0), None), leaf(5)),
             Tree(4, Tree(8, None, leaf(3)),
                  Tree(26, Tree(-3, leaf(19), leaf(5)),
                       leaf(2))))) == (-19, 26)
    assert get_bounds(
        Tree(-50, Tree(-1, Tree(-19, leaf(0), None), leaf(5)),
             Tree(4, Tree(8, None, leaf(3)),
                  Tree(26, Tree(-3, leaf(19), leaf(5)),
                       leaf(2))))) == (-50, 26)
    assert get_bounds(
        Tree(100, Tree(-1, Tree(-19, leaf(0), None), leaf(5)),
             Tree(4, Tree(8, None, leaf(3)),
                  Tree(26, Tree(-3, leaf(19), leaf(5)),
                       leaf(2))))) == (-19, 100)
    assert get_bounds(
        Tree(0, Tree(-1, Tree(-19, leaf(0), None), leaf(5)),
             Tree(4, Tree(80, None, leaf(3)),
                  Tree(26, Tree(-3, leaf(19), leaf(5)),
                       leaf(-22))))) == (-22, 80)
    assert get_bounds(
        Tree(-1, Tree(-1, Tree(-19, leaf(-3), None), leaf(-5)),
             Tree(-4, Tree(-8, None, leaf(-3)),
                  Tree(-26, Tree(-3, leaf(-19), leaf(-5)),
                       leaf(-2))))) == (-26, -1)


if __name__ == '__main__':
    main()
