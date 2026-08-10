class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, dis: classmethod | int) -> classmethod:
        if isinstance(dis, Distance):
            return Distance(self.km + dis.km)
        return Distance(self.km + dis)

    def __iadd__(self, dis: classmethod | int) -> classmethod:
        if isinstance(dis, Distance):
            self.km += dis.km
            return self
        self.km += dis
        return self

    def __mul__(self, dis: classmethod | int) -> classmethod:
        # if isinstance(dis, Distance):  Why not???
        #     return Distance(self.km * dis.km)
        return Distance(self.km * dis)

    def __truediv__(self, dis: classmethod | int) -> classmethod:
        # if isinstance(dis, Distance):  Why not???
        #     return Distance(round(self.km / dis.km, 2))
        return Distance(round(self.km / dis, 2))

    def __lt__(self, dis: classmethod | int) -> bool:
        if isinstance(dis, Distance):
            return self.km < dis.km
        return self.km < dis

    def __gt__(self, dis: classmethod | int) -> bool:
        if isinstance(dis, Distance):
            return self.km > dis.km
        return self.km > dis

    def __eq__(self, dis: classmethod | int) -> bool:
        if isinstance(dis, Distance):
            return self.km == dis.km
        return self.km == dis

    def __le__(self, dis: classmethod | int) -> bool:
        if isinstance(dis, Distance):
            return self.km <= dis.km
        return self.km <= dis

    def __ge__(self, dis: classmethod | int) -> bool:
        if isinstance(dis, Distance):
            return self.km >= dis.km
        return self.km >= dis
