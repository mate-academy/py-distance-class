class Distance:

    def __init__(self, km):
        self.km = km

    def __str__(self):
        return f"Distance: {self.km} kilometers"

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return Distance(
                km=self.km + other
            )
        else:
            return Distance(
                km=self.km + other.km
            )

    def __iadd__(self, other):
        if isinstance(other, (int, float)):
            self.km += other
        else:
            self.km += other.km
        return self

    def __mul__(self, multiplicator):
        return Distance(
            km=self.km * multiplicator
        )

    def __truediv__(self, divider):
        result_km = round(self.km / divider, 2)
        return Distance(
            km=result_km
        )

    def __lt__(self, other):
        if isinstance(other, Distance):
            return self.km < other.km
        return self.km < other

    def __gt__(self, other):
        if isinstance(other, Distance):
            return self.km > other.km
        return self.km > other

    def __eq__(self, other):
        if isinstance(other, Distance):
            return self.km == other.km
        return self.km == other

    def __le__(self, other):
        return not self > other

    def __ge__(self, other):
        return not self < other

    def __len__(self):
        return self.km
