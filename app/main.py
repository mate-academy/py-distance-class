class Distance:
    # Write your code here
    def __init__(self, km: int):
        self.km = km

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, other):
        if isinstance(other, Distance):
            return Distance(
                km=self.km + other.km
            )
        else:
            return Distance(
                km=self.km + other
            )

    def __iadd__(self, other):
        if isinstance(other, Distance):
            self.km += other.km
            return self
        else:
            self.km += other
            return self

    def __mul__(self, other):
        return Distance(
            km=self.km * other
        )

    def __truediv__(self, other):
        return Distance(
            km=round(self.km / other, 2)
        )