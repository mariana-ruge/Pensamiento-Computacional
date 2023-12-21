import unittest
import os
os.system('cls')

def mayor_de_edad(edad):
    if edad >= 18:
        return True
    else:
        return False

class PruebaCajaCristalTest(unittest.TestCase):
    
    def test_mayor_edad(self):
        edad = 20

        resultado = mayor_de_edad(edad)

        self.assertEqual(resultado, True)

    def test_menor_edad(self):
        edad = 15

        resultado = mayor_de_edad(edad)

        self.assertEqual(resultado, False)

if __name__ == "__main__":
    unittest.main()