class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, other):
        return Distance(self.km + other.km)

    def __iadd__(self, other):
        self.km += other.km
        return self