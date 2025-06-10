#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame.image


class Menu:
    def __init__(self, window):
        self.window = window
        #para inserir a imagem do menu: carregue a imagem, desenha o retangulo e coloca a imagem no retangulo
        self.surf = pygame.image.load('./asset/menuBg.png') #load the background image
        self.rect = self.surf.get_rect(left=0, top=0)  #get the rectangle of the image setting the position (0,0 is default)
        

    def run(self, ):
        self.window.blit(source=self.surf, dest=self.rect)  #draw the image on the window - source is the image, dest is the rectangle where the image will be drawn
        pygame.display.flip()  #update the display to show the image
        pass