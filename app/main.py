class Distance:
    # Write your code here
    def __init__(self, km: float):
        self.km = km

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, other):
        if not isinstance(other, Distance):
            if type(other) is int or type(other) is float:
                return Distance(km=self.km + other)
            raise TypeError(f"unsupported operand type(s) for + :"
                            f"'Distance' and {type(other)}")
        return Distance(km=self.km + other.km)

    def __iadd__(self, other):
        if type(other) is Distance:
            self.km += other.km
            return self
        elif type(other) is int or type(other) is float:
            self.km += other
            return self
        else:
            raise TypeError(f"{type(other)} is error type."
                            f" Need type Distance, int or float.")

    def __mul__(self, other):
        if type(other) is int or type(other) is float:
            return Distance(self.km * other)
        else:
            raise TypeError(f"{type(other)} is error type."
                            f" Need type int or float.")

    def __truediv__(self, other):
        if type(other) is int or type(other) is float:
            return Distance(km=round(self.km / other, 2))
        else:
            raise TypeError(f"{type(other)} is error type."
                            f" Need type int or float.")

    def __lt__(self, other):
        return self.km < other

    def __gt__(self, other):
        return self.km > other

    def __eq__(self, other):
        return self.km == other

    def __le__(self, other):
        return self.km <= other

    def __ge__(self, other):
        return self.km >= other

    def __len__(self):
        return self.km
