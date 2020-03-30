import unittest
from src.variaciones import variacion

class TestVariacion(unittest.TestCase):
    def test_variacion_2numeros_enteros_menor_mayor(self):
        assert variacion(1,2) == 1
    def test_variacion_2numeros_enteros_mayor_menor(self):
        with self.assertRaises(AssertionError):
            variacion(2,1)
    def test_variacion_0_mayor(self):
        assert  variacion(0,1)==1

    def test_variacion_2numeros_enteros_mayor_menor(self):
        with self.assertRaises(AssertionError):
            variacion("hola","nuestros")

if __name__ == '__main__':
    unittest.main()