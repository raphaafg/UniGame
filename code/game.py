#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame as pyg

from code.menu import Menu # Import the pygame library as 'pyg'

class Game:
    def __init__(self):
        #EU COLOCO PYG.INIT E SETUP DA JANELA DENTRO DO CONSTRUTOR DA CLASSE, POIS QUERO QUE SEJA FEITO APENAS UMA VEZ E NÃO REESCRITO A CADA LOOP DO JOGO
        pyg.init() # Initialize the pygame library
        self.window = pyg.display.set_mode (size=(800,500)) # Create a window with a size of 800x600 pixels -> size deve ser criada em tupla

    def run(self, ):
       
        while True: # Start an infinite loop
            menu = Menu(self.window)
            menu.run() #execute the run method of the Menu class
            pass





            # Check for all events
            # for event in pyg.event.get():
            #     if event.type == pyg.QUIT:
            #         pyg.quit() #if the event is a quit event, exit the loop == close the window
            #         quit() #End PYGAME





 





