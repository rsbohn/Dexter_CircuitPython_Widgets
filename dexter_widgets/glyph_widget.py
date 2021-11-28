# SPDX-FileCopyrightText: Copyright (c) 2021 Randall Bohn (dexter)
#
# SPDX-License-Identifier: MIT
"""
`dexter_widgets.glyph_widget`

You can get ForkAwesome-42.pcf
from https://emergent.unpythonic.net/01606790241
"""

from adafruit_bitmap_font.bitmap_font import load_font
from adafruit_displayio_layout.widgets.widget import Widget
from adafruit_display_text.label import Label


__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/rsbohn/Dexter_CircuitPython_Widgets.git"

FONT = load_font("/fonts/forkawesome-42.pcf")


class GlyphWidget(Widget):
    """Provides a ForkAwesome glyph as a Widget."""

    def __init__(self, glyph: str, **kwargs):
        super().__init__(**kwargs)
        self.label = Label(FONT, text=glyph)
        self.label.anchor_point = 0.5, 0.5
        self.label.anchored_position = 21, 21
        self.append(self.label)

    def resize(self, new_width: int, new_height: int) -> None:
        """Resize the widget to a new width and height.
        Since the font size is fixed, we update the
        label's anchored_position.

        :param int new_width: requested maximum width
        :param int new_height: request maximum height
        :return: None
        """
        self.label.anchored_position = new_width // 2, new_height // 2
