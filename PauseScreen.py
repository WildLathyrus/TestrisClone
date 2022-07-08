import pygame
from pygame.locals import *

class PauseScreenGame():

    def __init__(self, settings, game_colors):

        # PAUSE
        self.pausetitlestr = "PAUSE"
        self.pausetitlefont = pygame.font.Font(settings.FONT, 30)
        self.pausetitlecolor = game_colors[3]
        self.pausetitle = self.pausetitlefont.render(self.pausetitlestr, False, self.pausetitlecolor)
        _x = settings.WINDOWWIDTH // 2 - self.pausetitle.get_width() // 2
        _y = settings.WINDOWHEIGHT // 2 - self.pausetitle.get_height() * 2
        self.pausetitle_pos = (_x, _y)

        # RESTART
        self.restartstr = "< :RESTART"
        self.restartfont = pygame.font.Font(settings.FONT, 10)
        self.restartcolor = game_colors[3]
        self.restarttitle = self.restartfont.render(self.restartstr, False, self.restartcolor)
        _x = settings.BLOCKSIZE // 3
        _y = settings.WINDOWHEIGHT - self.restarttitle.get_height() * 3/2
        self.restart_pos = (_x, _y)

        # MENU
        self.menustr = "MENU: >"
        self.menufont = pygame.font.Font(settings.FONT, 10)
        self.menucolor = game_colors[3]
        self.menutitle = self.menufont.render(self.menustr, False, self.menucolor)
        _x = settings.WINDOWWIDTH - self.menutitle.get_width() - settings.BLOCKSIZE // 3
        _y = settings.WINDOWHEIGHT - self.menutitle.get_height() * 3/2
        self.menu_pos = (_x, _y)

        self.paused_bool = False
        self.new_game = False

    def pause_screen_loop(self, settings, keywatch):

        if keywatch.pause:
            keywatch.pause = False
            for _screen, _bool in settings.CURRENTSCREEN.items():
                if _screen == "GAME":
                    settings.CURRENTSCREEN[_screen] = True
                else:
                    settings.CURRENTSCREEN[_screen] = False

        elif keywatch.move_right:
            # RESTART
            self.new_game = True
            keywatch.move_right = False
            print("PAUSE START")
            for _screen, _bool in settings.CURRENTSCREEN.items():
                if _screen == "START":
                    settings.CURRENTSCREEN[_screen] = True
                else:
                    settings.CURRENTSCREEN[_screen] = False

        elif keywatch.move_left:
            # MENU
            keywatch.move_left = False
            self.new_game = True
            print("PAUSE GAME")
            for _screen, _bool in settings.CURRENTSCREEN.items():
                if _screen == "GAME":
                    settings.CURRENTSCREEN[_screen] = True
                else:
                    settings.CURRENTSCREEN[_screen] = False

        #print(keywatch.move_right, keywatch.move_left, keywatch.move_rotate)


if __name__ == "__main__":
    pass
