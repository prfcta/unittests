import unittest
from ex1 import expanded_form


class TestExpandedForm(unittest.TestCase):
    
    def test_good_work(self):
        self.assertEqual(expanded_form(1234), '1000 + 200 + 30 + 4')
    
    def test_incoming_value(self):
        with self.assertRaises(ValueError):
            expanded_form(-50)
    
    def test_incoming_type(self):
        with self.assertRaises(TypeError):
            expanded_form(True)
            
            
if __name__ == "__main__":
    unittest.main()







