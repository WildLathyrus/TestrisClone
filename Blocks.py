"""
    @author            Josh Page
    @date_of_creation  July 8th, 2022
    @date_last_edit    ?? ??, 2022
    @version           V1.14
    @description       all the block parameters:
                        -> name
                        -> color
                        -> rec
                        -> in play
                        -> in move
                        -> ratated position index
                        -> ratate positions

                        as-well-as color themes

                        SOULD THIS BE A JSON? or aleast the blocks

"""

import pygame
from pygame.locals import *

class GameBlocks():
    """
    This class contains all the block parameter and colors
    including the game board colors/ themes
    """

    # BLOCKS
    T_block = {
                        "name": "T Block",
                        "color": None,#pygame.Color('#e2a97e'),
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
                        "color": None,#pygame.Color('#cb8175'),
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
                        "color": None,#pygame.Color('#6d8d8a'),
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
                        "color": None,#pygame.Color('#655057'),
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
                        "color": None,#pygame.Color('#a8c8ab'),
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
                        "color": None,#pygame.Color('#f0cf8e'),
                        "pos": [(4,0),(5,0),(4,1),(5,1)],
                        "in_play": False,
                        "move_block": False,
                        "rec": None,
                        "rotate_pos": 0,
                        "rotate":[[(0,0,),(0,0,),(0,0,),(0,0,)]],
                    }
    S_block = {
                        "name": "S Block",
                        "color": None,#pygame.Color('#fbedcd'),
                        "pos": [(4,0),(5,0),(3,1),(4,1)],
                        "in_play": False,
                        "move_block": False,
                        "rec": None,
                        "rotate_pos": 0,
                        "rotate":[[(1,0),(0,1),(1,-2),(0,-1)],
                                  [(-1,0),(0,-1),(-1,2),(0,1)]],
                    }

    block_lst = [T_block, Z_block, I_block, J_block, L_block, O_block, S_block]

    #COLORS
    blockThemes = [
                    # https://lospec.com/palette-list/pastel-qt
                    # @auther polyphrog
                    # PASTEL QT PALETTE
                    [
                    pygame.Color('#e2a97e'),
                    pygame.Color('#cb8175'),
                    pygame.Color('#6d8d8a'),
                    pygame.Color('#655057'),
                    pygame.Color('#a8c8ab'),
                    pygame.Color('#f0cf8e'),
                    pygame.Color('#fbedcd')
                    ],

                    # from http://colormind.io/
                    # @auther ??
                    # MINT TEA
                    [
                    pygame.Color("#94a96a"),
                    pygame.Color("#A8E8BF"),
                    pygame.Color("#B9DFCA"),
                    pygame.Color("#7F9786"),
                    pygame.Color("#9CE3B7"),
                    pygame.Color("#7B656E"),
                    pygame.Color("#B6BFC6")
                    ],

                    # https://lospec.com/palette-list/midnight-ablaze
                    # @auther Inkpendude
                    # MIDNIGHT ABLAZE PALETTE
                    [
                    pygame.Color("#ff8274"),
                    pygame.Color("#d53c6a"),
                    pygame.Color("#7c183c"),
                    pygame.Color("#460e2b"),
                    pygame.Color("#31051e"),
                    pygame.Color("#1f0510"),
                    pygame.Color("#130208")
                    ],

                    # https://lospec.com/palette-list/cherry7
                    # @auther Mustard
                    # CHERRY7 PALETTE
                    [
                    pygame.Color("#ffdcde"),
                    pygame.Color("#ffb2b6"),
                    pygame.Color("#ff868d"),
                    pygame.Color("#f8414e"),
                    pygame.Color("#d22247"),
                    pygame.Color("#ad1544"),
                    pygame.Color("#760f42")
                    ],

                    # https://lospec.com/palette-list/sirens-at-night
                    # @auther avianAnnihilator
                    # SIRENS NIGHT PALETTE
                    [
                    pygame.Color("#daf2e9"),
                    pygame.Color("#95e0cc"),
                    pygame.Color("#39707a"),
                    pygame.Color("#23495d"),
                    pygame.Color("#1c2638"),
                    pygame.Color("#9b222b"),
                    pygame.Color("#f14e52")
                    ],

                    # https://lospec.com/palette-list/calm-sunset
                    # @auther Paulina Riva
                    # CALM SUNSET PALETTE
                    [
                    pygame.Color("#684971"),
                    pygame.Color("#a06389"),
                    pygame.Color("#cb7ca2"),
                    pygame.Color("#e1aea4"),
                    pygame.Color("#f9d8a1"),
                    pygame.Color("#ffecb2"),
                    pygame.Color("#fffcf1")
                    ],

                    # https://lospec.com/palette-list/pastel7
                    # @auther Alpha6
                    # PASTEL7 PALETTE
                    # changes name: PASTEL OG
                    [
                    pygame.Color("#484c57"),
                    pygame.Color("#877182"),
                    pygame.Color("#9e9c9e"),
                    pygame.Color("#eb8d95"),
                    pygame.Color("#f5beae"),
                    pygame.Color("#ffeaba"),
                    pygame.Color("#ffffff")
                    ],

                    # https://lospec.com/palette-list/deep-maze
                    # @auther Ryosuke
                    # DEEP MAZE PALETTE
                    [
                    pygame.Color("#f2ff66"),
                    pygame.Color("#9af089"),
                    pygame.Color("#38d88e"),
                    pygame.Color("#00be91"),
                    pygame.Color("#009a98"),
                    pygame.Color("#085562"),
                    pygame.Color("#001d2a")
                    ]
                 ]

    boardThemes = [
                    pygame.Color("#332f35"), # board_color
                    pygame.Color('#1f1c23'), # boarder_color
                    pygame.Color('#f2efe3'), # title_color
                    #pygame.Color('#e2ac69'), # title_color -> original title color
                    pygame.Color("#B6BFC6"), # font_color
                  ]

    blockThemeNames = ["PASTEL QT", "MINT TEA", "ABLAZE",
                       "CHERRY", "SIRENS", "SUNSET",
                       "PASTEL OG", "DEEP MAZE"]
    boardTheme = list()


    def __init__(self):
        self.themeIdx = 0
        self.updateTheme()

    def changeBlockTheme(self, idx=0):
        # the index in the selected theme from blockThemes
        if idx > len(self.blockThemes):
            idx = 0
            raise Exception(f"idx must be in range of the block themes list -> {0} to {len(self.blockThemes)-1}")

        for i in range(len(self.block_lst)):
            self.block_lst[i]["color"] = self.blockThemes[idx][i]

    def changeGameTheme(self, idx=0):
        self.boardTheme = self.boardThemes.copy()
        #self.boardTheme[2] = self.blockThemes[idx][0]

    def updateTheme(self):
        self.changeBlockTheme(self.themeIdx)
        self.changeGameTheme(self.themeIdx)

if __name__ == "__main__":
    pass
