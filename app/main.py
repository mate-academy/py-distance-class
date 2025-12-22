from __future__ import annotations

class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km
    
    def __str__(self: Distance) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self: Distance) -> str:
        return f"Distance(km={self.km})"