class Distance:
    def __init__(self, km: int):
        self.km = km

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, other):
        if not isinstance(other, (int, Distance)):
            raise ArithmeticError("The operand must be an object of type 'int' or 'Distance'")

        return Distance(self.km + other.km)

    def __iadd__(self, other):
        if not isinstance(other, (int, Distance)):
            raise ArithmeticError("The operand must be an object of type 'int' or 'Distance'")

        sc = other if isinstance(other, int) else other.km
        self.km += sc

        return self

    def __mul__(self, other):
        if not isinstance(other, (int, Distance)):
            raise ArithmeticError("The operand must be an object of type 'int' or 'Distance'")

        return Distance(self.km * other.km)

    def __truediv__(self, other):
        if not isinstance(other, (int, Distance)):
            raise ArithmeticError("The operand must be an object of type 'int' or 'Distance'")

        return Distance(self.km / other.km)

    def __lt__(self, other):
        if not isinstance(other, (int, Distance)):
            raise ArithmeticError("The operand must be an object of type 'int' or 'Distance'")

    def __gt__(self, other):
        if not isinstance(other, (int, Distance)):
            raise ArithmeticError("The operand must be an object of type 'int' or 'Distance'")

    def __eq__(self, other):
        if not isinstance(other, (int, Distance)):
            raise ArithmeticError("The operand must be an object of type 'int' or 'Distance'")

    def __le__(self, other):
        if not isinstance(other, (int, Distance)):
            raise ArithmeticError("The operand must be an object of type 'int' or 'Distance'")

    def __ge__(self, other):
        if not isinstance(other, (int, Distance)):
            raise ArithmeticError("The operand must be an object of type 'int' or 'Distance'")

    def __len__(self):
        ...


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
print(distance) # distance.km == 50