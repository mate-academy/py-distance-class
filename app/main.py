from __future__ import annotations


class Distance:

    def __eq__(self, other: Distance | float | int) -> bool:
        if isinstance(other, Distance):
            if self.km != other.km:
                return False
        if self.km != other:
            return False
        return True

    def __ge__(self, other: Distance | float | int) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        return self.km >= other

    def __le__(self, other: Distance | float | int) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        return self.km <= other

    def __gt__(self, other: Distance | float | int) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        return self.km > other

    def __lt__(self, other: Distance | float | int) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        return self.km < other

    def __truediv__(self, other: float | int) -> float:
        return Distance(round(self.km / other, 2))

    def __mul__(self, other: float | int) -> float:
        return Distance(round(self.km * other, 3))

    def __iadd__(self, other: Distance | float | int) -> Distance:
        if isinstance(other, Distance):
            self.km = self.km + other.km
            return self
        self.km = self.km + other
        return self

    def __add__(self, other: Distance | float | int) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        return Distance(self.km + other)

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __init__(self, km: float) -> Distance:
        self.km = km


distance = Distance(20)  # distance.km == 20
print(distance.km)
print(distance)
print(repr(distance))

distance1 = Distance(20)
distance2 = Distance(30)
distance3 = distance1 + distance2

isinstance(distance3, Distance) is True
print(distance3)
print(distance3.km == 50)


distance1 = Distance(20)
distance2 = distance1 + 10

print(isinstance(distance2, Distance) is True)
print(distance2.km == 30)
# both variants ^ are possible

distance1 = Distance(20)
distance2 = Distance(30)
distance1 += distance2  # distance1.km is 50
print(distance1)

distance = Distance(20)
distance += 30  # distance.km == 50
print(distance)

distance1 = Distance(20)
distance2 = distance1 * 5

print(isinstance(distance2, Distance) is True)
print(distance2.km == 100)

distance1 = Distance(20)
distance2 = distance1 / 7
print(distance2.km)
print(isinstance(distance2, Distance) is True)
print(distance2.km == 2.85)
# Note: rounded to 2 decimals


print("compare")
distance = Distance(50)
print(distance < Distance(60))  # True  # distance.km < 60 == True
print(distance > Distance(120))  # False
print(distance == Distance(100))  # False
print(distance <= Distance(49))  # False
print(distance >= Distance(50))  # True

print(distance < 60)  # True  # distance.km < 60 == True
print(distance > 120)  # False
print(distance == 100)  # False
print(distance <= 49)  # False
print(distance >= 50)  # True


distance1 = Distance(21.4)
distance2 = distance1 * 5.88

print(distance2)
print(isinstance(distance2, Distance) is True)
print(distance2.km == 100)
