import pygame
from pygame.locals import *

class KeyMapScreenGame():

    def __init__(self, settings, game_colors):

        self.fontsize = 10

        # KEYBOARD MAP
        self.keymapstr =  ["< : L     ARROW | MOVE LEFT      ",
                           "> : R     ARROW | MOVE RIGHT     ",
                           "  : DOWN ARROW  | DROP BLOCK     ",
                           "  : UP ARROW    | ROTATE BLOCK   ",
                           "      esc       | PAUSE GAME     ",
                           "     return     | SELECT         ",
                           "     shift      | SHOW GAME INFO "]

        self.keymapfont = pygame.font.Font(settings.FONT, self.fontsize)
        self.keymapcolor = game_colors[3]
        self.keymap = []
        self.keymap_pos = []
        _pos = 4
        for _str in self.keymapstr:
            _pos -= 1
            _render = self.keymapfont.render(_str, False, self.keymapcolor)
            self.keymap.append(_render)
            _x = settings.WINDOWWIDTH // 2 - _render.get_width() // 2
            _y = settings.WINDOWHEIGHT // 2 - _render.get_height() // 2 - settings.BLOCKSIZE * _pos
            self.keymap_pos.append((_x, _y))
            #_pos -= 1

        self.forwardslashstr = "/"
        self.forwardslashfont = pygame.font.Font(settings.FONT, self.fontsize)
        self.forwardslash = self.forwardslashfont.render(self.forwardslashstr, False, self.keymapcolor)

        self.backslashstr = "\\"
        self.backslashfont = pygame.font.Font(settings.FONT, self.fontsize)
        self.backslash = self.backslashfont.render(self.backslashstr, False, self.keymapcolor)

        # doesnt work ! :(
        _x1 = settings.WINDOWWIDTH // 2 - self.keymap_pos[2][0] // 2
        _y1 = settings.WINDOWHEIGHT // 2 - self.backslash.get_height() // 2 - settings.BLOCKSIZE * 1
        _x2 = settings.WINDOWWIDTH // 2 - self.keymap_pos[3][0] // 2
        _y2 = settings.WINDOWHEIGHT // 2 - self.backslash.get_height() // 2 - settings.BLOCKSIZE * -1
        self.forwardslash_pos = [[_x1, _y1], [_x2, _y2]]
        _x1 = settings.WINDOWWIDTH // 2 - self.keymap_pos[2][0] // 2
        _y1 = settings.WINDOWHEIGHT // 2 - self.backslash.get_height() // 2 - settings.BLOCKSIZE * 1
        _x2 = settings.WINDOWWIDTH // 2 - self.keymap_pos[3][0] // 2
        _y2 = settings.WINDOWHEIGHT // 2 - self.backslash.get_height() // 2 - settings.BLOCKSIZE * -1
        self.backslash_pos = [[_x1, _y1], [_x2, _y2]]


        # CONTROLLER MAP
        pass

    def keymap_screen_loop(self, settings, keywatch):

        if keywatch.select:
            keywatch.select = False
            keywatch.can_select = True
            #print("true")
            for _screen, _bool in settings.CURRENTSCREEN.items():
                if _screen == "SETTINGS":
                    settings.CURRENTSCREEN[_screen] = True
                else:
                    settings.CURRENTSCREEN[_screen] = False
