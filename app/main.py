class Distance:
    def __init__(self, km):
        self.km = km

    def __len__(self):
        return self.km

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, arg):
        if isinstance(arg, Distance):
            return Distance(self.km + arg.km)
        return Distance(self.km + arg)

    def __iadd__(self, arg):
        if isinstance(arg, Distance):
            self.km += arg.km
        else:
            self.km += arg

        return self

    def __mul__(self, arg):
        if isinstance(arg, Distance):
            return Distance(self.km * arg.km)
        return Distance(self.km * arg)

    def __truediv__(self, arg):
        if isinstance(arg, Distance):
            return Distance(round(self.km / arg.km, 2))
        return Distance(round(self.km / arg, 2))

    def __lt__(self, arg):
        if isinstance(arg, Distance):
            return self.km < arg.km
        return self.km < arg

    def __gt__(self, arg):
        if isinstance(arg, Distance):
            return self.km > arg.km
        return self.km > arg

    def __eq__(self, arg):
        if isinstance(arg, Distance):
            return self.km == arg.km
        return self.km == arg

    def __le__(self, arg):
        if isinstance(arg, Distance):
            return self.km <= arg.km
        return self.km <= arg

    def __ge__(self, arg):
        if isinstance(arg, Distance):
            return self.km >= arg.km
        return self.km >= arg
