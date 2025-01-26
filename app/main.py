class Distance:
    def __init__(self, km: "int | float") -> None:
        if not isinstance(km, (int, float)):
            raise ValueError("km must be a number.")
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: "Distance | int | float") -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        else:
            raise ValueError("Can only add Distance or numeric values.")

    def __iadd__(self, other: "Distance | int | float") -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            raise ValueError("Can only add Distance or numeric values.")
        return self

    def __mul__(self, factor: "int | float | Distance") -> "Distance":
        if isinstance(factor, (int, float)):
            return Distance(self.km * factor)
        elif isinstance(factor, Distance):
            return Distance(self.km * factor.km)
        else:
            raise ValueError("Can only multiply by a numeric value or another Distance.")

    def __truediv__(self, divisor: "int | float | Distance") -> "Distance":
        if isinstance(divisor, (int, float)):
            if divisor == 0:
                raise ValueError("Divisor must be a non-zero numeric value.")
            return Distance(round(self.km / divisor, 2))
        elif isinstance(divisor, Distance):
            if divisor.km == 0:
                raise ValueError("Divisor Distance cannot have zero km.")
            return Distance(round(self.km / divisor.km, 2))
        else:
            raise ValueError("Divisor must be a non-zero numeric value or another Distance.")

    def __lt__(self, other: "Distance | int | float") -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other
        else:
            raise ValueError("Comparison is only supported with Distance or numeric values.")

    def __le__(self, other: "Distance | int | float") -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other
        else:
            raise ValueError("Comparison is only supported with Distance or numeric values.")

    def __eq__(self, other: "Distance | int | float") -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other
        else:
            return False

    def __ne__(self, other: "Distance | int | float") -> bool:
        return not self.__eq__(other)

    def __gt__(self, other: "Distance | int | float") -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other
        else:
            raise ValueError("Comparison is only supported with Distance or numeric values.")

    def __ge__(self, other: "Distance | int | float") -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= other
        else:
            raise ValueError("Comparison is only supported with Distance or numeric values.")
