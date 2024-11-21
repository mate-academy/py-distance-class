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
        if isinstance(new_distance, (int, float)):
            return self + Distance(new_distance)

    def __iadd__(self, new_distance):
        if isinstance(new_distance, Distance):
            self.km += new_distance.km
        if isinstance(new_distance, (int, float)):
            self.km += new_distance
        return self

    def __mul__(self, new_distance):
        if isinstance(new_distance, Distance):
            return Distance(self.km * new_distance.km)
        if isinstance(new_distance, (int, float)):
            return self * Distance(new_distance)

    def __truediv__(self, new_distance):
        if isinstance(new_distance, Distance):
            result = result = self.km / new_distance.km
        if isinstance(new_distance, (int, float)):
            result = result = self.km / new_distance
        return Distance(round(result, 2))

    def __lt__(self, new_distance):
        if isinstance(new_distance, Distance):
            result = self.km < new_distance.km
        if isinstance(new_distance, (int, float)):
            result = self.km < new_distance
        return result

    def __gt__(self, new_distance):
        if isinstance(new_distance, Distance):
            result = self.km > new_distance.km
        if isinstance(new_distance, (int, float)):
            result = self.km > new_distance
        return result

    def __eq__(self, new_distance):
        if isinstance(new_distance, Distance):
            result = self.km == new_distance.km
        if isinstance(new_distance, (int, float)):
            result = self.km == new_distance
        return result

    def __le__(self, new_distance):
        if isinstance(new_distance, Distance):
            result = self.km <= new_distance.km
        if isinstance(new_distance, (int, float)):
            result = self.km <= new_distance
        return result

    def __ge__(self, new_distance):
        if isinstance(new_distance, Distance):
            result = self.km >= new_distance.km
        if isinstance(new_distance, (int, float)):
            result = self.km >= new_distance
        return result

    def __len__(self):
        return self.km
