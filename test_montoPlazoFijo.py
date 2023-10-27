import unittest
from informe import descontar_comision

class TestDescontarComision(unittest.TestCase):
    def test_calculo_correcto(self):
        monto = 100
        comision_porcentual = 10
        resultado_esperado = 90
        resultado_obtenido = descontar_comision(monto, comision_porcentual)
        self.assertEqual(resultado_obtenido, resultado_esperado)

    def test_calculo_con_monto_cero(self):
        monto = 0
        comision_porcentual = 10
        resultado_esperado = 0
        resultado_obtenido = descontar_comision(monto, comision_porcentual)
        self.assertEqual(resultado_obtenido, resultado_esperado)

    def test_calculo_con_comision_cero(self):
        monto = 100
        comision_porcentual = 0
        resultado_esperado = 100
        resultado_obtenido = descontar_comision(monto, comision_porcentual)
        self.assertEqual(resultado_obtenido, resultado_esperado)

    def test_calculo_con_comision_mayor_que_monto(self):
        monto = 100
        comision_porcentual = 110
        resultado_esperado = 0
        resultado_obtenido = descontar_comision(monto, comision_porcentual)
        self.assertEqual(resultado_obtenido, resultado_esperado)

if __name__ == '__main__':
    unittest.main()