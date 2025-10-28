# Exercise 1: Rectangle Class
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        # Calculate and return area
        return self.length * self.width

    def perimeter(self):
        # Calculate and return perimeter
        return 2 * (self.length + self.width)


# Exercise 2: Book Class
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        # Return info neatly as a string
        return f"Title: {self.title}, Author: {self.author}, Price: ${self.price}"


# Exercise 3: ShoppingCart Class
class ShoppingCart:
    def __init__(self):
        self.items = []  # list of (name, price)

    def add_item(self, name, price):
        self.items.append((name, price))

    def total_price(self):
        total = 0
        for _, price in self.items:
            total += price
        return total

    def show_items(self):
        result = ""
        for name, price in self.items:
            result += f"{name}: ${price}\n"
        return result.strip()
