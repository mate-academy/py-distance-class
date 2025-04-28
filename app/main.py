from typing import Union, Callable
from types import NotImplementedType
import operator


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def _operation_arithmetic(self,
                              other: Union[int, float, "Distance"],
                              oper: Callable[[float, float], float]
                              ) -> Union["Distance", NotImplementedType]:
        if isinstance(other, (float, int)):
            return Distance(oper(self.km, other))
        elif isinstance(other, Distance):
            return Distance(oper(self.km, other.km))
        else:
            return NotImplemented

    def _operation_arithmetic_locked(self,
                                     other: Union[int, float],
                                     oper: Callable[[float, float], float]
                                     ) -> (
            Union)["Distance", NotImplementedType]:
        if oper is operator.mul:
            if isinstance(other, (int, float)):
                return Distance(oper(self.km, other))
            else:
                return NotImplemented
        elif oper is operator.truediv:
            if isinstance(other, (int, float)):
                return Distance(round(oper(self.km, other), 2))
            else:
                return NotImplemented
        else:
            raise ValueError("Operator not supported")

    def _operation_logic(self,
                         other: Union[int, float, "Distance"],
                         oper: Callable[[float, float], float]
                         ) -> Union[bool, NotImplementedType]:
        if isinstance(other, (int, float)):
            return oper(self.km, other)
        elif isinstance(other, Distance):
            return oper(self.km, other.km)
        else:
            return NotImplemented

    def __add__(self,
                other: Union[int, float, "Distance"]
                ) -> Union["Distance", NotImplementedType]:
        return self._operation_arithmetic(other, operator.add)

    def __iadd__(self,
                 other: Union[int, float, "Distance"]
                 ) -> Union["Distance", NotImplementedType]:
        if isinstance(other, (int, float)):
            self.km += other
        elif isinstance(other, Distance):
            self.km += other.km
        else:
            return NotImplemented
        return self

    def __mul__(self,
                other: Union[int, float]
                ) -> Union["Distance", NotImplementedType]:
        return self._operation_arithmetic_locked(other, operator.mul)

    def __truediv__(self,
                    other: Union[int, float]
                    ) -> Union["Distance", NotImplementedType]:
        return self._operation_arithmetic_locked(other, operator.truediv)

    def __lt__(self,
               other: Union[int, float, "Distance"]
               ) -> Union[bool, NotImplementedType]:
        return self._operation_logic(other, operator.lt)

    def __gt__(self,
               other: Union[int, float, "Distance"]
               ) -> Union[bool, NotImplementedType]:
        return self._operation_logic(other, operator.gt)

    def __eq__(self,
               other: Union[int, float, "Distance"]
               ) -> Union[bool, NotImplementedType]:
        return self._operation_logic(other, operator.eq)

    def __le__(self,
               other: Union[int, float, "Distance"]
               ) -> Union[bool, NotImplementedType]:
        return self._operation_logic(other, operator.le)

    def __ge__(self,
               other: Union[int, float, "Distance"]
               ) -> Union[bool, NotImplementedType]:
        return self._operation_logic(other, operator.ge)
