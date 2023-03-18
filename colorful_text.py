from curses import color_pair


class Colorful_Text:

    def __init__(self, text, colors=None):
        if colors is None:
            colors = []
        self.text = text
        self.colors = colors

    def get_text(self):
        return self.text

    def print_text(self, screen):
        if len(self.colors) == 0:
            screen.addstr(self.text)
        elif len(self.colors) == 1:
            screen.addstr(self.text, color_pair(self.colors[0]))
        else:
            skip_count = 0
            for i, char in enumerate(self.text):
                if char.isspace() or char == '\n':
                    screen.addstr(char)
                    skip_count += 1
                else:
                    screen.addstr(char, color_pair(self.colors[(i-skip_count) % len(self.colors)]))
