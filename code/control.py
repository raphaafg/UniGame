import sys
import pygame

from code.const import COLOR_DARKGREEN, COLOR_ORANGEFIRE, COLOR_PURPLE, FONT_OPTION_SIZE, FONT_TITLE_SIZE, WIN_HEIGHT, WIN_SCORE_POS, WIN_WIDTH



class Control:

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/controleBgg.png').convert_alpha() #load the background image
        self.rect = self.surf.get_rect(left=0, top=0)  #get the rectangle of the image setting the position (0,0 is default)


    

    def run(self):
        pygame.mixer.music.load('./asset/Sound_control.wav')
        pygame.mixer.music.play(loops=-1) # Play the background music in a loop
        pygame.mixer.music.set_volume(0.4)
        self.window.blit(source=self.surf, dest=self.rect)
        while True:
            self.control_text(FONT_TITLE_SIZE, "CONTROL", COLOR_PURPLE, WIN_SCORE_POS['Title'] )
            self.control_text(30, "PLAYER 1", COLOR_DARKGREEN,text_center_pos=((WIN_WIDTH/2)-270, 150))
            self.control_text(30, "PLAYER 2", COLOR_ORANGEFIRE,text_center_pos=((WIN_WIDTH/2)+270, 150))
            self.control_text(20, "Pess any key to return to Menu", COLOR_PURPLE,text_center_pos=((WIN_WIDTH/2), WIN_HEIGHT-30))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    return True
            
            pass

    def control_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        Font = pygame.font.SysFont(name="bauhaus93", size=text_size) #cria a fonte
        Surface = Font.render(text, True, text_color).convert_alpha() #renderiza o texto com a fonte, antialiasing e cor
        Rect = Surface.get_rect(center=text_center_pos) #centra o retangulo do texto na posicao especificada
        self.window.blit(source=Surface, dest=Rect) #blit padrao, ou seja, desenha o texto na janela