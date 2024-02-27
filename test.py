import unittest
from main import Kalkulacka

class TestSucet(unittest.TestCase):
    def test_add_integer(self):
        calc = Kalkulacka()
        self.assertEqual(calc.sucetfunc(1,2), 3)

    def test_add_integer(self):
        calc = Kalkulacka()
        self.assertEqual(calc.sucetfunc(-10,5), -5)

    def test_kvadraticka(self):
        calc = Kalkulacka()
        self.assertEqual(calc.quadratic_roots(1, 3, 2), 0)



if __name__ == '__main__':
    unittest.main()
