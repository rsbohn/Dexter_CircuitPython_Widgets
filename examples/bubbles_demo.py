# SPDX-FileCopyrightText: Copyright (c) 2021 Randall Bohn (dexter)
#
# SPDX-License-Identifier: Unlicense

# Run me on the 3.5" TFT FeatherWing
import time
import board
import displayio

from adafruit_displayio_layout.layouts.grid_layout import GridLayout
from dexter_widgets.bubbles import BubblesWidget, september, snow, ice

if "DISPLAY" in dir(board):
    display = board.DISPLAY
else:
    from adafruit_featherwing import tft_featherwing_35

    displayio.release_displays()
    wing = tft_featherwing_35.TFTFeatherWing35()
    display = wing.display

layout = GridLayout(
    x=0,
    y=0,
    width=display.width,
    height=display.height,
    grid_size=(3, 1),
    divider_lines=True,
)
display.show(layout)

single = (1, 1)
september_bubbles = BubblesWidget(12, gradient=september)
layout.add_content(september_bubbles, (0, 0), single)
snow_bubbles = BubblesWidget(12, gradient=snow)
layout.add_content(snow_bubbles, (1, 0), single)
ice_bubbles = BubblesWidget(12, gradient=ice)
layout.add_content(ice_bubbles, (2, 0), single)

# from adafruit_bitmapsaver import save_pixels
# save_pixels("/sd/awesome.bmp", display)
while True:
    # time.sleep(0.01)
    september_bubbles.animate()
    snow_bubbles.animate()
    ice_bubbles.animate()
