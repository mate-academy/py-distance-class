class Distance:
    # Write your code here
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: [int, float]) -> list:
        sc = other
        if isinstance(other, Distance):
            sc = other.km
        return Distance(self.km + sc)

    def __iadd__(self, other: [int, float]) -> "Distance":
        sc = other
        if isinstance(other, Distance):
            sc = other.km
        self.km += sc
        return self

    def __mul__(self, other: [int, float]) -> "Distance":
        sc = other
        if isinstance(other, int) and other >= 0:
            sc = other
        return Distance(self.km * sc)

    def __truediv__(self, other: [int, float]) -> "Distance":
        sc = other
        if isinstance(other, int) or isinstance(other, float):
            sc = other
        if sc != 0:
            return Distance(round(self.km / sc, 2))
        else:
            raise ValueError("Division by zero is not allowed.")

    @classmethod
    def __verify(cls, other: ["Distance", int, float]) -> int:
        return other if isinstance(other, int) \
                        or isinstance(other, float) else other.km

    def __eq__(self, other: ["Distance", int, float]) -> bool:
        sc = self.__verify(other)
        return self.km == sc

    def __lt__(self, other: ["Distance", int, float]) -> bool:
        sc = self.__verify(other)
        return self.km < sc

    def __gt__(self, other: ["Distance", int, float]) -> bool:
        sc = self.__verify(other)
        return self.km > sc

    def __le__(self, other: ["Distance", int, float]) -> bool:
        sc = self.__verify(other)
        return self.km <= sc

    def __ge__(self, other: ["Distance", int, float]) -> bool:
        sc = self.__verify(other)
        return self.km >= sc
