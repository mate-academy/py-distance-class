class Distance:
    def __init__(self, km):
        self.km = km

    def __str__(self):
        return f'Distance: {self.km} kilometers'

    def __repr__(self):
        return f'Distance(km={self.km})'

    def __add__(self, other):
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        else:
            raise TypeError("Unsupported operand type for +: 'Distance' and '{}'".format(type(other).__name__))

    def __iadd__(self, other):
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            raise TypeError("Unsupported operand type for +=: 'Distance' and '{}'".format(type(other).__name__))
        return self

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        else:
            raise TypeError("Unsupported operand type for *: 'Distance' and '{}'".format(type(other).__name__))

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            if other == 0:
                raise ValueError("Cannot divide by zero.")
            return Distance(self.km / other)
        else:
            raise TypeError("Unsupported operand type for /: 'Distance' and '{}'".format(type(other).__name__))

    def __lt__(self, other):
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other
        else:
            raise TypeError("Unsupported operand type for <: 'Distance' and '{}'".format(type(other).__name__))

    def __le__(self, other):
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other
        else:
            raise TypeError("Unsupported operand type for <=: 'Distance' and '{}'".format(type(other).__name__))

     def __eq__(self, other):
         if isinstance(other, Distance):
             return self.km == other.km
         elif isinstance(other, (int, float)):
             return self.km == other
         else:
             return NotImplemented  # Allow other types to handle comparison if they implement it

    def __gt__(self, other):
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other
        else:
            raise TypeError("Unsupported operand type for >: 'Distance' and '{}'".format(type(other).__name__))

    def __ge__(self, other):
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= other
        else:
            raise TypeError("Unsupported operand type for >=: 'Distance' and '{}'".format(type(other).__name__))
