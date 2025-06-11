import pygame, sys

pygame.init()
WIN = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Preview de Fontes")
clock = pygame.time.Clock()

samples = [
    ("AgencyFB",         pygame.font.SysFont("agencyfb", 48)),
    ("AgencyFB Bold",    pygame.font.SysFont("agencyfbnegrito", 48)),
    ("Bauhaus 93",       pygame.font.SysFont("bauhaus93", 48)),
    ("Berlin Sans FB",   pygame.font.SysFont("berlinsansfb", 48)),
    ("Impact",           pygame.font.SysFont("impact", 48)),
    ("Bahnschrift",      pygame.font.SysFont("bahnschrift", 48)),
    ("Candara",          pygame.font.SysFont("candara", 48)),
    ("Calibri",          pygame.font.SysFont("calibri", 48)),
    ("Franklin Gothic",  pygame.font.SysFont("franklingothicbook", 48)),
    ("Trebuchet MS",     pygame.font.SysFont("trebuchetms", 48)),
]

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    WIN.fill((10, 10, 40))
    y = 20
    for name, fnt in samples:
        text = fnt.render(f"{name}: SPACE", True, (200, 100, 220))
        WIN.blit(text, (20, y))
        y += 55

    pygame.display.flip()
    clock.tick(60)
