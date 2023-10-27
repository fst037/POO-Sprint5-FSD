import json

def calcular_monto_total(precioUSD, montoUSD, impuesto_pais = 0.3, impuesto_ganancias = 0.45):
    return montoUSD * precioUSD * (1 + impuesto_pais + impuesto_ganancias)

def descontar_comision(monto, comision_porcentual):
    return monto * (1 - comision_porcentual / 100)

def calcular_monto_plazo_fijo(monto, interes):
    return monto * (1 + interes / 100)

#realizar pruebas unarias

def validar_informe(informe):

    '''
        ESTA FUNCION VALIDA Y CORRIGE UN INFORME EN BASE A LAS SUPUESTAS REGLAS DE NEGOCIO.
        Las mismas consisten en:

            "RETIRO_EFECTIVO_CAJERO_AUTOMATICO", #TODOS solo si tiene permitidoActualParaTransaccion > monto
            "RETIRO_EFECTIVO_POR_CAJA", #TODOS solo si tiene permitidoActualParaTransaccion > monto
            "COMPRA_EN_CUOTAS_TARJETA_CREDITO_MASTER", #GOLD si < 100000 y BLACK si < 600000
            "COMPRA_EN_CUOTAS_TARJETA_CREDITO_VISA", #GOLD si < 100000 y BLACK si < 600000
            "COMPRA_EN_CUOTAS_TARJETA_CREDITO_AMEX", #GOLD si < 100000 y BLACK si < 600000
            "COMPRA_TARJETA_CREDITO_MASTER", #GOLD si < 100000 y BLACK si < 600000
            "COMPRA_TARJETA_CREDITO_VISA", #GOLD si < 100000 y BLACK si < 600000
            "COMPRA_TARJETA_CREDITO_AMEX", #GOLD si < 100000 y BLACK si < 600000
            "ALTA_TARJETA_CREDITO_MASTER", #GOLD y BLACK (hay un maximo teorico, pero no se provee la cantidad actual en el informe, se da por hecho que tiene 0)
            "ALTA_TARJETA_CREDITO_VISA", #GOLD y BLACK (hay un maximo teorico, pero no se provee la cantidad actual en el informe, se da por hecho que tiene 0)
            "ALTA_TARJETA_CREDITO_AMEX", #GOLD y BLACK (hay un maximo teorico, pero no se provee la cantidad actual en el informe, se da por hecho que tiene 0)
            "ALTA_TARJETA_DEBITO", #TODOS (hay un maximo teorico, pero no se provee la cantidad actual en el informe, se da por hecho que tiene 0)
            "ALTA_CHEQUERA", #GOLD y BLACK (hay un maximo teorico, pero no se provee la cantidad actual en el informe, se da por hecho que tiene 0)
            "ALTA_CUENTA_CTE_PESOS", #GOLD y BLACK (hay un maximo teorico, pero no se provee la cantidad actual en el informe, se da por hecho que tiene 0)
            "ALTA_CUENTA_CTE_DOLARES", #GOLD y BLACK (hay un maximo teorico, pero no se provee la cantidad actual en el informe, se da por hecho que tiene 0)
            "ALTA_CAJA_DE_AHORRO_PESOS", #TODOS (hay un maximo teorico, pero no se provee la cantidad actual en el informe, se da por hecho que tiene 0)
            "ALTA_CAJA_DE_AHORRO_DOLARES", #TODOS (hay un maximo teorico, pero no se provee la cantidad actual en el informe, se da por hecho que tiene 0)
            "ALTA_CUENTA_DE_INVERSION", #GOLD y BLACK (hay un maximo teorico, pero no se provee la cantidad actual en el informe, se da por hecho que tiene 0)
            "COMPRA_DOLAR", #TODOS solo si tiene permitidoActualParaTransaccion > monto
            "VENTA_DOLAR", #TODOS solo si tiene permitidoActualParaTransaccion > monto
            "TRANSFERENCIA_ENVIADA_PESOS", #TODOS solo si tiene permitidoActualParaTransaccion > monto
            "TRANSFERENCIA_ENVIADA_DOLARES", #TODOS solo si tiene permitidoActualParaTransaccion > monto
            "TRANSFERENCIA_RECIBIDA_PESOS", #TODOS solo si tiene permitidoActualParaTransaccion > monto
            "TRANSFERENCIA_RECIBIDA_DOLARES", #TODOS solo si tiene permitidoActualParaTransaccion > monto
        
        La estructura del listado anterior es:
            <TipoTransaccion>, #<TipoCliente> [si <Monto> < <MaximoTeorico>]
    '''


    for cliente in informe:
        # Desempaqueto datos utiles del cliente, para facilitar manejo
        cliente_tipo = cliente["tipo"]

        for transaccion in cliente["transacciones"]:

            # Desempaqueto datos utiles de la transaccion, para facilitar manejo
            descripcion_transaccion = transaccion["tipo"]
            permitido = transaccion["permitidoActualParaTransaccion"]
            monto = transaccion["monto"]

            # Se asume que la transaccion es invalida hasta que se demuestre lo contrario
            valida = False

            # Atributos del cliente SUPUESTOS, porque el informe esta pobre de informacion
            # en un sistema real estos datos deberian darse por el sistema Legacy
            # aca solo sirven como PlaceHolder para poder hacer las validaciones correctamente
            cantidades = {
                "tarjetasDebito": 0,
                "tarjetasCreditoVisa": 0,
                "tarjetasCreditoMaster": 0,
                "tarjetasCreditoAmex": 0,
                "cajasAhorroPesos": 0,
                "cajasAhorroDolares": 0,
                "cuentasCorrientePesos": 0,
                "cuentasCorrienteDolares": 0,
                "cuentasInversion": 0,
                "chequeras": 0,
            }

            # Maximos teoricos de tarjetas, cuentas y pagos Credito             
            # (None significa que el maximo es infinito)
            maximos = {
                "tarjetasDebito": {'Classic': 1, 'Gold': 1, 'Black': 5},
                "tarjetasCreditoVisa": {'Classic': 0, 'Gold': 1, 'Black': 1},                
                "tarjetasCreditoMaster": {'Classic': 0, 'Gold': 1, 'Black': 1},                
                "tarjetasCreditoAmex": {'Classic': 0, 'Gold': 0, 'Black': 1},
                "cajasAhorroPesos": {'Classic': 1, 'Gold': 2, 'Black': 5},
                "cajasAhorroDolares": {'Classic': 1, 'Gold': 2, 'Black': 5},
                "cuentasCorrientePesos": {'Classic': 0, 'Gold': 1, 'Black': 3},
                "cuentasCorrienteDolares": {'Classic': 0, 'Gold': 1, 'Black': 3},
                "cuentasInversion": {'Classic': 0, 'Gold': None, 'Black': None},
                "pagoUnicoCredito": {'Classic': 0, 'Gold': 150000, 'Black': 500000},
                "pagoCuotasCredito": {'Classic': 0, 'Gold': 100000, 'Black': 600000},
                "chequeras": {'Classic': 0, 'Gold': 1, 'Black': 2},
            }

            # Validaciones REALES segun datos del INFORME
            if descripcion_transaccion in  ['RETIRO_EFECTIVO_CAJERO_AUTOMATICO', 
                                            'RETIRO_EFECTIVO_POR_CAJA', 
                                            'COMPRA_DOLAR', 
                                            'VENTA_DOLAR',
                                            'TRANSFERENCIA_ENVIADA_PESOS', 
                                            'TRANSFERENCIA_ENVIADA_DOLARES']:
                if permitido >= monto:
                    valida = True

            # Validaciones IDEALES segun SUPOSICIONES DE DATOS
            else:
                # Asigno correspondencia entre transacciones y maximos, para facilitar manejo
                # y para poder usar diccionarios en vez de multiples if/elif/else
                correspondenciaTransaccionesmMaximos = {
                    "COMPRA_EN_CUOTAS_TARJETA_CREDITO_MASTER" : "pagoCuotasCredito", 
                    "COMPRA_EN_CUOTAS_TARJETA_CREDITO_VISA" : "pagoCuotasCredito", 
                    "COMPRA_EN_CUOTAS_TARJETA_CREDITO_AMEX" : "pagoCuotasCredito",
                    "COMPRA_TARJETA_CREDITO_MASTER" : "pagoUnicoCredito", 
                    "COMPRA_TARJETA_CREDITO_VISA" : "pagoUnicoCredito", 
                    "COMPRA_TARJETA_CREDITO_AMEX" : "pagoUnicoCredito",
                    "ALTA_TARJETA_CREDITO_MASTER" : "tarjetasCreditoMaster",
                    "ALTA_TARJETA_CREDITO_VISA" : "tarjetasCreditoVisa", 
                    "ALTA_TARJETA_CREDITO_AMEX" : "tarjetasCreditoAmex",
                    "ALTA_TARJETA_DEBITO" : "tarjetasDebito", 
                    "ALTA_CHEQUERA" : "chequeras",
                    "ALTA_CUENTA_CTE_PESOS" : "cuentasCorrientePesos", 
                    "ALTA_CUENTA_CTE_DOLARES" : "cuentasCorrienteDolares",
                    "ALTA_CAJA_DE_AHORRO_PESOS" : "cajasAhorroPesos",
                    "ALTA_CAJA_DE_AHORRO_DOLARES" : "cajasAhorroDolares",
                    "ALTA_CUENTA_DE_INVERSION" : "cuentasInversion",
                }

                #Asigno maximo correspondiende a transaccion actual
                nombreMaximoElegido = correspondenciaTransaccionesmMaximos[descripcion_transaccion]

                #Obtengo el maximo correspondiente al tipo de cliente
                maximoDeTransaccion = maximos[nombreMaximoElegido][cliente_tipo]

                #Si el maximo es None, significa que no hay limite
                if maximoDeTransaccion == None:
                    valida = True
                #chequeo que el limite de gasto no supere el maximo
                elif nombreMaximoElegido == 'pagoCuotasCredito' or nombreMaximoElegido == 'pagoUnicoCredito':
                    if monto <= maximoDeTransaccion:
                        valida = True
                #chequeo que las cantidades actuales no superen el maximo                
                elif cantidades[nombreMaximoElegido] < maximoDeTransaccion:
                    valida = True
            
            # Se corrige en la transaccion el estado de la misma
            transaccion["estado"] = "ACEPTADA" if valida else "RECHAZADA"

