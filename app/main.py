from __future__ import division
from typing import Any


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __add__(self, other: Any) -> Any:
        if not isinstance(other, Distance):
            return Distance(self.km + other)
        return Distance(self.km + other.km)

    def __iadd__(self, other: Any) -> Any:
        if not isinstance(other, Distance):
            self.km += other
            return self
        self.km += other.km
        return self

    def __mul__(self, other: Any) -> Any:
        return Distance(self.km * other)

    def __truediv__(self, other: Any) -> Any:
        return Distance(round((self.km / other), 2))

    def __lt__(self, other: Any) -> bool:
        return self.km < other

    def __gt__(self, other: Any) -> bool:
        return self.km > other

    def __eq__(self, other: Any) -> bool:
        return self.km == other

    def __le__(self, other: Any) -> bool:
        return self.km <= other

    def __ge__(self, other: Any) -> bool:
        return self.km >= other

# __init__
# distance = Distance(20)  # distance.km == 20
#
# __str__
# distance = Distance(20)
# print(distance)  # "Distance: 20 kilometers."
#
# __repr__
# distance = Distance(20)
# print(repr(distance))  # "Distance(km=20)"
#
# __add__
# distance1 = Distance(20)
# distance2 = Distance(30)
# distance3 = distance1 + distance2
# print(type(distance3))
# #
# print(isinstance(distance3, Distance)) # is True
# # # distance3.km == 50
#
# distance1 = Distance(20)
# distance2 = distance1 + 10
#
# print(isinstance(distance2, Distance)) #is True
# print(distance2.km) # == 30
# both variants ^ are possible
#
# __iadd__
# distance1 = Distance(20)
# distance2 = Distance(30)
# distance1 += distance2  # distance1.km is 50
#
# distance = Distance(20)
# distance += 30  # distance.km == 50
# print(distance1)
# print(distance)

#
# __mul__
# distance1 = Distance(20)
# distance2 = distance1 * 5
#
# print(isinstance(distance2, Distance)) # is True
# print(distance2.km) # == 100
#
# __truediv__
# distance1 = Distance(20)
# distance2 = distance1 / 7
#
# print(isinstance(distance2, Distance)) #is True
# print(distance2.km) # == 2.85
# Note: rounded to 2 decimals
#
# __lt__, __gt__, __eq__, __le__, __ge__
# distance = Distance(50)
# print(distance < Distance(60))  # True  # distance.km < 60 == True
# print(distance > Distance(120))  # False
# print(distance == Distance(100))  # False
# print(distance <= Distance(49))  # False
# print(distance >= Distance(50))  # True
#
# print(distance < 60)  # True  # distance.km < 60 == True
# print(distance > 120)  # False
# print(distance == 100)  # False
# print(distance <= 49)  # False
# print(distance >= 50)  # True
