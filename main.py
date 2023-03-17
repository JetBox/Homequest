import sys, textwrap, time, math
from colorama import Fore, Back, Style
from os import system, name
from player import Player
from events.default_events import *
from events.house import *
from events.town import *

debug_mode = True


def str_to_class(classname):
    return getattr(sys.modules[__name__], classname)


def format_minutes_to_time(minute,is_clock=False):
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
    if not name == 'nt':
        _ = system('clear')
    else:
        _ = system('cls')


class EventManager:

    def __init__(self):
        self.event = None
        self.player = None
        self.current_event = None

    def generate_name(self):
        pname = ""
        while not pname:
            if debug_mode:
                pname = "Jack"
            else:
                print("Before we begin, please input your name:")
                pname = input("> ")

        return pname

    def setup_game(self):
        # TODO: load game from file? generate starting options?
        pname = self.generate_name()
        self.player = Player(name=pname)
        self.current_event = "Event_LivingRoom"

    def run(self):
        self.setup_game()
        self.play_game()

    def get_next_event(self):
        event = str_to_class(self.current_event)(self.player)
        return event.get_event()

    def play_game(self):
        while True:
            clear_screen()
            self.event = self.get_next_event()
            flavor_text, event_map = self.event.execute()

            player_choice = -1
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
            print("({}) {}".format(i + 1, event_map[ev][0]), end='')
            if event_map[ev][1] == 0:
                print("")
            else:
                print(" ({})".format(format_minutes_to_time(event_map[ev][1])))

        return actions

    def get_player_choice(self, actions):
        choice = ""
        while not choice or not choice.isdigit() or int(choice) <= 0 or int(choice) > len(actions):
            if choice:
                print("Not a valid choice. Try again.")
            choice = input("> ")

        return int(choice)

    def print_header(self):
        print("\n")
        print("{}{} - Day {}".format(format_minutes_to_time(self.player.time,is_clock=True), get_am_or_pm(self.player.time),
                                     self.player.day))
        print("${}".format(self.player.money))
        print("Current Location: {}".format(str_to_class(self.player.current_location).description))
        print("--------------------------------------------------------------------------------")

    def print_footer(self):
        print("--------------------------------------------------------------------------------")
        print("\n")

    def print_flavor_text(self, flavor_text):
        self.print_header()

        paragraphs = flavor_text.splitlines()
        for paragraph in paragraphs:
            p = textwrap.fill(paragraph, 80)
            speed = 2
            if debug_mode:
                speed = 90
            for i, char in enumerate(p):
                if i % speed == 0:
                    time.sleep(0.01)
                print(char, end='', flush=True)
            print("")

        self.print_footer()


if __name__ == "__main__":
    clear_screen()
    game = EventManager()
    game.run()
    clear_screen()