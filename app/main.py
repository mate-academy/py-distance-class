from __future__ import annotations

class Distance:
    
    def __init__ (self, real: int) ->None:
        self.real = real
        self.km = real
       

    def __str__(self) -> str:
        return f"Distance: {self.real} kilometers."

    def __repr__(self) -> str:
        self.messege = f"Distance(km={self.real})"
        return self.messege

    def __add__(self, other):
        self.real = self.real + other.real
        return self.real

    def __iadd__(self, other) -> int:
        self.real += other.real
        return self
    
    def __mul__(self, other) -> int:
        self.real = self.real * other.real
        return self
    def __truediv__(self, other) -> int:
        self.real = round(self.real / other.real, 2)
        return self.real

    def __lt__(self, other) -> bool:
        return self.real < other.real

    def __gt__(self, other) -> bool:
        return self.real > other.real
    
    def __eq__(self, other) -> bool:
        return self.real == other.real

    def __le__(self, other) -> bool: 
        return self.real <= other.real
       
    def __ge__(self, other) -> bool:
        return self.real >= other.real
    