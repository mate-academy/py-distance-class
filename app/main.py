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


        




# %%
distance1 = Distance(20)
distance2 = Distance(30)
# %%
distance1 += distance2 
# %%
distance1.km
# %%
