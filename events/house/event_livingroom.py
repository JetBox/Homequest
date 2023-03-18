from event import Event
from colorful_text import Colorful_Text


class Event_LivingRoom(Event):
    description = "Your Living Room"

    def initial_entry(self):
        if self.player.previous_location is None:
            return
        if self.is_location and self.player.current_location != type(self):
            self.set_player_locations()
            self.increment_player_visited_stat()

    def generate_flavor_text(self):
        flavor_text = []

        # set intro of the flavor text
        if not self.player.previous_location:
            self.player.previous_location = self.name
            self.initial_entry()
            flavor_text.append(Colorful_Text("You are "))
            flavor_text.append(Colorful_Text(self.player.name))
            flavor_text.append(Colorful_Text(", and you are ready to begin your quest... your Homequest. The world is "
                                             "your oyster. But beware! The world is rife with danger, and if you "
                                             "aren't careful you could lose your life!\n\n"))
        elif not self.player.previous_location == self.__class__.__name__:
            flavor_text.append(Colorful_Text("You walk into your living room.\n\n"))

        # generate text describing what is in your living room, if applicable
        flavor_text.append(Colorful_Text("The room is completely empty of all furniture and objects. You should "
                                         "probably buy some furniture once you get more money.\n\n"))

        # generate text depending on where the player can go
        flavor_text.append(Colorful_Text("From here, you can go upstairs to your bedroom. You can also head to your "
                                         "kitchen, or to your guestroom. You can also leave your house via the front "
                                         "door.\n\n"))

        # generate text depending on what you can do
        return flavor_text

    def generate_actions(self):
        event_map = {}
        event_map["Event_Bedroom"] = ("Go upstairs to your bedroom", 1)
        event_map["Event_Guestroom"] = ("Go to the guest room", 1)
        event_map["Event_Kitchen"] = ("Go to the kitchen", 1)
        event_map["Event_Neighborhood"] = ("Leave your house", 1)

        return event_map
