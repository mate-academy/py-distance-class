class Distance:
    def __init__(self, km: int):
        self.km = km

    def __str__(self):
        return f"Distance: {self.km} kilometers"

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, other):
        if isinstance(other, Distance):
            return Distance(
                km=self.km + other.km
            )
        else:
            return Distance(
                km=self.km + other
            )

    def __iadd__(self, other):
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other

        return self

    def __mul__(self, other):
        return Distance(
            km=self.km * other
        )

    def __truediv__(self, other):
        return Distance(
            km=round(self.km / other, 2)
        )

    def __lt__(self, other):
        if isinstance(other, Distance):
            answer = self.km < other.km
        else:
            answer = self.km < other
        return answer

    def __gt__(self, other):
        if isinstance(other, Distance):
            answer = self.km > other.km
        else:
            answer = self.km > other
        return answer

    def __eq__(self, other):
        if isinstance(other, Distance):
            answer = self.km == other.km
        else:
            answer = self.km == other
        return answer

    def __le__(self, other):
        return not self > other

    def __ge__(self, other):
        return not self < other

    def __len__(self):
        return self.km
