import pygame
from pygame.locals import *

from random import choice
import time
import json

class GameLoopUpdate:

    def __init__(self, settings, game_colors):
        self.next_block = None

        self.game_blocks_recs_in_play = []
        self.game_blocks_recs = []
        self.game_blocks_recs_only = []
        self.row_height = []

        self.new_block_bool = True
        self.new_game = False
        self.end_game_bool = False
        self.end_game_score_bool = False
        self.time_bool = False

        self.past_time = time.time() # input movement time
        self.game_time = time.time() # passive downward movement game time
        self.current_time = time.time()
        self.end_time = time.time()
        self.end_time_menu_time = time.time()

        self.level_speed = 0
        self.level = 0
        self.score = 0
        self.lines_made = 0
        self.game_speeds = [0.48, 0.43, 0.38, 0.33, 0.28, 0.23, 0.18, 0.13,
                            0.08, 0.06, 0.05, 0.04, 0.03, 0.02, 0.01]
        self.level_lines = 10
        self.current_level_lines = self.level_lines
        self.horiz_speed = 0.175
        self.drop_speed = 0.1
        self.instant_horiz_move = False
        self.block_removal = 0.5
        self.original_block_removal = self.block_removal
        self.end_time_menu = 10

        for _num in range(settings.ROW):
            self.row_height.append(_num * settings.BLOCKSIZE)

        self.highscore, self.date = GameLoopUpdate.load_high_score()
        self.highscore_str = GameLoopUpdate.str_a_number(self.highscore)

        # info test
        self.fontsize = 10
        self.test_font = pygame.font.Font(settings.FONT, self.fontsize)
        self.infocolor = game_colors[3]

        self.info_test1 = "NEXT BLOCK:"
        self.info1 = self.test_font.render(self.info_test1, False, self.infocolor)
        _x =  settings.BLOCKSIZE // 2
        _y = settings.BLOCKSIZE // 2 * 4
        self.info1_pos = (_x, _y)

        self.info_test1_var = ""
        self.info1_var = self.test_font.render(self.info_test1_var, False, self.infocolor)
        _x = settings.BLOCKSIZE // 2 + self.info1.get_width() * 0.75#settings.WINDOWWIDTH // 2 - self.info1.get_width() // 2 + self.info1.get_width()
        _y = settings.BLOCKSIZE // 2 * 4.25
        self.info1_var_pos = (_x, _y)

        self.info1_lst = [[self.info1, self.info1_pos],[self.info1_var, self.info1_var_pos]]

        self.info_test2 = "SCORE:"
        self.info2 = self.test_font.render(self.info_test2, False, self.infocolor)
        _x = settings.BLOCKSIZE // 2
        _y = settings.BLOCKSIZE // 2 * 2
        self.info2_pos = (_x, _y)

        self.info_test2_var = "000, 000"
        self.info2_var = self.test_font.render(self.info_test2_var, False, self.infocolor)
        _x = settings.WINDOWWIDTH // 2# - self.info2.get_width() // 2
        _y = settings.BLOCKSIZE // 2 * 2
        self.info2_var_pos = (_x, _y)

        self.info2_lst = [[self.info2, self.info2_pos],[self.info2_var, self.info2_var_pos]]

        self.info_test3 = "HIGH SCORE:"
        self.info3 = self.test_font.render(self.info_test3, False, self.infocolor)
        _x = settings.BLOCKSIZE // 2
        _y = settings.BLOCKSIZE // 2
        self.info3_pos = (_x, _y)

        self.info_test3_var = self.highscore_str
        self.info3_var = self.test_font.render(self.info_test3_var, False, self.infocolor)
        _x = settings.WINDOWWIDTH // 2# - self.info3.get_width() // 2
        _y = settings.BLOCKSIZE // 2
        self.info3_var_pos = (_x, _y)

        self.info3_lst = [[self.info3, self.info3_pos],[self.info3_var, self.info3_var_pos]]

        self.info_test4 = "LEVEL:"
        self.info4 = self.test_font.render(self.info_test4, False, self.infocolor)
        _x = settings.BLOCKSIZE // 2
        _y = settings.BLOCKSIZE // 2 * 3
        self.info4_pos = (_x, _y)

        self.info_test4_var = "00"
        self.info4_var = self.test_font.render(self.info_test4_var, False, self.infocolor)
        _x = settings.WINDOWWIDTH // 2# - self.info4.get_width() // 2
        _y = settings.BLOCKSIZE // 2 * 3
        self.info4_var_pos = (_x, _y)

        self.info4_lst = [[self.info4, self.info4_pos],[self.info4_var, self.info4_var_pos]]

        # GAME OVER
        self.gameovertitlestr = "GAME OVER"
        self.gameovertitlefont = pygame.font.Font(settings.FONT, 30)
        self.gameovertitlecolor = game_colors[3]
        self.gameovertitle = self.gameovertitlefont.render(self.gameovertitlestr, False, self.gameovertitlecolor)
        _x = settings.WINDOWWIDTH // 2 - self.gameovertitle.get_width() // 2
        _y = settings.WINDOWHEIGHT // 4 - self.gameovertitle.get_height() // 2
        self.gameovertitle_pos = (_x, _y)

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

        self.new_game = False

    @staticmethod
    def map(x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    @staticmethod
    def load_high_score():
        """ONLY READ THE JSON FILE"""
        _filename = "scores.json"
        _file = open(_filename)
        _data = json.load(_file)
        _highscore = _data["highscore"]
        _date = _data["date_time"]
        _file.close()
        return _highscore, _date

    @staticmethod
    def str_a_number(number):
        str_num = str(number)
        if len(str_num) == 2:
            str_num = "000, 0" + str_num
        if len(str_num) == 3:
            str_num = "000, " + str_num
        elif len(str_num) == 4:
            str_num = "00" + str_num[0] + ", " + str_num[1:]
        elif len(str_num) == 5:
            str_num = "0" + str_num[:2] + ", " + str_num[2:]
        elif len(str_num) == 6:
            str_num = str_num[:3] + ", " + str_num[3:]
        else:
            str_num = "000, 00" + str_num
        return str_num

    def loop(self, settings, keywatch, block_lst):

        def game_over_update(self):
            """READS AND WRITES THE JSON FILE"""
            # update json file with highscore and date & time
            _new_score = self.highscore
            _filename = "scores.json"
            with open(_filename, "r") as _file:
                _data = json.load(_file)
            _file.close()

            _data["highscore"] = _new_score
            _data["date_time"] = time.asctime( time.localtime(time.time()))
            _new_data = _data.copy()

            with open(_filename, "w") as file:
                json.dump(_new_data, file, indent = 6)
            _file.close()

            self.new_game = True

        def update_info(self):

            level_str = str(self.level)
            if len(level_str) == 1:
                level_str = "0" + level_str

            # SCORE
            _render, _pos = self.info2_lst[1]
            self.info2_lst.pop(-1)
            self.info_test2_var = GameLoopUpdate.str_a_number(self.score)
            _render = self.test_font.render(self.info_test2_var, False, self.infocolor)
            _x = settings.WINDOWWIDTH // 2
            _y = settings.BLOCKSIZE // 2 * 2
            _pos = (_x, _y)
            self.info2_lst.append([_render, _pos])

            # HIGHSCORE
            _render, _pos = self.info3_lst[1]
            self.info3_lst.pop(-1)
            self.info_test3_var = GameLoopUpdate.str_a_number(self.highscore)
            _render = self.test_font.render(self.info_test3_var, False, self.infocolor)
            _x = settings.WINDOWWIDTH // 2
            _y = settings.BLOCKSIZE // 2
            _pos = (_x, _y)
            self.info3_lst.append([_render, _pos])

            # LEVEL
            _render, _pos = self.info4_lst[1]
            self.info4_lst.pop(-1)
            self.info_test4_var = level_str
            _render = self.test_font.render(self.info_test4_var, False, self.infocolor)
            _x = settings.WINDOWWIDTH // 2
            _y = settings.BLOCKSIZE // 2 * 3
            _pos = (_x, _y)
            self.info4_lst.append([_render, _pos])


        def calculatre_score_level(self, num_lines_cleared):
            self.lines_made += num_lines_cleared
            self.score += 40 * (num_lines_cleared + 1)

            if self.lines_made > self.current_level_lines:
                if self.current_level_lines != 100:
                    self.current_level_lines += self.level_lines
                if self.level != len(self.game_speeds):
                    self.level += 1
                if self.level_speed >= 29:
                    self.level_speed += 1
            # check curren score against high score
            if self.score > self.highscore: self.highscore = self.score


        def lines(self, settings):
            _lines_made = []
            _y_pos_lst = []
            for _block in self.game_blocks_recs:
                _y_pos_lst.append(_block["rec"].y)

            for _row in self.row_height:
                if _y_pos_lst.count(_row) == settings.COLUMN:
                    _lines_made.append(_row)

            if len(_lines_made) > 0:

                if len(_lines_made) == 4:
                    keywatch.tetris_clear = True
                else:
                    keywatch.line_clear = True

                calculatre_score_level(self, len(_lines_made))
                update_info(self)

                _new_game_blocks_recs = []
                _new_game_blocks_recs_only = []

                for _block in self.game_blocks_recs:

                    if _block["rec"].y not in _lines_made:

                        for _line in _lines_made:

                            if _block["rec"].y < _line:
                                _block["rec"].y += settings.BLOCKSIZE

                        _new_game_blocks_recs.append(_block)
                        _new_game_blocks_recs_only.append(_block["rec"])

                del self.game_blocks_recs
                del self.game_blocks_recs_only

                self.game_blocks_recs = _new_game_blocks_recs
                self.game_blocks_recs_only = _new_game_blocks_recs_only

        def vertical_movement(settings):

            _bottom_collision_bool = False

            for _block in self.game_blocks_recs_in_play:
                _future_rec = _block["rec"].copy()
                _future_rec.y += settings.BLOCKSIZE

                if _future_rec.y == settings.WINDOWHEIGHT or \
                    _future_rec.collidelistall(self.game_blocks_recs_only):
                    _bottom_collision_bool = True

            if _bottom_collision_bool:

                for _block in self.game_blocks_recs_in_play:
                    self.game_blocks_recs.append(_block)
                    self.game_blocks_recs_only.append(_block["rec"])
                    #print(_block["rec"].x, _block["rec"].y)
                del self.game_blocks_recs_in_play
                self.game_blocks_recs_in_play = []
                self.new_block_bool = True
                keywatch.move_down = False
                keywatch.block_placed = True

            else:

                for _block in self.game_blocks_recs_in_play:
                    _block["rec"].y += settings.BLOCKSIZE

        def horizontal_movement(keywatch, settings):

            _side_collision_bool = False

            if keywatch.move_right:
                for _block in self.game_blocks_recs_in_play:
                    _future_rec = _block["rec"].copy()
                    _future_rec.x += settings.BLOCKSIZE

                    if _future_rec.x == settings.WINDOWWIDTH or \
                         _future_rec.collidelistall(self.game_blocks_recs_only):
                        _side_collision_bool = True

                if not _side_collision_bool:

                    for _block in self.game_blocks_recs_in_play:
                        _block["rec"].x += settings.BLOCKSIZE

            elif keywatch.move_left:

                for _block in self.game_blocks_recs_in_play:
                    _future_rec = _block["rec"].copy()
                    _future_rec.x -= settings.BLOCKSIZE

                    if _future_rec.x < 0 or \
                         _future_rec.collidelistall(self.game_blocks_recs_only):
                        _side_collision_bool = True

                if not _side_collision_bool:

                    for _block in self.game_blocks_recs_in_play:
                        _block["rec"].x -= settings.BLOCKSIZE

        def rotate_movement(settings):

            _side_collision_bool = False

            for _block in self.game_blocks_recs_in_play:

                _future_rec = _block["rec"].copy()

                _future_rec.x += _block["rotate"][_block["rotate_pos"]][0]*settings.BLOCKSIZE
                _future_rec.y += _block["rotate"][_block["rotate_pos"]][1]*settings.BLOCKSIZE

                """Check collsions (boarder, other rec's)"""
                # if _future_rec.x < 0 or _future_rec.x == settings.WINDOWWIDTH or \
                #                              _future_rec.y < 0 or _future_rec.collidelistall(self.game_blocks_recs_only):
                if _future_rec.x < 0 or _future_rec.x == settings.WINDOWWIDTH or \
                             _future_rec.collidelistall(self.game_blocks_recs_only):
                    _side_collision_bool = True

            if not _side_collision_bool:

                for _block in self.game_blocks_recs_in_play:

                    _future_rec = _block["rec"].copy()

                    _future_rec.x += _block["rotate"][_block["rotate_pos"]][0]*settings.BLOCKSIZE
                    _future_rec.y += _block["rotate"][_block["rotate_pos"]][1]*settings.BLOCKSIZE

                    _block["rec"] = _future_rec

                    if _block["rotate_pos"] == _block["max_rotate"] - 1:
                        _block["rotate_pos"] = 0
                    else:
                        _block["rotate_pos"] += 1

                keywatch.can_rotate = True


        """New BLOCK in play"""
        if self.new_block_bool:

            lines(self, settings)

            if self.next_block == None:
                _block = choice(block_lst)
                self.next_block = choice(block_lst)
            else:
                _block = self.next_block
                self.next_block = choice(block_lst)
            #_block = block_lst[6]
            self.new_block_bool = False
            # check inplay block collition on board
            #print(self.next_block)
            _count = 0
            for pos in _block["pos"]:
                _x, _y = pos
                _rec = pygame.Rect((_x*settings.BLOCKSIZE, _y*settings.BLOCKSIZE),
                                   (settings.BLOCKSIZE, settings.BLOCKSIZE))
                _dic = {
                        "name": _block["name"],
                        "rec": _rec,
                        "color": _block["color"],
                        "in_play": True,
                        "rotate":[row[_count] for row in _block["rotate"]] ,
                        "rotate_pos": 0,
                        "max_rotate": len(_block["rotate"]),
                        }

                # condition to check GAME OVER !!!!!!!!!!!
                if _rec.collidelistall(self.game_blocks_recs_only):
                    self.end_game_bool = True

                self.game_blocks_recs_in_play.append(_dic)

                _count += 1

        elif not self.new_block_bool and self.end_game_bool:

            self.end_game_bool = False
            game_over_update(self)

            for _end_block in self.game_blocks_recs_in_play:
                self.game_blocks_recs.append(_end_block)

            keywatch.end = True

            for _screen, _bool in settings.CURRENTSCREEN.items():
                if _screen == "END":
                    settings.CURRENTSCREEN[_screen] = True
                else:
                    settings.CURRENTSCREEN[_screen] = False


        else:

            if keywatch.move_rotate:
                rotate_movement(settings)
                keywatch.move_rotate = False

            if keywatch.move_left:
                if self.current_time - self.past_time > self.horiz_speed or  \
                                                           keywatch.toggle_left:
                    keywatch.toggle_left = False
                    self.past_time = time.time()
                    horizontal_movement(keywatch, settings)

            if keywatch.move_right:
                if self.current_time - self.past_time > self.horiz_speed or \
                                                          keywatch.toggle_right:
                    keywatch.toggle_right = False
                    self.past_time = time.time()
                    horizontal_movement(keywatch, settings)

            if keywatch.move_down:
                if self.current_time - self.past_time > self.drop_speed:
                    self.past_time = time.time()
                    vertical_movement(settings)

            if keywatch.pause:
                keywatch.pause = False
                for _screen, _bool in settings.CURRENTSCREEN.items():
                    if _screen == "PAUSE":
                        settings.CURRENTSCREEN[_screen] = True
                    else:
                        settings.CURRENTSCREEN[_screen] = False

            if self.current_time - self.game_time > self.game_speeds[self.level_speed]:
                self.game_time = time.time()
                vertical_movement(settings)

            self.current_time = time.time()

    def end_loop_update(self, settings, keywatch):

        if self.end_game_score_bool:


            #keywatch.select = True

            if keywatch.move_right:
                # RESTART
                self.new_game = True
                keywatch.can_select = False
                for _screen, _bool in settings.CURRENTSCREEN.items():
                    if _screen == "START":
                        settings.CURRENTSCREEN[_screen] = True
                    else:
                        settings.CURRENTSCREEN[_screen] = False

            elif keywatch.move_left:
                # MENU

                self.new_game = True
                keywatch.can_select = False
                for _screen, _bool in settings.CURRENTSCREEN.items():
                    if _screen == "GAME":
                        settings.CURRENTSCREEN[_screen] = True
                    else:
                        settings.CURRENTSCREEN[_screen] = False

        else:

            if self.current_time - self.end_time > self.block_removal:

                if len(self.game_blocks_recs) == 0:

                    self.end_game_score_bool = True
                    self.time_bool = False
                    keywatch.highscore = True

                    self.highscore, self.date = GameLoopUpdate.load_high_score()

                    self.fontsize = 18

                    # SCORE ____________________________________________________
                    _text = "SCORE: " + GameLoopUpdate.str_a_number(self.score)
                    _render = self.test_font.render(_text, False, self.infocolor)
                    _x = settings.WINDOWWIDTH // 2 - _render.get_width() // 2
                    _y = self.gameovertitle_pos[1] + self.gameovertitle.get_height() + settings.BLOCKSIZE
                    _pos = (_x, _y)
                    _lst = [_render, _pos]
                    del self.info2_lst
                    self.info2_lst = [_lst]

                    # HIGHSCORE ________________________________________________
                    _text = "HIGH SCORE: " + GameLoopUpdate.str_a_number(self.highscore)
                    _render = self.test_font.render(_text, False, self.infocolor)
                    _x = settings.WINDOWWIDTH // 2 - _render.get_width() // 2
                    _y = self.gameovertitle_pos[1] + self.gameovertitle.get_height() + settings.BLOCKSIZE * 2
                    _pos = (_x, _y)
                    _lst = [_render, _pos]

                    # DATE AND TIME
                    self.info5_text_time = self.date
                    self.info5_time = self.test_font.render(self.info5_text_time, False, self.infocolor)
                    _x = settings.WINDOWWIDTH // 2 - self.info5_time.get_width() // 2
                    _y = self.gameovertitle_pos[1] + self.gameovertitle.get_height() + settings.BLOCKSIZE * 3
                    self.info5_time_pos = (_x, _y)
                    lst3 = [self.info5_time, self.info5_time_pos]
                    del self.info3_lst
                    self.info3_lst = [_lst, lst3]

                    # LEVEL ____________________________________________________
                    level_str = str(self.level)
                    if len(level_str) == 1:
                        level_str = "0" + level_str

                    _text = "LEVEL:  " + level_str
                    _render = self.test_font.render(_text, False, self.infocolor)
                    _x = settings.WINDOWWIDTH // 2 - _render.get_width() // 2
                    _y = self.gameovertitle_pos[1] + self.gameovertitle.get_height() + settings.BLOCKSIZE * 4
                    _pos = (_x, _y)
                    _lst = [_render, _pos]
                    del self.info4_lst
                    self.info4_lst = [_lst]

                else:

                    _pop_block = choice(self.game_blocks_recs)
                    self.game_blocks_recs.remove(_pop_block)

                    self.end_time = time.time()

                    if self.block_removal > 0.05:

                        self.block_removal -= GameLoopUpdate.map(self.block_removal, 0, self.original_block_removal, 0.01, 0.1)


            self.current_time = time.time()




if __name__ == "__main__":

    # xs_num = 67
    # s_num = 999
    # m_num = 1589
    # l_num = 34876
    # xl_num = 185763
    #
    # str_num = str(xs_num)
    #
    # if len(str_num) == 3:
    #     str_num = "000," + str_num
    # elif len(str_num) == 4:
    #     str_num = "00" + str_num[0] + "," + str_num[1:]
    # elif len(str_num) == 5:
    #     str_num = "0" + str_num[:2] + "," + str_num[2:]
    # elif len(str_num) == 6:
    #     str_num = str_num[:3] + "," + str_num[3:]
    # else:
    #     str_num = "000,0" + str_num
    #
    # print(str_num)
    #
    # _new_score = 0
    #
    # # Read file content
    # _filename = "scores.json"
    # # _file = open(_filename)
    # # _data = json.load(_file)
    # # _file.close()
    # # print(_data)
    # with open(_filename, "r") as _file:
    #     #print(_file)
    #     _data = json.load(_file)
    # _file.close()
    #
    # print(_data)
    #
    # # Update json object
    # _data["highscore"] = _new_score
    # _data["date_time"] = time.asctime( time.localtime(time.time()))
    # print(_data)
    # _new_data = _data.copy()
    #
    # #Write json file
    # with open(_filename, "w") as file:
    #     #json.dump(_date, file)
    #     json.dump(_new_data, file, indent = 6)
    #     pass
    # _file.close()
    #
    #
    #
    # # localtime = time.asctime( time.localtime(time.time()))
    # # print( "Local current time :", localtime)


    pass


# {
#     "highscore": 0,
#     "date_time": null
# }
