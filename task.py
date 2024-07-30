import re
import unittest

class StringCalculator:
    #Check if input string empty then return 0
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0
        
        delimiter = ","
        if numbers.startswith("//"):
            parts = numbers.split("\n", 1)
            delimiter = re.escape(parts[0][2:])
            numbers = parts[1]
        
        numbers = numbers.replace("\n", delimiter)
        number_list = re.split(delimiter, numbers)
        
        sum = 0
        negative_numbers = []
        for number in number_list:
            if number:
                num = int(number)
                if num < 0:
                    negative_numbers.append(num)
                sum += num
        #if in input string negative numbers are there in it generate valueError with message
        if negative_numbers:
            raise ValueError(f"Negative numbers not allowed: {','.join(map(str, negative_numbers))}")
        
        return sum



class TestStringCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = StringCalculator()
    
    def test_empty_string(self):
        self.assertEqual(self.calculator.add(""), 0)
    
    def test_single_number(self):
        self.assertEqual(self.calculator.add("1"), 1)
    
    def test_two_numbers(self):
        self.assertEqual(self.calculator.add("1,2"), 3)
    
    def test_multiple_numbers(self):
        self.assertEqual(self.calculator.add("1,2,3,4,5"), 15)
    
    def test_new_lines_between_numbers(self):
        self.assertEqual(self.calculator.add("1\n2,3"), 6)
    
    def test_different_delimiters(self):
        self.assertEqual(self.calculator.add("//;\n1;2"), 3)
    
    def test_negative_numbers(self):
        with self.assertRaises(ValueError) as context:
            self.calculator.add("1,-2,3,-4")
        self.assertEqual(str(context.exception), "Negative numbers not allowed: -2,-4")

if __name__ == "__main__":
    unittest.main()
