import unittest
from src.variaciones import factorial

class TestFactorial(unittest.TestCase):
    def test_factorial_numero_valor_0(self):
        assert factorial(0) == 1
    def test_factorial_numero_negativo(self):
        with self.assertRaises(AssertionError):
            factorial(-3)
    def test_factorial_numero_entero_positivo(self):
        assert factorial(5) == 120
    def test_factorial_cadena(self):
        with self.assertRaises(AssertionError):
            factorial("hola")

if __name__ == '__main__':
    unittest.main()