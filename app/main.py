class Distance:

    def __init__(self, km):
        self.km = km

    def __add__(self, other):
        if isinstance(other, Distance):
            raise TypeError(f"{other} should not be an instance of {Distance}")
        else:
            return Distance(self.km + other)

    def __iadd__(self, other):
        if isinstance(other, Distance):
            raise TypeError(f"{other} should not be an instance of {Distance}")
        else:
            self.km = self.km + other
            return Distance(self.km)

    def __mul__(self, other):
        if isinstance(other, Distance):
            raise TypeError(f"{other} should not be an instance of {Distance}")
        else:
            return Distance(self.km * other)

    def __truediv__(self, other):
        if isinstance(other, Distance):
            raise TypeError(f"{other} should not be an instance of {Distance}")
        else:
            return Distance(self.km / other)

    def __lt__(self, other):
        if isinstance(other, Distance):
            raise TypeError(f"{other} should not be an instance of {Distance}")
        else:
            return self.km < other

    def __gt__(self, other):
        if isinstance(other, Distance):
            raise TypeError(f"{other} should not be an instance of {Distance}")
        else:
            return self.km > other

    def __eq__(self, other):
        if isinstance(other, Distance):
            raise TypeError(f"{other} should not be an instance of {Distance}")
        else:
            return self.km == other

    def __le__(self, other):
        if isinstance(other, Distance):
            raise TypeError(f"{other} should not be an instance of {Distance}")
        else:
            return self.km <= other

    def __ge__(self, other):
        if isinstance(other, Distance):
            raise TypeError(f"{other} should not be an instance of {Distance}")
        else:
            return self.km >= other

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"{self.__class__.__name__}(km={self.km})"