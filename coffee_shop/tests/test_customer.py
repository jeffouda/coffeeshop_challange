import pytest
from coffee_shop.customer import Customer
from coffee_shop.coffee import Coffee

def test_customer_name_validation():
    with pytest.raises(TypeError):
        Customer(123)
    with pytest.raises(ValueError):
        Customer("")
    with pytest.raises(ValueError):
        Customer("a"*16)
    c = Customer("Alice")
    assert c.name == "Alice"

def test_orders_and_coffees_relationship():
    alice = Customer("Alice")
    espresso = Coffee("Espresso")
    latte = Coffee("Latte")

    order1 = alice.create_order(espresso, 3.5)
    order2 = alice.create_order(latte, 4.0)

    assert len(alice.orders()) == 2
    coffees = alice.coffees()
    assert espresso in coffees and latte in coffees
    assert coffees.count(espresso) == 1
    assert coffees.count(latte) == 1

def test_most_aficionado():
    alice = Customer("Alice")
    bob = Customer("Bob")
    espresso = Coffee("Espresso")

    alice.create_order(espresso, 3.0)
    alice.create_order(espresso, 2.5)
    bob.create_order(espresso, 6.0)

    top_customer = Customer.most_aficionado(espresso)
    assert top_customer == bob
