import unittest
from ex2 import remove_duplicates


class TestRemoveDuplocates(unittest.TestCase):
    
    def test_good_work(self):
        self.assertEqual(remove_duplicates([1, 1, 3, 5]), [3, 5])

    def test_incoming_type(self):
        with self.assertRaises(TypeError):
            remove_duplicates((4, 5, 5))
    
    def test_len_incoming_list(self):
        with self.assertRaises(ValueError):
            remove_duplicates([])
            
    def test_count_args(self):
        with self.assertRaises(TypeError):
            remove_duplicates([1, 2, 2], [])
            
    def test_type_of_char_in_elements(self):
        with self.assertRaises(TypeError):
            remove_duplicates([1, 1, '2'])
            
            
if __name__ == "__main__":
    unittest.main()


