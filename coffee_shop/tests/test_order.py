import pytest
from coffee_shop.order import Order
from coffee_shop.customer import Customer
from coffee_shop.coffee import Coffee


def test_order_property_validation():
    alice = Customer("Alice")
    espresso = Coffee("Espresso")

    with pytest.raises(TypeError):
        Order("not_a_customer", espresso, 3.5)
    with pytest.raises(TypeError):
        Order(alice, "not_a_coffee", 3.5)
    with pytest.raises(TypeError):
        Order(alice, espresso, "not_a_price")
    with pytest.raises(ValueError):
        Order(alice, espresso, 0.5)
    with pytest.raises(ValueError):
        Order(alice, espresso, 12.0)

    order = Order(alice, espresso, 5.0)
    assert order.customer == alice
    assert order.coffee == espresso
    assert order.price == 5.0
