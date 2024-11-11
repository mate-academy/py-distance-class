class Distance:

    def __init__(self, km: (float, int)) -> None:
        self.km = km

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __add__(self, other: (object, float, int)) -> object:
        if isinstance(other, (float, int)):
            create_object_from_int = Distance(other)
            return Distance(self.km + create_object_from_int.km)

        return Distance(self.km + other.km)

    def __iadd__(self, other: (object, float, int)) -> object:
        if isinstance(other, (float, int)):
            create_object_from_int = Distance(other)
            self.km = self.__add__(create_object_from_int)
            return self

        self.km = self.__add__(other)
        return self

    def __mul__(self, other: (object, float, int)) -> object:
        if isinstance(other, (float, int)):
            create_object_from_int = Distance(other)
            return Distance(self.km * create_object_from_int.km)

        return Distance(self.km * other)

    def __truediv__(self, other: (object, float, int)) -> object:

        return Distance(round(self.km / other, 2))

    def __lt__(self, other: (object, float, int)) -> bool:
        if isinstance(other, (float, int)):
            create_object_from_int = Distance(other)
            return self.km < create_object_from_int.km

        return self.km < other.km

    def __gt__(self, other: (object, float, int)) -> bool:
        if isinstance(other, (float, int)):
            create_object_from_int = Distance(other)
            return self.km > create_object_from_int.km

        return self.km > other.km

    def __eq__(self, other: (object, float, int)) -> bool:
        if isinstance(other, (float, int)):
            create_object_from_int = Distance(other)
            return self.km == create_object_from_int.km

        return self.km == other.km

    def __le__(self, other: (object, float, int)) -> bool:
        if isinstance(other, (float, int)):
            create_object_from_int = Distance(other)
            return self.km <= create_object_from_int.km

        return self.km <= other.km

    def __ge__(self, other: (object, float, int)) -> bool:
        if isinstance(other, (float, int)):
            create_object_from_int = Distance(other)
            return self.km >= create_object_from_int.km

        return self.km >= other.km


distance1 = Distance(12)
print(distance1.__le__(False))
