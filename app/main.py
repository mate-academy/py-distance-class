from __future__ import annotations


class Distance:
    @staticmethod
    def get_km_value(obj: Distance | int | float) -> int | float | None:
        km = None

        if isinstance(obj, Distance):
            km = obj.km
        elif isinstance(obj, (int, float)):
            km = obj

        return km

    @staticmethod
    def get_operation_error(operation: str, other_type: type) -> str:
        return (
            "unsupported operand type(s) for "
            + f"{operation}: 'Distance' and {other_type}"
        )

    @staticmethod
    def get_comparison_error(comparison_sign: str, other_type: type) -> str:
        return (
            f'Operator "{comparison_sign}" '
            + 'not supported for types "Distance" and {other_type}'
        )

    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        other_km = self.get_km_value(other)

        if other_km is None:
            raise TypeError(self.get_operation_error("+", type(other)))

        return Distance(km=self.km + other_km)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        other_km = self.get_km_value(other)

        if other_km is None:
            raise TypeError(self.get_operation_error("+=", type(other)))

        self.km += other_km

        return self

    def __mul__(self, other: int | float) -> Distance:

        if isinstance(other, (int, float)):
            return Distance(km=self.km * other)

        raise TypeError(self.get_operation_error("*", type(other)))

    def __truediv__(self, other: int | float) -> Distance:

        if isinstance(other, (int, float)):
            return Distance(km=round(self.km / other, 2))

        raise TypeError(self.get_operation_error("/", type(other)))

    def __lt__(self, other: Distance | int | float) -> bool:
        other_km = self.get_km_value(other)

        if other_km is None:
            raise TypeError(self.get_comparison_error("<", type(other)))

        return self.km < other_km

    def __gt__(self, other: Distance | int | float) -> bool:
        other_km = self.get_km_value(other)

        if other_km is None:
            raise TypeError(self.get_comparison_error(">", type(other)))

        return self.km > other_km

    def __eq__(self, other: Distance | int | float) -> bool:
        other_km = self.get_km_value(other)

        if other_km is None:
            raise TypeError(self.get_comparison_error("==", type(other)))

        return self.km == other_km

    def __le__(self, other: Distance | int | float) -> bool:
        return self == other or self < other

    def __ge__(self, other: Distance | int | float) -> bool:
        return self == other or self > other
