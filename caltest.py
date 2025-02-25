import unittest
import calculator

class TestCalculator(unittest.TestCase):

    def test_square_root(self):
        self.assertAlmostEqual(calculator.square_root(9), 3.0)    
        self.assertAlmostEqual(calculator.square_root(36), 6.0)   
        self.assertAlmostEqual(calculator.square_root(49), 7.0)   
        self.assertAlmostEqual(calculator.square_root(64), 8.0)   

    def test_factorial(self):
        self.assertEqual(calculator.factorial(2), 2)     
        self.assertEqual(calculator.factorial(3), 6)     
        self.assertEqual(calculator.factorial(4), 24)    
        self.assertEqual(calculator.factorial(7), 5040)  

    def test_natural_log(self):
        self.assertAlmostEqual(calculator.natural_log(1), 0.0)          
        self.assertAlmostEqual(calculator.natural_log(10), 2.3025850929) 
        self.assertAlmostEqual(calculator.natural_log(7), 1.9459101491)  
        self.assertAlmostEqual(calculator.natural_log(20), 2.9957322736) 

    def test_power(self):
        self.assertAlmostEqual(calculator.power(3, 3), 27.0)    
        self.assertAlmostEqual(calculator.power(2, 4), 16.0)    
        self.assertAlmostEqual(calculator.power(6, 2), 36.0)    
        self.assertAlmostEqual(calculator.power(3, 4), 81.0)    

if __name__ == '__main__':
    unittest.main()
