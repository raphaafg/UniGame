#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.const import ENTITY_SPEED, WIN_WIDTH
from code.entity import Entity
import random


class Enemy(Entity):
    def __init__(self, nome: str, position: tuple):
        super().__init__(nome, position)

    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.name]                
        if self.rect.right <= 0: #if the right side of a image gets 0, set the left side to the final right again
            self.rect.left = WIN_WIDTH 
