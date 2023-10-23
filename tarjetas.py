class Tarjeta:
    def __init__(self, numero, fecha_vencimiento):
        self.numero = numero
        self.fecha_vencimiento = fecha_vencimiento

  

class TarjetaCredito(Tarjeta):
    def __init__(self, numero, fecha_vencimiento, limite_credito):
        super().__init__(numero, fecha_vencimiento)
        self.limite_credito = limite_credito

class TarjetaDebito(Tarjeta):
    def __init__(self, numero, fecha_vencimiento, saldo_disponible):
        super().__init__(numero, fecha_vencimiento)
        self.saldo_disponible = saldo_disponible

