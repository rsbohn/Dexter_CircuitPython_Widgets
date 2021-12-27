# SPDX-FileCopyrightText: Copyright (c) 2021 Randall Bohn (dexter)
#
# SPDX-License-Identifier: MIT
"""BubblesWidget
Just for fun."""
# circup install adafruit_displayio_layout
# circup install adafruit_display_shapes
# circup install adafruit_fancyled
import random

from adafruit_display_shapes.circle import Circle
import adafruit_fancyled.adafruit_fancyled as fancy
from adafruit_displayio_layout.widgets.widget import Widget

september = [fancy.CRGB(255, 0, 0), fancy.CRGB(255, 240, 0), fancy.CRGB(128, 255, 0)]
ice = [
    fancy.CRGB(255, 255, 255),
    fancy.CRGB(240, 240, 240),
    fancy.CRGB(255, 255, 255),
    fancy.CRGB(128, 255, 255),
]
snow = [fancy.CRGB(255, 255, 255), fancy.CRGB(160, 192, 192)]
tms = [
    fancy.CRGB(0xD7, 0xB4, 0x54),
    fancy.CRGB(0x0A, 0x8C, 0x18),
    fancy.CRGB(0xFF, 0x5F, 0x4C),
]
red_blue = [fancy.CRGB(255, 0, 0), fancy.CRGB(0, 0, 255)]


class BubblesWidget(Widget):
    """
    A widget with n 'bubbles'.
    Add it to a GridLayout or other layout.
    Call animate() repeatedly.
    Bubbles move within the widget.
    """

    def __init__(self, n, gradient=None, **kwargs):
        gradient = gradient or snow
        super().__init__(**kwargs)
        self.max_bubble_radius = 6
        for _ in range(n):
            self.append(
                Circle(
                    30 + random.randint(-5, 5),
                    30 + random.randint(-5, 5),
                    6,
                    fill=fancy.palette_lookup(gradient, random.random()).pack(),
                )
            )

    def resize(self, new_width: int, new_height: int) -> None:
        """
        Sets self._width and self._height.
        Spread the bubbles across y.
        """

        super().resize(new_width, new_height)
        for shape in self:
            shape.x = random.randrange(0, new_width - self.max_bubble_radius)
            shape.y = random.randrange(0, new_height)

    def animate(self):
        """
        Move the bubbles.
        Wrap side-to-side or bottom-to-top.
        """
        for shape in self:
            shape.x += random.randint(-1, 1)
            shape.y += random.randint(0, 2)
            if shape.x < 0:
                shape.x = self._width - 1
            if shape.x > self._width - self.max_bubble_radius:
                shape.x = 1
            if shape.y > self._height:
                shape.y = 0
