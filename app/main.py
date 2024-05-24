from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, add_: int | float | Distance) -> Distance:
        if isinstance(add_, (int, float)):
            return Distance(self.km + add_)
        return Distance(self.km + add_.km)

    def __iadd__(self, iadd_: int | float | Distance) -> Distance:
        if isinstance(iadd_, (int, float)):
            self.km += iadd_
        else:
            self.km += iadd_.km
        return self

    def __mul__(self, mul_: int | float) -> Distance:
        if isinstance(mul_, (int, float)):
            return Distance(self.km * mul_)

    def __truediv__(self, div_: int | float) -> Distance:
        if isinstance(div_, (int, float)):
            return Distance(round(self.km / div_, 2))

    def __lt__(self, lt_: Distance | int | float) -> bool:
        if isinstance(lt_, Distance):
            return self.km < lt_.km
        if isinstance(lt_, (int, float)):
            return self.km < lt_

    def __gt__(self, gt_: Distance | int | float) -> bool:
        if isinstance(gt_, Distance):
            return self.km > gt_.km
        if isinstance(gt_, (int, float)):
            return self.km > gt_

    def __eq__(self, eq_: Distance | int | float) -> bool:
        if isinstance(eq_, Distance):
            return self.km == eq_.km
        if isinstance(eq_, (int, float)):
            return self.km == eq_

    def __le__(self, le_: Distance | int | float) -> bool:
        if isinstance(le_, Distance):
            return self.km <= le_.km
        if isinstance(le_, (int, float)):
            return self.km <= le_

    def __ge__(self, ge_: Distance | int | float) -> bool:
        if isinstance(ge_, Distance):
            return self.km >= ge_.km
        if isinstance(ge_, (int, float)):
            return self.km >= ge_
