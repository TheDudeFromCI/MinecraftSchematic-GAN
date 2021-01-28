import numpy as np


class ToBinary():
    def __call__(_, blocks):
        with np.nditer(blocks, op_flags=['readwrite']) as it:
            for x in it:
                x[...] = 1 if x > 0 else 0


class CenterCrop():
    def __init__(self, size):
        self.size = size

    def __call__(self, blocks):
        x, y, z = blocks.shape
        sizex, sizey, sizez = self.size
        startx, starty, startz = x // 2, y // 2, z // 2
        return blocks[startx:startx+sizex, startx:starty+sizey, startx:startz+sizez]
