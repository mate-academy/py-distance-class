def decor_funk(func: any) -> any:
    def wraper(self: any, other: any) -> any:
        if isinstance(other, Distance):
            return func(self.km, other.km)
        if isinstance(other, (int, float)):
            return func(self.km, other)

    return wraper


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    @decor_funk
    def __add__(self, other: any) -> object:
        return Distance(self + other)

    def __iadd__(self, other: any) -> object:
        if isinstance(other, Distance):
            self.km = self.km + other.km
        if isinstance(other, (int, float)):
            self.km = self.km + other
        return self

    def __mul__(self, other: any) -> object:
        return Distance(self.km * other)

    def __truediv__(self, other: any) -> object:
        return Distance(round((self.km / other), 2))

    @decor_funk
    def __lt__(self, other: any) -> bool:
        return self < other

    @decor_funk
    def __gt__(self, other: any) -> bool:
        return self > other

    @decor_funk
    def __eq__(self, other: any) -> bool:
        return self == other

    @decor_funk
    def __le__(self, other: any) -> bool:
        return self <= other

    @decor_funk
    def __ge__(self, other: any) -> bool:
        return self >= other

    def __len__(self) -> float:
        return self.km
