from shopping import Cart, Item, Shop
import unittest

class ShoppingCart(unittest.TestCase):
    def test_add(self):
        cart = Cart()
        cart.add('food',1,2)
        self.assertIn('food', cart.items)


    def test_delete(self):
        cart = Cart()
        cart.add('food',1,2)
        cart.delete('food')
        self.assertTrue('food', cart.items)
        
    
    def test_show(self):
        cart = Cart()
        cart.add('milk',1,2)
        self.assertIn('milk', cart.items)
        self.assertIsNot('food', cart.items)
        
    def test_exceptions(self):
        cart = Cart()
        self.assertRaises(Exception, cart.add, 'food', 1, 2, cart.items)
    
    
unittest.main() 