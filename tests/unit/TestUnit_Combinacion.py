import unittest
from src.variaciones import convinatoria

class TestConvinatoria(unittest.TestCase):
    def test_combinatoria_numeros_iguales(self):
        assert convinatoria(3,3) == 1
    def test_combinatoria_numeros_negativos(self):
        with self.assertRaises(AssertionError):
            convinatoria(-3,-3)
    def test_combinatoria_menor_mayor(self):
        assert convinatoria(1,3) == 3
    def test_combinatoria_mayor_menor(self):
        with self.assertRaises(AssertionError):
            convinatoria(4,2)
    def test_combinatoria_numeros_reles(self):
        with self.assertRaises(AssertionError):
            convinatoria(4.2,2.1)


if __name__ == '__main__':
    unittest.main()