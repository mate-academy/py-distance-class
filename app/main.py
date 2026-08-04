class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, outro: int) -> any:
        if isinstance(outro, (int, float)):
            return Distance(self.km + outro)
        else:
            return Distance(self.km + outro.km)

    def __iadd__(self, outro: int) -> any:
        if isinstance(outro, (int, float)):
            self.km += outro
            return self
        else:
            self.km += outro.km
            return self

    def __mul__(self, outro: int) -> any:
        return Distance(self.km * outro)

    def __truediv__(self, outro: int) -> any:
        return Distance(round((self.km / outro), 2))

    def __lt__(self, outro: int) -> bool:
        if self.km < outro:
            return True
        else:
            return False

    def __gt__(self, outro: int) -> bool:
        if self.km > outro:
            return True
        else:
            return False

    def __eq__(self, outro: int) -> bool:
        if self.km == outro:
            return True
        else:
            return False

    def __le__(self, outro: int) -> bool:
        if self.km <= outro:
            return True
        else:
            return False

    def __ge__(self, outro: int) -> bool:
        if self.km >= outro:
            return True
        else:
            return False
