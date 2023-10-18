import json

tipos_cliente = ["Classic", "Gold", "Black"]
operaciones_permitidas = [
    "RETIRO_EFECTIVO_CAJERO_AUTOMATICO",
    "RETIRO_EFECTIVO_POR_CAJA",
    "COMPRA_EN_CUOTAS_TARJETA_CREDITO_MASTER",
    "COMPRA_EN_CUOTAS_TARJETA_CREDITO_VISA",
    "COMPRA_EN_CUOTAS_TARJETA_CREDITO_AMEX",
    "COMPRA_TARJETA_CREDITO_MASTER",
    "COMPRA_TARJETA_CREDITO_VISA",
    "COMPRA_TARJETA_CREDITO_AMEX",
    "ALTA_TARJETA_CREDITO_MASTER",
    "ALTA_TARJETA_CREDITO_VISA",
    "ALTA_TARJETA_CREDITO_AMEX",
    "ALTA_TARJETA_DEBITO",
    "ALTA_CHEQUERA",
    "ALTA_CUENTA_CTE_PESOS",
    "ALTA_CUENTA_CTE_DOLARES",
    "ALTA_CAJA_DE_AHORRO_PESOS",
    "ALTA_CAJA_DE_AHORRO_DOLARES",
    "ALTA_CUENTA_DE_INVERSION",
    "COMPRA_DOLAR",
    "VENTA_DOLAR",
    "TRANSFERENCIA_ENVIADA_PESOS",
    "TRANSFERENCIA_ENVIADA_DOLARES",
    "TRANSFERENCIA_RECIBIDA_PESOS",
    "TRANSFERENCIA_RECIBIDA_DOLARES",
]


def calcular_monto_total(monto, impuesto_pais, ganancias):
    return monto * (1 + impuesto_pais + ganancias)

def descontar_comision(monto, comision_porcentual):
    return monto * (1 - comision_porcentual / 100)

def calcular_monto_plazo_fijo(monto, interes):
    return monto * (1 + interes / 100)



def validar_transaccion(cliente_tipo, transaccion):
    if cliente_tipo == "Classic":
        if transaccion.startswith("ALTA_TARJETA") or transaccion.startswith("ALTA_CHEQUERA") or transaccion.startswith("ALTA_CUENTA_CTE") or transaccion.startswith("ALTA_CAJA_DE_AHORRO") or transaccion.startswith("ALTA_CUENTA_DE_INVERSION"):
            return False
        elif transaccion.startswith("RETIRO_EFECTIVO_CAJERO_AUTOMATICO"):
            return True
        elif transaccion.startswith("TRANSFERENCIA"):
            return True
        else:
            return False
    elif cliente_tipo == "Gold":
        if transaccion.startswith("ALTA_TARJETA") or transaccion.startswith("ALTA_CHEQUERA") or transaccion.startswith("ALTA_CUENTA_CTE") or transaccion.startswith("ALTA_CAJA_DE_AHORRO") or transaccion.startswith("ALTA_CUENTA_DE_INVERSION"):
            return False
        elif transaccion.startswith("RETIRO_EFECTIVO_CAJERO_AUTOMATICO") or transaccion.startswith("RETIRO_EFECTIVO_POR_CAJA"):
            return True
        elif transaccion.startswith("COMPRA_EN_CUOTAS_TARJETA_CREDITO") or transaccion.startswith("COMPRA_TARJETA_CREDITO"):
            return True
        elif transaccion.startswith("TRANSFERENCIA"):
            return True
        else:
            return False
    elif cliente_tipo == "Black":
        if transaccion.startswith("ALTA_TARJETA") or transaccion.startswith("ALTA_CHEQUERA") or transaccion.startswith("ALTA_CUENTA_CTE") or transaccion.startswith("ALTA_CAJA_DE_AHORRO") or transaccion.startswith("ALTA_CUENTA_DE_INVERSION"):
            return False
        elif transaccion.startswith("RETIRO_EFECTIVO_CAJERO_AUTOMATICO") or transaccion.startswith("RETIRO_EFECTIVO_POR_CAJA"):
            return True
        elif transaccion.startswith("TRANSFERENCIA"):
            return True
        else:
            return False
    else:
        return False


# datos de ejemplo
cliente = {
    "numero": 100001,
    "nombre": "Nicolas",
    "apellido": "Gaston",
    "dni": "29494777",
    "tipo": "Black",
    "transacciones": [
        {
            "estado": "ACEPTADA",
            "tipo": "RETIRO_EFECTIVO_CAJERO_AUTOMATICO",
            "cuentaNumero": 190,
            "permitidoActualParaTransaccion": 9000,
            "monto": 1000,
            "fecha": "10/10/2022 16: 00: 55",
            "numero": 1
        },
        {
            "estado": "RECHAZADA",
            "tipo": "COMPRA_EN_CUOTAS_TARJETA_VISA",
            "permitidoActualParaTransaccion": 9000,
            "monto": 750000,
            "fecha": "10/10/2022 16: 14: 35",
            "numero": 2
        }
    ]
}

for transaccion in cliente["transacciones"]:
    transaccion_tipo = transaccion["tipo"]
    transaccion_estado = "ACEPTADA" if validar_transaccion(cliente["tipo"], transaccion_tipo) else "RECHAZADA"
    transaccion["estado"] = transaccion_estado


informe_json = json.dumps(cliente, indent=2)


html_output = f"<pre>{informe_json}</pre>"


with open("informe.html", "w") as file:
    file.write(html_output)
