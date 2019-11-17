class A:

  def __init__(self, some)
    self._b = some

  def get_b(self):
    return self._b

  def set_b(self, val):
    self._b = val

a = A('123')
print(a.get_b())
a.set_b('444')