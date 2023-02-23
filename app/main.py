class Distance:
    def __init__(self, km):
        self.km = km

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, dist):
        if isinstance(dist, Distance):
            return Distance(self.km + dist.km)
        return Distance(self.km + dist)

    def __iadd__(self, dist):
        if isinstance(dist, Distance):
            self.km += dist.km
            return self
        self.km += dist
        return self

    def __mul__(self, dist):
        return Distance(self.km * dist)

    def __truediv__(self, dist):
        return Distance(round(self.km / dist, 2))

    def __lt__(self, dist):
        if isinstance(dist, Distance):
            return True if self.km < dist.km else False
        return True if self.km < dist else False

    def __gt__(self, dist):
        if isinstance(dist, Distance):
            return True if self.km > dist.km else False
        return True if self.km > dist else False

    def __eq__(self, dist):
        if isinstance(dist, Distance):
            return True if self.km == dist.km else False
        return True if self.km ==dist else False

    def __le__(self, dist):
        if isinstance(dist, Distance):
            return True if self.km <= dist.km else False
        return True if self.km <= dist else False

    def __ge__(self, dist):
        if isinstance(dist, Distance):
            return True if self.km >= dist.km else False
        return True if self.km >= dist else False


d = Distance(15)
d += 30
print(d)