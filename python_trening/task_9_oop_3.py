class Soda:
    def __init__(self, add=None):
        self.add = add

    def show_my_drink(self):
        if self.add:
            print(f"Газировка и {self.add}")
        else:
            print("Обычная газировка")


add_flavor = Soda('coconut')
not_add_flavor = Soda()

add_flavor.show_my_drink()
not_add_flavor.show_my_drink()
