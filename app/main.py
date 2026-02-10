class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, km2: (Distance, int, float)) -> Distance:
        if isinstance(km2, Distance):
            return Distance(self.km + km2.km)
        elif isinstance(km2, (int, float)):
            return Distance(self.km + km2)

    def __iadd__(self, km2: (Distance, int, float)) -> Distance:
        if isinstance(km2, Distance):
            self.km += km2.km
        elif isinstance(km2, (int, float)):
            self.km += km2
        return self
