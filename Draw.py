import pygame
from pygame.locals import *

def draw_info(settings, gamerules, boarder_color):

    for _render, _pos in gamerules.info1_lst:
        settings.screen.blit(_render, _pos)

    for _render, _pos in gamerules.info2_lst:
        settings.screen.blit(_render, _pos)

    for _render, _pos in gamerules.info3_lst:
        settings.screen.blit(_render, _pos)

    for _render, _pos in gamerules.info4_lst:
        settings.screen.blit(_render, _pos)

    for _x, _y in gamerules.next_block["pos"]:
        _new_block_size = settings.BLOCKSIZE // 2
        _x = _x * _new_block_size + gamerules.info1_var_pos[0]
        _y = _y * _new_block_size + gamerules.info1_var_pos[1]
        _rec = pygame.Rect((_x,_y), (_new_block_size, _new_block_size))
        pygame.draw.rect(settings.screen, gamerules.next_block["color"], _rec)
        pygame.draw.rect(settings.screen, boarder_color, _rec, width=2)


def draw_drop_blocks(settings, drop, boarder_color):

    for _block in drop.fall_block_lst:
        for _rec in _block.falling_blocks:
            pygame.draw.rect(settings.screen, _block.color, _rec["rec"])
            pygame.draw.rect(settings.screen, boarder_color, _rec["rec"], width=2)

def draw_block(settings, boarder_color, block_lst):

    for _block in block_lst:

        pygame.draw.rect(settings.screen, _block["color"], _block["rec"])
        pygame.draw.rect(settings.screen, boarder_color, _block["rec"], width=2)

def draw_main(settings, start, drop, game_colors):

    settings.screen.fill(game_colors[0])

    draw_drop_blocks(settings, drop, game_colors[1])

    settings.screen.blit(start.titleboarder, start.title_boarder_pos)
    settings.screen.blit(start.title, start.title_pos)

    settings.screen.blit(start.option1, start.option1_pos)
    settings.screen.blit(start.option2, start.option2_pos)
    settings.screen.blit(start.option3, start.option3_pos)
    settings.screen.blit(start.option4, start.option4_pos)

    settings.screen.blit(start.triangle_left, start.tringale_leftpos[start.option_select_pos])
    settings.screen.blit(start.triangle_right, start.tringale_rightpos[start.option_select_pos])

    pygame.display.flip()

def draw_keymap(settings, option, key, drop, start,  game_colors):

    settings.screen.fill(game_colors[0])

    draw_drop_blocks(settings, drop, game_colors[1])

    settings.screen.blit(start.titleboarder, start.title_boarder_pos)
    settings.screen.blit(start.title, start.title_pos)

    if not option.ONOFFCONTROLLER:
        for idx in range(len(key.keymap)):
            settings.screen.blit(key.keymap[idx], key.keymap_pos[idx])
        for idx in range(len(key.forwardslash_pos)):
            settings.screen.blit(key.forwardslash, key.forwardslash_pos[idx])
        for idx in range(len(key.forwardslash_pos)):
            settings.screen.blit(key.backslash, key.backslash_pos[idx])
    else:
        # controller key map
        pass

    pygame.display.flip()

def draw_settings(settings, start, option, drop, game_colors):
    """DRAW WHAT IS IN SettingsScreen.py  SettingsScreenGame()"""
    settings.screen.fill(game_colors[0])

    draw_drop_blocks(settings, drop, game_colors[1])

    settings.screen.blit(start.titleboarder, start.title_boarder_pos)
    settings.screen.blit(start.title, start.title_pos)

    settings.screen.blit(option.option1title, option.option1title_pos)
    settings.screen.blit(option.option1, option.option1_pos)
    settings.screen.blit(option.option2, option.option2_pos)
    settings.screen.blit(option.option3title, option.option3title_pos)
    settings.screen.blit(option.option3, option.option3_pos)
    settings.screen.blit(option.option4title, option.option4title_pos)
    settings.screen.blit(option.option4, option.option4_pos)
    settings.screen.blit(option.option5, option.option5_pos)

    settings.screen.blit(option.triangle_left, option.tringale_leftpos[option.option_select_pos])
    settings.screen.blit(option.triangle_right, option.tringale_rightpos[option.option_select_pos])


    pygame.display.flip()

def draw_game(settings, gamerules, game_colors, info_bool):

    settings.screen.fill(game_colors[0])

    draw_block(settings, game_colors[1], gamerules.game_blocks_recs_in_play)
    draw_block(settings, game_colors[1], gamerules.game_blocks_recs)

    if info_bool:
        draw_info(settings, gamerules, game_colors[1])

    pygame.display.flip()

def draw_pause(settings, pause, gamerules, game_colors):

    draw_info(settings, gamerules, game_colors[1])

    settings.screen.blit(pause.pausetitle, pause.pausetitle_pos)
    settings.screen.blit(pause.restarttitle, pause.restart_pos)
    settings.screen.blit(pause.menutitle, pause.menu_pos)

    pygame.display.flip()

def draw_end(settings, gamerules, drop, game_colors):

    settings.screen.fill(game_colors[0])

    draw_drop_blocks(settings, drop, game_colors[1])

    draw_block(settings, game_colors[1], gamerules.game_blocks_recs)

    settings.screen.blit(gamerules.gameovertitle, gamerules.gameovertitle_pos)

    if gamerules.end_game_score_bool:

        for _render, _pos in gamerules.info2_lst:
            settings.screen.blit(_render, _pos)

        for _render, _pos in gamerules.info3_lst:
            settings.screen.blit(_render, _pos)

        for _render, _pos in gamerules.info4_lst:
            settings.screen.blit(_render, _pos)

        settings.screen.blit(gamerules.restarttitle, gamerules.restart_pos)
        settings.screen.blit(gamerules.menutitle, gamerules.menu_pos)

    pygame.display.flip()

if __name__ == "__main__":
    pass
