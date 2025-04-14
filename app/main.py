class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __add__(self, km_of_the_day: callable) -> callable:
        return Distance(
            self.km + km_of_the_day.km
        )

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __iadd__(self, km_of_the_day: callable) -> callable:
        return Distance(
            self.km + km_of_the_day.km
        )

    def __mul__(self, num: float) -> callable:
        return Distance(
            self.km * num
        )

    def __truediv__(self, num: float) -> callable:
        return Distance(
            round(self.km / num, 2)
        )

    def __lt__(self, km_compara: callable) -> bool:
        if isinstance(km_compara, Distance):
            return self.km < km_compara.km
        return self.km < km_compara

    def __gt__(self, km_compara: callable) -> bool:
        if isinstance(km_compara, Distance):
            return self.km > km_compara.km
        return self.km > km_compara

    def __eq__(self, km_compara: callable) -> bool:
        if isinstance(km_compara, Distance):
            return self.km == km_compara.km
        return self.km == km_compara

    def __le__(self, km_compara: callable) -> bool:
        if isinstance(km_compara, Distance):
            return self.km <= km_compara.km
        return self.km <= km_compara

    def __ge__(self, km_compara: callable) -> bool:
        if isinstance(km_compara, Distance):
            return self.km >= km_compara.km
        return self.km >= km_compara
