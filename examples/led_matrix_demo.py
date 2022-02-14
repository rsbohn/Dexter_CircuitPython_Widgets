# SPDX-FileCopyrightText: Copyright (c) 2022 Randall Bohn (dexter)
#
# SPDX-License-Identifier: MIT
import time
import board
import displayio
from dexter_widgets.led_matrix import LedMatrix

"""Run on FunHouse or PyBadge"""
display = board.DISPLAY
main_group = displayio.Group()
display.show(main_group)

margin = display.width // 2 - 64
matrix = LedMatrix(margin, margin)
matrix._background_color = 0x125690
matrix.resize(128, 128)
main_group.append(matrix)

color0 = 0x999900
color1 = 0xFFFF33
pixels = matrix.pixels()
pixels.fill(color0)
while True:
    for x in range(len(pixels)):
        pixels[x - 1] = color0
        pixels[x] = color1
        time.sleep(0.375)
