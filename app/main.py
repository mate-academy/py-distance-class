class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, float) or isinstance(other, int):
            result = self.km + other
            return Distance(km=result)
        elif isinstance(other, Distance):
            result = self.km + other.km
            return Distance(km=result)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, float) or isinstance(other, int):
            self.km += other
            return self
        if isinstance(other, Distance):
            self.km += other.km
            return self
        if not other:
            return self

    def __mul__(self, other: int | float) -> Distance:
        result = self.km * other
        return Distance(km=result)

    def __truediv__(self, other: int | float) -> Distance:
        result = round(self.km / other, 2)
        return Distance(
            km=result
        )

    def __lt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, float) or isinstance(other, int):
            return self.km < other
        elif isinstance(other, Distance):
            result = self.km < other.km
            return result

    def __gt__(self, other: Distance | int | float) -> bool:
        trig = False
        if isinstance(other, float) or isinstance(other, int):
            trig = self.km > other
        if isinstance(other, Distance):
            trig = self.km > other.km
        return trig

    def __eq__(self, other: Distance | int | float) -> bool:
        trig = False
        if isinstance(other, float) or isinstance(other, int):
            trig = self.km == other
        elif isinstance(other, Distance):
            trig = self.km == other.km
        return trig

    def __le__(self, other: Distance | int | float) -> bool:
        result = True
        if isinstance(other, float) or isinstance(other, int):
            temp = Distance(km=other)
            result = self.km <= temp.km
        elif isinstance(other, Distance):
            result = self.km <= other.km
        return result

    def __ge__(self, other: Distance | int | float) -> bool:
        trig = False
        if isinstance(other, float) or isinstance(other, int):
            trig = self.km >= other
        elif isinstance(other, Distance):
            trig = self.km >= other.km
        return trig
