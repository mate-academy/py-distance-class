class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"
    
    def __add__(self, outro_km: int) -> int:
        return self.km + self.outro_km

    def __iadd__(self, outro_km: int) -> int:
        self.km += self.outro_km
        return self.km

    def __mul__(self, outro_km: int) -> int:
        return self.km * self.outro_km

    def __truediv__(self, outro_km: int) -> int
        return self.km / self.outro_km

    def __lt__(self, outro_km: int) -> bool
        return self.km < self.outro_km

    def __eq__(self, outro_km: int) -> bool
        if isinstance(outro_km, Distance):
            if self.km == outro.km:
                return True
        return False

    def __gt__(self, outro_km: int) -> bool
        return self.km > self.outro_km

    def __le__(self, outro_k: int) -> bool
        return self.km <= self.outro_km

    def __ge__(self, outro_km: int) -> bool
        return self.km >= self.outro_km
