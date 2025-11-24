import pytest
from coffee_shop.coffee import Coffee
from coffee_shop.customer import Customer

def test_coffee_name_validation():
    with pytest.raises(TypeError):
        Coffee(123)
    with pytest.raises(ValueError):
        Coffee("ab")
    c = Coffee("Espresso")
    assert c.name == "Espresso"

def test_orders_customers_relationship_and_stats():
    espresso = Coffee("Espresso")
    alice = Customer("Alice")
    bob = Customer("Bob")

    order1 = alice.create_order(espresso, 3.0)
    order2 = bob.create_order(espresso, 5.0)
    order3 = alice.create_order(espresso, 4.0)

    orders = espresso.orders()
    customers = espresso.customers()

    assert len(orders) == 3
    assert alice in customers and bob in customers
    assert espresso.num_orders() == 3
    assert pytest.approx(espresso.average_price(), 0.01) == (3.0 + 5.0 + 4.0) / 3
