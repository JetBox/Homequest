from event import Event


class Event_Neighborhood(Event):
    description = "Your Neighborhood"

    def generate_flavor_text(self):
        flavor_text = ""

        # set intro of the flavor text
        if self.player.previous_location == "Event_LivingRoom":
            flavor_text += "You get a breath of fresh air as you walk outside to your neighborhood.\n\n"
        elif self.player.previous_location != self.__class__.__name__:
            flavor_text += "You walk outside .\n\n"

        # generate text describing what is in your living room, if applicable
        flavor_text += "Describe the neighborhood here\n\n"

        # generate text depending on where the player can go
        flavor_text += "You can go home from here. You can also go other places! Wow!\n\n"

        # generate text depending on what you can do
        flavor_text += "You can't do jack diddly squat here!\n\n"

        return flavor_text

    def generate_actions(self):
        event_map = {}
        event_map["Event_LivingRoom"] = ("Go home", 1)

        return event_map
