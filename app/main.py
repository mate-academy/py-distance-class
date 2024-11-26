class Distance:
    # Write your code here
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: int) -> object:
        if type(other) is int or type(other) is float:
            return Distance(self.km + other)
        else:
            return Distance(self.km + other.km)

    def __iadd__(self, other: int) -> object:
        if type(other) is int or type(other) is float:
            self.km = self.km + other
            return self
        else:
            self.km = self.km + other.km
            return self

    def __mul__(self, other: int) -> object:
        if type(other) is int or type(other) is float:
            return Distance(self.km * other)
        else:
            raise TypeError(
                f"Unsuporteed type of other {type(other)}. "
                f"Int or float expected")
    def __truediv__(self, other: int) -> object:
        if type(other) is int or type(other) is float:
            return Distance(round((self.km / other), 2))
        else:
            raise TypeError(
                f"Unsuporteed type of other {type(other)}. "
                f"Int or float expected")

    def __lt__(self, other: object) -> bool:
        if type(other) is int or type(other) is float:
            return self.km < other
        else:
            return self.km < other.km

    def __gt__(self, other: object) -> bool:
        if type(other) is int or type(other) is float:
            return self.km > other
        else:
            return self.km > other.km

    def __eq__(self, other: object) -> bool:
        if type(other) is int or type(other) is float:
            return self.km == other
        else:
            return self.km == other.km

    def __le__(self, other: object) -> bool:
        if type(other) is int or type(other) is float:
            return (self.km < other) or (self.km == other)
        else:
            return (self.km < other.km) or (self.km == other.km)

    def __ge__(self, other: object) -> bool:
        if type(other) is int or type(other) is float:
            return (self.km > other) or (self.km == other)
        else:
            return (self.km > other.km) or (self.km == other.km)
