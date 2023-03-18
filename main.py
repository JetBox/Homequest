import curses
import math
import sys
import textwrap

from colors import *
from colorful_text import Colorful_Text
from events.house import *
from events.town import *
from events.default_events import Event_CheckStats, Event_QuitGame
from player import Player

debug_mode = True


def str_to_class(classname):
    return getattr(sys.modules[__name__], classname)


def format_minutes_to_time(minute, is_clock=False):
    hours = math.floor(minute / 60)
    if is_clock:
        hours = hours % 12
    minute = minute % 60
    if hours == 0 and is_clock:
        hours = 12

    if not is_clock and hours == 0:
        if minute < 10:
            return "00:0" + str(minute)
        elif minute < 60:
            return "00:" + str(minute)

    if hours < 10 and minute < 10:
        return "0" + str(hours) + ":0" + str(minute)
    elif hours < 10:
        return "0" + str(hours) + ":" + str(minute)
    elif minute < 10:
        return str(hours) + ":0" + str(minute)
    else:
        return str(hours) + ":" + str(minute)


def get_am_or_pm(min):
    if min < 720:
        return "AM"
    return "PM"


def clear_screen():
    ColorManager.update_special_colors()
    stdscr.clear()


class EventManager:

    def __init__(self, stdscr):
        self.text = None
        self.event = None
        self.player = None
        self.current_event = None
        self.screen = stdscr
        self.line_length = 80

    def print_text(self, text=None):
        write_text = text if text else self.text
        for ct in write_text:
            ct.print_text(self.screen)

    def generate_name(self):
        pname = ""
        while not pname:
            if debug_mode:
                pname = "Jack"
            else:
                self.print_text("Before we begin, please input your name:")
                pname = input("> ")

        return pname

    def setup_game(self):
        # TODO: load game from file? generate starting options?
        pname = self.generate_name()
        self.player = Player(name=pname)
        self.current_event = "Event_LivingRoom"

    def run(self):
        ColorManager.create_special_colors()
        ColorManager.init_color_pairs()
        self.setup_game()
        self.play_game()

    def get_next_event(self):
        event = str_to_class(self.current_event)(self.player)
        return event.get_event()

    def play_game(self):
        while True:
            clear_screen()
            self.text = []
            self.event = self.get_next_event()
            flavor_text, event_map = self.event.execute()

            # print text to screen
            self.print_flavor_text(flavor_text)

            # print actions to screen
            actions = self.print_actions(event_map)

            # get players action
            choice = self.get_player_choice(actions)

            self.current_event = actions[choice - 1][0]
            self.player.update_time(actions[choice - 1][1])

    def print_actions(self, event_map):
        actions = []
        for i, ev in enumerate(event_map.keys()):
            actions.append((ev, event_map[ev][1]))
            self.text.append(Colorful_Text("({}) {}".format(i + 1, event_map[ev][0])))
            if event_map[ev][1] == 0:
                self.text.append(Colorful_Text("\n"))
            else:
                self.text.append(Colorful_Text(" ({})\n".format(format_minutes_to_time(event_map[ev][1]))))

        return actions

    def get_player_choice(self, actions):
        choice = -1
        while choice < 49 or choice > 48 + len(actions):
            self.print_text()
            stdscr.refresh()
            choice = self.screen.getch()
            clear_screen()

        return int(choice - 48)

    def print_header(self):
        self.text.append(Colorful_Text("\n"))
        self.text.append(Colorful_Text("{}{} - Day {}\n".format(format_minutes_to_time(self.player.time, is_clock=True),
                                                            get_am_or_pm(self.player.time),
                                                            self.player.day)))
        self.text.append(Colorful_Text("${}\n".format(self.player.money)))
        self.text.append(Colorful_Text("Current Location: {}\n".format(str_to_class(self.player.current_location).description)))
        self.text.append(Colorful_Text("--------------------------------------------------------------------------------\n"))

    def print_footer(self):
        self.text.append(Colorful_Text("--------------------------------------------------------------------------------\n\n"))

    def print_flavor_text(self, flavor_text):
        self.print_header()

        c_count = 0
        last_space_index = 0
        for ct in flavor_text:
            t = ct.get_text()
            last_space_index = 0
            for i, char in enumerate(t):
                if char == '\n':
                    c_count = 0
                    last_space_index = i
                    continue
                if char.isspace():
                    last_space_index = i
                c_count += 1

                if c_count > self.line_length:
                    ct.text = ct.text[:last_space_index] + '\n' + ct.text[last_space_index+1:]
                    c_count = 0

        for ct in flavor_text:
            self.text.append(ct)

        self.print_footer()


def main(screen):
    game = EventManager(screen)
    game.run()


# TODO: Make text colorful. Then make that colorful text animate while waiting on user input
if __name__ == "__main__":
    stdscr = curses.initscr()  # curses screen
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
    stdscr.timeout(100)
    stdscr.scrollok(True)  # enable scrolling
    curses.curs_set(False)  # disable curses
    curses.noecho()  # disable echo typing
    curses.cbreak()  # remove need to press enter

    # wrap curses screen in case of error
    curses.wrapper(main)
