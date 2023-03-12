from typing import Union


class Distance:

    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union[float, "Distance"]
                ) -> [float, "Distance"]:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        return Distance(float(self.km) + other)

    def __iadd__(self, other: Union[float, "Distance"]
                 ) -> [float, "Distance"]:
        if isinstance(other, Distance):
            self.km += other.km
            return self
        else:
            self.km += other
        return self

    def __mul__(self, other: "Distance") -> "Distance":
        return Distance(self.km * other)

    def __truediv__(self, other: "Distance") -> "Distance":
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: Union[float, "Distance"]) -> bool:
        if isinstance(other, Distance):
            return True if self.km < other.km else False
        else:
            return True if self.km < other else False

    def __gt__(self, other: Union[float, "Distance"]) -> bool:
        if isinstance(other, Distance):
            return True if self.km > other.km else False
        else:
            return True if self.km > other else False

    def __eq__(self, other: Union[float, "Distance"]) -> bool:
        if isinstance(other, Distance):
            return True if self.km == other.km else False
        else:
            return True if self.km == other else False

    def __le__(self, other: Union[float, "Distance"]) -> bool:
        if isinstance(other, Distance):
            return True if self.km <= other.km else False
        else:
            return True if self.km <= other else False

    def __ge__(self, other: Union[float, "Distance"]) -> bool:
        if isinstance(other, Distance):
            return True if self.km >= other.km else False
        else:
            return True if self.km >= other else False
