class Distance:

    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, other):
        if isinstance(other, int):
            return Distance(int(self.km) + other)
        return Distance(self.km + other.km)

    def __iadd__(self, other):

        print(f"type : {type(self.km.__repr__())}, \n"
              f"value: {self.km.__repr__()}")

        print(f"type : {type(other.__repr__())}, \n"
              f"value: {other.__repr__()}")

        if isinstance(other, int):
            self.km += int(other)
        return self

    # def __mul__(self, other):
    #     return self.km * other
    #
    # def __truediv__(self, other):
    #     return math.floor(self.km * 100 / other) / 100
    #
    # def __lt__(self, other):
    #     return True if self.km < other.km else False
    #
    # def __gt__(self, other):
    #     return True if self.km > other.km else False
    #
    # def __eq__(self, other):
    #     return True if self.km == other.km else False
    #
    # def __le__(self, other):
    #     return True if self.km <= other.km else False
    #
    # def __ge__(self, other):
    #     return True if self.km >= other.km else False


distance1 = Distance(20)
distance2 = Distance(30)
distance1 += distance2  # distance1.km is 50

distance = Distance(20)
distance += 30  # distance.km == 50
