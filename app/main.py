class Distance:

    def __init__(self, km: (int, float)) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: (int, float)) -> object:
        number = other if isinstance(other, (int, float)) else other.km

        return Distance(self.km + number)

    def __iadd__(self, other: (int, float)) -> object:
        number = other if isinstance(other, (int, float)) else other.km
        self.km += number

        return self

    def __mul__(self, other: (int, float)) -> object:
        number = other if isinstance(other, (int, float)) else other.km

        return Distance(self.km * number)

    def __truediv__(self, other: (int, float)) -> object:
        number = other if isinstance(other, (int, float)) else other.km

        return Distance(round(self.km / number, 2))

    def __lt__(self, other: (int, float)) -> bool:
        number = other if isinstance(other, (int, float)) else other.km

        return self.km < number

    def __gt__(self, other: (int, float)) -> bool:
        number = other if isinstance(other, (int, float)) else other.km

        return self.km > number

    def __eq__(self, other: (int, float)) -> bool:
        number = other if isinstance(other, (int, float)) else other.km

        return self.km == number

    def __le__(self, other: (int, float)) -> bool:
        number = other if isinstance(other, (int, float)) else other.km

        return self.km <= number

    def __ge__(self, other: (int, float)) -> bool:
        number = other if isinstance(other, (int, float)) else other.km

        return self.km >= number

    def __len__(self) -> (int, float):
        return self.km
