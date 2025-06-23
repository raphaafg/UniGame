#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
from code.background import Background
from code.const import WIN_HEIGHT, WIN_WIDTH
from code.enemy import Enemy
from code.player import Player


class EntityFactory: #design pattern factory doesnt need a init
    

    @staticmethod 
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            #lvl1 factory
            case 'lvl1':                
                list_bg = []
                for i in range (4): # 4 backgrounds images for level 1
                    list_bg.append(Background(f'lvl1_{i}', (0,0)))
                    list_bg.append(Background(f'lvl1_{i}', (WIN_WIDTH,0)))
                return list_bg
            
            #lvl2 factory
            case 'lvl2':                
                list_bg = []
                for i in range (3): # 3 backgrounds images for level 2
                    list_bg.append(Background(f'lvl2_{i}', (0,0)))
                    list_bg.append(Background(f'lvl2_{i}', (WIN_WIDTH,0)))
                return list_bg
            
            #Player1 factory
            case 'Player1':
                return Player('Player1_DLC', (10 , (WIN_HEIGHT/2)-40))
            #Player2 factory
            case 'Player2':
                return Player('Player2_DLC', (10, (WIN_HEIGHT/2)+40))
            
            #Enemy1 factory
            case 'Enemy1':
                return Enemy('Enemy1', (WIN_WIDTH + 15, random.randint(50, WIN_HEIGHT - 50)))
            #Enemy2 factory
            case 'Enemy2':
                return Enemy('Enemy2', (WIN_WIDTH + 15, random.randint(50, WIN_HEIGHT - 50)))
            
            
            