from typing import Union


class Distance:
    def __init__(self, km: Union[int, float]) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, distance2: Union[int, float, "Distance"]) -> "Distance":
        if isinstance(distance2, Distance):
            return Distance(self.km + distance2.km)
        elif isinstance(distance2, (int, float)):
            return Distance(self.km + distance2)

    def __iadd__(self, distance2: Union[int, float, "Distance"]) -> "Distance":
        if isinstance(distance2, Distance):
            self.km += distance2.km
        elif isinstance(distance2, (int, float)):
            self.km += distance2
        return self

    def __mul__(self, factor: Union[int, float]) -> "Distance":
        if isinstance(factor, (int, float)):
            return Distance(self.km * factor)

    def __truediv__(self, factor: Union[int, float]) -> "Distance":
        if isinstance(factor, (float, int)) and factor != 0:
            result_km = round(self.km / factor, 2)
            return Distance(result_km)

    def __lt__(self, distance2: Union[int, float, "Distance"]) -> bool:
        other_km = distance2.km \
            if isinstance(distance2, Distance) else distance2
        return self.km < other_km

    def __gt__(self, distance2: Union[int, float, "Distance"]) -> bool:
        other_km = distance2.km \
            if isinstance(distance2, Distance) else distance2
        return self.km > other_km

    def __eq__(self, distance2: Union[int, float, "Distance"]) -> bool:
        other_km = distance2.km \
            if isinstance(distance2, Distance) else distance2
        return self.km == other_km

    def __le__(self, distance2: Union[int, float, "Distance"]) -> bool:
        other_km = distance2.km \
            if isinstance(distance2, Distance) else distance2
        return self.km <= other_km

    def __ge__(self, distance2: Union[int, float, "Distance"]) -> bool:
        other_km = distance2.km \
            if isinstance(distance2, Distance) else distance2
        return self.km >= other_km
