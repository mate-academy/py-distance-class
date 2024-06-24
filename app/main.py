from __future__ import annotations
#


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, addends: Distance | int | float) -> Distance:
        if isinstance(addends, int | float):
            return Distance(self.km + addends)

        return Distance(self.km + addends.km)

    def __iadd__(self, addends: Distance | int | float) -> Distance:
        if isinstance(addends, int | float):
            self.km = self.km + addends
            return self

        self.km = self.km + addends.km
        return self

    def __mul__(self, multiplier: int | float) -> Distance:
        return Distance(self.km * multiplier)

    def __truediv__(self, divisor: int | float) -> Distance:
        return Distance(round(self.km / divisor, 2))

    @staticmethod
    def compare_objs(
            inst: Distance,
            comp_obj: Distance | int | float,
            operation_type: str
    ) -> bool:
        curr_inst_value = inst.km
        comp_value = None

        if isinstance(comp_obj, int | float):
            comp_value = comp_obj
        else:
            comp_value = comp_obj.km

        operations = {
            "lt": curr_inst_value < comp_value,
            "gt": curr_inst_value > comp_value,
            "eq": curr_inst_value == comp_value,
            "le": curr_inst_value <= comp_value,
            "ge": curr_inst_value >= comp_value,
        }

        return operations.get(operation_type)

    def __lt__(self, obj: Distance | int | float) -> bool:
        return Distance.compare_objs(self, obj, "lt")

    def __gt__(self, obj: Distance | int | float) -> bool:
        return Distance.compare_objs(self, obj, "gt")

    def __eq__(self, obj: Distance | int | float) -> bool:
        return Distance.compare_objs(self, obj, "eq")

    def __le__(self, obj: Distance | int | float) -> bool:
        return Distance.compare_objs(self, obj, "le")

    def __ge__(self, obj: Distance | int | float) -> bool:
        return Distance.compare_objs(self, obj, "ge")
