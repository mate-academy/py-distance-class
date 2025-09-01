class Distance:
    # Write your code here
    def __init__(self, km: int):
        self.km = km

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, other):
        if isinstance(other, Distance):
            return Distance(
                km=self.km + other.km
            )
        else:
            return Distance(
                km=self.km + other
            )


