#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame


from code.menu import Menu # Import the pygame library as 'pyg'
from code.const import WIN_WIDTH # Import the constant WIN_WIDTH from the const module
from code.const import WIN_HEIGHT # Import the constant WIN_HEIGHT from the const module



class Game:
    def __init__(self):
        #EU COLOCO PYG.INIT E SETUP DA JANELA DENTRO DO CONSTRUTOR DA CLASSE, POIS QUERO QUE SEJA FEITO APENAS UMA VEZ E NÃO REESCRITO A CADA LOOP DO JOGO
        pygame.init() # Initialize the pygame library
        pygame.mixer.init() # Initialize the mixer module for sound playback
        self.window = pygame.display.set_mode (size=(WIN_WIDTH,WIN_HEIGHT)) # Create a window with a size of 800x600 pixels -> size deve ser criada em tupla

    def run(self, ):
        

        while True: # Start an infinite loop
            menu = Menu(self.window)
            menu.run() #execute the run method of the Menu class
            pass





           



 





