#%%
class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."
    
    def __repr__(self) -> str:
        return f"Distance(km={self.km})"
    
    def __add__(self, other):
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, int):
            return Distance(self.km + other)
        else:
            raise f"Gosh,- relax, drink coffee"
    
    def __iadd__(self, other):
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, int):
            self.km += other
        else:
            raise f"Gosh,- relax, drink coffee"
        return self
    
    def __mul__(self, other):
        if isinstance(other, Distance):
            self.km *= other.km
        elif isinstance(other, int):
            self.km *= other
        else:
            raise f"Gosh,- relax, drink coffee"
        return self
    
    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other,2))
        else:
            raise f"Division error - math is your pain"
    
    def __lt__(self, other):
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other
        else: 
            return NotImplemented


        




# %%
distance = Distance(50)

# %%
distance < Distance(60)
# %%
