from colorful_text import Colorful_Text
from event import Event
import curses
import sys


class Event_QuitGame(Event):

    def generate_flavor_text(self):
        pass

    def generate_actions(self):
        pass

    def execute(self):
        curses.nocbreak()
        curses.echo()
        curses.endwin()
        sys.exit()


class Event_CheckStats(Event):

    def initial_entry(self):
        pass

    def generate_flavor_text(self):
        p = self.player
        flavor_text = []
        flavor_text.append(Colorful_Text("Name: {}\n".format(p.name)))
        flavor_text.append(Colorful_Text("Money: {}\n".format(p.money)))
        flavor_text.append(Colorful_Text("Creativity: {}\n".format(p.creativity)))
        flavor_text.append(Colorful_Text("Writing Skills: {}\n".format(p.writing)))

        return flavor_text

    def generate_actions(self):
        return {self.player.current_location: ("Go back", 0)}

    def execute(self):
        flavor_text = self.generate_flavor_text()
        actions = self.generate_actions()
        return flavor_text, actions
