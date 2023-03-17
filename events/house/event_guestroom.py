from event import Event


class Event_Guestroom(Event):
    description = "Your Guestroom"

    def generate_flavor_text(self):
        flavor_text = ""

        # set intro of the flavor text
        if self.player.previous_location != self.__class__.__name__:
            flavor_text += "You enter your guest room.\n\n"

        # generate text describing what is in your living room, if applicable
        flavor_text += "Your guestroom is completely void of all furniture and objects. You should buy some furniture once you get some cash.\n\n"

        # generate text depending on where the player can go
        flavor_text += "From here, you can go to your living room, or you can go to your backyard.\n\n"

        # generate text depending on what you can do

        return flavor_text

    def generate_actions(self):
        event_map = {}
        event_map["Event_LivingRoom"] = ("Go to your living room", 1)
        event_map["Event_Backyard"] = ("Go out back", 1)

        return event_map
