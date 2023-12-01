class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, second: any) -> any:
        if type(second) == (int, float):
            return Distance(self.km + second)
        elif type(second) == float:
            return Distance(self.km + second)
        else:
            return Distance(self.km + second.km)

    def __iadd__(self, second: any) -> any:
        if type(second) == int:
            return Distance(self.km + second)
        elif type(second) == float:
            return Distance(self.km + second)
        else:
            return Distance(self.km + second.km)

    def __mul__(self, second: any) -> any:
        if type(second) == int:
            return Distance(self.km * second)
        elif type(second) == float:
            return Distance(round(self.km * second, 2))
        else:
            return Distance(self.km * second.km)

    def __truediv__(self, second: any) -> any:
        if type(second) == int:
            return Distance(round(self.km / second, 2))
        elif type(second) == float:
            return Distance(round(self.km / second, 2))
        else:
            return Distance(round(self.km / second.km, 2))

    def __eq__(self, second: any) -> any:
        if type(second) == int:
            return self.km == second
        elif type(second) == float:
            return self.km == second
        else:
            return self.km == second.km

    def __lt__(self, second: any) -> any:
        if type(second) == int:
            return self.km < second
        elif type(second) == float:
            return self.km < second
        else:
            return self.km < second.km

    def __gt__(self, second: any) -> any:
        if type(second) == int:
            return self.km > second
        elif type(second) == float:
            return self.km > second
        else:
            return self.km > second.km

    def __le__(self, second: any) -> any:
        if type(second) == int:
            return self.km <= second
        elif type(second) == float:
            return self.km <= second
        else:
            return self.km <= second.km

    def __ge__(self, second: any) -> any:
        if type(second) == int:
            return self.km >= second
        elif type(second) == float:
            return self.km >= second
        else:
            return self.km >= second.km
