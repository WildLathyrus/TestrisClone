import pygame
from pygame.locals import *

class StartScreenGame():

    def __init__(self, settings, game_colors):

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
        self.option4str = "V  1 . 1 2"
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
            #keywatch.move_down = False
        # print(self.option_select_pos)
        # print(keywatch.can_move_down, keywatch.can_move_up)



        # self.start_current_time = time.time()


if __name__ == "__main__":

    # for _ in range(10):
    #     _x_pos = DropBlock.positive_or_negative() * random.randint(0,5)
    #     print(_x_pos)
    pass
