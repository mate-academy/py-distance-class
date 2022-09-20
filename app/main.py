class Distance:
    def __init__(self, km):
        self.km = km

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, number):
        if isinstance(number, Distance):
            return Distance(self.km + number.km)
        return Distance(self.km + number)

    def __iadd__(self, number):
        if isinstance(number, Distance):
            self.km += number.km
        else:
            self.km += number
        return self

    def __mul__(self, number):
        if isinstance(number, Distance):
            return Distance(self.km * number.km)
        return Distance(self.km * number)

    def __truediv__(self, number):
        if isinstance(number, Distance):
            return Distance(round(self.km / number.km, 2))
        return Distance(round(self.km / number, 2))

    def __lt__(self, number):
        if isinstance(number, Distance):
            return self.km < number.km
        return self.km < number

    def __gt__(self, number):
        if isinstance(number, Distance):
            return self.km > number.km
        return self.km > number

    def __eq__(self, number):
        if isinstance(number, Distance):
            return self.km == number.km
        return self.km == number

    def __le__(self, number):
        if isinstance(number, Distance):
            return self.km <= number.km
        return self.km <= number

    def __ge__(self, number):
        if isinstance(number, Distance):
            return self.km >= number.km
        return self.km >= number

    def __len__(self):
        return self.km
