from __future__ import annotations


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        return Distance(self.km + other)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
            return self
        self.km += other
        return self

    def __mul__(self, number: int | float) -> Distance:
        return Distance(self.km * number)

    def __truediv__(self, number: int | float) -> Distance:
        return Distance(round(self.km / number, 2))

    def __lt__(self, other: int | float | Distance) -> bool:
        if isinstance(other, Distance):
            if self.km < other.km:
                return True
            return False
        if self.km < other:
            return True
        return False

    def __gt__(self, other: int | float | Distance) -> bool:
        if isinstance(other, Distance):
            if self.km > other.km:
                return True
            return False
        if self.km > other:
            return True
        return False

    def __eq__(self, other: int | float | Distance) -> bool:
        if isinstance(other, Distance):
            if self.km == other.km:
                return True
            return False
        if self.km == other:
            return True
        return False

    def __le__(self, other: int | float | Distance) -> bool:
        if isinstance(other, Distance):
            if self.km <= other.km:
                return True
            return False
        if self.km <= other:
            return True
        return False

    def __ge__(self, other: int | float | Distance) -> bool:
        if isinstance(other, Distance):
            if self.km >= other.km:
                return True
            return False
        if self.km >= other:
            return True
        return False


# test = Distance(20)
# test += 5
# print(test)

kilometers = 50.2655
kilometers2 = 15.0
result = 65
distance1 = Distance(kilometers)
instance_1 = distance1
distance1 += kilometers2
instance_2 = distance1
print(instance_2)

# print(test)
# print(repr(test))
#
# print(test + Distance(10))
# print(test + 50)

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
