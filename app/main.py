class Distance:
    def __init__(self, km: float) -> None:
        self.km = km


    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other):
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Distance):
            self.km += other.km
            return self
        elif isinstance(other, (int, float)):
            self.km += other
            return self
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            unrounded = self.km / other
            rounded = round(unrounded, 2)
            return Distance(rounded)
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, (Distance, int, float)):
            return self.km < (other.km if isinstance(other, Distance)
                              else other)

    def __gt__(self, other):
        if isinstance(other, (Distance, int, float)):
            return self.km > (other.km if isinstance(other, Distance)
                              else other)

    def __eq__(self, other):
        if isinstance(other, (Distance, int, float)):
            return self.km == (other.km if isinstance(other, Distance)
                               else other)

    def __le__(self, other):
        if isinstance(other, (Distance, int, float)):
            return self.km <= (other.km if isinstance(other, Distance)
                               else other)

    def __ge__(self, other):
        if isinstance(other, (Distance, int, float)):
            return self.km >= (other.km if isinstance(other, Distance)
                               else other)
