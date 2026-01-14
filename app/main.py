class Distance:
    def __init__(self, km : int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    # addition with creating new one
    def __add__(self, second : object) -> object:
        if getattr(second, "km", 0):
            return Distance(self.km + getattr(second, "km", 0))
        else:  # isinstance(second, int):
            return Distance(self.km + second)
        # else :
        #     return Distance(self.km)

    # addition while adding to the first one
    def __iadd__(self, add : object) -> object:
        if getattr(add, "km", 0):
            self.km += getattr(add, "km", 0)
            return self
        else :  # isinstance(add, int) :
            self.km += add
            return self

    def __truediv__(self, second : int) -> object:
        return Distance(round(self.km / second, 2))

    def __mul__(self, number : int) -> object:
        self.km *= number
        return self

    def __lt__(self, number : object) -> bool:
        if getattr(number, "km", 0):
            return self.km < getattr(number, "km", 0)
        else :  # isinstance(number, int):
            return self.km < number

    def __gt__(self, number : object) -> bool:
        if getattr(number, "km", 0):
            return self.km > getattr(number, "km", 0)
        else:  # isinstance(number, int):
            return self.km > number

    def __eq__(self, number : object) -> bool:
        if getattr(number, "km", 0):
            return self.km == getattr(number, "km", 0)
        else:  # isinstance(number ,int):
            return self.km == number

    def __le__(self, number : object) -> bool:
        if getattr(number, "km", 0):
            return self.km <= getattr(number, "km", 0)
        else :  # isinstance(number, int):
            return self.km <= number

    def __ge__(self, number : object) -> bool:
        if getattr(number, "km", 0):
            return self.km >= getattr(number, "km", 0)
        else :  # isinstance(number, int):
            return self.km >= number
