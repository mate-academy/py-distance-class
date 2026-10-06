from __future__ import annotations

class Distance:
    def __init__(self, km) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __iadd__(self, element: Distance | int):
        if isinstance(element, Distance):
            self.km += element.km
            return self
        elif isinstance(element, (int, float)):
            self.km += element
            return self
        
    def __mul__(self, element: Distance | int) -> Distance:
        if isinstance(element, (int, float)):
            return Distance(self.km * element)

    def __add__(self, element: Distance | int) -> Distance:
        if isinstance(element, Distance):
            return Distance(self.km + element.km)
        elif isinstance(element, (int, float)):
            return Distance(self.km + element)

    def __truediv__(self, element: Distance | int) -> Distance:
        if isinstance(element, (int, float)):
            return Distance(round(self.km / element, 2))

    def __lt__(self, element: Distance | int) -> bool:
        if isinstance(element, Distance):
            return self.km < element.km
        if isinstance(element, (int, float)):
            return self.km < element

    def __le__(self, element: Distance | int) -> bool:
        if isinstance(element, Distance):
            return self.km <= element.km
        if isinstance(element, (int, float)):
            return self.km <= element

    def __eq__(self, element: Distance | int) -> bool:
        if isinstance(element, Distance):
            return self.km == element.km
        if isinstance(element, (int, float)):
            return self.km == element

    def __gt__(self, element: Distance | int) -> bool:
        if isinstance(element, Distance):
            return self.km > element.km
        if isinstance(element, (int, float)):
            return self.km > element

    def __ge__(self, element: Distance | int | float) -> bool:
        if isinstance(element, Distance):
            return self.km >= element.km
        if isinstance(element, (int, float)):
            return self.km >= element
    