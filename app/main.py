class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    # Add -- +
    def __add__(self, value: "Distance | float | int") -> "Distance":
        if isinstance(value, float):
            return Distance(self.km + value)
        elif isinstance(value, Distance):
            return Distance(self.km + value.km)
        elif isinstance(value, int):
            return Distance(self.km + value)
        else:
            return NotImplemented

    # Add -- +=
    def __iadd__(self, value: "Distance | float | int") -> "Distance":
        if isinstance(value, Distance):
            self.km += value.km
        elif isinstance(value, float):
            self.km += value
        elif isinstance(value, int):
            self.km += value
        else:
            return NotImplemented
        return self

    # Multiply -- *
    def __mul__(self, value: "float | int") -> "Distance":
        if isinstance(value, float):
            return Distance(self.km * value)
        elif isinstance(value, int):
            return Distance(self.km * value)
        else:
            return NotImplemented

    # Divide -- /
    def __truediv__(self, value: "float | int") -> "Distance":
        if isinstance(value, float):
            return Distance(round(self.km / value, 2))
        elif isinstance(value, int):
            return Distance(round(self.km / value, 2))
        else:
            return NotImplemented

    # Less then -- <
    def __lt__(self, value: "Distance | float | int") -> "bool":
        if isinstance(value, float):
            return (self.km) < value
        elif isinstance(value, Distance):
            return (self.km) < value.km
        elif isinstance(value, int):
            return (self.km) < value
        else:
            return NotImplemented

    # Greater then -- >
    def __gt__(self, value: "Distance | float | int") -> "bool":
        if isinstance(value, float):
            return (self.km) > value
        elif isinstance(value, Distance):
            return (self.km) > value.km
        elif isinstance(value, int):
            return (self.km) > value
        else:
            return NotImplemented

    # Equal -- ==
    def __eq__(self, value: "Distance | float | int") -> "bool":
        if isinstance(value, float):
            return (self.km) == value
        elif isinstance(value, Distance):
            return (self.km) == value.km
        elif isinstance(value, int):
            return (self.km) == value
        else:
            return NotImplemented

    # Less equal than -- <=
    def __le__(self, value: "Distance | float | int") -> "bool":
        if isinstance(value, float):
            return (self.km) <= value
        elif isinstance(value, Distance):
            return (self.km) <= value.km
        elif isinstance(value, int):
            return (self.km) <= value
        else:
            return NotImplemented

    # Greater equal than -- >=
    def __ge__(self, value: "Distance | float | int") -> "bool":
        if isinstance(value, float):
            return (self.km) >= value
        elif isinstance(value, Distance):
            return (self.km) >= value.km
        elif isinstance(value, int):
            return (self.km) >= value
        else:
            return NotImplemented
