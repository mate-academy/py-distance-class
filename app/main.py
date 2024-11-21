from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __add_eval_value__(self, simbl: str,
                           value: Distance | int | float
                           ) -> int | float | bool:
        if isinstance(value, Distance):
            return eval(f"{self.km} {simbl} {value.km}")
        return eval(f"{self.km} {simbl} {value}")

    def __str__(self) -> str:
        return f"{Distance.__name__}: {self.km} kilometers."

    def __repr__(self) -> str:
        item = self.__dict__.items()
        for key, value in item:
            return f"{Distance.__name__}({key}={value})"

    def __add__(self, other: Distance | int | float) -> Distance:
        return Distance(self.__add_eval_value__(simbl="+",
                                                value=other))

    def __iadd__(self, other: Distance | int | float) -> Distance:
        self.km = self.__add_eval_value__(simbl="+",
                                          value=other)
        return self

    def __mul__(self, value: int | float) -> Distance:
        return Distance(round(self.km * value, 3))

    def __truediv__(self, value: int | float) -> Distance:
        return Distance(round(self.km / value, 2))

    def __lt__(self, other: Distance | int | float) -> bool:
        return self.__add_eval_value__(simbl="<", value=other)

    def __gt__(self, other: Distance | int | float) -> bool:
        return self.__add_eval_value__(simbl=">", value=other)

    def __eq__(self, other: Distance | int | float) -> bool:
        return self.__add_eval_value__(simbl="==", value=other)

    def __le__(self, other: Distance | int | float) -> bool:
        return self.__add_eval_value__(simbl="<=", value=other)

    def __ge__(self, other: Distance | int | float) -> bool:
        return self.__add_eval_value__(simbl=">=", value=other)
