from ib111 import week_07  # noqa


# Naprogramujte třídu ‹RingBuffer› která se bude chovat jako fronta,
# ale bude mít shora omezenou velikost. Pro ukládání dat bude
# využívat jinou třídu, ‹SimpleList› (tuto třídu nesmíte měnit, ani
# přistupovat k jejím atributům), která poskytuje toto rozhraní
# (‹sl› je instance ‹SimpleList›):
#
#  • ‹sl.append(x)› vloží na konec seznamu prvek ‹x›,
#  • ‹sl.get(i)› vrátí hodnotu na indexu ‹i›,
#  • ‹sl.size()› vrátí aktuální velikost seznamu,
#  • ‹sl.set(i, x)› nastaví index ‹i› na hodnotu ‹x›.
#
# «Pozor:» V žádné metodě neprocházejte celý seznam.

class RingBuffer:

    # Při inicializaci se nastaví velikost kruhové fronty na ‹size›.
    # Pro ukládání dat bude použita instance třídy ‹SimpleList›
    # předaná parametrem ‹storage›.

    def __init__(self, size: int, storage: 'SimpleList') -> None:
        self.storage = storage
        self.size = size
        self.start = 0
        self.count = 0

    # Metoda ‹push› se pokusí přidat prvek na konec fronty. Je-li
    # fronta plná, metoda vrátí ‹False› a nic neudělá. V opačném
    # případě prvek vloží na konec fronty a vrátí ‹True›.

    def push(self, value: int) -> bool:
        if self.count >= self.size:
            return False

        if self.storage.size() < self.size:     # to full ring buffer
            self.storage.append(value)
        else:
            self.storage.set((self.start + self.count) % self.size, value)

        self.count += 1
        return True

    # Metoda ‹pop› odstraní prvek ze začátku fronty a vrátí jej.
    # Je-li fronta prázdná, metoda nic neudělá a vrátí ‹None›.

    def pop(self) -> int | None:
        if self.count == 0:
            return None

        self.count -= 1
        self.start += 1
        return self.storage.get((self.start - 1) % self.size)


def main() -> None:
    sl = SimpleList()
    buf = RingBuffer(4, sl)
    for num in [1, 2, 7, 4]:
        assert buf.push(num)
    assert not buf.push(5)

    check_result(buf.pop(), 1)
    check_result(buf.pop(), 2)
    assert buf.push(7)
    assert sl.size() <= 4
    check_result(buf.pop(), 7)
    check_result(buf.pop(), 4)
    check_result(buf.pop(), 7)
    assert buf.pop() is None
    for num in [11, 12, 13, 14]:
        buf.push(num)
    assert sl.size() <= 4
    assert not buf.push(0)
    check_result(buf.pop(), 11)
    assert sl.size() <= 4

    sl = SimpleList()
    buf = RingBuffer(3, sl)
    assert buf.pop() is None
    assert buf.push(0)
    check_result(buf.pop(), 0)
    assert buf.push(0)
    check_result(buf.pop(), 0)
    assert buf.pop() is None
    assert sl.size() <= 3

    sl = SimpleList()
    buf = RingBuffer(1, sl)
    assert buf.pop() is None
    assert buf.push(3)
    assert not buf.push(1)
    check_result(buf.pop(), 3)
    assert buf.push(3)


def check_result(result: int | None, expected: int) -> None:
    assert result is not None
    assert result == expected


class SimpleList:

    def __init__(self) -> None:
        self.__items: list[int] = []

    def append(self, x: int) -> None:
        self.__items.append(x)

    def get(self, i: int) -> int:
        return self.__items[i]

    def set(self, i: int, x: int) -> None:
        self.__items[i] = x

    def size(self) -> int:
        return len(self.__items)


if __name__ == "__main__":
    main()
