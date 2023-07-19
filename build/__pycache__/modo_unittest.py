# Unittest - Test Unitário 

import unittest 

from atividades import comer, dormir
 
class Atividadesunitest(unittest.TestCase):
    def test_comer(self):
        self.assertEqual(comer('cachorro', True), 'cachorro está comendo comida')
        self.assertEqual(comer('cachorro', False), 'cachorro está comendo comida')
        
    def test_dormir (self):
        self.assertEqual(dormir('gato', True), 'gato está dormindo')
        self.assertEqual(dormir('gato', False), 'gato está dormindo')
    
 
if __name__ == '__main__':
  unittest.main()
  
  


