from typing import Union, Any
import math

# Визначаємо тип, який може бути або Distance, або числом
DistanceOrNumber = Union['Distance', int, float]


class Distance:
    """
    Клас для зберігання та обробки відстаней у кілометрах,
    реалізує повний набір магічних методів.
    """

    def __init__(self, km: Union[int, float]):
        """
        Конструктор, що ініціалізує відстань у кілометрах.
        """
        self.km = km

    # --- 1. Представлення (Display) ---

    def __str__(self) -> str:
        """
        Повертає дружнє для читача рядкове представлення (для print()).
        """
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        """
        Повертає офіційне рядкове представлення (для debug).
        """
        return f"Distance(km={self.km})"

    # --- 2. Допоміжний метод для операцій ---

    @staticmethod
    def _get_km_value(other: DistanceOrNumber) -> Union[int, float]:
        """
        Витягує значення km з об'єкта Distance або повертає його, якщо це число.
        """
        if isinstance(other, Distance):
            return other.km
        return other

    # --- 3. Арифметичні операції ---

    def __add__(self, other: DistanceOrNumber) -> 'Distance':
        """
        Реалізує оператор додавання (+).
        Додає об'єкт Distance або число (int/float).
        """
        other_km = self._get_km_value(other)
        new_km = self.km + other_km
        return Distance(new_km)

    def __iadd__(self, other: DistanceOrNumber) -> 'Distance':
        """
        Реалізує оператор додавання з присвоєнням (+=).
        Модифікує поточний об'єкт.
        """
        other_km = self._get_km_value(other)
        self.km += other_km
        return self

    def __mul__(self, other: Union[int, float]) -> 'Distance':
        """
        Реалізує оператор множення (*).
        Множення на число (int/float).
        """
        new_km = self.km * other
        return Distance(new_km)

    def __truediv__(self, other: Union[int, float]) -> 'Distance':
        """
        Реалізує оператор ділення (/).
        Результат округлюється до 2 знаків після коми.
        """
        if other == 0 or (isinstance(other, Distance) and other.km == 0):
            raise ZeroDivisionError("Cannot divide by zero distance or number.")

        other_val = self._get_km_value(other)

        # Виконуємо ділення та округлюємо
        new_km = round(self.km / other_val, 2)
        return Distance(new_km)

    # --- 4. Оператори порівняння ---

    def __eq__(self, other: DistanceOrNumber) -> bool:
        """Реалізує оператор рівності (==)."""
        other_km = self._get_km_value(other)
        return self.km == other_km

    def __lt__(self, other: DistanceOrNumber) -> bool:
        """Реалізує оператор менше (<)."""
        other_km = self._get_km_value(other)
        return self.km < other_km

    def __gt__(self, other: DistanceOrNumber) -> bool:
        """Реалізує оператор більше (>)."""
        other_km = self._get_km_value(other)
        return self.km > other_km

    def __le__(self, other: DistanceOrNumber) -> bool:
        """Реалізує оператор менше або дорівнює (<=)."""
        other_km = self._get_km_value(other)
        return self.km <= other_km

    def __ge__(self, other: DistanceOrNumber) -> bool:
        """Реалізує оператор більше або дорівнює (>=)."""
        other_km = self._get_get_km_value(other)
        return self.km >= other_km


# --- Приклад використання та перевірки ---
print("--- Перевірка __str__ та __repr__ ---")
d_test = Distance(20)
print(d_test)
print(repr(d_test))

print("\n--- Перевірка __add__ (Distance + Distance) ---")
d1 = Distance(20)
d2 = Distance(30)
d3 = d1 + d2
print(f"d1 + d2 = {d3} ({isinstance(d3, Distance)})")  # 50.0

print("\n--- Перевірка __add__ (Distance + Number) ---")
d4 = d1 + 10
print(f"d1 + 10 = {d4} ({isinstance(d4, Distance)})")  # 30.0

print("\n--- Перевірка __iadd__ (+=) ---")
d5 = Distance(20)
d5 += Distance(30)
print(f"d5 += d2: {d5.km}")  # 50.0
d5 += 5
print(f"d5 += 5: {d5.km}")  # 55.0

print("\n--- Перевірка __mul__ (*) ---")
d6 = Distance(20)
d7 = d6 * 5
print(f"d6 * 5 = {d7} ({isinstance(d7, Distance)})")  # 100.0

print("\n--- Перевірка __truediv__ (/) ---")
d8 = Distance(20)
d9 = d8 / 7
print(f"d8 / 7 = {d9}")  # 2.86

print("\n--- Перевірка Порівняння ---")
d_comp = Distance(50)
print(f"d_comp < Distance(60): {d_comp < Distance(60)}")  # True
print(f"d_comp > 120: {d_comp > 120}")  # False
print(f"d_comp == 50: {d_comp == 50}")  # True