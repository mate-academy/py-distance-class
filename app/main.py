#%%
class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."
    
    def __repr__(self) -> str:
        return f"Distance(km={self.km})"
    
    def __add__(self, other):
        return Distance(self.km + other.km)




    

# %%
distance1 = Distance(20)
distance2 = Distance(30)
distance3 = distance1 + distance2  


# %%
isinstance(distance3, Distance)
# %%
distance3.km
# %%
