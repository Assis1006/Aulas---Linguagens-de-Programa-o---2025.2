import recursao
import unittest # Testes unitários são OBRIGATÓRIOS em empresas. É considerado o teste mais simples.

class TestFatorial(unittest.TestCase): # Para fazer casos de unittest, devemos criar classes
    def test_greater_than_1(self): # E uma função com o comando "assert"
        self.assertEqual(recursao.fatorial(2), 2)
        self.assertEqual(recursao.fatorial(3), 6)
        self.assertEqual(recursao.fatorial(4), 24)
        self.assertEqual(recursao.fatorial(5), 120)

    def test_lesser_than_0(self):
        self.assertEqual(recursao.fatorial(-1), 1)
        
    def test_equal_to_0(self):
        self.assertEqual(recursao.fatorial(1), 1)
        
    def test_input_type(self): # Nesse caso, esperamos um "TypeError" ao digitar uma string. Isso é verdade.
        self.assertRaises(TypeError, recursao.fatorial, "Oi") # O "assertRaises" verifica se certo erro realmente ocorre e o levanta.
        self.assertRaises(TypeError, recursao.fatorial, 1) # Nesse caso, o erro não foi de "TypeError", já que o objeto passado foi de fato um inteiro. Isso dá erro.
       
    def test_decimal_digits(self):
        num_1 = 1.1415926535
        num_2 = 1.14159265359
        digitos_decimais = 9
        
        self.assertAlmostEqual(num_1, num_2, digitos_decimais) # Nesse caso, os números são comparados até o 9° dígito. Como são iguais até esse número, o teste dá certo.
        self.assertAlmostEqual(num_1, num_2, 10) # Aqui dá erro, pois o 10° dígito não é igual.
if __name__ == "__main__":
    unittest.main()

# Técnica de teste: existem diversas técnicas de testes, uma delas é dividir por "limites/barreiras". Essa forma é chamada de "teste por partições". 
# No caso do fatorial, por exemplo, poderíamos fazer um teste para números negativos, para 1 e para algum número acima de 1.
# Somente esses testes já seriam suficientes para provar o código.
