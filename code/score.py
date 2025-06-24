import pygame

from code.DBProxy import DBProxy
from code.const import COLOR_PURPLE, FONT_TITLE_SIZE, MENU_OPTION, WIN_SCORE_POS, WIN_WIDTH


class Score:

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/ScoreBg.png').convert_alpha() #load the background image
        self.rect = self.surf.get_rect(left=0, top=0)  #get the rectangle of the image setting the position (0,0 is default)


    def save(self, game_mode: str, player_score: list[int]):
        pygame.mixer_music.load('./asset/Sound_score.wav')
        pygame.mixer_music.play(loops=-1) # Play the background music in a loop 
        self.window.blit(source=self.surf, dest=self.rect)

        db_proxy = DBProxy('DBScore') #connectin to DB when winning game

        while True:
            self.score_text(FONT_TITLE_SIZE, "YOU WIN!", COLOR_PURPLE, WIN_SCORE_POS['Title'] )
            if game_mode == MENU_OPTION[0]: #GAME FOR 1P
                text = 'Player 1, enter your name (4 char):'



            pygame.display.flip()
            pass
        

    def show(self):
        pygame.mixer_music.load('./asset/Sound_score.wav')
        pygame.mixer_music.play(loops=-1) # Play the background music in a loop 
        self.window.blit(source=self.surf, dest=self.rect)
        while True:
            pygame.display.flip()
            pass

    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        Font = pygame.font.SysFont(name="bauhaus93", size=text_size) #cria a fonte
        Surface = Font.render(text, True, text_color).convert_alpha() #renderiza o texto com a fonte, antialiasing e cor
        Rect = Surface.get_rect(center=text_center_pos) #centra o retangulo do texto na posicao especificada
        self.window.blit(source=Surface, dest=Rect) #blit padrao, ou seja, desenha o texto na janela