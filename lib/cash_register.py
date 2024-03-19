
class CashRegister:
    def __init__(self):
        self.items = []
        self.total_price = 0

    def add_item(self, name, quantity, price):
        self.items.append({"name": name, "quantity": quantity, "price": price})
        self.total_price += quantity * price

    def calculate_discount(self, discount_percentage):
        discount_amount = self.total_price * (discount_percentage / 100)
        discounted_price = self.total_price - discount_amount
        return discounted_price

    def void_last_transaction(self):
        if self.items:
            last_item = self.items.pop()
            self.total_price -= last_item["quantity"] * last_item["price"]

    def get_items(self):
        return self.items

    def get_total_price(self):
        return self.total_price
