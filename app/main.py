class Distance:
    # Write your code here
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, other):
        if isinstance(other, Distance):
            return  Distance(self.km + other.km)
        elif isinstance(other, int | float):
            return Distance(self.km + other)
        else:
            raise (
                TypeError("Unsupported")
            )



