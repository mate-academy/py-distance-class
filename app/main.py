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

    def __mul__(self, other):
        if isinstance(other,Distance):
            return self.km * other

        return Distance(self.km * other)



    def __truediv__(self, other):
        if isinstance(other, Distance):
            return self.km * other


        return Distance(round(self.km / other, 2))




    def __lt__(self, other):
        if self.km < (other.km if isinstance(other, Distance) else other):
            return True
        else:
            return False

    def __gt__(self, other):
        return self.km > (other.km if isinstance(other, Distance) else other)

    def __eq__(self, other):
        return self.km == (other.km if isinstance(other, Distance) else other)

    def __le__(self, other):
        return self.km <= (other.km if isinstance(other, Distance) else other)

    def __ge__(self, other):
        return self.km >= (other.km if isinstance(other, Distance) else other)

