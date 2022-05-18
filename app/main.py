class Distance:
    def __init__(self, km):
        self.km = km

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, other):
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        return Distance(self.km + other)

    def __iadd__(self, other):
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, num):
        self.km *= num
        return self

    def __truediv__(self, num):
        res = round(self.km / num, 2)
        self.km = res
        return self

    def __lt__(self, num):
        return self.km < num

    def __gt__(self, num):
        return self.km > num

    def __eq__(self, num):
        return self.km == num

    def __le__(self, num):
        return self.km <= num

    def __ge__(self, num):
        return self.km >= num

    def __len__(self):
        return self.km
