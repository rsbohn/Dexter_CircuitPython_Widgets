# SPDX-FileCopyrightText: Copyright (c) 2022 Randall Bohn (dexter)
#
# SPDX-License-Identifier: MIT
"""
dexter_utils.vectorpixel

VectorIO shapes that act like NeoPixels.
"""
import displayio


class VectorPixel:
    """Turn a group of Vectorio shapes into a string of NeoPixel-like objects."""

    def __init__(self, group: displayio.Group):
        self.shaders = [item.pixel_shader for item in group]

    def fill(self, color):
        """Fill all with color"""
        for item in self.shaders:
            item[0] = color

    def show(self):
        """I do nothing"""

    def __len__(self) -> int:
        return len(self.shaders)

    def __getitem__(self, key: int):
        return self.shaders[key][0]

    def __setitem__(self, key, value):
        if isinstance(key, slice):
            for x, item in enumerate(value):
                self.shaders[x][0] = item
        else:
            self.shaders[key][0] = value
