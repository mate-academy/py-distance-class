class Distance:
    # Write your code here
    def __init__(self, km):
        self.km = km

    def __str__(self):
        print(f"Distance: {self.km} kilometers.")

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, second):
        if isinstance(second, Distance):
            return Distance(self.km + second.km)
        elif isinstance(second, int):
            return Distance(self.km + second)

    def __iadd__(self, second):
        if isinstance(second, Distance):
            self.km += second.km
            return self
        if isinstance(second, int):
            self.km += second
            return self

    def __mul__(self, other):

        if isinstance(other, int):
            return Distance(self.km * other)
        else:
            return Distance(self.km * other.km)

    def __truediv__(self, other):
        if isinstance(other, int):
            return Distance(round(self.km / other, 2))
        else:
            return Distance(round(self.km / other.km, 2))

    def __eq__(self, other):
        return self.km == other

    def __gt__(self, other):
        return self.km > other

    def __lt__(self, other):
        return self.km < other

    def __ge__(self, other):
        return self.km >= other

    def __le__(self, other):
        return self.km <= other

    def __len__(self):
        return self.km
