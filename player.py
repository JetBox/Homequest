

class Player:
    def __init__(self, load_from_file=False, name=None):
        # if not load from file, start a new game
        self.name = name

        #################################################################
        # META STATS (Not specific to Player, but the game)             #
        #################################################################

        self.time = 480
        self.day = 1

        # Event/Location information
        self.current_location = "Event_LivingRoom"
        self.previous_location = None
        self.locations_visited_count = {}

        #################################################################
        # PLAYER STATS                                                  #
        #################################################################

        # Player Inventory
        self.money = 0

        # Player Stats
        self.creativity = 5
        self.writing = 0

    def update_time(self, minutes):
        self.time += minutes
        if self.time >= 1440:
            self.time = self.time % 1440
            self.day += 1
