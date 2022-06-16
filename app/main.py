class Distance:
    def __init__(self, distance):
        self.km = distance

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, other):
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        if isinstance(other, int):
            return Distance(self.km + other)

    def __iadd__(self, other):
        if isinstance(other, Distance):
            val2 = other.km
        else:
            val2 = other
        self.km += val2
        return self

    def __mul__(self, other):
        return Distance(self.km * other)

    def __truediv__(self, other):
        return Distance(round((self.km / other), 2))

    def __lt__(self, other):
        val1 = self.km
        if isinstance(other, Distance):
            val2 = other.km
        else:
            val2 = other
        if val1 < val2:
            return True
        else:
            return False

    def __gt__(self, other):
        val1 = self.km
        if isinstance(other, Distance):
            val2 = other.km
        else:
            val2 = other
        if val1 > val2:
            return True
        else:
            return False

    def __eq__(self, other):
        val1 = self.km
        if isinstance(other, Distance):
            val2 = other.km
        else:
            val2 = other
        if val1 == val2:
            return True
        else:
            return False

    def __le__(self, other):
        val1 = self.km
        if isinstance(other, Distance):
            val2 = other.km
        else:
            val2 = other
        if val1 <= val2:
            return True
        else:
            return False

    def __ge__(self, other):
        val1 = self.km
        if isinstance(other, Distance):
            val2 = other.km
        else:
            val2 = other
        if val1 >= val2:
            return True
        else:
            return False

    def __len__(self):
        return self.km
