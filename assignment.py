# Exercise 1
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


# Exercise 2
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        return f"Title: {self.title}, Author: {self.author}, Price: ${self.price}"


# Exercise 3
class ShoppingCart:
    def __init__(self):
        self.names = []   # only storing names
        self.prices = []  # storing prices separately

    def add_item(self, name, price):
        self.names.append(name)
        self.prices.append(price)

    def total_price(self):
        return sum(self.prices)

    def show_items(self):
        result = ""
        for i in range(len(self.names)):
            result += f"{self.names[i]}: ${self.prices[i]}\n"
        return result.strip()  # handles last line \n
