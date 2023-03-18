from curses import init_pair, init_color
from enum import Enum


class ColorCodes(Enum):
    BLUE = 1
    GREEN = 2
    SKY_BLUE = 3
    RED = 4
    PURPLE = 5
    YELLOW = 6
    GREY = 7
    DARK_GREY = 8
    OCEAN_BLUE = 9
    LIME_GREEN = 10
    CYAN = 11
    BLOOD_ORANGE = 12
    DEEP_PURPLE = 13
    TAN_YELLOW = 14
    BRIGHT_WHITE = 15
    BLACK = 16
    ORANGE = 17


class SpecialColor:
    def __init__(self, pair, pattern, init_index=0):
        self.pair = pair
        self.index = init_index
        self.pattern = pattern

    def update_and_increment(self):
        self.index = (self.index + 1) % len(self.pattern)
        init_pair(self.pair, self.pattern[self.index], 0)


class ColorManager:
    special_colors = []

    @staticmethod
    def create_special_colors():
        ColorManager.special_colors.append(
            SpecialColor(7, [ColorCodes.RED.value, ColorCodes.ORANGE.value, ColorCodes.YELLOW.value,
                             ColorCodes.GREEN.value, ColorCodes.BLUE.value, ColorCodes.PURPLE.value]))
        ColorManager.special_colors.append(
            SpecialColor(8, [ColorCodes.ORANGE.value, ColorCodes.YELLOW.value, ColorCodes.GREEN.value,
                             ColorCodes.BLUE.value, ColorCodes.PURPLE.value, ColorCodes.RED.value]))
        ColorManager.special_colors.append(
            SpecialColor(9, [ColorCodes.YELLOW.value, ColorCodes.GREEN.value, ColorCodes.BLUE.value,
                             ColorCodes.PURPLE.value, ColorCodes.RED.value, ColorCodes.ORANGE.value]))
        ColorManager.special_colors.append(
            SpecialColor(10, [ColorCodes.GREEN.value, ColorCodes.BLUE.value, ColorCodes.PURPLE.value,
                              ColorCodes.RED.value, ColorCodes.ORANGE.value, ColorCodes.YELLOW.value]))
        ColorManager.special_colors.append(
            SpecialColor(11, [ColorCodes.BLUE.value, ColorCodes.PURPLE.value, ColorCodes.RED.value,
                              ColorCodes.ORANGE.value, ColorCodes.YELLOW.value, ColorCodes.GREEN.value]))
        ColorManager.special_colors.append(
            SpecialColor(12, [ColorCodes.PURPLE.value, ColorCodes.RED.value, ColorCodes.ORANGE.value,
                              ColorCodes.YELLOW.value, ColorCodes.GREEN.value, ColorCodes.BLUE.value]))


    @staticmethod
    def update_special_colors():
        for sc in ColorManager.special_colors:
            sc.update_and_increment()

    @staticmethod
    def init_color_pairs():
        # Create Custom Colors
        init_color(17, 929, 439, 78)  # Orange

        # Create the initial color pairs
        init_pair(1, ColorCodes.RED.value, 0)      # Red
        init_pair(2, ColorCodes.ORANGE.value, 0)   # Orange
        init_pair(3, ColorCodes.YELLOW.value, 0)   # Yellow
        init_pair(4, ColorCodes.GREEN.value, 0)    # Green
        init_pair(5, ColorCodes.BLUE.value, 0)     # Blue
        init_pair(6, ColorCodes.PURPLE.value, 0)   # Purple
        init_pair(7, ColorCodes.RED.value, 0)      # RAINBOW [special]
        init_pair(8, ColorCodes.ORANGE.value, 0)   # RAINBOW [special]
        init_pair(9, ColorCodes.YELLOW.value, 0)   # RAINBOW [special]
        init_pair(10, ColorCodes.GREEN.value, 0)   # RAINBOW [special]
        init_pair(11, ColorCodes.BLUE.value, 0)    # RAINBOW [special]
        init_pair(12, ColorCodes.PURPLE.value, 0)  # RAINBOW [special]
