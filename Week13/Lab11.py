# Lab 11
# Author: Nate Harris

# Lab 11 will show basic understanding of Object Oriented Programming in Python.

from tabulate import tabulate

# 1. Create a class called Product. The class should have the following attributes in the __init__ method:
# name -> this should be a string
# price -> this should be a float
# product_id (this should be a unique number)

class Product:
    def __init__(self, name: str, price: float, product_id: int):
        """
        Create a Product object with the following attributes:
        name -> this should be a string
        price -> this should be a float
        product_id (this should be a unique number)
        """
        self.name = name
        self.price = price
        self.product_id = product_id  

# 2. Create a method called __str__ that returns a string with the following format:
# Product: <name>, Price: <price>, ID: <product_id>
# Hint: use f-strings to format the string.

    def __str__(self):
        """
        Return a string using the __str__ method with the following format:
        Product: <name>, Price: <price>, ID: <product_id>
        """
        return f'Product: {self.name}, Price: {self.price}, ID: {self.product_id}'


# Great now that we have a Product lets create a Customer class.
# 3. Create a class called Customer. The class should have the following attributes in the __init__ method:
# name -> this should be a string
# customer_id (this should be a unique number)
# cart -> this should be a list that contains Product objects.

class Customer:
    def __init__(self, name: str, customer_id: int):
        """
        Create a Customer object with the following attributes:
        name -> this should be a string
        customer_id (this should be a unique number)
        cart -> this should be a list that contains Product objects.
        """
        self.name = name
        self.customer_id = customer_id
        self.cart = []

# also create a __str__ method that returns a string with the following format:
# Customer: <name>, ID: <customer_id>
# Hint: use f-strings to format the string.

    def __str__(self):
        return f'Customer: {self.name}, ID: {self.customer_id}'

# 4. Create a method called add_to_cart that takes in a Product object and adds it to the cart list. print out the product that was added and the customer's name.

    def add_to_cart(self, Product):
        self.cart.append(Product)
        print(f'{Product} was added to {self.name}\'s cart')

# 5. Create a method called remove_from_cart that takes in a Product object and removes it from the cart list.

    def remove_from_cart(self, Product):
        self.cart.remove(Product)
        print(f'{Product} was removed from {self.name}\'s cart')

# 6. Create a method called checkout calculates the total price of all the products in the cart and prints out the total. After printing out the total, empty the cart.
# Hint: you will need to loop through the cart and add up the prices.

    def checkout(self):
        total = 0
        for product in self.cart:
            total += product.price
        print(f'{self.name}\'s Total: {total}')
        self.cart = ["Empty"]

# 7. Create a method called display_products that prints out all the products in the cart list.

    def display_products(self):
        print(f'{self.name}\'s cart:')
        for product in self.cart:
            print(product)

# 8. **Extra** Create a method called display_products_pretty that prints out all the products in the cart list. (use the tabulate library)
# Make a nice table table using the tabulate library.

    def display_products_pretty(self):
        print(f'{self.name}\'s cart:')
        table = [[product.name, product.price, product.product_id] for product in self.cart]
        print(tabulate(table, headers=['Name', 'Price', 'ID'], tablefmt='rounded_outline'))

# 7. Create a class called Store. The class should have the following attributes in the __init__ method:
# products -> this should be a list that contains Product objects.
# customers -> this should be a list that contains Customer objects.

class Store:
    def __init__(self):
        self.products = []
        self.customers = []

# 8. Create a method called add_product that takes in a Product object and adds it to the products list.

    def add_product(self, product: Product):
        self.products.append(product)
        print(f'{product} was added to the store')


# 9. Create a method called add_customer that takes in a Customer object and adds it to the customers list.

    def add_customer(self, customer: Customer):
        self.customers.append(customer)
        print(f'{customer} was added to the store')

# 10. Create a method called display_products that prints out all the products in the products list.

    def display_products(self):
        print('Products in store:')
        for product in self.products:
            print(product)

# 11. Create a method called display_customers that prints out all the customers in the customers list.

    def display_customers(self):
        print('Customers in store:')
        for customer in self.customers:
            print(customer)

# Typically we would create another file and import the classes we created. For this lab, we will just create the objects in this file to show how its possible.

# 12. Create a store object called store.

store = Store()

# 13. Create a product object called product1 with the following attributes:

product1 = Product('iPhone 12', 799.99, 1)

# 14. Create a product object called product2 with the following attributes:

product2 = Product('iPhone 12 Pro', 999.99, 2)
# name: "iPhone 12 Pro"
# price: 999.99
# product_id: 2

# 15. Create a product object called product3 with the following attributes:

product3 = Product('iPhone 12 Pro Max', 1099.99, 3)
# name: "iPhone 12 Pro Max"
# price: 1099.99
# product_id: 3

# 16. Create a customer object called customer1 with the following attributes:

customer1 = Customer('John', 1)
# name: "John"
# customer_id: 1

# 17. Create a customer object called customer2 with the following attributes:

customer2 = Customer('Jane', 2)
# name: "Jane"
# customer_id: 2


# 18. Add product1 to the store using the add_product method.

store.add_product(product1)

# 19. Add product2 to the store using the add_product method.

store.add_product(product2)

# 20. Add product3 to the store using the add_product method.

store.add_product(product3)

# 21. Add customer1 to the store using the add_customer method.

store.add_customer(customer1)

# 22. Add customer2 to the store using the add_customer method.

store.add_customer(customer2)

# 23. Add product1 to customer1's cart using the add_to_cart method.

customer1.add_to_cart(product1)

# 24. Add product2 to customer1's cart using the add_to_cart method.

customer1.add_to_cart(product2)

# 25. Add product3 to customer2's cart using the add_to_cart method.

customer2.add_to_cart(product3)

# 26. Display current products in customer1's cart using the display_products method.

customer1.display_products_pretty()

# 27. Display current products in customer2's cart using the display_products method.

customer2.display_products()

# 28. Checkout customer1's cart using the checkout method.

customer1.checkout()

# 29. Checkout customer2's cart using the checkout method.

customer2.checkout()

# 30. Display current products in customer1's cart using the display_products method. (should be empty)

customer1.display_products()
