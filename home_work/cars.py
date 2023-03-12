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

    def years(self, new_year):
        self.year = new_year

    def car_type(self, types_new):
        self.types = types_new

    def car_color(self, color_new):
        self.color = color_new
