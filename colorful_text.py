class Colorful_Text:

    def __init__(self, text, colors):
        self.text = text
        self.colors = colors

    def print_text(self, screen):
        if not self.colors:
            screen.addstr(self.text)
        elif len(self.colors == 1):
            screen.addstr(self.text, self.colors[0])
        else:
            for i, char in enumerate(self.text):
                screen.addstr(self.text, self.colors[i % len(self.colors)])
