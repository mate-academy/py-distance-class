class Distance:

    def __init__(self, km: int | float) -> None:
        self.km = km

    def __add__(self, distance_to_add: Distance | int) -> Distance:
        if isinstance(distance_to_add, (int, float)):
            return Distance(self.km + distance_to_add)
        return Distance(self.km + distance_to_add.km)

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __iadd__(self, distance_to_add: int | float | Distance) -> Distance:
        if isinstance(distance_to_add, (int, float)):
            self.km += distance_to_add
            return self
        if isinstance(distance_to_add, Distance):
            self.km += distance_to_add.km
            return self
        return NotImplemented

    def __mul__(self, distance_to_multiply: int | float) -> Distance:
        return Distance(self.km * distance_to_multiply)

    def __truediv__(self, distance_to_div: int | float) -> Distance:
        return Distance(round(self.km / distance_to_div, 2))

    def __eq__(self, distance_to_compare: object) -> bool:
        if isinstance(distance_to_compare, Distance):
            return self.km == distance_to_compare.km
        if isinstance(distance_to_compare, (float, int)):
            return self.km == distance_to_compare
        return NotImplemented

    def __gt__(self, distance_to_compare: object) -> bool:
        if isinstance(distance_to_compare, Distance):
            return self.km > distance_to_compare.km
        if isinstance(distance_to_compare, (float, int)):
            return self.km > distance_to_compare
        return NotImplemented

    def __lt__(self, distance_to_compare: object) -> bool:
        if isinstance(distance_to_compare, Distance):
            return self.km < distance_to_compare.km
        if isinstance(distance_to_compare, (float, int)):
            return self.km < distance_to_compare
        return NotImplemented

    def __le__(self, distance_to_compare: object) -> bool:
        if isinstance(distance_to_compare, Distance):
            return self.km <= distance_to_compare.km
        if isinstance(distance_to_compare, (float, int)):
            return self.km <= distance_to_compare
        return NotImplemented

    def __ge__(self, distance_to_compare: object) -> bool:
        if isinstance(distance_to_compare, Distance):
            return self.km >= distance_to_compare.km
        if isinstance(distance_to_compare, (float, int)):
            return self.km >= distance_to_compare
        return NotImplemented
