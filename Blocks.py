import pygame
from pygame.locals import *

# BLOCKS
T_block = {
                    "name": "T Block",
                    "color": pygame.Color('#e2a97e'),
                    "pos": [(4,0), (3,1), (4,1), (5,1)],
                    "rec": None,
                    "in_play": False,
                    "move_block": False,
                    "rotate_pos": 0,
                    "rotate":[[(1,1),(1,-1),(0,0),(-1,1)],
                              [(-1,1),(1,1),(0,0),(-1,-1)],
                              [(-1,-1),(-1,1),(0,0),(1,-1)],
                              [(1,-1),(-1,-1),(0,0),(1,1)]],

                }
Z_block = {
                    "name": "Z Block",
                    "color": pygame.Color('#cb8175'),
                    "pos": [(3,0),(4,0),(4,1),(5,1)],
                    "in_play": False,
                    "move_block": False,
                    "rec": None,
                    "rotate_pos": 0,
                    "rotate":[[(2,-1),(1,0),(0,-1),(-1,0)],
                              [(-2,1),(-1,0),(0,1),(1,0)]],
                }
I_block = {
                    "name": "I Block",
                    "color": pygame.Color('#6d8d8a'),
                    "pos": [(3,0),(4,0),(5,0),(6,0)],
                    "in_play": False,
                    "move_block": False,
                    "rec": None,
                    #"move":[(2,2),(1,1),(0,0),(1,1)],
                    "rotate_pos": 0,
                    "rotate":[[(2,-2),(1,-1),(0,0),(-1,1)],
                              [(-2,2),(-1,1),(0,0),(1,-1)]],
                }
J_block = {
                    "name": "J Block",
                    "color": pygame.Color('#655057'),
                    "pos": [(3,0),(3,1),(4,1),(5,1)],
                    "in_play": False,
                    "move_block": False,
                    "rec": None,
                    "rotate_pos": 0,
                    "rotate":[[(2,0),(1,-1),(0,0),(-1,1)],
                              [(0,2),(1,1),(0,0),(-1,-1)],
                              [(-2,0),(-1,1),(0,0),(1,-1)],
                              [(0,-2),(-1,-1),(0,0),(1,1)]],
                }
L_block = {
                    "name": "L Block",
                    "color": pygame.Color('#a8c8ab'),
                    "pos": [(5,0),(3,1),(4,1),(5,1)],
                    "in_play": False,
                    "move_block": False,
                    "rec": None,
                    "rotate_pos": 0,
                    "rotate":[[(0,2),(1,-1),(0,0),(-1,1)],
                              [(-2,0),(1,1),(0,0),(-1,-1)],
                              [(0,-2),(-1,1),(0,0),(1,-1)],
                              [(2,0),(-1,-1),(0,0),(1,1)]],
                }
O_block = {
                    "name": "O Block",
                    "color": pygame.Color('#f0cf8e'),
                    "pos": [(4,0),(5,0),(4,1),(5,1)],
                    "in_play": False,
                    "move_block": False,
                    "rec": None,
                    "rotate_pos": 0,
                    "rotate":[[(0,0,),(0,0,),(0,0,),(0,0,)]],
                }
S_block = {
                    "name": "S Block",
                    "color": pygame.Color('#fbedcd'),
                    "pos": [(4,0),(5,0),(3,1),(4,1)],
                    "in_play": False,
                    "move_block": False,
                    "rec": None,
                    "rotate_pos": 0,
                    "rotate":[[(1,0),(0,1),(1,-2),(0,-1)],
                              [(-1,0),(0,-1),(-1,2),(0,1)]],
                }

block_lst = [T_block, Z_block, I_block,
                  J_block, L_block, O_block,
                  S_block]

#game board
board_color = pygame.Color("#332f35")
boarder_color = pygame.Color('#1f1c23')
title_color = pygame.Color('#e2a97e')
font_color = pygame.Color("#B6BFC6")

game_colors_1 = [board_color, boarder_color, title_color, font_color]
game_colors = [game_colors_1]


# sample colors
# https://lospec.com/palette-list/pastel-qt
# from http://colormind.io/
color1 = pygame.Color("#94a96a")
color2 = pygame.Color("#A8E8BF")
color3 = pygame.Color("#B9DFCA")
color4 = pygame.Color("#7F9786")
color5 = pygame.Color("#9CE3B7")
color6 = pygame.Color("#7B656E")
color7 = pygame.Color("#B6BFC6")

if __name__ == "__main__":
    print()
    pass
