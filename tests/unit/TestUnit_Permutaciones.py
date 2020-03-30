import unittest
from src.variaciones import permutacion

class TestPermutacion(unittest.TestCase):
    def test_permutacion_0(self):
        assert permutacion(0) == 1
    def test_permutacion_entero_postivo(self):
        assert permutacion(3)==6
    def test_permutacion_negativo(self):
        with self.assertRaises(AssertionError):
            permutacion(-5)
    def test_permutacion_real(self):
        with self.assertRaises(AssertionError):
            permutacion(5.5)


if __name__ == '__main__':
    unittest.main()