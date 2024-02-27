from __future__ import annotations


class Distance:
    # ініціалізація об'єкта класу
    def __init__(self, km: int) -> None:
        self.km = km

    # представлення у зручному для людини форматі
    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    # формат для відтворення у новому об'єкті з тими ж властивостями
    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    # дозволяє додавати до об'єкта відстань і зберігати результат
    def __add__(self, other: int | float | Distance) -> callable:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        else:
            raise TypeError("Unsupported operand type(s) "
                            "for +: 'Distance' and '{}'".format(type(other)))

    # Цей метод реалізує операцію += для об'єктів Distance
    def __iadd__(self, other: int | float) -> callable:
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            raise TypeError("Unsupported operand type(s) "
                            "for +=: 'Distance' and '{}'".format(type(other)))
        return self

    # множення на скаляр
    def __mul__(self, scalar: int | float) -> callable:
        return Distance(self.km * scalar)

    # ділення з округленням
    def __truediv__(self, scalar: int | float) -> callable:
        return Distance(round(self.km / scalar, 2))

    # Порівнює поточну відстань з other "<"
    def __lt__(self, other: int | float) -> callable:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other
        else:
            raise TypeError("Unsupported operand type(s) "
                            "for <: 'Distance' and '{}'".format(type(other)))

    # Порівнює поточну відстань з other ">"
    def __gt__(self, other: int | float) -> callable:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other
        else:
            raise TypeError("Unsupported operand type(s) "
                            "for >: 'Distance' and '{}'".format(type(other)))

    # Порівнює поточну відстань з other "="
    def __eq__(self, other: int | float) -> int | str:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other
        else:
            raise TypeError("Unsupported operand type(s) "
                            "for ==: 'Distance' and '{}'".format(type(other)))

    # Порівнює поточну відстань з other "<="
    def __le__(self, other: int | float) -> int | float | str:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other
        else:
            raise TypeError("Unsupported operand type(s) "
                            "for <=: 'Distance' and '{}'".format(type(other)))

    # Порівнює поточну відстань з other ">="
    def __ge__(self, other: int | float) -> callable:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= other
        else:
            raise TypeError("Unsupported operand type(s) "
                            "for >=: 'Distance' and '{}'".format(type(other)))
