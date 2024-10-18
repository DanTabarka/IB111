from ib111 import week_07  # noqa


# Naprogramujte třídu ‹TimeInterval›, která bude reprezentovat
# časový interval.

class TimeInterval:
    def __init__(self, hours: int, minutes: int, seconds: int) -> None:
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    # Metoda zkrátí interval o čas reprezentovaný parametrem
    # ‹interval›.

    def shorten(self, interval: 'TimeInterval') -> None:
        all_seconds = self.seconds - interval.seconds   # -10
        self.seconds = all_seconds % 60                 # 50
        all_minutes = self.minutes - interval.minutes - (1 if all_seconds < 0 else 0)  
        self.minutes = all_minutes % 60
        all_hours = self.hours - interval.hours - (1 if all_minutes < 0 else 0)
        self.hours = all_hours

    # Metoda prodlouží interval o čas reprezentovaný parametrem
    # ‹interval›.

    def extend(self, interval: 'TimeInterval') -> None:
        all_seconds = self.seconds + interval.seconds
        self.seconds = all_seconds % 60
        all_minutes = self.minutes + interval.minutes + all_seconds // 60
        self.minutes = all_minutes % 60
        all_hours = self.hours + interval.hours + all_minutes // 60
        self.hours = all_hours

    # Metoda vrátí reprezentovaný interval jako n-tici ve formátu
    # (hodiny, minuty, sekundy), kde minuty a sekundy nabývají
    # hodnoty z uzavřeného intervalu [0, 59].

    def format(self) -> tuple[int, int, int]:
        return self.hours, self.minutes, self.seconds


def main() -> None:
    # for h, m, s in [(12, 3, 59), (14, 59, 59), (0, 0, 0),
    #                 (0, 0, 1), (0, 12, 12)]:
    #     assert TimeInterval(h, m, s).format() == (h, m, s)

    duration = TimeInterval(0, 0, 0)
    duration.extend(TimeInterval(0, 5, 30))
    assert duration.format() == (0, 5, 30)
    duration.extend(TimeInterval(0, 5, 30))
    assert duration.format() == (0, 11, 0)
    duration.extend(TimeInterval(0, 49, 0))
    assert duration.format() == (1, 0, 0)

    duration.shorten(TimeInterval(0, 32, 41))
    assert duration.format() == (0, 27, 19)
    duration.shorten(TimeInterval(123, 12, 43))
    assert duration.format() == (0, 0, 0)

    duration.extend(TimeInterval(1, 32, 56))
    duration.extend(duration)
    assert duration.format() == (3, 5, 52)
    duration.extend(duration)
    assert duration.format() == (6, 11, 44)
    duration.shorten(duration)
    assert duration.format() == (0, 0, 0)

    duration = TimeInterval(1, 0, 20)
    duration.shorten(TimeInterval(0, 0, 40))
    assert duration.format() == (0, 59, 40)


if __name__ == "__main__":
    main()
