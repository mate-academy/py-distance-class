class Distance:

    def __init__(self, km):
        self.km = km

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, distance):
        if isinstance(distance, (int, float)):
            dist = self.km + distance
        else:
            dist = self.km + distance.km
        return Distance(dist)

    def __iadd__(self, distance):
        if isinstance(distance, (int, float)):
            self.km += distance
        else:
            self.km += distance.km
        return self

    def __mul__(self, distance):
        if isinstance(distance, (int, float)):
            self.km = self.km * distance
        else:
            self.km = self.km * distance.km
        return Distance(self.km)

    def __truediv__(self, distance):
        if isinstance(distance, (int, float)):
            self.km = round((self.km / distance), 2)
        else:
            self.km = round((self.km / distance.km), 2)
        return Distance(self.km)

    def __lt__(self, distance):
        if isinstance(distance, (int, float)):
            dist = distance
        else:
            dist = distance.km
        return self.km < dist

    def __gt__(self, distance):
        if isinstance(distance, (int, float)):
            dist = distance
        else:
            dist = distance.km
        return self.km > dist

    def __eq__(self, distance):
        if isinstance(distance, (int, float)):
            dist = distance
        else:
            dist = distance.km
        return self.km == dist

    def __le__(self, distance):
        if isinstance(distance, (int, float)):
            dist = distance
        else:
            dist = distance.km
        return self.km <= dist

    def __ge__(self, distance):
        if isinstance(distance, (int, float)):
            dist = distance
        else:
            dist = distance.km
        return self.km >= dist

    def __len__(self):
        return self.km
