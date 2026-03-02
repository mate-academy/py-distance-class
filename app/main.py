from __future__ import division, annotations


class Distance:
    def __init__(
            self,
            km: int
    ) -> None:

        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, new_km: Distance | int | float) -> Distance:
        if isinstance(new_km, Distance):
            return Distance(self.km + new_km.km)

        if isinstance(new_km, (int, float)):
            return Distance(self.km + new_km)

        return NotImplemented

    def __iadd__(self, new_km: Distance | int | float) -> Distance:
        if isinstance(new_km, Distance):

            self.km += new_km.km
            return self

        if isinstance(new_km, (int, float)):
            self.km += new_km
            return self

        return NotImplemented

    def __mul__(self, new_km: int | float) -> Distance:
        if isinstance(new_km, (int, float)):
            return Distance(self.km * new_km)

        return NotImplemented

    def __truediv__(self, new_km: int | float) -> Distance:
        if isinstance(new_km, (int, float)):
            return Distance(round(self.km / new_km, 2))

        return NotImplemented

    def __lt__(self, new_km: Distance | int | float) -> bool:
        if isinstance(new_km, Distance):
            return self.km < new_km.km

        if isinstance(new_km, (int, float)):
            return self.km < new_km

        return NotImplemented

    def __gt__(self, new_km: Distance | int | float) -> bool:
        if isinstance(new_km, Distance):
            return self.km > new_km.km

        if isinstance(new_km, (int, float)):
            return self.km > new_km

        return NotImplemented

    def __eq__(self, new_km: Distance | int | float) -> bool:
        if isinstance(new_km, Distance):
            return self.km == new_km.km

        if isinstance(new_km, (int, float)):
            return self.km == new_km

        return NotImplemented

    def __le__(self, new_km: Distance | int | float) -> bool:
        if isinstance(new_km, Distance):
            return self.km <= new_km.km

        if isinstance(new_km, (int, float)):
            return self.km <= new_km

        return NotImplemented

    def __ge__(self, new_km: Distance | int | float) -> bool:
        if isinstance(new_km, Distance):
            return self.km >= new_km.km
        if isinstance(new_km, (int, float)):
            return self.km >= new_km

        return NotImplemented
