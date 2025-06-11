

#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame


from pygame.font import Font # Import the Font class from the pygame.font module


#from font.font import Font # Import the Font class from the font module
from pygame import Rect
from pygame import Surface # Import the Rect and Surface classes from the pygame module
from code.const import WIN_WIDTH # Import the constant WIN_WIDTH from the const module
from code.const import WIN_HEIGHT # Import the constant WIN_HEIGHT from the const module
from code.const import COLOR_PURPLE # Import the constant COLOR_PURPLE from the const module
from code.const import FONT_MENU_SIZE # Import the constant FONT_MENU_SIZE from the const module

class Menu:
    def __init__(self, window):
        self.window = window
        #para inserir a imagem do menu: carregue a imagem, desenha o retangulo e coloca a imagem no retangulo
        self.surf = pygame.image.load('./asset/menuBg.png') #load the background image
        self.rect = self.surf.get_rect(left=0, top=0)  #get the rectangle of the image setting the position (0,0 is default)
        self.clock = pygame.time.Clock()

    #criacao de um metodo para desenhar o texto no menu
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        Font = pygame.font.SysFont(name="bauhaus93", size=text_size) #cria a fonte
        Surface = Font.render(text, True, text_color).convert_alpha() #renderiza o texto com a fonte, antialiasing e cor
        Rect = Surface.get_rect(center=text_center_pos) #centra o retangulo do texto na posicao especificada
        self.window.blit(source=Surface, dest=Rect) #blit padrao, ou seja, desenha o texto na janela


    def run(self, ):
        pygame.mixer_music.load('./asset/Sound_menu.wav') # Load the background music for the menu
        pygame.mixer_music.play(loops=-1) # Play the background music in a loop (-1 means loop indefinitely)

        while True:
            self.window.blit(source=self.surf, dest=self.rect)  #draw the image on the window - source is the image, dest is the rectangle where the image will be drawn
            self.menu_text(FONT_MENU_SIZE, "SPACE", COLOR_PURPLE, text_center_pos=((WIN_WIDTH/2), 100) )
            self.menu_text(FONT_MENU_SIZE, "SHOOTER", COLOR_PURPLE, text_center_pos=((WIN_WIDTH/2), 180) )
            self.menu_text(FONT_MENU_SIZE, "-"*3, COLOR_PURPLE, text_center_pos=(((WIN_WIDTH/2)-16), 195) )
           
            pygame.display.flip()  #update the display to show the image
            self.clock.tick(60) # Limit the frame rate to 60 FPS

            #Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() #if the event is a quit event, exit the loop == close the window
                    quit() #End PYGAME




