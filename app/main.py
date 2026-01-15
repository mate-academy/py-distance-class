class Distance:
    def __init__(self, km):
        # Guarda a distância em quilômetros
        self.km = km

    def __str__(self):
        # Como aparece quando usamos print()
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        # Como aparece no console, no interpretador
        return f"Distance(km={self.km})"

    def __add__(self, other):
        # Soma com outro Distance ou número
        if isinstance(other, Distance):
            total_km = self.km + other.km
        else:
            total_km = self.km + other
        return Distance(total_km)

    def __iadd__(self, other):
        # Soma in-place, modifica o objeto atual
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, other):
        # Multiplicação por número
        return Distance(self.km * other)

    def __truediv__(self, other):
        # Divisão por número, arredonda para 2 casas decimais
        return Distance(round(self.km / other, 2))

    # Métodos de comparação:
    def __lt__(self, other):
        if isinstance(other, Distance):
            return self.km < other.km
        return self.km < other

    def __gt__(self, other):
        if isinstance(other, Distance):
            return self.km > other.km
        return self.km > other

    def __eq__(self, other):
        if isinstance(other, Distance):
            return self.km == other.km
        return self.km == other

    def __le__(self, other):
        if isinstance(other, Distance):
            return self.km <= other.km
        return self.km <= other

    def __ge__(self, other):
        if isinstance(other, Distance):
            return self.km >= other.km
        return self.km >= other

