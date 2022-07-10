"""
    @author            ? ?
    @date_of_creation  July 8th, 2022
    @date_last_edit    July 8th, 2022
    @version           V?.?? -> from my original code before recording versions
    @description       This file is for all the backround game managment
                        -> setup settings
                        -> terminate program
                        -> sound and sound event triggers
                        -> keyinput and key event triggers
"""


import pygame
from pygame.locals import *

import sys
import time

class Settings:

    def __init__(self):

        self.SCALE = 80 * 2 //3
        self.RATIO =  [(16,9), (21,9), (4,3)]
        self.RATIOIDX = 0
        # self.WINDOWWIDTH = self.RATIO[self.RATIOIDX][0] * self.SCALE
        # self.WINDOWHEIGHT = self.RATIO[self.RATIOIDX][1] * self.SCALE
        #self.BOARDOFFSET = [0,0]
        self.BLOCKSIZE = 30
        self.ROW, self.COLUMN = 20, 10
        self.WINDOWWIDTH = self.BLOCKSIZE * self.COLUMN
        self.WINDOWHEIGHT = self.BLOCKSIZE * self.ROW
        self.WINDOWSIZE = (self.WINDOWWIDTH, self.WINDOWHEIGHT)

        self.screen = pygame.display.set_mode(self.WINDOWSIZE)
        #self.pygame.display.set_icon(WINDOWLOGO)
        pygame.display.set_caption(" T E T R I S ")

        pygame_icon = pygame.image.load("images/tetris.png").convert()
        pygame.display.set_icon(pygame_icon)

        # off set the screen to make room for score or menu later on
        x_offset, y_offset = 0, 0

        self.FONT = "fonts\8-bit-pusab.ttf"

        # screen
        self.CURRENTSCREEN = {
                            "START": True,
                            "GAME": False,
                            "KEYMAP": False,
                            "SETTINGS": False,
                            "PAUSE": False,
                            "END": False,
                            }

    @classmethod
    def terminate(cls):
        pygame.time.delay(500)
        pygame.quit()
        sys.exit()

class SoundEffects():

    def __init__(self):
        _music1_filename = "audio/1 - Music 1.1.mp3"
        _music2_filename = "audio/2 - Music 2.mp3"
        _music3_filename = "audio/3 - Music 3.mp3"
        _curser_filename = "audio/SFX 2.mp3"
        _select_filename = "audio/SFX 3.mp3"
        _move_block_filename = "audio/SFX 4.mp3"
        _place_block_filename = "audio/SFX 8.mp3"
        _rotate_block_filename = "audio/SFX 6.mp3"
        _line_clear_filename = "audio/SFX 11.mp3"
        _tetris_clear_filename = "audio/tetris clear.mp3"
        _end_filename = "audio/SFX 14.mp3"
        _highscore = "audio/6 - High Score (Tetris Master).mp3"

        # print('init =', pygame.mixer.get_init())
        # print('channels =', pygame.mixer.get_num_channels())

        _music1 = pygame.mixer.Sound(_music1_filename)
        _music2 = pygame.mixer.Sound(_music2_filename)
        _music3 = pygame.mixer.Sound(_music3_filename)

        _curser = pygame.mixer.Sound(_curser_filename)
        _select = pygame.mixer.Sound(_select_filename)

        _move_block = pygame.mixer.Sound(_move_block_filename)
        _place_block = pygame.mixer.Sound(_place_block_filename)
        _rotate_block = pygame.mixer.Sound(_rotate_block_filename)

        _line_clear = pygame.mixer.Sound(_line_clear_filename)
        _tetris_clear = pygame.mixer.Sound(_tetris_clear_filename)

        _end = pygame.mixer.Sound(_end_filename)
        _highscore = pygame.mixer.Sound(_highscore)

        self.music_channel = pygame.mixer.Channel(0)
        self.curser_channel = pygame.mixer.Channel(1)
        self.rotate_channel = pygame.mixer.Channel(2)
        self.place_channel = pygame.mixer.Channel(3)
        self.end_channel = pygame.mixer.Channel(4)

        self.music_lst = [_music1, _music2, _music3]
        self.music_select = 0
        self.curser = _curser
        self.select = _select
        self.move_block = _move_block
        self.place_block = _place_block
        self.rotate_block = _rotate_block
        self.end = _end
        self.highscore = _highscore

        self.line_clear = _line_clear
        self.tetris_clear = _tetris_clear

        self.play_music = False
        self.pause_music = False

        self.volume = 0.6 # -> range 0.0 to 1.0 float
        # self.curser_move = False
        # self.curser_select = False

    def play_game_music(self, settings, keywatch):

        if (settings.CURRENTSCREEN["START"] or settings.CURRENTSCREEN["GAME"]) and keywatch.end_end:

            if (keywatch.move_right or keywatch.move_left) and keywatch.end_end:
                keywatch.end_end = False
                self.end_channel.set_volume(self.volume)
                self.end_channel.pause()
                self.curser_channel.set_volume(self.volume)
                self.curser_channel.play(self.select)


        if self.play_music and not settings.CURRENTSCREEN["END"]:
            self.play_music = False
            self.music_channel.set_volume(self.volume)
            self.music_channel.play(self.music_lst[self.music_select], loops = -1)
            #print(self.music_channel.get_volume())
        else:
            if self.pause_music and settings.CURRENTSCREEN["PAUSE"]:
                #self.music_lst[self.music_select].pause()
                #print(keywatch.move_left, keywatch.move_right)
                self.music_channel.pause()
            elif self.pause_music and settings.CURRENTSCREEN["GAME"]:
                self.pause_music = False
                self.music_channel.unpause()

        if settings.CURRENTSCREEN["START"] and keywatch.can_move_sound and \
                                   (keywatch.move_down or keywatch.move_rotate):

            self.curser_channel.set_volume(self.volume)
            self.curser_channel.play(self.curser)
            keywatch.move_down, keywatch.move_rotate = False, False
            keywatch.can_move_sound = False

        if settings.CURRENTSCREEN["SETTINGS"] and keywatch.can_move_sound and \
                                   (keywatch.move_down or keywatch.move_rotate):
            self.curser_channel.set_volume(self.volume)
            self.curser_channel.play(self.curser)
            keywatch.move_down, keywatch.move_rotate = False, False
            keywatch.can_move_sound = False

        if keywatch.can_select == True and not settings.CURRENTSCREEN["END"]:
            self.curser_channel.set_volume(self.volume)
            self.curser_channel.play(self.select)
            keywatch.select = False
            keywatch.can_select = False

        if settings.CURRENTSCREEN["GAME"]:
            #print(self.curser_channel.get_busy())
            if (keywatch.move_right or keywatch.move_left) and not self.curser_channel.get_busy():
                self.curser_channel.set_volume(self.volume)
                self.curser_channel.play(self.move_block)

            if keywatch.can_rotate:
                self.rotate_channel.set_volume(self.volume)
                self.rotate_channel.play(self.rotate_block)
                keywatch.can_rotate = False

            if keywatch.block_placed:
                self.place_channel.set_volume(self.volume)
                self.place_channel.play(self.place_block)
                keywatch.block_placed = False

            if keywatch.line_clear:
                self.curser_channel.set_volume(self.volume)
                self.curser_channel.play(self.line_clear)
                keywatch.line_clear = False

            if keywatch.tetris_clear:
                self.curser_channel.set_volume(self.volume)
                self.curser_channel.play(self.tetris_clear)
                keywatch.tetris_clear = False

        if settings.CURRENTSCREEN["END"]:

            if keywatch.end:
                #print("first pass")
                self.music_channel.pause()
                self.end_channel.set_volume(self.volume)
                self.end_channel.play(self.end)
                keywatch.end = False

            if not self.end_channel.get_busy() and not keywatch.end and keywatch.highscore:
                #print("pass")
                self.end_channel.set_volume(self.volume)
                self.end_channel.play(self.highscore)
                keywatch.highscore = False
                keywatch.end_end = True




