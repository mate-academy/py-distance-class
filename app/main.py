class Distance:
    round_digit = 2
    type_error_message = 'Unsuported type'

    def __init__(self, km):
        self.km = km

    def __str__(self):
        return f"Distance: {self.km} kilometers"

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, other):
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, int):
            return Distance(self.km + other)
        else:
            raise TypeError(self.type_error_message)

    def __iadd__(self, other):
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, int):
            self.km += other
        else:
            raise TypeError(self.type_error_message)
        return self

    def __mul__(self, other):
        if isinstance(other, int):
            return Distance(self.km * other)
        else:
            raise TypeError(self.type_error_message)

    def __truediv__(self, other):
        if isinstance(other, int):
            return Distance(round(self.km / other, self.round_digit))
        else:
            raise TypeError(self.type_error_message)

    def __eq__(self, other):
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, int):
            return self.km == other
        else:
            raise TypeError(self.type_error_message)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, int):
            return self.km < other
        else:
            raise TypeError(self.type_error_message)

    def __gt__(self, other):
        return not (self.__eq__(other) or self.__lt__(other))

    def __le__(self, other):
        return not self.__gt__(other)

    def __ge__(self, other):
        return not self.__lt__(other)

    def __len__(self):
        return self.km
