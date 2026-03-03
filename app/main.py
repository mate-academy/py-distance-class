class Distance:
    # Write your code here
    def __init__(self, km: int) -> int:
        self.km = km

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"Distance(km={self.km!r})"

    def __add__(self, km2):
        if isinstance(km2, Distance):
            return Distance(self.km + km2.km)
        elif isinstance(km2, (float, int)):
            return Distance(self.km + km2)

    def __iadd__(self, km2):
        if isinstance(km2, Distance):
            self.km += km2.km
        elif isinstance(km2, (float, int)):
            self.km += km2
        return self

    def __mul__(self, num):
        if isinstance(num, (int, float)):
            return Distance(self.km * num)

    def __truediv__(self, km2):
        if isinstance(km2, (int, float)):
            return Distance(round((self.km / km2), 2))

    def __gt__(self, km2):
        if isinstance(km2, Distance):
            return self.km > km2.km
        elif isinstance(km2, (float, int)):
            return self.km > km2

    def __lt__(self, km2):
        if isinstance(km2, Distance):
            return self.km < km2.km
        elif isinstance(km2, (float, int)):
            return self.km < km2

    def __eq__(self, km2):
        if isinstance(km2, Distance):
            return self.km == km2.km
        elif isinstance(km2, (float, int)):
            return self.km == km2

    def __le__(self, km2):
        if isinstance(km2, Distance):
            return self.km <= km2.km
        elif isinstance(km2, (float, int)):
            return self.km <= km2

    def __ge__(self, km2):
        if isinstance(km2, Distance):
            return self.km >= km2.km
        elif isinstance(km2, (float, int)):
            return self.km >= km2
