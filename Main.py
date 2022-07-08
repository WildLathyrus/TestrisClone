import pygame
from pygame.locals import *

import Settings as set
import Blocks as block
import GameRules as gam
import Draw as draw

import DropBlocks as drop

import StartScreen as start
import SettingsScreen as option
import PauseScreen as pause
import KeyMappingScreen as key


class Main:

    pygame.init()
    pygame.mixer.init()

    pygame.mouse.set_visible(False)

    game_colors = block.game_colors[0]

    settings = set.Settings()
    keywatch = set.KeyInput()
    audio = set.SoundEffects()
    dropblocks = drop.UpdateDrop()

    startscreen = start.StartScreenGame(settings, game_colors)
    settingsscreen = option.SettingsScreenGame(settings, game_colors)
    pausescreen = pause.PauseScreenGame(settings, game_colors)
    keymapscreen = key.KeyMapScreenGame(settings, game_colors)

    new_game = True

    def __init__(self):
        return self.MainLoop()

    def MainLoop(self):
        # game loopl
        while True:

            if self.settings.CURRENTSCREEN["START"]:

                self.keywatch.events(self.settings)
                self.startscreen.start_screen_loop(self.settings, self.keywatch)
                self.dropblocks.update_drop(self.settings, self.startscreen, block.block_lst)

                self.audio.play_game_music(self.settings, self.keywatch)

                draw.draw_main(self.settings, self.startscreen, self.dropblocks, self.game_colors)

            elif self.settings.CURRENTSCREEN["SETTINGS"]:

                self.keywatch.events(self.settings)
                self.settingsscreen.settings_screen_loop(self.settings, self.keywatch)
                self.dropblocks.update_drop(self.settings, self.startscreen, block.block_lst)

                self.audio.volume = self.settingsscreen.master_volume / 100
                self.audio.play_game_music(self.settings, self.keywatch)

                draw.draw_settings(self.settings, self.startscreen, self.settingsscreen, self.dropblocks, self.game_colors)

            elif self.settings.CURRENTSCREEN["GAME"]:

                if self.new_game:
                    self.dropblocks.new_drops = True
                    self.new_game = False
                    self.audio.play_music = True
                    # setup new game
                    self.gamerules = gam.GameLoopUpdate(self.settings, self.game_colors)

                self.keywatch.events(self.settings)

                self.gamerules.loop(self.settings, self.keywatch, block.block_lst)
                self.audio.play_game_music(self.settings, self.keywatch)
                self.new_game = self.gamerules.new_game

                draw.draw_game(self.settings, self.gamerules, self.game_colors, self.keywatch.info)


            elif self.settings.CURRENTSCREEN["KEYMAP"]:

                self.keywatch.events(self.settings)
                self.keymapscreen.keymap_screen_loop(self.settings, self.keywatch)
                self.dropblocks.update_drop(self.settings, self.startscreen, block.block_lst)

                draw.draw_keymap(self.settings, self.settingsscreen, self.keymapscreen, self.dropblocks, self.startscreen, self.game_colors)


            elif self.settings.CURRENTSCREEN["PAUSE"]:

                self.keywatch.events(self.settings)

                self.audio.pause_music = True
                self.audio.play_game_music(self.settings, self.keywatch)

                self.pausescreen.pause_screen_loop(self.settings, self.keywatch)
                self.new_game = self.pausescreen.new_game

                draw.draw_pause(self.settings, self.pausescreen, self.gamerules, self.game_colors)

            elif self.settings.CURRENTSCREEN["END"]:

                self.keywatch.events(self.settings)

                self.gamerules.end_loop_update(self.settings, self.keywatch)
                self.audio.play_game_music(self.settings, self.keywatch)

                self.dropblocks.update_drop(self.settings, self.startscreen, block.block_lst)

                draw.draw_end(self.settings, self.gamerules, self.dropblocks, self.game_colors)

                self.new_game = self.gamerules.new_game

            else:

                print("no screen selected")

                for _screen, _bool in self.settings.CURRENTSCREEN.items():
                    if _screen == "START":
                        self.settings.CURRENTSCREEN[_screen] = True
                    else:
                        self.settings.CURRENTSCREEN[_screen] = False




if __name__ == "__main__":
    Main()
