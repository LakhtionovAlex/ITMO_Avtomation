class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def square(self):
        s_rect = self.width * self.height
        print(f"Площадь прямоугольника = {s_rect}")

    def perimeter(self):
        p_rect = (self.width + self.height) * 2
        print(f"Периметр прямоугольника = {p_rect}")


# Создайте класс Math.
class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @staticmethod
    def addition(a, b):
        print(a + b)

    @staticmethod
    def multiplication(a, b):
        print(a * b)

    @staticmethod
    def division(a, b):
        print(a / b)

    @staticmethod
    def subtraction(a, b):
        print(a - b)


# откройте страницу https://demoqa.com/text-box
class ButtonLight:
    def __init__(self, text, types, loc):
        self.text = text
        self.type = types
        self.loc = loc

    def text_output(self):
        print(self.text)

    def click_button(self):
        print('{', self.text, '}', sep='')
