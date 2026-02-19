class Distance:
    def __init__(self, km : int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        return Distance(self.km + other)

    def __iadd__(self, other: Distance | int) -> Distance:
        if not isinstance(other, Distance):
            self.km += other
        else:
            self.km += other.km
        return self

    def __mul__(self, number : int) -> Distance:
        self.km *= number
        return self

    def __truediv__(self, number: int) -> Distance:
        self.km = round((self.km / number), 2)
        return self

    def __lt__(self, number : int) -> bool:
        return self.km < number

    def __gt__(self, number : int) -> bool:
        return self.km > number

    def __eq__(self, number : int) -> bool:
        return self.km == number

    def __le__(self, number : int) -> bool:
        return self.km <= number

    def __ge__(self, number : int) -> bool:
        return self.km >= number
