from typing import Union


class Distance:
    def __init__(self, km: Union[float, int]) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, dist: Union["Distance", float, int]) -> "Distance":
        if isinstance(dist, Distance):
            return Distance(self.km + dist.km)
        return Distance(self.km + dist)

    def __iadd__(self, dist: Union["Distance", float, int]) -> "Distance":
        if isinstance(dist, Distance):
            self.km += dist.km
            return self
        self.km += dist
        return self

    def __mul__(self, dist: Union[float, int]) -> "Distance":
        return Distance(self.km * dist)

    def __truediv__(self, dist: Union[float, int]) -> "Distance":
        return Distance(round(self.km / dist, 2))

    def __lt__(self, dist: Union["Distance", float, int]) -> bool:
        if isinstance(dist, Distance):
            return self.km < dist.km
        return self.km < dist

    def __gt__(self, dist: Union["Distance", float, int]) -> bool:
        if isinstance(dist, Distance):
            return self.km > dist.km
        return self.km > dist

    def __eq__(self, dist: Union["Distance", float, int]) -> bool:
        if isinstance(dist, Distance):
            return self.km == dist.km
        return self.km == dist

    def __ge__(self, dist: Union["Distance", float, int]) -> bool:
        return not self.__lt__(dist)

    def __le__(self, dist: Union["Distance", float, int]) -> bool:
        return not self.__gt__(dist)
