class Distance:

    def __init__(self, km):
        self.km = km

    def __str__(self):
        print(f"Distance: {self.km} kilometers)")

    def __repr__(self):
        return f'Distance(km={self.km})'

    def __add__(self, kilometers):
        if isinstance(kilometers, int) or isinstance(kilometers, float):
            return Distance(
                km=self.km + kilometers)
        else:
            return Distance(
                km=self.km + kilometers.km
            )

    def __iadd__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            self.km += other
        else:
            self.km += other.km
        return self

    def __mul__(self, multiplicator):
        return Distance(
            km=self.km * multiplicator)

    def __truediv__(self, divider):
        result_km = round(self.km / divider, 2)
        return Distance(
            km=result_km
        )

    def __lt__(self, other):
        return self.km < other

    def __gt__(self, other):
        return self.km > other

    def __eq__(self, other):
        return self.km == other

    def __le__(self, other):
        return self.km <= other

    def __ge__(self, other):
        return self.km >= other

    def __len__(self):
        return self.km
