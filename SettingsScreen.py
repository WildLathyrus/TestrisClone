import pygame
from pygame.locals import *

class SettingsScreenGame():

    def __init__(self, settings, game_colors):
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

        # option 4 -> EXIT
        self.option4titlestr = "THEMES"
        self.option4titlefont = pygame.font.Font(settings.FONT, self.fontsize)
        self.option4titlecolor = game_colors[3]
        self.option4title = self.option4titlefont.render(self.option4titlestr, False, self.option4titlecolor)
        _x = settings.WINDOWWIDTH // 2 - self.option4title.get_width() // 2
        _y = settings.WINDOWHEIGHT // 2 - self.option4title.get_height() // 2 + settings.BLOCKSIZE * 2.75
        self.option4title_pos = (_x, _y)

        # option 5 -> BACK TO MENU
        self.theme = 0
        self.option4str = ["ORIGINAL"]
        self.option4font = pygame.font.Font(settings.FONT, self.fontsize)
        self.option4color = game_colors[3]
        self.option4 = self.option4font.render(self.option4str[self.theme], False, self.option4color)
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

    def settings_screen_loop(self, settings, keywatch):

        if keywatch.select:
            #keywatch.select = False
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

            elif self.option_select_pos == 1:
                # CONTROLLER MAP
                for _screen, _bool in settings.CURRENTSCREEN.items():
                    if _screen == "KEYMAP":
                        settings.CURRENTSCREEN[_screen] = True
                    else:
                        settings.CURRENTSCREEN[_screen] = False

            elif self.option_select_pos == 2:

                if self.volume == self.maxvolume - 1:
                    self.volume = 0
                    self.master_volume = 0
                else:
                    self.volume += 1
                    self.master_volume += self.master_volume_control

                self.option3 = self.option3font.render(self.option3str[self.volume], False, self.option3color)

            elif self.option_select_pos == 3:
                # THEME CHANGE
                """ change the color theme of the game. chang in the block.py file
                    DEFINITLLY DO LATE OR EVEN LAST """
                keywatch.can_select = True

            elif self.option_select_pos == 4:
                for _screen, _bool in settings.CURRENTSCREEN.items():
                    if _screen == "START":
                        settings.CURRENTSCREEN[_screen] = True
                    else:
                        settings.CURRENTSCREEN[_screen] = False

                self.option_select_pos = 0


        elif (keywatch.move_left or keywatch.move_right) and self.option_select_pos == 2:

            if keywatch.move_left and self.volume > 0:
                self.volume -= 1
                self.master_volume -= self.master_volume_control
                keywatch.can_select = True
                keywatch.move_left = False

            elif keywatch.move_right and self.volume < 5:
                self.volume += 1
                self.master_volume += self.master_volume_control
                keywatch.can_select = True
                keywatch.move_right = False


            self.option3 = self.option3font.render(self.option3str[self.volume], False, self.option3color)

        elif keywatch.move_rotate and self.option_select_pos > 0:
            self.option_select_pos -= 1
            keywatch.can_move_sound = True
            #keywatch.move_rotate = False

        elif keywatch.move_down and self.option_select_pos < self.option_select_pos_max:
            self.option_select_pos += 1
            keywatch.can_move_sound = True
            #keywatch.move_down = False


if __name__ == "__main__":
    pass
