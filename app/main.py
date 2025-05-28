class Distance:
    # W tym zadaniu masz zaimplementować klasę Distance,
    # która będzie reprezentować dystans w kilometrach i
    # umożliwiać podstawowe operacje na tych dystansach.
    # Oto dokładne wyjaśnienie wymagań:

    # 1. Podstawowa struktura klasy
    # Klasa musi mieć metodę __init__ przyjmującą
    # jeden argument km (liczba kilometrów)
    # Powinna zapisywać tę wartość w atrybucie
    # instancyjnym self.km
    def __init__(self, km: (int, float)) -> None:
        self.km = km

    # 2. Metody do zaimplementowania:
    # a) Reprezentacja tekstowa:

    # __str__ - powinna zwracać string w formacie
    # "Distance: X kilometers." (gdzie X to wartość km)
    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    # __repr__ - powinna zwracać string w formacie "Distance(km=X)"
    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    # b) Operacje arytmetyczne:

    # __add__ - dodawanie:
    # Obsługuje zarówno dodawanie dwóch obiektów Distance
    # Jak i dodawanie liczby (int/float) do Distance
    # Zawsze zwraca nowy obiekt Distance
    def __add__(self, other: (int, float, "Distance")) -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        else:
            return Distance(self.km + other)

    # __iadd__ - dodawanie z przypisaniem (+=):
    # Analogiczne do add, ale modyfikuje istniejący obiekt
    def __iadd__(self, other: (int, float, "Distance")) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
            return self
        else:
            self.km += other
            return self

# __mul__ - mnożenie:
# Obsługuje mnożenie Distance przez liczbę (nie przez inny Distance)
# Zwraca nowy obiekt Distance
    def __mul__(self, other: (int, float)) -> "Distance":
        return Distance(self.km * other)

    # __truediv__ - dzielenie:
    # Obsługuje dzielenie Distance przez liczbę
    # Wynik zaokrąglony do 2 miejsc po przecinku
    # Zwraca nowy obiekt Distance
    def __truediv__(self, other: (int, float)) -> "Distance":
        return Distance(round(self.km / other, 2))

    # c) Operacje porównawcze:

    # __lt__, __gt__, __eq__, __le__, __ge__:
    # Obsługują porównania zarówno z innym obiektem Distance jak i z liczbą
    # Zwracają True/False w zależności od wyniku porównania wartości km
    def __lt__(self, other: (int, float, "Distance")) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        else:
            return self.km < other

    def __gt__(self, other: (int, float, "Distance")) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        else:
            return self.km > other

    def __eq__(self, other: (int, float, "Distance")) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        else:
            return self.km == other

    def __le__(self, other: (int, float, "Distance")) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        else:
            return self.km <= other

    def __ge__(self, other: (int, float, "Distance")) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        else:
            return self.km >= other

# 3. Ważne wymagania:
#
# Wszystkie operacje (poza iadd) powinny zwracać
# NOWY obiekt Distance, a nie modyfikować istniejący
# Klasa powinna obsługiwać zarówno operacje na
# innych Distance jak i na zwykłych liczbach
# Wyniki dzielenia muszą być zaokrąglone do 2
# miejsc po przecinku
# Metody specjalne powinny zwracać odpowiednie typy
# (bool dla porównań, Distance dla operacji arytmetycznych)
# 4. Przykłady użycia:
#
# Tworzenie obiektu: d = Distance(10)
# Drukowanie: print(d) → "Distance: 10 kilometers."
# Dodawanie: d + 5 → Distance(15), d + Distance(5) → Distance(15)
# Porównania: d > 5 → True, d == Distance(10) → True
