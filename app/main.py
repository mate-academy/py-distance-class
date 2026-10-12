class Distance:

  def __init__(self, km):
    self.km = km

  def __str__(self):
    return f"Distance: {self.km} kilometers."

  def __repr__(self):
    return f"Distance(km={self.km})"

  def __add__(self, other):
    if isinstance(other, Distance):
      return Distance(self.km + other.km)
    elif isinstance(other, (int, float)):
      return Distance(self.km + other)
    return NotImplemented

  def __radd__(self, other):
    return self.__add__(other)

  def __iadd__(self, other):
    if isinstance(other, Distance):
      self.km += other.km
    elif isinstance(other, (int, float)):
      self.km += other
    else:
      return NotImplemented
    return self

  def __mul__(self, other):
    if isinstance(other, (int, float)):
      return Distance(self.km * other)
    return NotImplemented

  def __rmul__(self, other):
    return self.__mul__(other)

  def __truediv__(self, other):
    if isinstance(other, (int, float)):
      return Distance(round(self.km / other, 2))
    return NotImplemented

  def _get_val(self, other):
    if isinstance(other, Distance):
      return other.km
    elif isinstance(other, (int, float)):
      return other
    return None

  def __lt__(self, other):
    val = self._get_val(other)
    if val is not None:
      return self.km < val
    return NotImplemented

  def __gt__(self, other):
    val = self._get_val(other)
    if val is not None:
      return self.km > val
    return NotImplemented

  def __eq__(self, other):
    val = self._get_val(other)
    if val is not None:
      return self.km == val
    return NotImplemented

  def __le__(self, other):
    val = self._get_val(other)
    if val is not None:
      return self.km <= val
    return NotImplemented

  def __ge__(self, other):
    val = self._get_val(other)
    if val is not None:
      return self.km >= val
    return NotImplemented
