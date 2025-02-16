from products import Product


class Store():
    def __init__(self,products ):
        self.products = products


    def add_product(self, product):
        self.products.append(product)


    def remove_product(self, product):
        try:
            self.products.remove(product)
        except ValueError as e:
            print(f'{e}: {product} does not exist in Store')


    def get_total_quantity(self):
        total = 0
        for product in self.products:
            total += product.quantity
        return total


    def get_all_products(self):
        all_products = []
        for product in self.products:
            if product.is_active():
                all_products.append(product)
        return all_products


    def order(self, shopping_list):
        total_price = 0
        for item in shopping_list:
            item[0].quantity -= item[1]
            total_price += item[1] * item[0].price
        return total_price


product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                Product("Google Pixel 7", price=500, quantity=250),
               ]

best_buy = Store(product_list)
products = best_buy.get_all_products()
print(best_buy.get_total_quantity())
print(best_buy.order([(products[0], 1), (products[1], 2)]))