# SPDX-FileCopyrightText: Copyright (c) 2021 Randall Bohn (dexter)
#
# SPDX-License-Identifier: Unlicense

# Run me on the 3.5" TFT FeatherWing
# You can get ForkAwesome-42.pcf
# from https://emergent.unpythonic.net/01606790241
import time
import displayio

from adafruit_featherwing import tft_featherwing_35
from adafruit_displayio_layout.layouts.grid_layout import GridLayout
from dexter_widgets.glyph_widget import GlyphWidget

displayio.release_displays()
wing = tft_featherwing_35.TFTFeatherWing35()
display = wing.display

layout = GridLayout(
    x=0,
    y=0,
    width=display.width,
    height=display.height,
    grid_size=(3, 2),
    divider_lines=True,
)
display.show(layout)

single = (1, 1)
layout.add_content(GlyphWidget("\uF1B0"), (0, 0), single)
layout.add_content(GlyphWidget("\uF1EA"), (1, 0), single)
layout.add_content(GlyphWidget("\uF069"), (2, 0), (1, 2))
layout.add_content(GlyphWidget("\uF2CB"), (0, 1), (2, 1))

while True:
    time.sleep(0.1)
