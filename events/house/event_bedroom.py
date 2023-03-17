from event import Event


class Event_Bedroom(Event):
    description = "Your Bedroom"

    def generate_flavor_text(self):
        flavor_text = ""

        # set intro of the flavor text
        if self.player.previous_location != self.__class__.__name__:
            flavor_text += "You walk up the stairs into your living room.\n\n"

        # generate text describing what is in your living room, if applicable
        flavor_text += "Your bedroom is shabby. You have a cozy bed in the corner, showing clear signs of having recently been slept in. At the opposite side of the room, your desk can be found supporting your computer.\n\n"

        # generate text depending on where the player can go
        flavor_text += "There isn't anywhere you can go except back down stairs.\n\n"

        # generate text depending on what you can do
        flavor_text += "You can go to sleep if you want, or you can get on your computer.\n\n"

        return flavor_text

    def generate_actions(self):
        event_map = {}
        event_map["Event_LivingRoom"] = ("Go downstairs to your living room", 60)
        # event_map["Event_Guestroom"] = ("Go to the guest room", 1)
        # event_map["Event_Kitchen"] = ("Go to the kitchen", 1)
        # event_map["Event_Neighborhood"] = ("Leave your house", 1)

        return event_map
