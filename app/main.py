class Distance:

    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, distance2: "Distance | int | float") -> "Distance":
        if isinstance(distance2, Distance):
            return Distance(self.km + distance2.km)
        elif isinstance(distance2, (int, float)):
            return Distance(self.km + distance2)

    def __iadd__(self, distance2: "Distance | int | float") -> "Distance":
        if isinstance(distance2, Distance):
            self.km += distance2.km
        elif isinstance(distance2, (int, float)):
            self.km += distance2
        return self

    def __mul__(self, multp: int | float) -> "Distance":
        if isinstance(multp, (int, float)):
            return Distance(self.km * multp)
        return NotImplemented

    def __truediv__(self, diver: "Distance | int | float") -> "Distance":
        if isinstance(diver, int | float) and diver != 0:
            return Distance(round(self.km / diver, 2))
        return NotImplemented

    def __lt__(self, distance2: "Distance | int | float") -> bool:
        if isinstance(distance2, Distance):
            return self.km < distance2.km
        elif isinstance(distance2, (int, float)):
            return self.km < distance2

    def __gt__(self, distance2: "Distance | int | float") -> bool:
        if isinstance(distance2, Distance):
            return self.km > distance2.km
        elif isinstance(distance2, (int, float)):
            return self.km > distance2

    def __eq__(self, distance2: "Distance | int | float") -> bool:
        if isinstance(distance2, Distance):
            return self.km == distance2.km
        elif isinstance(distance2, (int, float)):
            return self.km == distance2

    def __le__(self, distance2: "Distance | int | float") -> bool:
        if isinstance(distance2, Distance):
            return self.km <= distance2.km
        elif isinstance(distance2, (int, float)):
            return self.km <= distance2

    def __ge__(self, distance2: "Distance | int | float") -> bool:
        if isinstance(distance2, Distance):
            return self.km >= distance2.km
        elif isinstance(distance2, (int, float)):
            return self.km >= distance2
