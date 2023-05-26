from __future__ import annotations


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __float__(self) -> float:
        return float(self.km)

    def __radd__(self, rho: float | Distance) -> Distance:
        return self.__add__(rho)

    def __add__(self, rho: float | Distance) -> Distance:
        return Distance(self.km + float(rho))

    def __iadd__(self, rho: float | Distance) -> Distance:
        self.km += float(rho)
        return self

    def __mul__(self, rho: float) -> Distance:
        return Distance(self.km * rho)

    def __truediv__(self, rho: float) -> Distance:
        return Distance(round(self.km / rho, 2))

    def __lt__(self, rho: float | Distance) -> bool:
        return self.km < float(rho)

    def __gt__(self, rho: float | Distance) -> bool:
        return self.km > float(rho)

    def __eq__(self, rho: float | Distance) -> bool:
        return self.km == float(rho)

    def __le__(self, rho: float | Distance) -> bool:
        return self.km <= float(rho)

    def __ge__(self, rho: float | Distance) -> bool:
        return self.km >= float(rho)
