class Distance:

    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, another: int | float) -> float:
        if isinstance(another, Distance):
            return Distance(self.km + another.km)
        elif isinstance(another, (int, float)):
            return Distance(self.km + another)

    def __iadd__(self, another: int | float) -> float:
        if isinstance(another, Distance):
            self.km += another.km
            return self
        elif isinstance(another, (int, float)):
            self.km += another
            return self

    def __mul__(self, another: int | float) -> float:
        return Distance(
            self.km * another
        )

    def __truediv__(self, another: int | float) -> float:
        return Distance(
            round(self.km / another, 2)
        )

    def __lt__(self, another: int | float) -> bool:
        if isinstance(another, (int, float)):
            return self.km < another
        elif isinstance(another, Distance):
            return self.km < another.km

    def __gt__(self, another: int | float) -> bool:
        if isinstance(another, (int, float)):
            return self.km > another
        elif isinstance(another, Distance):
            return self.km > another.km

    def __eq__(self, another: int | float) -> bool:
        if isinstance(another, (int, float)):
            return self.km == another
        elif isinstance(another, Distance):
            return self.km == another.km

    def __le__(self, another: int | float) -> bool:
        if isinstance(another, (int, float)):
            return self.km <= another
        elif isinstance(another, Distance):
            return self.km <= another.km

    def __ge__(self, another: int | float) -> bool:
        if isinstance(another, (int, float)):
            return self.km >= another
        elif isinstance(another, Distance):
            return self.km >= another.km
