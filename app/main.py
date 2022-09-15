class Distance:
    def __init__(self, km):
        self.km = km

    def __str__(self):
        return "Distance: " + str(self.km) + " kilometers."

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, new_distance):
        if isinstance(new_distance, Distance):
            return Distance(self.km + new_distance.km)
        elif new_distance is not isinstance:
            return self + Distance(new_distance)

    def __iadd__(self, new_distance):
        if isinstance(new_distance, Distance):
            self.km += new_distance.km
            return self
        elif new_distance is not isinstance:
            self.km += new_distance
            return self

    def __mul__(self, new_distance):
        if isinstance(new_distance, Distance):
            return Distance(self.km * new_distance.km)
        elif new_distance is not isinstance:
            return self * Distance(new_distance)

    def __truediv__(self, new_distance):
        if isinstance(new_distance, Distance):
            return Distance(round((self.km / new_distance.km), 2))
        elif new_distance is not isinstance:
            return Distance(round((self.km / new_distance), 2))

    def __lt__(self, new_distance):
        if isinstance(new_distance, Distance):
            return self.km < new_distance.km
        elif new_distance is not isinstance:
            return self.km < new_distance

    def __gt__(self, new_distance):
        if isinstance(new_distance, Distance):
            return self.km > new_distance.km
        elif new_distance is not isinstance:
            return self.km > new_distance

    def __eq__(self, new_distance):
        if isinstance(new_distance, Distance):
            return self.km == new_distance.km
        elif new_distance is not isinstance:
            return self.km == new_distance

    def __le__(self, new_distance):
        if isinstance(new_distance, Distance):
            return self.km <= new_distance.km
        elif new_distance is not isinstance:
            return self.km <= new_distance

    def __ge__(self, new_distance):
        if isinstance(new_distance, Distance):
            return self.km >= new_distance.km
        elif new_distance is not isinstance:
            return self.km >= new_distance

    def __len__(self):
        return self.km
