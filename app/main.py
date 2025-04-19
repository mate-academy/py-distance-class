class Distance:
    """
    Клас для представлення та управління відстанню в кілометрах.
    Підтримує арифметичні операції та порівняння.
    """

    def __init__(self, km: float) -> None:
        """
        Ініціалізує новий об'єкт Distance.

        Args:
            km: Значення відстані в кілометрах
        """
        self.km = km

    def __str__(self) -> str:
        """
        Повертає рядкове представлення об'єкта для друку.

        Returns:
            str: Рядок у форматі "Distance: X kilometers."
        """
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        """
        Повертає рядкове представлення об'єкта для розробника.

        Returns:
            str: Рядок у форматі "Distance(km=X)"
        """
        return f"Distance(km={self.km})"

    def __add__(self, other: object) -> "Distance":
        """
        Додає відстані або числа.

        Args:
            other: Інший об'єкт Distance або числове значення

        Returns:
            Distance: Новий об'єкт з сумою відстаней
        """
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        else:
            return NotImplemented

    def __iadd__(self, other: object) -> "Distance":
        """
        Збільшує поточну відстань на інший об'єкт Distance або число.

        Args:
            other: Інший об'єкт Distance або числове значення

        Returns:
            Distance: Поточний об'єкт зі зміненим значенням
        """
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            return NotImplemented
        return self

    def __mul__(self, other: object) -> "Distance":
        """
        Множить відстань на число.

        Args:
            other: Числовий множник

        Returns:
            Distance: Новий об'єкт з результатом множення
        """
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        else:
            return NotImplemented

    def __truediv__(self, other: object) -> "Distance":
        """
        Ділить відстань на число.

        Args:
            other: Числовий дільник

        Returns:
            Distance: Новий об'єкт з результатом ділення, округленим до 2 знаків
        """
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))
        else:
            return NotImplemented

    def __lt__(self, other: object) -> bool:
        """
        Перевіряє, чи відстань менша за іншу.

        Args:
            other: Інший об'єкт Distance або числове значення

        Returns:
            bool: True, якщо поточна відстань менша
        """
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other
        else:
            return NotImplemented

    def __gt__(self, other: object) -> bool:
        """
        Перевіряє, чи відстань більша за іншу.

        Args:
            other: Інший об'єкт Distance або числове значення

        Returns:
            bool: True, якщо поточна відстань більша
        """
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other
        else:
            return NotImplemented

    def __eq__(self, other: object) -> bool:
        """
        Перевіряє, чи відстань дорівнює іншій.

        Args:
            other: Інший об'єкт Distance або числове значення

        Returns:
            bool: True, якщо відстані рівні
        """
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other
        else:
            return NotImplemented

    def __le__(self, other: object) -> bool:
        """
        Перевіряє, чи відстань менша або дорівнює іншій.

        Args:
            other: Інший об'єкт Distance або числове значення

        Returns:
            bool: True, якщо поточна відстань менша або дорівнює
        """
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other
        else:
            return NotImplemented

    def __ge__(self, other: object) -> bool:
        """
        Перевіряє, чи відстань більша або дорівнює іншій.

        Args:
            other: Інший об'єкт Distance або числове значення

        Returns:
            bool: True, якщо поточна відстань більша або дорівнює
        """
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= other
        else:
            return NotImplemented
