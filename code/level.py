#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import sys
import pygame
from code.const import COLOR_BLUESKY, COLOR_DARKGREEN, COLOR_ORANGEFIRE, ENEMY_SPAWN, MENU_OPTION, SPAWN_TIME, WIN_HEIGHT
from code.enemy import Enemy
from code.entity import Entity
from code.entityFactory import EntityFactory
from code.entityMediator import EntityMediator
from code.player import Player


class Level:
    def __init__(self, window, name, game_mode):
        self.timeout = 25000 #ms = 25seconds
        self.window = window
        self.name = name
        self.game_mode = game_mode #game mode selected in the menu (menu_option)
        self.entity_list : list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('lvl1'))  # Get the entities for level 1 from the factory
        self.entity_list.append(EntityFactory.get_entity('Player1'))
        if self.game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            self.entity_list.append(EntityFactory.get_entity('Player2'))
        pygame.time.set_timer(ENEMY_SPAWN, SPAWN_TIME)  # Set a timer to spawn enemies every 2 seconds

    def run(self, ):
        pygame.mixer.music.load('./asset/Sound_lvl1.wav')  # Load the background music for level 1
        pygame.mixer.music.play(loops=-1)
        clock = pygame.time.Clock()  # Create a clock to control FPS
           
        ##---------MAIN GAME LOOP---------##
        while True:
            clock.tick(60)
            self.window.fill((0,0,0)) #reset screen
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)  # Draw each entity on the window
                ent.move()
                if isinstance(ent,(Player, Enemy)):
                    shoot = ent.shoot()  # If the entity is a player or enemy, check if it can shoot
                    if shoot is not None:
                        self.entity_list.append(shoot) # Add the shot to the entity list if it exists
                
                ##---------SHOW HEALTH OF PLAYERS---------##
                if ent.name == 'Player1_DLC':
                    self.level_text( 14, f'Player 1 -    Health: {ent.health}    Score: {ent.score}', COLOR_DARKGREEN,(10, 20))             
                if ent.name == 'Player2_DLC':
                    self.level_text( 14, f'Player 2 -    Health: {ent.health}    Score: {ent.score}', COLOR_ORANGEFIRE,(10, 35))


                

            ##---------CHECK FOR ALL EVENTS---------##
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()  # Exit the game if the window is closed
                    
                ##---------SPAWN OF ENEMIES---------##
                if event.type == ENEMY_SPAWN:
                    choice = random.choice(['Enemy1', 'Enemy2'])  # Randomly choose an enemy type to spawn
                    self.entity_list.append(EntityFactory.get_entity(choice))  #add a random enemy to the entity list

            
           
            
            
            #printed text on the screen
            
            self.level_text( 14, f'{self.name} - Timeout: {self.timeout / 1000:.0f}s', COLOR_BLUESKY,(10, 5)) #show the level name and timeout
            self.level_text( 14, f'FPS: {clock.get_fps():.0f}', COLOR_BLUESKY,(10, WIN_HEIGHT - 30)) #show the current FPS
            self.level_text( 14, f'Entidades: {len(self.entity_list)}', COLOR_BLUESKY,(10, WIN_HEIGHT - 45)) #show number of entities
            pygame.display.flip()


            ##---------COLLISION AND HEALTH CHECK---------##
            EntityMediator.verify_collision(entity_list=self.entity_list)  # Check for collisions between entities
            EntityMediator.verify_health(entity_list=self.entity_list)
        pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        Font = pygame.font.SysFont(name="bauhaus93", size=text_size) #cria a fonte
        Surface = Font.render(text, True, text_color).convert_alpha() #renderiza o texto com a fonte, antialiasing e cor
        Rect = Surface.get_rect(topleft = text_pos) #centra o retangulo do texto na posicao especificada
        self.window.blit(source=Surface, dest=Rect) #blit padrao, ou seja, desenha o texto na janela
