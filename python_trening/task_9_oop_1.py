class Input:

    def __init__(self, text, loc):
        self.text = text
        self.loc = loc


class Button:
    def __init__(self, text, loc):
        self.text = text
        self.loc = loc


class Title:
    def __init__(self, text, loc):
        self.text = text
        self.loc = loc


class Link:
    def __init__(self, text, loc):
        self.text = text
        self.loc = loc


input1 = Input('input', '123')
button = Button('button', '123')
title = Title('title', '123')
link = Link('link', '123')

print(input1.text, input1.loc)
print(button.text, button.loc)
print(title.text, title.loc)
print(link.text, link.loc)
