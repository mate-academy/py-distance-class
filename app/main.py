from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, added: int | float | Distance) -> Distance:
        if isinstance(added, (int, float)):
            return Distance(self.km + added)
        return Distance(self.km + added.km)

    def __iadd__(self, added: int | float | Distance) -> Distance:
        if isinstance(added, (int, float)):
            self.km += added
        else:
            self.km += added.km
        return self

    def __mul__(self, multiplier: int | float) -> Distance:
        if isinstance(multiplier, (int, float)):
            return Distance(self.km * multiplier)

    def __truediv__(self, divider: int | float) -> Distance:
        if divider == 0:
            raise ZeroDivisionError("You can't divide by zero")
        if isinstance(divider, (int, float)) and divider != 0:
            return Distance(round(self.km / divider, 2))

### __lt__ <, __gt__ >, __eq__ =, __le__ <=, __ge__ >=

    def __lt__(self, other: int | float | Distance) -> bool:
        if isinstance(other, (int, float)):
            return self.km < other
        return self.km < other.km

    def __gt__(self, other: int | float | Distance) -> bool:
        if isinstance(other, (int, float)):
            return self.km > other
        return self.km > other.km

    def __eq__(self, other: int | float | Distance) -> bool:
        if isinstance(other, (int, float)):
            return self.km == other
        return self.km == other.km

    def __le__(self, other: int | float | Distance) -> bool:
        if isinstance(other, (int, float)):
            return self.km <= other
        return self.km <= other.km

    def __ge__(self, other: int | float | Distance) -> bool:
        if isinstance(other, (int, float)):
            return self.km >= other
        return self.km >= other.km


### My Debuger
"""
# __add__
distance1 = Distance(20)
distance2 = Distance(30)
distance3 = distance1 + distance2
print(distance3)            # distance3.km == 50

# __iadd__
distance1 = Distance(20)
distance2 = Distance(30)
distance1 += distance2      # distance1.km is 50
print(distance1)

distance = Distance(20)
distance += 30              # distance.km == 50
print(distance)


distance = Distance(50)

print(distance < 60)  # True  # distance.km < 60 == True
print(distance > 120)  # False
print(distance == 100)  # False
print(distance <= 49)  # False
print(distance >= 50.1)  # True

print(distance < Distance(60))  # True  # distance.km < 60 == True
print(distance > Distance(120))  # False
print(distance == Distance(100))  # False
print(distance <= Distance(49))  # False
print(distance >= Distance(50))  # True

# __str__
distance = Distance(20)
print(distance)             # "Distance: 20 kilometers."

# __repr__
distance = Distance(20)
print(repr(distance))       # "Distance(km=20)"

distance1 = Distance(20)
distance2 = distance1 + 10.5
print(distance2)            # distance2.km == 30
                            # both variants ^ are possible

# __mul__
distance1 = Distance(20)
distance2 = distance1 * 5.2
print(distance2)            # distance2.km == 100

# __truediv__
distance1 = Distance(20)
distance2 = distance1 / 7.7
print(distance2)            # distance2.km == 2.85
"""
