class Cuenta:
  def __init__(self, propietario):
    self.propietario = propietario
    self.saldo = 0


class CCDolares(Cuenta):
  def __init__(self, propietario):
    super().__init__(propietario)
    self.descubiertoMaximo = 100
    self.interesDescubierto = 0.01
    self.moneda = "USD"

class CCPesos(Cuenta):
  def __init__(self, propietario):
    super().__init__(propietario)
    self.descubiertoMaximo = 100000
    self.interesDescubierto = 0.01
    self.moneda = "ARS"

class CADolares(Cuenta):
  def __init__(self, propietario):
    super().__init__(propietario)
    self.moneda = "USD"

class CAPesos(Cuenta):
  def __init__(self, propietario):
    super().__init__(propietario)
    self.moneda = "ARS"

class CuentaInversion(Cuenta):
  def __init__(self, propietario):
    super().__init__(propietario)

class Chequera:
  def __init__(self):
    self.cheques = []