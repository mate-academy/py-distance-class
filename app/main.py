class Distance:

    def __init__(self, km):
        self.km = km

    def __add__(self, other):
        if isinstance(other, Distance):
            return  self.km + other.km
        else:
            raise TypeError(f"{other} is not an instance of {Distance}")

    def __iadd__(self, other):
        if isinstance(other, Distance):
            self.km = self.km + other.km
            return self.km
        else:
            raise TypeError(f"{other} is not an instance of {Distance}")

    def __mul__(self, other):
        if isinstance(other, Distance):S
            return self.km * other.km
        else:
            raise TypeError(f"{other} is not an instance of {Distance}")

    def __truediv__(self, other):
        if isinstance(other, Distance):
            return self.km / other.km
        else:
            raise TypeError(f"{other} is not an instance of {Distance}")

    def __lt__(self, other):
        if isinstance(other, Distance):
            return self.km < other.km
        else:
            raise TypeError(f"{other} is not an instance of {Distance}")

    def __gt__(self, other):
        if isinstance(other, Distance):
            return self.km > other.km
        else:
            raise TypeError(f"{other} is not an instance of {Distance}")

    def __eq__(self, other):
        if isinstance(other, Distance):
            return self.km == other.km
        else:
            raise TypeError(f"{other} is not an instance of {Distance}")

    def __le__(self, other):
        if isinstance(other, Distance):
            return self.km <= other.km
        else:
            raise TypeError(f"{other} is not an instance of {Distance}")

    def __ge__(self, other):
        if isinstance(other, Distance):
            return self.km >= other.km
        else:
            raise TypeError(f"{other} is not an instance of {Distance}")

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"{self.__class__.__name__}(km={self.km})"