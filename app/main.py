class Distance:
    def __init__(self, km) -> None:
        self.km = km

    def __add__(self, other) -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __iadd__(self, other) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        return self

    def __mul__(self, other) -> "Distance":
        return Distance(self.km * other)

    def __truediv__(self, other: (int, float)) -> "Distance":
        return Distance(round((self.km / other), 2))

    def __eq__(self, other) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other

    def __gt__(self, other) -> bool:
        if isinstance(other, (int, float)):  # Якщо other — число
            return self.km > other
        elif isinstance(other, Distance):  # Якщо other — об'єкт Distance
            return self.km > other.km

    def __lt__(self, other) -> bool:
        if isinstance(other, (int, float)):  # Якщо other — число
            return self.km < other
        elif isinstance(other, Distance):  # Якщо other — об'єкт Distance
            return self.km < other.km

    def __le__(self, other) -> bool:
        if isinstance(other, (int, float)):  # Якщо other — число
            return self.km <= other
        elif isinstance(other, Distance):  # Якщо other — об'єкт Distance
            return self.km <= other.km
        return self.km <= other.km

    def __ge__(self, other: "Distance") -> bool:
        if isinstance(other, (int, float)):  # Якщо other — число
            return self.km >= other
        elif isinstance(other, Distance):  # Якщо other — об'єкт Distance
            return self.km >= other.km
    pass
