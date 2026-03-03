class Distance:
    """
    Клас для роботи з дистанцією в кілометрах.
    """

    def __init__(self, km: int) -> None:
        """
        Ініціалізує об'єкт Distance з кількістю кілометрів.

        :param km: Дистанція в кілометрах
        (ціле число або число з плаваючою точкою).

        """
        if not isinstance(km, (int, float)):
            raise TypeError("Distance must be a number (int or float).")
        if km < 0:
            raise ValueError("Distance cannot be negative.")
        self.km = km

    def __str__(self) -> str:
        """
        Повертає текстове представлення об'єкта для користувача.

        :return: Рядок виду 'Distance: {self.km} kilometers.'
        """
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        """
        Повертає технічне представлення об'єкта для розробників.

        :return: Рядок виду 'Distance(km={self.km})'.
        """
        return f"Distance(km={self.km})"

    def __add__(self, other: int) -> None:
        """
        Реалізує додавання Distance + Distance або Distance + число.

        :param other: Інший об'єкт Distance або число.
        :return: Новий об'єкт Distance.
        """
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        if isinstance(other, (int, float)):
            return Distance(self.km + other)
        raise TypeError("Unsupported type for addition.")

    def __iadd__(self, other: int) -> None:
        """
        Реалізує оператор += для Distance.

        :param other: Інший об'єкт Distance або число.
        :return: Поточний об'єкт Distance після додавання.
        """
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            raise TypeError("Unsupported type for in-place addition.")
        return self

    def __mul__(self, other: int) -> None:
        """
        Реалізує множення Distance на число.

        :param other: Число (int або float).
        :return: Новий об'єкт Distance після множення.
        """
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        raise TypeError("Distance can only be multiplied by a number.")

    def __truediv__(self, other: int) -> None:
        """
        Реалізує ділення Distance на число.

        :param other: Число (int або float).
        :return: Новий об'єкт Distance після ділення.
        """
        if isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            return Distance(round(self.km / other, 2))
        raise TypeError("Distance can only be divided by a number.")

    def __lt__(self, other: int) -> bool:
        """
        Реалізує оператор < для порівняння.

        :param other: Інший об'єкт Distance або число.
        :return: True, якщо поточний об'єкт менший.
        """
        if isinstance(other, Distance):
            return self.km < other.km
        if isinstance(other, (int, float)):
            return self.km < other
        raise TypeError("Unsupported type for comparison.")

    def __gt__(self, other: int) -> bool:
        """
        Реалізує оператор > для порівняння.

        :param other: Інший об'єкт Distance або число.
        :return: True, якщо поточний об'єкт більший.
        """
        if isinstance(other, Distance):
            return self.km > other.km
        if isinstance(other, (int, float)):
            return self.km > other
        raise TypeError("Unsupported type for comparison.")

    def __eq__(self, other: int) -> bool:
        """
        Реалізує оператор == для порівняння.

        :param other: Інший об'єкт Distance або число.
        :return: True, якщо об'єкти рівні.
        """
        if isinstance(other, Distance):
            return self.km == other.km
        if isinstance(other, (int, float)):
            return self.km == other
        raise TypeError("Unsupported type for comparison.")

    def __le__(self, other: int) -> bool:
        """
        Реалізує оператор <= для порівняння.

        :param other: Інший об'єкт Distance або число.
        :return: True, якщо поточний об'єкт менший або рівний.
        """
        if isinstance(other, Distance):
            return self.km <= other.km
        if isinstance(other, (int, float)):
            return self.km <= other
        raise TypeError("Unsupported type for comparison.")

    def __ge__(self, other: int) -> bool:
        """
        Реалізує оператор >= для порівняння.

        :param other: Інший об'єкт Distance або число.
        :return: True, якщо поточний об'єкт більший або рівний.
        """
        if isinstance(other, Distance):
            return self.km >= other.km
        if isinstance(other, (int, float)):
            return self.km >= other
        raise TypeError("Unsupported type for comparison.")
