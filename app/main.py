from __future__ import annotations

class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, dis: Distance | int | float) -> Distance:
        if isinstance(dis, Distance):
            return Distance(self.km + dis.km)  
        else:
            return Distance(self.km + dis)

    def __iadd__(self, dis: Distance | int | float) -> None:
        if isinstance(dis, Distance):
            self.km = self.km + dis.km
        else:
            self.km = self.km + dis
        return self

    def __mul__(self, dis: int | float) -> Distance:
        return Distance(round(self.km * dis, 3))

    def __truediv__(self, dis: int | float) -> Distance:
        return Distance(round(self.km / dis, 2))

    def __lt__(self, dis: Distance | float | int) -> bool:
        if isinstance(dis, Distance):
            return self.km < dis.km
        else:
            return self.km < dis
    
    def __gt__(self, dis: Distance | float | int) -> bool:
        if isinstance(dis, Distance):
            return self.km > dis.km
        else:
            return self.km > dis
    
    def __eq__(self, dis: Distance | float | int) -> bool:
        if isinstance(dis, Distance):
            return self.km == dis.km
        else:
            return self.km == dis

    def __le__(self, dis: Distance | float | int) -> bool:
        if isinstance(dis, Distance):
            return self.km <= dis.km
        else:
            return self.km <= dis

    def __ge__(self, dis: Distance | float | int) -> bool:
        if isinstance(dis, Distance):
            return self.km >= dis.km
        else:
            return self.km >= dis
