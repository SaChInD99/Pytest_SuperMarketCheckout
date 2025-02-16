import unittest

import pytest

from Checkout import Checkout  # Ensure Checkout.py is in the same directory


class MyTestCase(unittest.TestCase):

    def setUp(self):
        """Runs before every test to set up a fresh Checkout instance."""
        self.checkout = Checkout()

    def test_CanAddItemPrice(self):
        """Tests if an item price can be added without errors."""
        self.checkout.additemprice("Coke", 1)

    def test_CanAddItem(self):
        """Tests if an item can be added only if the price is set."""
        self.checkout.additemprice("Coke", 1)
        self.checkout.additem("Coke")

    def test_CanCalculateTotal(self):
        """Tests if the total calculation works for a single item."""
        self.checkout.additemprice("Coke", 1)
        self.checkout.additem("Coke")
        self.assertEqual(self.checkout.calculateTotal(), 1)

    def test_GetCorrectTotalWithMultipleItems(self):
        """Tests if the total calculation works for multiple items."""
        self.checkout.additemprice("Coke", 1)
        self.checkout.additemprice("b", 2)
        self.checkout.additem("Coke")
        self.checkout.additem("b")
        self.assertEqual(self.checkout.calculateTotal(), 3)

    def test_CanAddDiscountRule(self):
        """Tests if a discount rule can be added without errors."""
        self.checkout.adddiscount("Coke", 3, 2)

    def test_CanApplyDiscountRule(self):
        """Tests if the discount rule is correctly applied."""
        self.checkout.additemprice("Coke", 1)
        self.checkout.adddiscount("Coke", 3, 2)
        self.checkout.additem("Coke")
        self.checkout.additem("Coke")
        self.checkout.additem("Coke")

        # 3 Cokes with a discount: should total to $2
        self.assertEqual(self.checkout.calculateTotal(), 2)

    def test_ExceptionWithBadItem(self):
        with pytest.raises(Exception):
            self.checkout.additem("c")




if __name__ == '__main__':
    unittest.main()
