class Distance:
    def __init__(self, km):
        self.km = km

    def __str__(self):
        print(f"Distance: {self.km} kilometers.")

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, other):
        if isinstance(other, Distance):
            sum_km = self.km + other.km
            return Distance(sum_km)
        elif isinstance(other, (int, float)):
            sum_km = self.km + other
            return Distance(sum_km)

    def __iadd__(self, other):
        if isinstance(other, Distance):
            self.km += other.km
            return self
        elif isinstance(other, (int, float)):
            self.km += other
            return self

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            mul_km = self.km * other
            return Distance(mul_km)

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            div_km = round(self.km / other, 2)
            return Distance(div_km)

    def __lt__(self, other):
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other

    def __gt__(self, other):
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other

    def __eq__(self, other):
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other

    def __le__(self, other):
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other

    def __ge__(self, other):
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= other

    def __len__(self):
        return self.km
