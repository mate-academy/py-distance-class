class Distance:
    def __init__(self, km: "int | float") -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    # Add -- +
    def __add__(self, value: "Distance | float | int") -> "Distance":
        if isinstance(value, Distance):
            return Distance(self.km + value.km)
        if isinstance(value, (int, float)):
            return Distance(self.km + value)
        return NotImplemented

    # Add -- +=
    def __iadd__(self, value: "Distance | float | int") -> "Distance":
        if isinstance(value, Distance):
            self.km += value.km
        elif isinstance(value, (float, int)):
            self.km += value
        else:
            return NotImplemented
        return self

    # Multiply -- *
    def __mul__(self, value: "float | int") -> "Distance":
        if isinstance(value, (float, int)):
            return Distance(self.km * value)
        return NotImplemented

    # Divide -- /
    def __truediv__(self, value: "float | int") -> "Distance":
        if isinstance(value, (float, int)):
            return Distance(round(self.km / value, 2))
        return NotImplemented

    # Less then -- <
    def __lt__(self, value: "Distance | float | int") -> "bool":
        if isinstance(value, Distance):
            return (self.km) < value.km
        if isinstance(value, (float, int)):
            return (self.km) < value
        return NotImplemented

    # Greater then -- >
    def __gt__(self, value: "Distance | float | int") -> "bool":
        if isinstance(value, Distance):
            return (self.km) > value.km
        if isinstance(value, (float, int)):
            return (self.km) > value
        return NotImplemented

    # Equal -- ==
    def __eq__(self, value: "Distance | float | int") -> "bool":
        if isinstance(value, Distance):
            return (self.km) == value.km
        if isinstance(value, (float, int)):
            return (self.km) == value
        return NotImplemented

    # Less equal than -- <=
    def __le__(self, value: "Distance | float | int") -> "bool":
        if isinstance(value, Distance):
            return (self.km) <= value.km
        if isinstance(value, (float, int)):
            return (self.km) <= value
        return NotImplemented

    # Greater equal than -- >=
    def __ge__(self, value: "Distance | float | int") -> "bool":
        if isinstance(value, Distance):
            return (self.km) >= value.km
        if isinstance(value, (float, int)):
            return (self.km) >= value
        return NotImplemented
