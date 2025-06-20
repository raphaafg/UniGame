#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame


from code.level import Level
from code.menu import Menu # Import the pygame library as 'pyg'
from code.const import MENU_OPTION, WIN_WIDTH # Import the constant WIN_WIDTH from the const module
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
            menu_return = menu.run() #execute the run method of the Menu class

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]: #if player selects to play 1p. 2p coop or 2p vs, starts the level 1
                level = Level(self.window, 'Level 1', menu_return) #create a new Level object with the window and level name
                level_return = level.run()
                        
            elif menu_return == MENU_OPTION[5]:
                pygame.quit() #quit the game closing the window
                quit()
            else:
                pass

            





           



 





