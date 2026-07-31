class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __add__(self, other) -> any:
        if not isinstance(other, Distance):
            return None
        return Distance(self.km + other.km)

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __str__(self) -> str:
        return __repr__()
    
    pass