# datos de ejemplo
informe = [{
    "numero": 100001,
    "nombre": "Nicolas",
    "apellido": "Gaston",
    "dni": "29494777",
    "tipo": "Black",
    "transacciones": [
        #ACLARACION: los datos que se proveen por el sistema Legacy son escasos, ya que no informan la cantidad de cuentas ni tarjetas que el cliente tiene.
        #            por lo que gran parte de las validaciones no se pueden hacer.
        #            idealmente el sistema deberia proveer un Cliente con una estructura similar a la de la clase Cliente definida en clientes.py
        #            y a partir de ahi se podria hacer una validacion mas completa, teniendo en cuenta todos los datos del cliente.
        #            De todas formas intentamos hacer un chequeo extenso, pero realmente, con los datos provistos,
        #            las unicas validaciones que se extrajeron del informe son las que se basan en el monto y el permitido para la transaccion.
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
            "tipo": "COMPRA_EN_CUOTAS_TARJETA_CREDITO_VISA",
            "permitidoActualParaTransaccion": 9000,
            "monto": 750000,
            "fecha": "10/10/2022 16: 14: 35",
            "numero": 2
        }
    ]
}]

validar_informe(informe)

informe_json = json.dumps(informe, indent=2)

html_output = f"<pre>{informe_json}</pre>"

with open("informe.html", "w") as file:
    file.write(html_output)
