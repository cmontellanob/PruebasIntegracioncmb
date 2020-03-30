import unittest
from src.variaciones import variacion, factorial,convinatoria,permutacion

class TestVariaciones(unittest.TestCase):
    def test_combinatoria_factorial_menor_factorial_mayor(self):
        assert convinatoria(factorial(0),factorial(2))==1
    def test_variación_2_factorial_entero(self):
        assert variacion(2, factorial(3)) == 15
    def test_permutacion_convinacion_numeros_iguales(self):
        assert permutacion(convinatoria(5, 5)) == 1
    def test_factorial_convinatoria_mayor_menor(self):
        with self.assertRaises(AssertionError):
            factorial(convinatoria(5, 4))

if __name__ == '__main__':
    unittest.main()