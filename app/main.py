class Distance:
    def __init__(self, km):
        self.km = km
    
    def __str__(self):
        return f"Distance: {self.km} kilometers."
    
    def __repr__(self):
        return f"Distance(km={self.distance})"
    
    def __add__(self, other):
        if not isinstance(other, Distance):
            raise TypeError(f"Wrong type(s) for +: 'Distance' and {type(other)}")
        return Distance(
            km=self.km + other.km
        )
    
    def __iadd__(self, other):
        if not isinstance(other, Distance):
            raise TypeError("Can only add Distance or numeric types.")
        
        self.km += other
        
        return self
        
    
    def __mul__(self, other):
        if not isinstance(other, Distance):
            raise TypeError("Can only multiply Distance or numeric types.")
        
        self.km *= other        
        
        return self
    
    def __truediv__(self, other):
        if not isinstance(other, Distance):
            raise TypeError("Can only divide Distance or numeric types.")
        
        self.km /= other
        round(self.km, 2)
        
        return self
    
    def __lt__(self, other):
        if isinstance(other, Distance):
            return self.km < other.km
        else:
            raise TypeError("Can only compare Distance or numeric types.")
        
    def __gt__(self, other):
        if isinstance(other, Distance):
            return self.km > other.km
        else:
            raise TypeError("Can only compare Distance or numeric types.")
    
    def __eq__(self, other):
        if isinstance(other, Distance):
            return self.km == other.km
        else:
            raise TypeError("Can only compare Distance or numeric types.")
    
    def __le__(self, other):
        if isinstance(other, Distance):
            return self.km <= other.km
        else:
            raise TypeError("Can only compare Distance or numeric types.")
        
    def __ge__(self, other):
        if isinstance(other, Distance):
            return self.km >= other.km
        else:
            raise TypeError("Can only compare Distance or numeric types.")