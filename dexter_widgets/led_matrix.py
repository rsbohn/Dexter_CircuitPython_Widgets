# SPDX-FileCopyrightText: Copyright (c) 2022 Randall Bohn (dexter)
#
# SPDX-License-Identifier: MIT
"""Provides a simulated nxn LED Matrix"""
import displayio
import vectorio
from adafruit_display_shapes.rect import Rect
from adafruit_displayio_layout.widgets import widget
from dexter_utils.vectorpixel import VectorPixel

GRAY = 0x999999


def vpal(color):
    """Create a Pallet with one slot of the given color"""
    palette = displayio.Palette(1)
    palette[0] = color
    return palette


class LedMatrix(widget.Widget):
    """Container for an LedGrid of any size"""

    def __init__(self, *kwargs):
        super().__init__(*kwargs)
        self._background_color = GRAY
        self._background = Rect(0, 0, 20, 20, fill=self._background_color)
        self.append(self._background)
        self.grid = None

    def resize(self, new_width: int, new_height: int):
        """Resize widget to fit as needed"""
        self.remove(self._background)
        self._background = Rect(0, 0, new_width, new_height, self._background_color)
        self.append(self._background)
        if self.grid is None:
            self.grid = LedGrid4x4()
            self.append(self.grid)
        self.grid.resize(new_width, new_height)

    def pixels(self) -> VectorPixel:
        """Get the LedGrid shapes as a string of VectorPixels"""
        return VectorPixel(self.grid)


class LedGrid4x4(widget.Widget):
    """A uniform group of circles in four rows and four columns."""

    def __init__(self, *kwargs):
        super().__init__(*kwargs)
        self.color0 = 0x440000
        self.color1 = 0xFF0000

    def resize(self, new_width, new_height):
        """resize will reset all shapes in the grid"""
        super().resize(new_width, new_height)
        while len(self) > 0:
            self.pop()
        self._fill()

    def _fill(self):
        for n in range(16):
            r = self.height // 8
            lamp = vectorio.Circle(
                radius=r,
                x=r + n % 4 * self.width // 4,
                y=r + n // 4 * self.height // 4,
                pixel_shader=vpal(self.color0),
            )
            self.append(lamp)
