class Distance:
    def __init__(self, km):
        self.km = km

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, distance_2):
        if isinstance(distance_2, Distance):
            return Distance(self.km + distance_2.km)

        return Distance(self.km + distance_2)

    def __iadd__(self, distance_2):
        if isinstance(distance_2, Distance):
            self.km += distance_2.km
            return self

        self.km += distance_2
        return self

    def __mul__(self, distance_2):
        return Distance(self.km * distance_2)

    def __truediv__(self, distance_2):
        return Distance(round(self.km / distance_2, 2))

    def __lt__(self, distance_2):
        if isinstance(distance_2, Distance):
            return self.km < distance_2.km

        return self.km < distance_2

    def __gt__(self, distance_2):
        if isinstance(distance_2, Distance):
            return self.km > distance_2.km

        return self.km > distance_2

    def __eq__(self, distance_2):
        if isinstance(distance_2, Distance):
            return self.km == distance_2.km

        return self.km == distance_2

    def __le__(self, distance_2):
        if isinstance(distance_2, Distance):
            return self.km <= distance_2.km

        return self.km <= distance_2

    def __ge__(self, distance_2):
        if isinstance(distance_2, Distance):
            return self.km >= distance_2.km

        return self.km >= distance_2

    def __len__(self):
        return self.km
