class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, distance_in_km: "Distance | int") -> "Distance":
        return Distance(self.km + self.check_instamce(distance_in_km))

    def __iadd__(self, distance_in_km: "Distance | int") -> "Distance":
        self.km += self.check_instamce(distance_in_km)
        return self

    def __mul__(self, multiplication_factor: int | float) -> "Distance":
        return Distance(self.km * multiplication_factor)

    def __truediv__(self, division_factor: int | float) -> "Distance":
        return Distance(round(self.km / division_factor, 2))

    def __lt__(self, value_in_km: "Distance | int | float") -> bool:
        return self.km < self.check_instamce(value_in_km)

    def __gt__(self, value_in_km: "Distance | int | float") -> bool:
        return self.km > self.check_instamce(value_in_km)

    def __eq__(self, value_in_km: "Distance | int | float") -> bool:
        return self.km == self.check_instamce(value_in_km)

    def __le__(self, value_in_km: "Distance | int | float") -> bool:
        return self.km <= self.check_instamce(value_in_km)

    def __ge__(self, value_in_km: "Distance | int | float") -> bool:
        return self.km >= self.check_instamce(value_in_km)

    @staticmethod
    def check_instamce(item: "Distance | int | float") -> int:
        return item.km if isinstance(item, Distance) else item
