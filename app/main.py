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
        

        




# %%

# %%

# %%
distance1 = Distance(20)
distance2 = distance1 + 10
# %%
isinstance(distance2, Distance)
# %%
distance2.km = 150
# %%
distance2.km
# %%
