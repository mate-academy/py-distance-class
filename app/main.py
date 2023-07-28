from typing import Union    # we use "Union" to indicate that the parameter can receive different data types


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union["Distance", int]) -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        # In the 15th and 17th lines: handles the addition of two Distance instances or Distance with an int or float.

    def __iadd__(self, other: Union["Distance", int]) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km  # Modifies the current Distance instance by adding the other distance.
        elif isinstance(other, (int, float)):
            self.km += other
        return self

    def __mul__(self, other: Union[int, float]) -> "Distance":
        if isinstance(other, (int, float)):   # Handles the multiplication of a Distance instance with an int or float.
            return Distance(self.km * other)
        # Returns a new Distance instance with the product of distance and the number.

    def __truediv__(self, number: Union[int, float]) -> "Distance":
        if isinstance(number, (int, float)):
            new_distance = self.km / number
            return Distance(round(new_distance, 2))
        # Returns a new Distance instance with the result of distance divided by the number.

    def __eq__(self, other: Union["Distance", int]) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other
        # Returns True if the distance of the current instance is equal to the other, False otherwise.

    def __lt__(self, other: Union["Distance", int]) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other
        # Compares the distance of two Distance instances.
        # Returns True if the distance of the current instance is less than the other, False otherwise.

    def __gt__(self, other: Union["Distance", int]) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other
        # Returns True if the distance of the current instance is greater than the other, False otherwise.

    def __le__(self, other: Union["Distance", int]) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other
        # Returns True if the distance of the current instance is less than or equal to the other, False otherwise.

    def __ge__(self, other: Union["Distance", int]) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= other
        # Returns True if the distance of the current instance is greater than or equal to the other, False otherwise.
