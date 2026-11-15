class Distance:
    def __init__(self, distance: float):
        self.distance = distance

    def __str__(self):
        return f"Distance: {self.distance} kilometers"

    def __repr__(self):
        return f"Distance(km={self.distance})"

    def __add__(self, other):
        return Distance(self.distance + other.distance)

    def __iadd__(self, other):
        self.distance += other.distance

    def __mul__(self, multiplier: int):
        return Distance(self.distance * multiplier)

    def __truediv__(self, divisor: int):
        return Distance(round(self.distance / divisor, 2))

    def __lt__(self, other):
        return self.distance < other.distance

    def __gt__(self, other):
        return self.distance > other.distance

    def __le__(self, other):
        return self.distance <= other.distance

    def __ge__(self, other):
        return self.distance >= other.distance

    def __eq__(self, other):
        return self.distance == other.distance
