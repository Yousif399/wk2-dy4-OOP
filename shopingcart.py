class ShoppingCart:
    def __init__(self):
        self.user_input = {}
        self.name = None

    def add_item(self, name, item):
        self.user_input[name] = item
        print(f"{item} added to {name}'s cart")

    def remove_item(self, name, item):
        if name in self.user_input:
            if item in self.user_input:
                del self.user_input[item]
                print(f"{item} deleted from {name}'s cart")
            else:
                print(f"{item} not in {name}'s cart.")
        else:
            print('User is unknown')

    def view_cart(self):
        if self.user_input:
            print('Shopping list:')
            for name, item in self.user_input.items():
                print(f"{name}: {item}")
        else:
            print('Shopping cart is empty')

    def shopping_cart(self):
        while True:
            select = input('Please select 1 to add, 2 to delete, 3 to view your cart, "q" to quit: ')
            if select == '1':
                self.name = input('Please enter your name: ')
                items = input('Please enter the item you want to buy: ')
                self.add_item(self.name, items)
            elif select == '2':
                if self.name:
                    items = input('Please enter the item you want to remove: ')
                    self.remove_item(self.name, items)
                else:
                    print('User is unknown')
            elif select == '3':
                self.view_cart()
            elif select.lower() == 'q':
                if self.user_input:
                    print('Here are your items in the cart:')
                    for name, item in self.user_input.items():
                        print(f"{name}: {item}")
                        break
                else:
                    print('There is nothing in your cart.')
                    break


if __name__ == "__main__":
    cart = ShoppingCart()
    cart.shopping_cart()






