class Distance:
    
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"
    
    def __add__(self, other: "Distance" | int | float) -> "Distance":
        return Distance(
            km=self.km + other.km if isinstance(other, type(self)) else self.km + other
        ) 
        
    def __iadd__(self, other: "Distance" | int | float) -> "Distance":
        self.km += other.km if isinstance(other, type(self)) else other
        return self

    def __mul__(self, number: int | float) -> "Distance":
        self.km *= number
        return self
