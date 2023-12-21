#unittest es un módulo de Python que permite generar pruebas
import unittest
import os
os.system('cls')

def suma(a, b):
    return a + b

class CajaNegraTest(unittest.TestCase):

    def test_suma(self):
        num1 = 10
        num2 = 5

        resultado = suma(num1, num2)

        self.assertEqual(resultado, 15)

    def suma(n1, n2):
        return n1 + n2

    def test_suma(self):
        num1 = 3
        num2 = 5
        resultado = suma(num1, num2)
        self.assertEqual(resultado, 9)    

if __name__ == '__main__':
    unittest.main()