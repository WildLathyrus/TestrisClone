"""
    @author            Josh Page
    @date_of_creation  July 8th, 2022
    @date_last_edit    ?? ??, 2022
    @version           V1.15
    @description       convert the Blocks file into a class

"""



import pygame
from pygame.locals import *

import Settings as set
import GameRules as gam
import Draw as draw
import Blocks as blocks

import DropBlocks as drop
import gameScreens as gs


class Main:

    VERSION = 1.15

    pygame.init()

    pygame.mixer.init()

    pygame.mouse.set_visible(False)

    block = blocks.GameBlocks()

    settings = set.Settings()
    keywatch = set.KeyInput()
    audio = set.SoundEffects()
    dropblocks = drop.UpdateDrop()

    startscreen = gs.StartScreenGame(settings, block.boardTheme, VERSION)
    settingsscreen = gs.SettingsScreenGame(settings, block.boardTheme, block)
    pausescreen = gs.PauseScreenGame(settings, block.boardTheme)
    keymapscreen = gs.KeyMapScreenGame(settings, block.boardTheme)

    new_game = True

    def __init__(self):
        return self.MainLoop()

    def MainLoop(self):
        # game loopl
        while True:

            if self.settings.CURRENTSCREEN["START"]:

                self.keywatch.events(self.settings)
                self.startscreen.start_screen_loop(self.settings, self.keywatch)
                self.dropblocks.update_drop(self.settings, self.startscreen, self.block.block_lst)

                self.audio.play_game_music(self.settings, self.keywatch)

                draw.draw_main(self.settings, self.startscreen, self.dropblocks, self.block.boardTheme)

            elif self.settings.CURRENTSCREEN["SETTINGS"]:

                self.keywatch.events(self.settings)
                self.settingsscreen.settings_screen_loop(self.settings, self.keywatch, self.block)
                self.dropblocks.update_drop(self.settings, self.startscreen, self.block.block_lst)

                self.audio.volume = self.settingsscreen.master_volume / 100
                self.audio.play_game_music(self.settings, self.keywatch)

                draw.draw_settings(self.settings, self.startscreen, self.settingsscreen, self.dropblocks, self.block.boardTheme)

            elif self.settings.CURRENTSCREEN["GAME"]:

                if self.new_game:
                    self.dropblocks.new_drops = True
                    self.new_game = False
                    self.audio.play_music = True
                    # setup new game
                    self.gamerules = gam.GameLoopUpdate(self.settings, self.block.boardTheme)

                self.keywatch.events(self.settings)

                self.gamerules.loop(self.settings, self.keywatch, self.block.block_lst)
                self.audio.play_game_music(self.settings, self.keywatch)
                self.new_game = self.gamerules.new_game

                draw.draw_game(self.settings, self.gamerules, self.block.boardTheme, self.keywatch.info)


            elif self.settings.CURRENTSCREEN["KEYMAP"]:

                self.keywatch.events(self.settings)
                self.keymapscreen.keymap_screen_loop(self.settings, self.keywatch)
                self.dropblocks.update_drop(self.settings, self.startscreen, self.block.block_lst)

                draw.draw_keymap(self.settings, self.settingsscreen, self.keymapscreen, self.dropblocks, self.startscreen, self.block.boardTheme)


            elif self.settings.CURRENTSCREEN["PAUSE"]:

                self.keywatch.events(self.settings)

                self.audio.pause_music = True
                self.audio.play_game_music(self.settings, self.keywatch)

                self.pausescreen.pause_screen_loop(self.settings, self.keywatch)
                self.new_game = self.pausescreen.new_game

                draw.draw_pause(self.settings, self.pausescreen, self.gamerules, self.block.boardTheme)

            elif self.settings.CURRENTSCREEN["END"]:

                self.keywatch.events(self.settings)

                self.gamerules.end_loop_update(self.settings, self.keywatch)
                self.audio.play_game_music(self.settings, self.keywatch)

                self.dropblocks.update_drop(self.settings, self.startscreen, self.block_lst)

                draw.draw_end(self.settings, self.gamerules, self.dropblocks, self.block.boardTheme)

                self.new_game = self.gamerules.new_game

            else:

                print("no screen selected")

                for _screen, _bool in self.settings.CURRENTSCREEN.items():
                    if _screen == "START":
                        self.settings.CURRENTSCREEN[_screen] = True
                    else:
                        self.settings.CURRENTSCREEN[_screen] = False

    def updateScreenThemes(self):
        pass




if __name__ == "__main__":
    Main()
