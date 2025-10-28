# Exercise 1:
class Rectangle:
    pass

# Exercise 2:
class Book:
    pass

# Exercise 3: 
class ShoppingCart:
    def __init__(self):
        # Two separate lists: one for names, one for prices
        self.item_names = []
        self.item_prices = []

    def add_item(self, name, price):
        self.item_names.append(name)
        self.item_prices.append(price)

    def total_price(self):
        total = 0
        for price in self.item_prices:
            total += price
        return total

    def show_items(self):
        result = ""
        for i in range(len(self.item_names)):
            result += f"{self.item_names[i]}: ${self.item_prices[i]}\n"
        return result.strip()

