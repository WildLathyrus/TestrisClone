"""
    @author            ? ?
    @date_of_creation  July 8th, 2022
    @date_last_edit    July 8th, 2022
    @version           V1.13+
    @description       This file contains all the screens inwhich the user
                       will see. Previouse version these screen classes were
                       all seperate.

                        -> start screen
                        -> menu/settings screen
                        -> key info screen
                        -> pause screen
                        -> end screen
"""

import pygame
from pygame.locals import *

class StartScreenGame():

    def __init__(self, settings, game_colors, VERSION):

        # title font blit
        self.TITLESTR = "TETRIS"
        self.TITLEFONT = pygame.font.Font(settings.FONT, 30)
        self.TITLEFONTBOARDER = pygame.font.Font(settings.FONT, 35)
        self.TITLECOLOR = game_colors[2]
        self.TITLECOLORBOARDER = game_colors[1]
        self.title = self.TITLEFONT.render(self.TITLESTR, False, self.TITLECOLOR)
        self.titleboarder = self.TITLEFONTBOARDER.render(self.TITLESTR, False, self.TITLECOLORBOARDER)
        _x = settings.WINDOWWIDTH // 2 - self.title.get_width() // 2
        _y = settings.WINDOWHEIGHT // 10
        self.title_pos = (_x, _y)
        _x = settings.WINDOWWIDTH // 2 - self.titleboarder.get_width() // 2
        _y -= self.titleboarder.get_height() // 10
        self.title_boarder_pos = (_x, _y)

        # otions font blit
        # option 1 -> start
        self.option1str = "START"
        self.option1font = pygame.font.Font(settings.FONT, 20)
        self.option1color = game_colors[3]
        self.option1 = self.option1font.render(self.option1str, False, self.option1color)
        _x = settings.WINDOWWIDTH // 2 - self.option1.get_width() // 2
        _y = settings.WINDOWHEIGHT // 2 - self.option1.get_height() * 2
        self.option1_pos = (_x, _y)

        # option 2 -> Settings
        self.option2str = "SETTINGS"
        self.option2font = pygame.font.Font(settings.FONT, 17)
        self.option2color = game_colors[3]
        self.option2 = self.option2font.render(self.option2str, False, self.option2color)
        _x = settings.WINDOWWIDTH // 2 - self.option2.get_width() // 2
        _y = settings.WINDOWHEIGHT // 2# + self.option2.get_height()
        self.option2_pos = (_x, _y)

        # option 3 -> EXIT
        self.option3str = "EXIT"
        self.option3font = pygame.font.Font(settings.FONT, 20)
        self.option3color = game_colors[3]
        self.option3 = self.option3font.render(self.option3str, False, self.option3color)
        _x = settings.WINDOWWIDTH // 2 - self.option3.get_width() // 2
        _y = settings.WINDOWHEIGHT // 2 + self.option2.get_height() * 2
        self.option3_pos = (_x, _y)

        # option 3 -> EXIT
        self.option4str = StartScreenGame.versionStr(VERSION)
        self.option4font = pygame.font.Font(settings.FONT, 8)
        self.option4color = game_colors[3]
        self.option4 = self.option4font.render(self.option4str, False, self.option4color)
        _x = settings.WINDOWWIDTH - self.option4.get_width() * 1.15
        _y = settings.WINDOWHEIGHT - self.option4.get_height() * 1.25
        self.option4_pos = (_x, _y)

        #option select arros
        self.triangle_color = game_colors[3]
        self.option_select_pos = 0
        self.option_select_pos_max = 2

        self.triangle_leftstr = ">"
        self.triangle_leftfont = pygame.font.Font(settings.FONT, 20)
        self.triangle_left = self.triangle_leftfont.render(self.triangle_leftstr, False, self.triangle_color)
        _x1 = self.option1_pos[0] - self.triangle_left.get_width() * 1.5
        _y1 = self.option1_pos[1]
        _x2 = self.option2_pos[0] - self.triangle_left.get_width() * 1.5
        _y2 = self.option2_pos[1]
        _x3 = self.option3_pos[0] - self.triangle_left.get_width() * 1.5
        _y3 = self.option3_pos[1]
        self.tringale_leftpos = [(_x1, _y1), (_x2, _y2), (_x3, _y3)]

        self.triangle_rightstr = "<"
        self.triangle_rightfont = pygame.font.Font(settings.FONT, 20)
        self.triangle_right = self.triangle_rightfont.render(self.triangle_rightstr, False, self.triangle_color)
        _x1 = self.option1_pos[0] + self.option1.get_width() + self.triangle_right.get_width() * 0.5
        _y1 = self.option1_pos[1]
        _x2 = self.option2_pos[0] + self.option2.get_width() + self.triangle_right.get_width() * 0.5
        _y2 = self.option2_pos[1]
        _x3 = self.option3_pos[0] + self.option3.get_width() + self.triangle_right.get_width() * 0.5
        _y3 = self.option3_pos[1]
        self.tringale_rightpos = [(_x1, _y1), (_x2, _y2), (_x3, _y3)]

    @staticmethod
    def versionStr(version):
        version = str(version)
        returnVersion = "V"
        for i in version:
            returnVersion += "  "+ i
        return returnVersion

    def start_screen_loop(self, settings, keywatch):

        if keywatch.select:
            #keywatch.select = False
            keywatch.can_select = True
            if self.option_select_pos == 0:
                for _screen, _bool in settings.CURRENTSCREEN.items():
                    if _screen == "GAME":
                        settings.CURRENTSCREEN[_screen] = True
                    else:
                        settings.CURRENTSCREEN[_screen] = False

            elif self.option_select_pos == 1:
                for _screen, _bool in settings.CURRENTSCREEN.items():
                    if _screen == "SETTINGS":
                        settings.CURRENTSCREEN[_screen] = True
                    else:
                        settings.CURRENTSCREEN[_screen] = False

            elif self.option_select_pos == 2:
                settings.terminate()

        elif keywatch.move_rotate and self.option_select_pos > 0:
            self.option_select_pos -= 1
            keywatch.can_move_sound = True

        elif keywatch.move_down and self.option_select_pos < self.option_select_pos_max:
            self.option_select_pos += 1
            keywatch.can_move_sound = True

