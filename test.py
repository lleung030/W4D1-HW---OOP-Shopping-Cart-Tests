from main import add, subtract, multiply, divide
from address_book import store_user_info, remove_user_info, address_book
import unittest

class CalculatorTest(unittest.TestCase):

    def test_add(self):
        result1 = add(1,5)
        self.assertEqual(result1, 6)
        result2 = add(-10, 5)
        self.assertEqual(result2, -5)
        result3 = add(-10, -5)
        self.assertEqual(result3, -15)
        result4 = add(4.5, 5.2)
        self.assertEqual(result4, 9.7)

    # 2.0 - 5.4
    def test_subtract(self):
        result1 = subtract(5, 2)
        self.assertEqual(result1, 3)

        result2 = subtract(2.0, 5.4)
        self.assertAlmostEqual(result2, -3.4)

    def test_multiply(self):
        result1 = multiply(5, 2)
        self.assertEqual(result1, 10)
        
        result2 = multiply(3.3, 2)
        self.assertAlmostEqual(result2, 6.6)

    def test_divide(self):
        result1 = divide(5, 2)
        self.assertEqual(result1, 2.5)
        
        result2 = divide(3.3, 2)
        self.assertAlmostEqual(result2, 1.65)


class AddressBookTest(unittest.TestCase):
    
    def test_store_user_info(self):
        store_user_info('dylan', '123 1st St', address_book)
        self.assertIn('dylan', address_book)

        store_user_info('chris', '55 2nd St', address_book)
        self.assertIn('chris', address_book)

        self.assertNotIn('johnny', address_book)

    def test_remove_user_info(self):
        test_address_book = {}
        test_address_book['jen'] = '1231 Main St'
        test_address_book['debra'] = '321 Alternative St'

        self.assertIn('jen', test_address_book)
        remove_user_info('jen', test_address_book)
        self.assertNotIn('jen', test_address_book)

    def test_exceptions(self):
        test_address_book = {}
        self.assertRaises(Exception, remove_user_info, 'jen', test_address_book)
        store_user_info('johnny', '555 Main St', test_address_book)
        self.assertRaises(Exception, store_user_info, 'johnny', '555 Main St', test_address_book)

unittest.main()