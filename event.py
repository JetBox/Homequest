from abc import ABC, abstractmethod


class Event(ABC):

    # --------------------------------------------------------
    # name:        the name of the event. used for decisions
    # --------------------------------------------------------
    # is_location: whether the event is tied to a physical
    #              place the user can travel to, or whether
    #              the event is situational, like a battle
    # ---------------------------------------------------------
    def __init__(self, player, is_location=True):
        self.player = player
        self.name = self.__class__.__name__
        self.is_location = is_location

    #########################################################
    # This method normally returns itself, but can return   #
    # other events, in case of random encounters and such   #
    #########################################################
    def get_event(self):
        return self

    #########################################################
    # This method is for updating the players position, for #
    #                 event related matters                 #
    #########################################################
    def set_player_locations(self):
        self.player.previous_location = self.player.current_location
        self.player.current_location = self.__class__.__name__

    #########################################################
    #   Not all locations need to keep track of how many    #
    #  times the player has visited, but for those that do, #
    #     this method is useful for updating that value     #
    #########################################################
    def increment_player_visited_stat(self):
        if self.__class__.__name__ not in self.player.locations_visited_count:
            self.player.locations_visited_count[self.__class__.__name__] = 1
        else:
            self.player.locations_visited_count[self.__class__.__name__] += 1

    #########################################################
    # When the player enters the event, update information  #
    #########################################################
    def initial_entry(self):
        if self.is_location and self.player.current_location != type(self):
            self.set_player_locations()
            self.increment_player_visited_stat()

    #########################################################
    #  The main meat and potatoes of the method. Is called  #
    # directly by the events manager, and so everything the #
    #         event should encompass should be here         #
    #########################################################
    def execute(self):
        self.initial_entry()

        flavor_text = self.generate_flavor_text()
        events = self.generate_actions()
        self.generate_default_actions(events)

        return flavor_text, events

    #########################################################
    # This method returns the text that will appear to the  #
    # user before the choices are displayed                 #
    #########################################################
    @abstractmethod
    def generate_flavor_text(self):
        pass

    #########################################################
    # Generates the actions/decisions the player can make.  #
    # The outuput, events is a map of strings to string/int #
    #   tuples. The key represents the event that will be   #
    # created should the user select it. The string in the  #
    #  tuple is the text they will see for that selection,  #
    #   and the int represents how long (in minutes) that   #
    #                 action will take                      #
    #########################################################
    @abstractmethod
    def generate_actions(self):
        pass

    #########################################################
    #   Generates the actions that should appear in every   #
    #   event, give or take. The player should always have  #
    #   the option to check their stats and quit the game   #
    #########################################################
    def generate_default_actions(self, events):
        if not self.__class__.__name__ == "Event_CheckStats":
            events["Event_CheckStats"] = ("Check Stats", 0)
        events["Event_QuitGame"] = ("Exit Game", 0)