class SettingsScreenGame():

    def __init__(self, settings, game_colors, block):

        self.fontsize = 16
        # otions font blit
        # option 1 -> start
        self.option1titlestr = "CONTROLLS"
        self.option1titlefont = pygame.font.Font(settings.FONT, self.fontsize)
        self.option1titlecolor = game_colors[3]
        self.option1title = self.option1titlefont.render(self.option1titlestr, False, self.option1titlecolor)
        _x = settings.WINDOWWIDTH // 2 - self.option1title.get_width() // 2
        _y = settings.WINDOWHEIGHT // 2 - self.option1title.get_height() // 2 - settings.BLOCKSIZE * 4.25
        self.option1title_pos = (_x, _y)

        self.ONOFFCONTROLLER = 0 # 0 means keyboard and 1 means controller
        self.option1str = ["KEYBOARD", "CONTROLLER"]
        self.option1font = pygame.font.Font(settings.FONT, self.fontsize)
        self.option1color = game_colors[3]
        self.option1 = self.option1font.render(self.option1str[self.ONOFFCONTROLLER], False, self.option1color)
        _x = settings.WINDOWWIDTH // 2 - self.option1.get_width() // 2
        _y = settings.WINDOWHEIGHT // 2 - self.option1.get_height() // 2 - settings.BLOCKSIZE * 3
        self.option1_pos = (_x, _y)


        # option 2 -> Settings
        self.option2str = "CONTROL MAP"
        self.option2font = pygame.font.Font(settings.FONT, self.fontsize)
        self.option2color = game_colors[3]
        self.option2 = self.option2font.render(self.option2str, False, self.option2color)
        _x = settings.WINDOWWIDTH // 2 - self.option2.get_width() // 2
        _y = settings.WINDOWHEIGHT // 2 - self.option2.get_height() // 2 - settings.BLOCKSIZE * 1.5
        self.option2_pos = (_x, _y)

        # option 3 title -> VOLUME middle of the screen
        self.option3titlestr = "VOLUME"
        self.option3titlefont = pygame.font.Font(settings.FONT, self.fontsize)
        self.option3titlecolor = game_colors[3]
        self.option3title = self.option3titlefont.render(self.option3titlestr, False, self.option3titlecolor)
        _x = settings.WINDOWWIDTH // 2 - self.option3title.get_width() // 2
        _y = settings.WINDOWHEIGHT // 2 - self.option3title.get_height() // 2
        self.option3title_pos = (_x, _y)

        # option 3 -> VOLUME BARS
        self.volume = 3
        self.master_volume_control = 20
        self.master_volume = self.volume * self.master_volume_control # -> range 0.0 to 1.0
        self.option3str = ["     ", "|   ", "||   ", "|||  ", "|||| ","|||||"]
        self.maxvolume = len(self.option3str)
        self.option3font = pygame.font.Font(settings.FONT, self.fontsize)
        self.option3color = game_colors[3]
        self.option3 = self.option3font.render(self.option3str[self.volume], False, self.option3color)
        _x = settings.WINDOWWIDTH // 2 - self.option3.get_width() // 2
        _y = settings.WINDOWHEIGHT // 2 - self.option3.get_height() // 2 + settings.BLOCKSIZE * 1.25
        self.option3_pos = (_x, _y)

        # option 4 -> THEME TITLE
        self.option4titlestr = "THEMES"
        self.option4titlefont = pygame.font.Font(settings.FONT, self.fontsize)
        self.option4titlecolor = game_colors[3]
        self.option4title = self.option4titlefont.render(self.option4titlestr, False, self.option4titlecolor)
        _x = settings.WINDOWWIDTH // 2 - self.option4title.get_width() // 2
        _y = settings.WINDOWHEIGHT // 2 - self.option4title.get_height() // 2 + settings.BLOCKSIZE * 2.75
        self.option4title_pos = (_x, _y)

        # option 4 -> THEMES
        block.themeIdx = block.themeIdx
        self.option4str = block.blockThemeNames
        self.option4font = pygame.font.Font(settings.FONT, self.fontsize)
        self.option4color = game_colors[3]
        self.option4 = self.option4font.render(self.option4str[block.themeIdx], False, self.option4color)
        _x = settings.WINDOWWIDTH // 2 - self.option4.get_width() // 2
        _y = settings.WINDOWHEIGHT // 2 - self.option4.get_height() // 2 + settings.BLOCKSIZE * 4
        self.option4_pos = (_x, _y)

        # option 5 -> BACK TO MENU
        self.option5str = "MENU"
        self.option5font = pygame.font.Font(settings.FONT, self.fontsize)
        self.option5color = game_colors[3]
        self.option5 = self.option5font.render(self.option5str, False, self.option5color)
        _x = settings.WINDOWWIDTH // 2 - self.option5.get_width() // 2
        _y = settings.WINDOWHEIGHT // 2 - self.option5.get_height() // 2 + settings.BLOCKSIZE * 5.5
        self.option5_pos = (_x, _y)

        #option select arros
        self.triangle_color = game_colors[3]
        self.CONTROLLER = False

        self.triangle_leftstr = ">"
        self.triangle_leftfont = pygame.font.Font(settings.FONT, self.fontsize)
        self.triangle_left = self.triangle_leftfont.render(self.triangle_leftstr, False, self.triangle_color)
        _x1 = self.option1_pos[0] - self.triangle_left.get_width() * 1.5
        _y1 = self.option1_pos[1]
        _x2 = self.option2_pos[0] - self.triangle_left.get_width() * 1.5
        _y2 = self.option2_pos[1]
        _x3 = self.option3_pos[0] - self.triangle_left.get_width() * 1.5
        _y3 = self.option3_pos[1]
        _x4 = self.option4_pos[0] - self.triangle_left.get_width() * 1.5
        _y4 = self.option4_pos[1]
        _x5 = self.option5_pos[0] - self.triangle_left.get_width() * 1.5
        _y5 = self.option5_pos[1]
        self.tringale_leftpos = [[_x1, _y1], [_x2, _y2], [_x3, _y3], [_x4, _y4], [_x5, _y5]]

        self.triangle_rightstr = "<"
        self.triangle_rightfont = pygame.font.Font(settings.FONT, self.fontsize)
        self.triangle_right = self.triangle_rightfont.render(self.triangle_rightstr, False, self.triangle_color)
        _x1 = self.option1_pos[0] + self.option1.get_width() + self.triangle_right.get_width() * 0.5
        _y1 = self.option1_pos[1]
        _x2 = self.option2_pos[0] + self.option2.get_width() + self.triangle_right.get_width() * 0.5
        _y2 = self.option2_pos[1]
        _x3 = self.option3_pos[0] + self.option3.get_width() + self.triangle_right.get_width() * 0.5
        _y3 = self.option3_pos[1]
        _x4 = self.option4_pos[0] + self.option4.get_width() + self.triangle_right.get_width() * 0.5
        _y4 = self.option4_pos[1]
        _x5 = self.option5_pos[0] + self.option5.get_width() + self.triangle_right.get_width() * 0.5
        _y5 = self.option5_pos[1]
        self.tringale_rightpos = [[_x1, _y1], [_x2, _y2], [_x3, _y3], [_x4, _y4], [_x5, _y5]]

        self.option_select_pos = 0
        self.option_select_pos_max = len(self.tringale_leftpos) - 1

    def settings_screen_loop(self, settings, keywatch, block):

        if keywatch.select:

            keywatch.can_select = True

            if self.option_select_pos == 0:
                if self.ONOFFCONTROLLER == 0:
                    self.ONOFFCONTROLLER = 1
                else:
                    self.ONOFFCONTROLLER = 0
                self.ONOFFCONTROLLER = 0

                self.option1 = self.option1font.render(self.option1str[self.ONOFFCONTROLLER], False, self.option1color)
                _x = settings.WINDOWWIDTH // 2 - self.option1.get_width() // 2
                _y = settings.WINDOWHEIGHT // 2 - self.option1.get_height() // 2 - settings.BLOCKSIZE * 3
                self.option1_pos = (_x, _y)
                self.tringale_leftpos[0][0] = self.option1_pos[0] - self.triangle_left.get_width() * 1.5
                self.tringale_rightpos[0][0] = self.option1_pos[0] + self.option1.get_width() + self.triangle_right.get_width() * 0.5

            # SWITCH SCREEN TO KEYMAP
            elif self.option_select_pos == 1:
                # CONTROLLER MAP
                for _screen, _bool in settings.CURRENTSCREEN.items():
                    if _screen == "KEYMAP":
                        settings.CURRENTSCREEN[_screen] = True
                    else:
                        settings.CURRENTSCREEN[_screen] = False

            # UPDATE VOLUME
            elif self.option_select_pos == 2:

                if self.volume == self.maxvolume - 1:
                    self.volume = 0
                    self.master_volume = 0
                else:
                    self.volume += 1
                    self.master_volume += self.master_volume_control

                self.option3 = self.option3font.render(self.option3str[self.volume], False, self.option3color)


            # UPDATE THEME
            elif self.option_select_pos == 3:
                # THEME CHANGE
                block.themeIdx += 1
                if block.themeIdx == len(self.option4str):
                    block.themeIdx = 0

                block.updateTheme()

                self.option4 = self.option4font.render(self.option4str[block.themeIdx], False, self.option4color)
                _x = settings.WINDOWWIDTH // 2 - self.option4.get_width() // 2
                _y = settings.WINDOWHEIGHT // 2 - self.option4.get_height() // 2 + settings.BLOCKSIZE * 4
                self.option4_pos = (_x, _y)

                keywatch.can_select = True

            # SWITCH BACK TO START SCREEN
            elif self.option_select_pos == 4:
                for _screen, _bool in settings.CURRENTSCREEN.items():
                    if _screen == "START":
                        settings.CURRENTSCREEN[_screen] = True
                    else:
                        settings.CURRENTSCREEN[_screen] = False

                self.option_select_pos = 0

        # KEY MAP USING THE ARROW KEYS
        elif (keywatch.move_left or keywatch.move_right) and self.option_select_pos == 1:
            # CONTROLLER MAP
            keywatch.can_select = True
            for _screen, _bool in settings.CURRENTSCREEN.items():
                if _screen == "KEYMAP":
                    settings.CURRENTSCREEN[_screen] = True
                else:
                    settings.CURRENTSCREEN[_screen] = False

        # UPDATE BLOCK THEME
        elif (keywatch.move_left or keywatch.move_right) and self.option_select_pos == 3:

            if keywatch.move_right: # right
                block.themeIdx += 1
                if block.themeIdx == len(self.option4str):
                    block.themeIdx = 0
                keywatch.move_right = False
            else: # left
                block.themeIdx -= 1
                if block.themeIdx < 0:
                    block.themeIdx = len(self.option4str)-1
                keywatch.move_left = False

            block.updateTheme()

            self.option4 = self.option4font.render(self.option4str[block.themeIdx], False, self.option4color)
            _x = settings.WINDOWWIDTH // 2 - self.option4.get_width() // 2
            _y = settings.WINDOWHEIGHT // 2 - self.option4.get_height() // 2 + settings.BLOCKSIZE * 4
            self.option4_pos = (_x, _y)

            keywatch.can_select = True

        elif (keywatch.move_left or keywatch.move_right) and self.option_select_pos == 2:

            if keywatch.move_left and self.volume > 0:
                self.volume -= 1
                self.master_volume -= self.master_volume_control
                keywatch.move_left = False

            elif keywatch.move_right and self.volume < 5:
                self.volume += 1
                self.master_volume += self.master_volume_control
                keywatch.move_right = False

            self.option3 = self.option3font.render(self.option3str[self.volume], False, self.option3color)
            keywatch.can_select = True

        elif keywatch.move_rotate and self.option_select_pos > 0:
            self.option_select_pos -= 1
            keywatch.can_move_sound = True
            #keywatch.move_rotate = False

        elif keywatch.move_down and self.option_select_pos < self.option_select_pos_max:
            self.option_select_pos += 1
            keywatch.can_move_sound = True

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

class EndScreen:
    """
    Some sort of end animation before the end score
    """
    def __init__(self):
        pass

if __name__ == "__main__":
    pass
