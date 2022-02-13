# SPDX-FileCopyrightText: Copyright (c) 2022 Randall Bohn (dexter)
#
# SPDX-License-Identifier: MIT
import random
import time
import board
import displayio
import rainbowio
import vectorio
from dexter_utils.vectorpixel import VectorPixel

"""Run on FunHouse or PyBadge"""
display = board.DISPLAY
main_group = displayio.Group()
display.show(main_group)

radius = 24
for x in range(0, display.width, radius):
    y = random.randrange(display.height)
    shader = displayio.Palette(1)
    shader[0] = 0x444444
    circle = vectorio.Circle(
        radius=random.randrange(12, radius), x=x, y=y, pixel_shader=shader
    )
    main_group.append(circle)

pixels = VectorPixel(main_group)
while True:
    time.sleep(0.2)
    color = rainbowio.colorwheel(time.monotonic() * 200 % 255)
    x = random.randrange(len(pixels))
    pixels[x] = color
