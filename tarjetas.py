import random
import datetime

class Tarjeta:
    def __init__(self):
        self.numero = random.randint(1000000000000000, 9999999999999999) #CLARAMENTE NO ESTA BIEN HACERLO ASI, ES SOLO DE PRUEBA
        self.fecha_vencimiento = datetime.date.today() + datetime.timedelta(years=5)


class TarjetaCredito(Tarjeta):
    def __init__(self, limite_credito, empresa):
        super().__init__()
        self.creditoActual= 0;
        self.limite_credito = limite_credito
        self.empresa = empresa

class TarjetaDebito(Tarjeta):
    def __init__(self, saldo_disponible):
        super().__init__()
        self.saldo_disponible = saldo_disponible

