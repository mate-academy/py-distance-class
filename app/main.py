class Distance:
    def __init__(self, km):
        self.km = km


        def __str__(self):
            return f"Distance: {self.km} kilometers"


        def __repr__(self):
            return f"Distance(km={self.km})"


        def __add__(self, other):
            if isinstance(other, Distance):
                return Distance(self.km + other.km)
            elif isinstance(other, (int, float)):
                return Distance(self.km + other)
            else:
                raise TypeError("Unsuported operand type for +")

        def __iadd__(self, other):
            if isinstance(other, Distance):
                self.km += other.km
            elif isinstance(other, (int, float)):
                self.km += other
            else:
                raise TypeError("Unsupported operand type for +=")
            return self

        # __mul__ method to multiply distance by a scalar
        def __mul__(self, other):
            if isinstance(other, (int, float)):
                return Distance(self.km * other)
            else:
                raise TypeError("Unsupported operand type for *")

        # __truediv__ method to divide distance by a scalar
        def __truediv__(self, other):
            if isinstance(other, (int, float)):
                return Distance(round(self.km / other, 2))  # rounded to 2 decimals
            else:
                raise TypeError("Unsupported operand type for /")

        # Comparison magic methods
        def __lt__(self, other):
            if isinstance(other, Distance):
                return self.km < other.km
            elif isinstance(other, (int, float)):
                return self.km < other
            else:
                raise TypeError("Unsupported operand type for <")

        def __gt__(self, other):
            if isinstance(other, Distance):
                return self.km > other.km
            elif isinstance(other, (int, float)):
                return self.km > other
            else:
                raise TypeError("Unsupported operand type for >")

        def __eq__(self, other):
            if isinstance(other, Distance):
                return self.km == other.km
            elif isinstance(other, (int, float)):
                return self.km == other
            else:
                raise TypeError("Unsupported operand type for ==")

        def __le__(self, other):
            if isinstance(other, Distance):
                return self.km <= other.km
            elif isinstance(other, (int, float)):
                return self.km <= other
            else:
                raise TypeError("Unsupported operand type for <=")

        def __ge__(self, other):
            if isinstance(other, Distance):
                return self.km >= other.km
            elif isinstance(other, (int, float)):
                return self.km >= other
            else:
                raise TypeError("Unsupported operand type for >=")



