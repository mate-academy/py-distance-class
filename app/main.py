class Distance:
    # Write your code here
    def __init__(self, km: (int, float)):
        self.km = km

    def __add__(self, other):
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __mul__(self, other):
        if isinstance(other, Distance):
            return Distance(self.km * other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km * other)

    def __iadd__(self, other):
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        return self

    def __truediv__(self, other):
        if isinstance(other, Distance):
            return Distance(round(self.km / other.km, 2))
        elif isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))

    def __eq__(self, other):
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other

    def __gt__(self, other):
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other

    def __lt__(self, other):
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other

    def __ge__(self, other):
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= other

    def __le__(self, other):
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other

    def __len__(self):
        return self.km
