#!/usr/bin/python
# -*- coding: utf-8 -*-
#classe abstrata
from abc import ABC, abstractmethod
import pygame
from code.const import ENTITY_DAMAGE, ENTITY_HEALTH, ENTITY_SCORE


class Entity (ABC):
    def __init__(self, name:str, position:tuple, ):
        self.name = name
        self.surf = pygame.image.load('./asset/' + name + '.png').convert_alpha()  # Load the image for the entity from the asset folder (every image is in asset folder)
        #convert_alpha: otmiza imagem para melhor desempenho, mantendo a transparência
        self.rect = self.surf.get_rect(left=position[0], top=position[1])  # Get the rectangle of the image and set its position 0=x e y=1
        self.speed = 0
        self.health = ENTITY_HEALTH[self.name]
        self.damage = ENTITY_DAMAGE[self.name]  # Damage is a dictionary that contains the damage of each entity, defined in const.py
        self.score = ENTITY_SCORE[self.name] 
        self.last_dmg = 'None' 

    @abstractmethod # To be implemented by subclasses, there is no default implementation
    def move(self, ):
        pass
