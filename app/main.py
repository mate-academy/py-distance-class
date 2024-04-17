class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, other, distance=None):
        return distance = distance1 + distance2

    # isinstance(distance3, Distance) is True
    # distance3.km == 50

    distance1 = Distance(20)
    distance2 = distance1 + 10

    # isinstance(distance2, Distance) is True
    # distance2.km == 30
    # both variants ^ are possible

    __iadd__
    distance1 = Distance(20)
    distance2 = Distance(30)
    distance1 += distance2  # distance1.km is 50

    distance = Distance(20)
    distance += 30  # distance.km == 50

    __mul__
    distance1 = Distance(20)
    distance2 = distance1 * 5

    # isinstance(distance2, Distance) is True
    # distance2.km == 100

    __truediv__
    distance1 = Distance(20)
    distance2 = distance1 / 7

    # isinstance(distance2, Distance) is True
    # distance2.km == 2.85
    # Note: rounded to 2 decimals

    __lt__, __gt__, __eq__, __le__, __ge__
    distance = Distance(50)
    distance < Distance(60)  # True  # distance.km < 60 == True
    distance > Distance(120)  # False
    distance == Distance(100)  # False
    distance <= Distance(49)  # False
    distance >= Distance(50)  # True

    distance < 60  # True  # distance.km < 60 == True
    distance > 120  # False
    distance == 100  # False
    distance <= 49  # False
    distance >= 50  # True
