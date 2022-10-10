class Distance:
    def __init__(self, km: (int, float)) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: (int, float)) -> object:
        second = other if isinstance(other, (int, float)) else other.km
        return Distance(self.km + second)

    def __iadd__(self, other: (int, float)) -> object:
        second = other if isinstance(other, (int, float)) else other.km
        self.km += second

        return self

    def __mul__(self, other: (int, float)) -> object:
        second = other if isinstance(other, (int, float)) else other.km
        return Distance(self.km * second)

    def __truediv__(self, other: (int, float)) -> object:
        second = other if isinstance(other, (int, float)) else other.km
        return Distance(round(self.km / second, 2))

    def __lt__(self, other: (int, float)) -> object:
        second = other if isinstance(other, (int, float)) else other.km
        return self.km < second

    def __gt__(self, other: (int, float)) -> object:
        second = other if isinstance(other, (int, float)) else other.km
        return self.km > second

    def __eq__(self, other: (int, float)) -> object:
        second = other if isinstance(other, (int, float)) else other.km
        return self.km == second

    def __le__(self, other: (int, float)) -> object:
        second = other if isinstance(other, (int, float)) else other.km
        return self.km <= second

    def __ge__(self, other: (int, float)) -> object:
        second = other if isinstance(other, (int, float)) else other.km
        return self.km >= second

    def __len__(self) -> object:
        return len(self.km)


# __init__
distance = Distance(20)  # distance.km == 20

# __str__
# distance = Distance(20)
# print(distance)  # "Distance: 20 kilometers."

# __repr__
# distance = Distance(20)
# repr(distance)  # "Distance(km=20)"

# __add__
# distance1 = Distance(20)
# distance2 = Distance(30)
# distance3 = distance1 + distance2
# print(distance3)
#
# print(isinstance(distance3, Distance))  # == True
# distance3.km == 50

# distance1 = Distance(20)
# distance2 = distance1 + 10

# isinstance(distance2, Distance) == True
# distance2.km == 30
# both variants ^ are possible

# __iadd__
distance1 = Distance(20)
distance2 = Distance(30)
distance1 += distance2  # distance1.km == 50
print(distance1)
distance = Distance(20)
distance += 30
print(distance)  # distance.km == 50
