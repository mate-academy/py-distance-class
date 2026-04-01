class Distance:

    def __init__(self, km: float):
        self.km = km

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, distance):
        if isinstance(distance, Distance):
            distance.km = self.km + distance.km
            return Distance(distance.km)
        distance = self.km + distance
        return Distance(distance)

    def __iadd__(self, distance):
        if isinstance(distance, Distance):
            self.km += distance.km
            return self
        self.km += distance
        return self

    def __mul__(self, distance):
        if isinstance(distance, (int, float)):
            distance = self.km * distance
            return Distance(distance)

    def __truediv__(self, distance):

        if isinstance(distance, (int, float)):
            distance = round((self.km / distance), 2)
        if self.km == distance:
            return True
        return Distance(distance)

    def __eq__(self, distance):
        if isinstance(distance, Distance):
            return self.km == distance.km
        return self.km == distance

    def __gt__(self, distance):
        if isinstance(distance, Distance):
            return self.km > distance.km
        return self.km > distance

    def __ge__(self, distance):
        if isinstance(distance, Distance):
            return self.km >= distance.km
        return self.km >= distance

    def __lt__(self, distance):
        if isinstance(distance, Distance):
            return self.km < distance.km
        return self.km < distance

    def __le__(self, distance):
        if isinstance(distance, Distance):
            return self.km <= distance.km
        return self.km <= distance
