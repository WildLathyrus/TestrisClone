import pygame

pygame.init()
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

fonts = pygame.font.get_fonts()
fonts_len = len(fonts)
num = 0
print(fonts_len)

font = "fonts\8-bit-pusab.ttf"
game_over_font = pygame.font.Font(font, 15)

# dialogue_font = pygame.font.SysFont('arial', 15)
# name_font = pygame.font.SysFont('Helvetica', 20)
#game_over_font = pygame.font.SysFont(fonts[num], 60)
#game_over = game_over_font.render(fonts[num], True, (255,0,0))

#dialogue = dialogue_font.render("Hey there, Beautfiul weather today!",
#                                True, (0,0,0))
#name = name_font.render("John Hubbard", True, (0,0,255))
#game_over = game_over_font.render(fonts[num], True, (255,0,0))

while True:

    #game_over_font = pygame.font.SysFont(font, 60)
    game_over = game_over_font.render(font, False, (255,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))

    # screen.blit(dialogue, (40,40))
    # screen.blit(name, (40,140))
    screen.blit(game_over, (40,240))

    pygame.display.flip()

    pygame.time.delay(250)
    clock.tick(60)

    if num == fonts_len:
        num = 0
    else:
        num+=1
