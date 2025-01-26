class Distance:
    def __init__(self, meters: float) -> None:
        self.meters = meters

    def to_kilometers(self) -> float:
        return self.meters / 1000

    def to_miles(self) -> float:
        return self.meters / 1609.34

    def to_yards(self) -> float:
        return self.meters * 1.09361

    def to_feet(self) -> float:
        return self.meters * 3.28084

    @staticmethod
    def from_kilometers(kilometers: float) -> 'Distance':
        return Distance(kilometers * 1000)

    @staticmethod
    def from_miles(miles: float) -> 'Distance':
        return Distance(miles * 1609.34)

    @staticmethod
    def from_yards(yards: float) -> 'Distance':
        return Distance(yards / 1.09361)

    @staticmethod
    def from_feet(feet: float) -> 'Distance':
        return Distance(feet / 3.28084)
