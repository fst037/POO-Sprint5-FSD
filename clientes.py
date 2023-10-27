import random
from cuentas import CuentaCorriente, CADolares, CAPesos, CuentaInversion
from tarjetas import TarjetaCredito, TarjetaDebito
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

  def agregar_tarjeta_debito(self, numero, fecha_vencimiento, saldo_disponible):
      tarjeta_debito = TarjetaDebito(numero, fecha_vencimiento, saldo_disponible)
      self.tarjetas_debito.append(tarjeta_debito)

  def agregar_tarjeta_credito(self, numero, fecha_vencimiento, limite_credito):
      tarjeta_credito = TarjetaCredito(numero, fecha_vencimiento, limite_credito)
      self.tarjetas_credito.append(tarjeta_credito)

  def agregar_cuenta(self, cuenta):
      if isinstance(cuenta, (CADolares, CAPesos, CuentaCorriente, CuentaInversion)):
        self.cuentas.append(cuenta)
      else:
          raise ValueError("Tipo de cuenta no válido.")
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
      "tarjetasCreditoVisa": 0,
      "tarjetasCreditoMaster": 0,
      "tarjetasCreditoAmex": 0,      
      "pagoUnicoCredito": 0,
      "pagoCuotasCredito": 0,
      "extensionesTarjeta": 0,
      "chequeras": 0,
      "cajasAhorroPesos": 1,
      "cajasAhorroDolares": 0,
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
      "tarjetasCreditoVisa": 1,
      "tarjetasCreditoMaster": 1,
      "tarjetasCreditoAmex": 0,      
      "pagoUnicoCredito": 150000,
      "pagoCuotasCredito": 100000,
      "extensionesPorTarjeta": 5,
      "chequeras": 1,
      "cajasAhorroPesos": 2,
      "cajasAhorroDolares": 2,
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
      "tarjetasCreditoVisa": 1,
      "tarjetasCreditoMaster": 1,
      "tarjetasCreditoAmex": 1,      
      "pagoUnicoCredito": 500000,
      "pagoCuotasCredito": 600000,
      "extensionesPorTarjeta": 10,
      "chequeras": 2,
      "cajasAhorroPesos": 5,
      "cajasAhorroDolares": 5,
      "cuentasCorrientePesos": 3,
      "cuentasCorrienteDolares": 3,
      "cuentasInversion": None,
    }




