class Distance:
    def __init__(self, km: int) -> int:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        if isinstance(other, (int, float)):
            return Distance(self.km + other)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
            return self
        if isinstance(other, (int, float)):
            self.km += other
            return self

    def __mul__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(self.km * other)

    def __truediv__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))

    def __lt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        if isinstance(other, (int, float)):
            return self.km < other

    def __gt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        if isinstance(other, (int, float)):
            return self.km > other

    def __eq__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        if isinstance(other, (int, float)):
            return self.km == other

    def __le__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        if isinstance(other, (int, float)):
            return self.km <= other

    def __ge__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        if isinstance(other, (int, float)):
            return self.km >= other

# distance = Distance(20)
# print(distance)      # Вызовет __str__ и напечатает текст
# print(repr(distance)) # Вызовет __repr__ и напечатает строковое представление

# distance1 = Distance(20)
# distance2 = Distance(30)
# distance3 = distance1 + distance2
# print(distance3)

# distance1 = Distance(20)
# distance2 = distance1 + 10
# print(distance2)

# distance1 = Distance(20)
# distance2 = Distance(30)
# distance1 += distance2
# print(distance1)

# distance = Distance(20)
# distance += 30
# print(distance)

# distance1 = Distance(20)
# distance2 = distance1 * 5
# print(distance2)  # Должно вывести Distance: 100 kilometers.

# distance1 = Distance(20)
# distance2 = distance1 / 7
# print(distance2)

# distance = Distance(50)

# print(distance < Distance(60))   # Ожидаем True
# print(distance > Distance(120))  # Ожидаем False
# print(distance == Distance(100)) # Ожидаем False
# print(distance <= Distance(49))  # Ожидаем False
# print(distance >= Distance(50))  # Ожидаем True

# print(distance < 60)             # Ожидаем True
# print(distance > 120)            # Ожидаем False
