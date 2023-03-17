from event import Event


class Event_Backyard(Event):
    description = "Your Backyard"

    def generate_flavor_text(self):
        flavor_text = ""

        # set intro of the flavor text
        if self.player.previous_location != self.__class__.__name__:
            flavor_text += "You take a breath of fresh air as you step out into your backyard.\n\n"

        # generate text describing what is in your living room, if applicable
        flavor_text += "Your backyard is decently sized, compared to most people, about the size of an acre. It's fenced off around the perimeter. You have a section penned off for farming and gardening, should you have the tools to do so. There's a large oak tree to the back, just beside the fence leading out into the forest. The rest of your backyard is dirt. It could use some improvement.\n\n"

        # generate text depending on where the player can go
        flavor_text += "From here, you can go back inside your house, either into the guestroom or the kitchen. You can also try entering the forest by climbing the tree to get over the fence, but you're not sure how you'd get back.\n\n"

        # generate text depending on what you can do

        return flavor_text

    def generate_actions(self):
        event_map = {}
        event_map["Event_Guestroom"] = ("Go to your guestroom", 1)
        event_map["Event_Kitchen"] = ("Go to your kitchen", 1)

        return event_map
