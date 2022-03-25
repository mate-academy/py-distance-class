from  typing import  Union

class Distance:
    # Write your code here
    def __init__(self, km: Union[int, float]) -> None:
        self.km = km

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, other):
        try:
            return Distance(self.km + other.km)
        except AttributeError:
            return Distance(self.km + other)

    def __len__(self):
        try:
            return len(self.km)
        except TypeError:
            return self.km



distance1 = Distance(20)
distance2 = Distance(30)
distance3 = distance1 + distance2

print(distance3)
distance3 = distance1 + 30
print(distance3)
distance3 += 20
print(distance3)
print(len(distance3))