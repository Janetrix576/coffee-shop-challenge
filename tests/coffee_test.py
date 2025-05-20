import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCoffee(unittest.TestCase):
    def test_valid_name(self):
        cf = Coffee("Flat White")
        self.assertEqual(cf.name, "Flat White")

    def test_invalid_name(self):
        with self.assertRaises(ValueError):
            Coffee("Hi")

    def test_orders_and_customers(self):
        c = Customer("Lara")
        cf = Coffee("Cappuccino")
        Order(c, cf, 4.5)
        self.assertEqual(len(cf.orders()), 1)
        self.assertIn(c, cf.customers())

    def test_average_price(self):
        c = Customer("Ray")
        cf = Coffee("Macchiato")
        Order(c, cf, 4.0)
        Order(c, cf, 6.0)
        self.assertAlmostEqual(cf.average_price(), 5.0)

if __name__ == "__main__":
    unittest.main()