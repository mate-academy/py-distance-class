class Distance:
    def __init__(self, km: float) -> None:
        self.km: float = float(km)

    def __str__(self) -> str:
        km_str = str(int(self.km)) if self.km.is_integer() else str(self.km)
        return f"Distance: {km_str} kilometers."

    def __repr__(self) -> str:
        km_str = str(int(self.km)) if self.km.is_integer() else str(self.km)
        return f"Distance(km={km_str})"

    def __add__(self, other: object) -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        try:
            return Distance(self.km + float(other))
        except (TypeError, ValueError):
            return NotImplemented

    def __iadd__(self, other: object) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        else:
            try:
                self.km += float(other)
            except (TypeError, ValueError):
                return NotImplemented
        return self

    def __mul__(self, other: object) -> "Distance":
        try:
            return Distance(self.km * float(other))
        except (TypeError, ValueError):
            return NotImplemented

    def __truediv__(self, other: object) -> "Distance":
        try:
            return Distance(round(self.km / float(other), 2))
        except (TypeError, ValueError, ZeroDivisionError):
            return NotImplemented

    def __lt__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        try:
            return self.km < float(other)
        except (TypeError, ValueError):
            return NotImplemented

    def __gt__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        try:
            return self.km > float(other)
        except (TypeError, ValueError):
            return NotImplemented

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        if isinstance(other, (int, float)):
            return self.km == float(other)
        return NotImplemented

    def __le__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        try:
            return self.km <= float(other)
        except (TypeError, ValueError):
            return NotImplemented

    def __ge__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        try:
            return self.km >= float(other)
        except (TypeError, ValueError):
            return NotImplemented
