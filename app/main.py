class Distance:
    def __init__(self, km: int):
        self.km = km

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, other: int):
        if isinstance(other, Distance):
            other = other.km
        return Distance(self.km + other)

    def __iadd__(self, other: int):
        if isinstance(other, Distance):
            other = other.km
        self.km += other
        return self

    def __mul__(self, other: int):
        if isinstance(other, Distance):
            other = other.km
        return Distance(self.km * other)

    def __truediv__(self, other):
        if isinstance(other, Distance):
            other = other.km
        return Distance(round(self.km / other, 2))

    def __lt__(self, other):
        temp_var = other if isinstance(other, (int, float)) else other.km
        return self.km < temp_var

    def __gt__(self, other):
        temp_var = other if isinstance(other, (int, float)) else other.km
        return self.km > temp_var

    def __eq__(self, other):
        temp_var = other if isinstance(other, (int, float)) else other.km
        return self.km == temp_var

    def __le__(self, other):
        temp_var = other if isinstance(other, (int, float)) else other.km
        return self.km <= temp_var

    def __ge__(self, other):
        temp_var = other if isinstance(other, (int, float)) else other.km
        return self.km >= temp_var

    def __len__(self, other):
        return len(self)
