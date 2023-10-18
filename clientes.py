import random
from cuentas import CADolares, CApesos
from tarjetas import TarjetaDebito
from datetime import date

class Cliente:

  def __init__(self, nombre, apellido, dni):
    self.nombre = nombre
    self.apellido = apellido
    self.dni = dni
    self.numero = random.randint(100000, 999999) #CLARAMENTE NO ESTA BIEN HACERLO ASI, ES SOLO DE PRUEBA
    self.tarjetas = []
    self.cuentas = []
    self.chequeras = []

  def actualizarDia(self):
    if self.ultimoRetiro != date.today():
      self.cantRetirosDia = 0
      self.dineroRetirosDia = 0
      self.ultimoRetiro = date.today()


    # ACLARACION: TOMAR CON PINZAS, ESTO ESTABA EN EL CLASSIC, 
    # PERO ME DI CUENTA QUE SE PUEDE HACER POR HERENCIA USANDO LOS MAXIMOS

    # FALTAN ADAPTAR LOS METODOS PARA QUE FUNCIONEN POLIMORFICAMENTE CON TODAS LAS CLASES HIJAS

  '''

    ACLARACION: TOMAR CON PINZAS, ESTO ESTABA EN EL CLASSIC, 
    PERO ME DI CUENTA QUE SE PUEDE HACER POR HERENCIA USANDO LOS MAXIMOS

    FALTAN ADAPTAR LOS METODOS PARA QUE FUNCIONEN POLIMORFICAMENTE CON TODAS LAS CLASES HIJAS

    def agregarTarjetaDebito(self, empresa):
    assert len(self.tarjetas) == 0, "El cliente alcanzo la cantida maxima de tarjetas"
    self.tarjetas.append(TarjetaDebito(empresa))

  def agregarCajaAhorroPesos(self):
    for cuenta in self.cuentas:
      if type(cuenta) == CApesos:
        assert False, "El cliente ya tiene una cuenta de ahorro en pesos"
    self.cuentas.append(CApesos(self))
  
  def agregarCajaAhorroDolares(self):
    for cuenta in self.cuentas:
      if type(cuenta) == CADolares:
        assert False, "El cliente ya tiene una cuenta de ahorro en dolares"
    self.cuentas.append(CApesos(self))
  
  def retirarDinero(self, monto, cuenta):

    self.actualizarDia()

    assert self.dineroRetirosDia + monto < 10000, "El cliente alcanzo el monto maximo de retiros por dia"

    if self.cantRetirosDia > 5:
      monto += monto * self.comisiones[0]
      self.cantRetirosDia += 1
      self.dineroRetirosDia += monto
    else:
      self.cantRetirosDia += 1
      self.dineroRetirosDia += monto

    for cuenta in self.cuentas:
      if cuenta == cuenta:
        cuenta.saldo -= monto
        return
      
    assert False, "El cliente no tiene esa cuenta"
  '''

class ClienteClassic(Cliente):

  def __init__(self, nombre, apellido, dni):
    super().__init__(nombre, apellido, dni)
    self.comisiones = (0.01, 0.005)
    self.maximos = {
      "retirosDiaGratis": 5,
      "retirosDineroDia": 10000,
      "tarjetasDebito": 1,
      "tarjetasCredito": 0,
      "pagoUnicoCredito": 0,
      "pagoCuotasCredito": 0,
      "extensionesTarjeta": 0,
      "chequeras": 0,
      "cajasAhorroPesosGratis": 1,
      "cajasAhorroDolaresGratis": 0,
      "cuentasCorrientePesos": 0,
      "cuentasCorrienteDolares": 0,
      "cuentasInversion": 0,
    }

class ClienteGold(Cliente):
  def __init__(self, nombre, apellido, dni):
    super().__init__(nombre, apellido, dni)
    self.comisionesTransferencias = (0.005, 0.001)
    self.empresasTarjetas = ["Visa", "Mastercard"]
    self.maximos = {
      "retirosDiaGratis": None,
      "retirosDineroDia": 20000,
      "tarjetasDebito": 1,
      "tarjetasCredito": 2,      
      "pagoUnicoCredito": 150000,
      "pagoCuotasCredito": 100000,
      "extensionesPorTarjeta": 5,
      "chequeras": 1,
      "cajasAhorroPesosGratis": 2,
      "cajasAhorroDolaresGratis": 2,
      "cuentasCorrientePesos": 1,
      "cuentasCorrienteDolares": 0,
      "cuentasInversion": None,
    }

class ClienteBlack(Cliente):
  def __init__(self, nombre, apellido, dni):
    super().__init__(nombre, apellido, dni)
    self.comisionesTransferencias = (0, 0)
    self.empresasTarjetas = ["Visa", "Mastercard", "American Express"]
    self.maximos = {
      "retirosDiaGratis": None,
      "retirosDineroDia": 100000,
      "tarjetasDebito": 5,
      "tarjetasCredito": 3,      
      "pagoUnicoCredito": 500000,
      "pagoCuotasCredito": 600000,
      "extensionesPorTarjeta": 10,
      "chequeras": 2,
      "cajasAhorroPesosGratis": 5,
      "cajasAhorroDolaresGratis": 5,
      "cuentasCorrientePesos": 3,
      "cuentasCorrienteDolares": 3,
      "cuentasInversion": None,
    }




