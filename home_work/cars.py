class Car:
    def __init__(self, color, types, year):
        self.color = color
        self.types = types
        self.year = year

    @staticmethod
    def start():
        print('Автомобиль заведен')

    @staticmethod
    def stop():
        print('Автомобиль заглушен')

    def years(self):
        print(self.year)

    def car_type(self):
        print(self.types)

    def car_color(self):
        print(self.color)
