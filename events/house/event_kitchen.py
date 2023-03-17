from event import Event


class Event_Kitchen(Event):
    description = "Your Kitchen"

    def generate_flavor_text(self):
        flavor_text = ""

        # set intro of the flavor text
        if self.player.previous_location != self.__class__.__name__:
            flavor_text += "You enter your kitchen.\n\n"

        # generate text describing what is in your living room, if applicable
        flavor_text += "Your kitchen has all you could ever need. You have a fridge and freezer filled to the brim with snacks and various ingredients for cooking. You have a pantry that contains cereals, canned soups, dry pasta, etc. You have an oven with a stove over it, as well as a microwave and a sink.\n\n"

        # generate text depending on where the player can go
        flavor_text += "From here, you can go to your living room, or you can go to your backyard.\n\n"

        # generate text depending on what you can do
        flavor_text += "If you're feeling bold, you can try to cook something.\n\n"

        return flavor_text

    def generate_actions(self):
        event_map = {}
        event_map["Event_LivingRoom"] = ("Go to your living room", 1)
        event_map["Event_Backyard"] = ("Go out back", 1)

        return event_map
