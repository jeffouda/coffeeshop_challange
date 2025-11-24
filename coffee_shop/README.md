# Coffee Shop Domain Model

This Python project models a Coffee Shop domain using object-oriented programming principles. It defines three main entities: Customer, Coffee, and Order, and implements their relationships and behaviors.

## Project Structure

- `customer.py`: Defines the Customer class with properties and methods related to customers.
- `coffee.py`: Defines the Coffee class with properties and methods related to coffee products.
- `order.py`: Defines the Order class representing orders placed by customers for coffee.
- `debug.py`: Script to interactively test class functionality and relationships.
- `tests/`: Directory containing pytest test files.
- `README.md`: Project documentation and instructions.

## Setup Instructions

1. Navigate to the project directory:
   ```bash
   cd coffee_shop
   ```

2. Setup the virtual environment using pipenv:
   ```bash
   pipenv install
   pipenv shell
   ```

3. Install pytest for testing:
   ```bash
   pipenv install pytest
   ```

4. To run the interactive debug script:
   ```bash
   python debug.py
   ```

5. To run tests:
   ```bash
   pytest
   ```

## Requirements

- Python 3.x
- pipenv
- pytest

## Features

- Customer and Coffee classes with validated properties.
- Order class linking Customers and Coffees with price validation.
- Many-to-many relationship between Customers and Coffees through Orders.
- Methods to retrieve related orders, coffees, customers, aggregate order data.
- Class method to find customer who spent most on a given coffee.
- Exception handling for invalid inputs.
- Test suite with pytest to validate functionality.
