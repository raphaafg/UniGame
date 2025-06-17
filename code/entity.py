#!/usr/bin/python
# -*- coding: utf-8 -*-
#classe abstrata
from abc import ABC, abstractmethod
import pygame


class Entity (ABC):
    def __init__(self, name:str, position:tuple, ):
        self.name = name
        self.surf = pygame.image.load('./asset/' + name + '.png')  # Load the image for the entity from the asset folder (every image is in asset folder)
        self.rect = self.surf.get_rect(left=position[0], top=position[1])  # Get the rectangle of the image and set its position 0=x e y=1
        self.speed = 0

    @abstractmethod # To be implemented by subclasses, there is no default implementation
    def move(self, ):
        pass
