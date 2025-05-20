import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestOrder(unittest.TestCase):
    def test_order_init(self):
        c = Customer("Derek")
        cf = Coffee("Cortado")
        o = Order(c, cf, 5.5)
        self.assertEqual(o.customer, c)
        self.assertEqual(o.coffee, cf)
        self.assertEqual(o.price, 5.5)

    def test_invalid_price(self):
        c = Customer("Zed")
        cf = Coffee("Brew")
        with self.assertRaises(ValueError):
            Order(c, cf, 0.5)

if __name__ == "__main__":
    unittest.main()