from customer import Customer
from coffee import Coffee
from order import Order

alice = Customer("Alice")
bob = Customer("Bob")

latte = Coffee("Latte")
espresso = Coffee("Espresso")

Order(alice, latte, 4.5)
Order(alice, espresso, 3.0)
Order(bob, espresso, 3.5)

print(f"Alice's coffees: {[coffee.name for coffee in alice.coffees()]}")

print(f"Espresso ordered {espresso.num_orders()} times.")

print(f"Latte average price: {latte.average_price():.2f}")

aficionado = Customer.most_aficionado(espresso)
print(f"Most aficionado for Espresso: {aficionado.name if aficionado else 'None'}")