import unittest
from informe import calcular_monto_total

class TestCalcularMontoTotal(unittest.TestCase):
    def test_calculo_correcto(self):
        monto = 100
        impuesto_pais = 0.1
        ganancias = 0.2
        resultado_esperado = 130
        resultado_obtenido = calcular_monto_total(monto, impuesto_pais, ganancias)
        self.assertEqual(resultado_obtenido, resultado_esperado)

    def test_calculo_con_monto_cero(self):
        monto = 0
        impuesto_pais = 0.1
        ganancias = 0.2
        resultado_esperado = 0
        resultado_obtenido = calcular_monto_total(monto, impuesto_pais, ganancias)
        self.assertEqual(resultado_obtenido, resultado_esperado)

    def test_calculo_con_impuesto_cero(self):
        monto = 100
        impuesto_pais = 0
        ganancias = 0.2
        resultado_esperado = 120
        resultado_obtenido = calcular_monto_total(monto, impuesto_pais, ganancias)
        self.assertEqual(resultado_obtenido, resultado_esperado)

    def test_calculo_con_ganancias_cero(self):
        monto = 100
        impuesto_pais = 0.1
        ganancias = 0
        resultado_esperado = 110
        resultado_obtenido = calcular_monto_total(monto, impuesto_pais, ganancias)
        self.assertEqual(resultado_obtenido, resultado_esperado)

if __name__ == '__main__':
    unittest.main()