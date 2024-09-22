from typing import Any


class Distance:
    def __init__(self, km: int or float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Any) -> Any:
        if isinstance(other, Distance):
            return Distance(km=self.km + other.km)

        if isinstance(other, int) or isinstance(other, float):
            return Distance(km=self.km + other.real)

    def __iadd__(self, other: Any) -> Any:
        if isinstance(other, Distance):
            self.km += other.km
            return self
        if isinstance(other, int) or isinstance(other, float):
            self.km += other.real
            return self

    def __mul__(self, other: Any) -> Any:
        if isinstance(other, int) or isinstance(other, float):
            return Distance(km=self.km * other.real)

    def __truediv__(self, other: Any) -> Any:
        if isinstance(other, int) or isinstance(other, float):
            return Distance(km=round(self.km / other.real, 2))

    def __lt__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            if self.km < other.km:
                return True

            return False

        if isinstance(other, int) or isinstance(other, float):
            if self.km < other.real:
                return True

            return False

    def __gt__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            if self.km > other.km:
                return True

            return False

        if isinstance(other, int) or isinstance(other, float):
            if self.km > other.real:
                return True

            return False

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            if self.km == other.km:
                return True

            return False

        if isinstance(other, int) or isinstance(other, float):
            if self.km == other.real:
                return True

            return False

    def __le__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            if self.km <= other.km:
                return True

            return False

        if isinstance(other, int) or isinstance(other, float):
            if self.km <= other.real:
                return True

            return False

    def __ge__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            if self.km >= other.km:
                return True

            return False

        if isinstance(other, int) or isinstance(other, float):
            if self.km >= other.real:
                return True

            return False


# distance = Distance(20)
# print("Distance(20):", Distance(20))
# print("distance.km:", distance.km)
# print("distance:", distance)
# print("str(distance):", str(distance))
# print("distance.__str__():", distance.__str__())
# print("distance.__repr__():", distance.__repr__())

# distance1 = Distance(20)
# distance2 = Distance(30)
# distance3 = distance1 + distance2
# print(isinstance(distance3, Distance)) # is True
# print(distance3.km)  # == 50


# distance1 = Distance(20)
# distance2 = distance1 + 10
# distance2 = distance1 + 3.5
# print(distance2.km)
# print(dir(distance1))

# __iadd__
# distance1 = Distance(20)
# distance2 = Distance(30)
# distance1 += distance2  # distance1.km is 50
# print(distance1)
# print(distance1.km is 50)
# print(distance1.km == 50)

# distance = Distance(20)
# distance += 30  # distance.km == 50
# print(distance)
# print(distance.km)

# __mul__
# distance1 = Distance(20)
# distance2 = Distance(30)
# distance3 = distance1 * distance2
# print(distance3)
# distance2 = distance1 * 5
# print(distance2)
# print(isinstance(distance2, Distance)) # is True
# print(distance2.km) # == 100

# __truediv__
# distance1 = Distance(20)
# distance2 = distance1 / 7
#
# print(isinstance(distance2, Distance)) # is True
# print(distance2.km) # == 2.85
# Note: rounded to 2 decimals

# __lt__, __gt__, __eq__, __le__, __ge__
# distance = Distance(50)
#
# print(distance < Distance(60))  # True  # distance.km < 60 == True
# print(distance > Distance(120))  # False
# print(distance == Distance(100))  # False
# print(distance <= Distance(49))  # False
# print(distance >= Distance(50))  # True
#
# print(distance < 60)  # True  # distance.km < 60 == True
# print(distance > 120 ) # False
# print(distance == 100 ) # False
# print(distance <= 49)  # False
# print(distance >= 50 ) # True
