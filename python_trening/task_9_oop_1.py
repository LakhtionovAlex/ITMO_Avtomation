from task_9_cheks import Cheks


class Input(Cheks):
    def __init__(self, text, loc):
        super().__init__(loc)
        self.text = text
        self.loc = loc


class Button(Cheks):
    def __init__(self, text, loc):
        super().__init__(loc)
        self.text = text
        self.loc = loc


class Title(Cheks):
    def __init__(self, text, loc):
        super().__init__(loc)
        self.text = text
        self.loc = loc


class Link(Cheks):
    def __init__(self, text, loc):
        super().__init__(loc)
        self.text = text
        self.loc = loc


input1 = Input('input', '123')
button = Button('button', '123')
title = Title('title', '123')
link = Link('link', '123')

print(input1.check_text())
print(button.check_text())
print(title.check_text())
print(link.check_text())
