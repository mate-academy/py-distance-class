class Distance:
    def __init__(self, km):
        self.km = km

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Distance(
                km=float(self.km) + other
            )
        else:
            return Distance(
                km=self.km + other.km
            )

    def __iadd__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            self.km = float(self.km) + other
        else:
            self.km += other.km
        return self

    def __mul__(self, multiplier):
        self.km = self.km * multiplier
        return self

    def __truediv__(self, divider):
        self.km = round(self.km / divider, 2)
        return self

    def __lt__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return float(self.km) < other
        return self.km < other.km

    def __gt__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return float(self.km) > other
        return self.km > other.km

    def __eq__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return float(self.km) == other
        return self.km == other.km

    def __le__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return float(self.km) <= other
        return self.km <= other.km

    def __ge__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return float(self.km) >= other
        return self.km >= other.km

    def __len__(self):
        return len(self)
