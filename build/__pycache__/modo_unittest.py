# Unittest - Test Unitário 

import unittest 

from atividades import comer, dormir, eh_engracada
 
class Atividadesunitest(unittest.TestCase):
    def test_comer(self):
        self.assertEqual(comer('cachorro', True), 'cachorro está comendo comida')
        self.assertEqual(comer('cachorro', False), 'cachorro está comendo comida')
        
    def test_dormir (self):
        self.assertEqual(dormir('gato', True), 'gato está dormindo')
        self.assertEqual(dormir('gato', False), 'gato está dormindo')
        
    def test_eh_engracada (self):
        self.assertEqual(eh_engracada('gato', True), 'gato está engracada')
    #   self.assertFalse(eh_engracada('gato', False), 'gato não está engracada')
  
 
if __name__ == '__main__':
  unittest.main()
  
  


