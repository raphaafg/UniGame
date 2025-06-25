#!/usr/bin/python
# -*- coding: utf-8 -*-

from pygame import Vector2
from code.const import ENTITY_SPEED, WIN_WIDTH
from code.entity import Entity


class Background(Entity):
    def __init__(self, name:str, position:tuple, ):
        super().__init__(name, position)
       

    def move(self):        
        self.rect.centerx -= ENTITY_SPEED[self.name] #using the const to set the speed for each background image, moving it to the left (-)
        #it is necessary to set self.name because it is a dict and the key is the name to reach the value (speed) of the dict ENTITY_SPEED
                
        if self.rect.right <= 0: #if the right side of a image gets 0, set the left side to the final right again
            self.rect.left = WIN_WIDTH 
      