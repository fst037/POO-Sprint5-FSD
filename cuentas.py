class Cuenta:
  def __init__(self, propietario):
    self.propietario = propietario
    self.saldo = 0


class CajaAhorro(Cuenta):
  def __init__(self, propietario):
    super().__init__(propietario)

class CuentaCorriente(Cuenta):
  def __init__(self, propietario, descubiertoMaximo):
    super().__init__(propietario)
    self.descubiertoMaximo = descubiertoMaximo
    self.interesDescubierto = 0.01

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

