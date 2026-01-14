from typing import Union


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, distance: "Distance") -> "Distance":
        if isinstance(distance, int | float):
            distance2 = self.km + distance
            return Distance(distance2)
        distance3 = self.km + distance.km
        return Distance(distance3)

    def __iadd__(self, distance: "Distance") -> "Distance":
        if isinstance(distance, int | float):
            self.km += distance
        else:
            self.km += distance.km
        return self

    def __mul__(self, distance: int | float) -> "Distance":
        distance2 = self.km * distance
        return Distance(distance2)

    def __truediv__(self, distance: int | float) -> "Distance":
        distance2 = self.km / distance
        return Distance(round(distance2, 2))

    def __lt__(self, distance: Union[int, "Distance", float]) -> bool:
        if isinstance(distance, int | float):
            return self.km < distance
        else:
            return self.km < distance.km

    def __gt__(self, distance: Union[int, "Distance", float]) -> bool:
        if isinstance(distance, int | float):
            return self.km > distance
        else:
            return self.km > distance.km

    def __eq__(self, distance: Union[int, "Distance", float]) -> bool:
        if isinstance(distance, int | float):
            return self.km == distance
        else:
            return self.km == distance.km

    def __le__(self, distance: Union[int, "Distance", float]) -> bool:
        if isinstance(distance, int | float):
            return self.km <= distance
        else:
            return self.km <= distance.km

    def __ge__(self, distance: Union[int, "Distance", float]) -> bool:
        if isinstance(distance, int | float):
            return self.km >= distance
        else:
            return self.km >= distance.km
