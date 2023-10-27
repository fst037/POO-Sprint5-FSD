import random
from cuentas import CCDolares, CCPesos, CADolares, CAPesos, CuentaInversion, Chequera
from tarjetas import TarjetaCredito, TarjetaDebito
from datetime import date

class Cliente:

  def __init__(self, nombre, apellido, dni):
    self.nombre = nombre
    self.apellido = apellido
    self.dni = dni
    self.numero = random.randint(100000, 999999) #CLARAMENTE NO ESTA BIEN HACERLO ASI, ES SOLO DE PRUEBA
    self.comisiones = (0, 0)
    self.maximos = {}
    self.tarjetas = []
    self.cuentas = []
    self.chequeras = []
    self.cantRetirosDia = 0
    self.dineroRetirosDia = 0
    self.ultimoRetiro = date.today()

  def actualizarDia(self):
    if self.ultimoRetiro != date.today():
      self.cantRetirosDia = 0
      self.dineroRetirosDia = 0
      self.ultimoRetiro = date.today()

  def retiroEfectivo(self, monto, moneda):
    self.actualizarDia()
    if self.dineroRetirosDia < self.maximos["retirosDineroDia"]:
      if self.maximos["retirosDiaGratis"] == None or self.cantRetirosDia > self.maximos["retirosDiaGratis"]:
        monto += monto * self.comisiones[0]
        self.cantRetirosDia += 1
        self.dineroRetirosDia += monto
      else:
        self.cantRetirosDia += 1
        self.dineroRetirosDia += monto

      if moneda == "ARS" or moneda == "USD":
        tipoCuenta = CAPesos if moneda == "ARS" else CADolares
        for cuenta in self.cuentas:
          if type(cuenta) == tipoCuenta and cuenta.saldo >= monto:
            cuenta.saldo -= monto
            return
      assert False, "El cliente no tiene una cuenta con esa moneda o no tiene saldo suficiente"
    assert False, "El cliente alcanzo el monto maximo de retiros por dia"

  def compraCredito(self, monto, empresaTarjeta, unPagoUnico):
    maximoCorrespondiente= "pagoUnicoCredito" if unPagoUnico else "pagoCuotasCredito"
    if (monto <= self.maximos[maximoCorrespondiente]):      
      for tarjeta in self.tarjetas:
        if type(tarjeta) == TarjetaCredito and tarjeta.empresa == empresaTarjeta:
          if tarjeta.limite_credito >= monto + tarjeta.creditoActual:
            tarjeta.creditoActual += monto
            return
          return
      assert False, "El cliente no tiene una tarjeta de credito con esa empresa con limite suficiente, pruebe pagar la deuda o sacar una nueva tarjeta con esa empresa"
    assert False, "El pago fue rechazado por llegar al limite de pago unico con tarjeta de credito"

  def agregar_tarjeta_debito(self):
    if len(filter(lambda x: type(x) == TarjetaDebito, self.tarjetas)) < self.maximos["tarjetasDebito"]:
      self.tarjetas.append(TarjetaDebito(0))
    else:
      assert False, "El cliente alcanzo la cantidad maxima de tarjetas de debito"

  def agregar_tarjeta_credito(self, empresa):
      tarjeta_credito = TarjetaCredito(1000000, empresa)
      if empresa in ['Visa','Master','Amex']:
        if len(filter(lambda x: type(x) == TarjetaCredito and x.empresa == empresa, self.tarjetas)) < self.maximos["tarjetasCredito" + empresa]:
          self.tarjetas.append(tarjeta_credito)
        else:
          assert False, "El cliente alcanzo la cantidad maxima de tarjetas de credito de " + empresa
  
  def agregar_cuenta(self, tipoCuenta):
    if tipoCuenta in ['CAPesos', 'CADolares', 'CCPesos', 'CCDolares', 'CuentaInversion' ]:
      correspondenciaTipoCuentaMaximoYConstructor = {
        'CAPesos': ('cajasAhorroPesos', CAPesos),
        'CADolares': ('cajasAhorroDolares', CADolares),
        'CCPesos': ('cuentasCorrientePesos', CCPesos),
        'CCDolares': ('cuentasCorrienteDolares', CCDolares),
        'CuentaInversion': ('cuentasInversion', CuentaInversion)
      }
      maximoCorrespondiente = correspondenciaTipoCuentaMaximoYConstructor[tipoCuenta][0]
      constructorCorrespondiente = correspondenciaTipoCuentaMaximoYConstructor[tipoCuenta][1]
      if len(filter(lambda x: type(x) == tipoCuenta, self.cuentas)) < self.maximos[maximoCorrespondiente]:
        self.cuentas.append(constructorCorrespondiente(self))
      else:
        assert False, f"El cliente alcanzo la cantidad maxima de cuentas tipo {tipoCuenta}"
    else:
      assert False, "El tipo de cuenta no es valido" 

  def agregar_chequera(self):
    if len(self.chequeras) < self.maximos["chequeras"]:
      self.chequeras.append(Chequera())
    else:
      assert False, "El cliente alcanzo la cantidad maxima de chequeras"

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




