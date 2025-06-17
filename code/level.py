#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from code.entity import Entity
from code.entityFactory import EntityFactory


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode #game mode selected in the menu (menu_option)
        self.entity_list : list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('lvl1'))  # Get the entities for level 1 from the factory

    def run(self, ):
        while True:
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)  # Draw each entity on the window
            pygame.display.flip()
        pass
