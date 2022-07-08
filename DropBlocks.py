import pygame
from pygame.locals import *

import time
import random

class DropBlock():

    def __init__(self, settings, block_lst):

        self.maxz = settings.BLOCKSIZE
        self.z = random.randint(0, self.maxz)
        self.rotatepos = random.randint(0,3)

        self.block_size = DropBlock.map(self.z, 0, self.maxz, settings.BLOCKSIZE // 3, settings.BLOCKSIZE)
        self.speed = DropBlock.map(self.z, 0, self.maxz, 0.05, 0.2)

        self.time = time.time()
        self.time_speed = random.randint(settings.COLUMN//2, settings.ROW//2) / 10

        self.block = random.choice(block_lst)
        self.color = self.block["color"]
        self.falling_blocks = []

        self.falling_block = {
                        "pos": None,
                        "rec": None,
                        "rotate": None,
                        }


        _x_pos = DropBlock.positive_or_negative() * random.randint(0,settings.COLUMN*1.5)
        _y_pos = -1 * random.randint(2, settings.COLUMN)

        # need to set random rotation
        _count = 0
        for pos in self.block["pos"]:
            _x, _y = pos
            _x *= self.block_size
            _y *= self.block_size
            _x += _x_pos * self.block_size
            _y += _y_pos * self.block_size
            _pos = pygame.math.Vector2(_x,_y)
            _rec = pygame.Rect(_pos,(self.block_size, self.block_size))
            self.falling_block["pos"] = _pos
            self.falling_block["rec"] = _rec
            self.falling_block['rotate'] = [row[_count] for row in self.block["rotate"]]

            self.falling_blocks.insert(0, self.falling_block.copy())

            _count += 1

        self.num_rotate = len(self.falling_block['rotate'])
        self.num_rotate_pos = 0
        self.rotate_pos = random.randint(-1,self.num_rotate)
        if self.rotate_pos != -1:
            for _rotate in range(self.rotate_pos):
                for _block in self.falling_blocks:
                    _block["pos"].x += _block['rotate'][_rotate][0]*self.block_size
                    _block["pos"].y += _block['rotate'][_rotate][1]*self.block_size
                    _block["rec"] = pygame.Rect(_block["pos"],(self.block_size, self.block_size))


    @staticmethod
    def map(x, in_min, in_max, out_min, out_max):

        """ Syntax

            map(value, fromLow, fromHigh, toLow, toHigh)

            Parameters

            value: the number to map.
            fromLow: the lower bound of the value’s current range.
            fromHigh: the upper bound of the value’s current range.
            toLow: the lower bound of the value’s target range.
            toHigh: the upper bound of the value’s target range."""

        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    @staticmethod
    def positive_or_negative():
        if random.random() < 0.5:
            return 1
        else:
            return -1

class UpdateDrop():

    def __init__(self):

        self.new_drops = False

        self.start_past_time = time.time()
        self.start_current_time = time.time()

        self.fall_block_lst = []
        self.new_block_select = 0.05 # original 0.5

    def update_drop(self, settings, start, block_lst):

        if self.new_drops:
            self.new_drops = False
            del self.fall_block_lst
            self.fall_block_lst = []

        if self.start_current_time - self.start_past_time > self.new_block_select \
                   and len(self.fall_block_lst) < 40:

            self.start_past_time = time.time()

            self.fall_block_lst.insert(0, DropBlock(settings, block_lst))
            self.fall_block_lst = sorted(self.fall_block_lst, key=lambda z:z.z)

        for _block in self.fall_block_lst:
            _pop_block = False
            if True:#self.start_current_time - _block.time > _block.time_speed:
                _block.time = time.time()
                for _rec in _block.falling_blocks:
                    #print(_rec["pos"].y, _block.block_size, _block.speed)

                    _rec["pos"].y += _block.speed
                    _rec["rec"] = pygame.Rect(_rec["pos"],(_block.block_size, _block.block_size))

                    if _rec["pos"].y > settings.WINDOWHEIGHT + settings.WINDOWHEIGHT // 3:
                        _pop_block = True

            if _pop_block:
                self.fall_block_lst.remove(_block)

        self.start_current_time = time.time()



if __name__ == "__main__":
    pass
