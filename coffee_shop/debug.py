from customer import Customer
from coffee import Coffee


def main():
    # Create customers
    alice = Customer("Alice")
    bob = Customer("Bob")

    # Create coffees
    espresso = Coffee("Espresso")
    latte = Coffee("Latte")

    # Create orders
    order1 = alice.create_order(espresso, 3.5)
    order2 = alice.create_order(latte, 4.0)
    order3 = bob.create_order(espresso, 3.0)

    # Print orders for Alice
    print(f"Orders for {alice.name}: {alice.orders()}")
    print(f"Coffees ordered by {alice.name}: {[c.name for c in alice.coffees()]}")

    # Print orders for coffee Espresso
    print(f"Orders for coffee {espresso.name}: {espresso.orders()}")
    print(
        f"Customers who ordered {espresso.name}: {[c.name for c in espresso.customers()]}"
    )
    print(f"Number of orders for {espresso.name}: {espresso.num_orders()}")
    print(f"Average price for {espresso.name}: {espresso.average_price()}")

    # Test most_aficionado
    top_customer = Customer.most_aficionado(espresso)
    if top_customer:
        print(f"Customer who spent most on {espresso.name}: {top_customer.name}")
    else:
        print(f"No customers found for {espresso.name}")


if __name__ == "__main__":
    main()
