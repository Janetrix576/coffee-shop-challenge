import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer(unittest.TestCase):
    def test_valid_name(self):
        c = Customer("John")
        self.assertEqual(c.name, "John")

    def test_invalid_name(self):
        with self.assertRaises(ValueError):
            Customer("")

    def test_orders_and_coffees(self):
        c = Customer("Mary")
        cf = Coffee("Mocha")
        Order(c, cf, 3.5)
        self.assertEqual(len(c.orders()), 1)
        self.assertIn(cf, c.coffees())

    def test_create_order(self):
        c = Customer("Tim")
        cf = Coffee("Americano")
        order = c.create_order(cf, 4.0)
        self.assertEqual(order.customer, c)
        self.assertEqual(order.coffee, cf)

if __name__ == "__main__":
    unittest.main()