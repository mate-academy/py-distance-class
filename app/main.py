from typing import Optional


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __repr__(self)-> str:
        return f"Distance(km={self.km})"
    def __str__(self)-> str:
        return f"Distance: {self.km} kilometers"
    def __add__(self, other) -> "Distance":
        if isinstance(other, Distance):
            return Distance(km=self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(km=self.km + other)
        else:
            raise TypeError(f"Unsupported operand type(s) for +: 'Distance' and '{type(other).__name__}')")
    def __mul__(self, other) -> "Distance":
        if isinstance(other, Distance):
            return Distance(km=self.km * other.km)
        elif isinstance(other, (int, float)):
            return Distance(km=self.km * other)
        else:
            raise TypeError(f"Unsupported operand type(s) for *: 'Distance' and '{type(other).__name__}')")

    def __truediv__(self, other) -> "Distance":
        if isinstance(other, Distance):
            return Distance(km=round(self.km / other.km, 2))
        elif isinstance(other, (int, float)):
            return Distance(km=round(self.km / other, 2))
        else:
            raise TypeError(f"Unsupported operand type(s) for /: 'Distance' and '{type(other).__name__}'")

    # __lt__, __gt__, __eq__, __le__, __ge__
    def __lt__(self, other) -> Optional[bool]:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other


    def __gt__(self, other)-> Optional[bool]:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other
    def __le__(self, other)-> Optional[bool]:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other
    def __ge__(self, other)-> Optional[bool]:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= other
    def __eq__(self, other)-> Optional[bool]:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other

#__init__
distance = Distance(20)  # distance.km == 20
print(distance)
# __str__
distance = Distance(20)
print(distance)  # "Distance: 20 kilometers."

# __repr__
distance = Distance(20)
print(repr(distance))  # "Distance(km=20)"

# __add__
distance1 = Distance(20)
distance2 = Distance(30)
distance3 = distance1 + distance2
print(distance3)
print(isinstance(distance3, Distance))# is True
# distance3.km == 50

distance1 = Distance(20)
distance2 = distance1 + 10
print(distance2)
print(isinstance(distance2, Distance))# is True
# distance2.km == 30
# both variants ^ are possible

#__iadd__
distance1 = Distance(20)
distance2 = Distance(30)
distance1 += distance2  # distance1.km is 50

distance = Distance(20)
distance += 30  #
print(distance.km)# == 50

#__mul__
distance1 = Distance(20)
distance2 = distance1 * 5

print(isinstance(distance2, Distance))# is True
print(distance2.km) #== 100

#__truediv__
distance1 = Distance(20)
distance2 = distance1 / 7

# isinstance(distance2, Distance) is True
# distance2.km == 2.85
# Note: rounded to 2 decimals

#__lt__, __gt__, __eq__, __le__, __ge__
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