class KeyInput:

    def __init__(self):

        self.key_input = []

        self.move_down = False
        self.move_left = False
        self.move_right = False
        self.move_rotate = False

        self.toggle_right = False
        self.toogle_left = False

        self.select = False
        self.pause = False
        self.info = False

        # FOR AUDIO
        self.can_move_sound = False
        self.can_select = False
        self.can_rotate = False
        self.block_placed = False

        self.line_clear = False
        self.tetris_clear = False
        self.end = False
        self.highscore = False
        self.end_end = False

    def events(self, settings):

        for event in pygame.event.get():

            if event.type == QUIT:
                settings.terminate()

            if event.type == KEYDOWN:

                if event.key == K_ESCAPE:
                    self.pause = True

                elif (event.key == K_w or event.key == K_UP) and not self.move_rotate and \
                                                settings.CURRENTSCREEN["PAUSE"] == False:
                    self.move_rotate = True

                elif (event.key == K_a or event.key == K_LEFT) and not self.move_left:# and \
                                                #settings.CURRENTSCREEN["PAUSE"] == False:
                    self.toggle_left = True
                    self.move_left = True
                    #print('left')

                elif (event.key == K_d or event.key == K_RIGHT) and not self.move_right:# and \
                                                #settings.CURRENTSCREEN["PAUSE"] == False:
                    self.toggle_right = True
                    self.move_right = True
                    #print('right')

                elif (event.key == K_s or event.key == K_DOWN) and not self.move_down and \
                                                settings.CURRENTSCREEN["PAUSE"] == False:
                    self.move_down = True
                    #print('down')

                elif event.key == K_RETURN and not self.select:
                    self.select = True


                elif (event.key == K_RSHIFT or event.key == K_LSHIFT):
                    if self.info: self.info = False
                    else: self.info = True


            if event.type == KEYUP:

                if (event.key == K_a or event.key == K_LEFT):
                    self.toggle_left = False
                    self.move_left = False
                    #print('left_keyup')

                elif (event.key == K_d or event.key == K_RIGHT):
                    self.toggle_right = False
                    self.move_right = False
                    #print('right')

                elif (event.key == K_s or event.key == K_DOWN):
                    self.move_down = False
                    #print('down_keyup')

                elif event.key == K_RETURN:
                    self.select = False

                elif event.key == K_ESCAPE:
                    self.pause = False

                # elif event.key == K_RSHIFT or event.key == K_LSHIFT:
                #     self.info = False


if __name__ == "__main__":
    pass
