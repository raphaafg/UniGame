#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.background import Background
from code.const import WIN_WIDTH


class EntityFactory: #design pattern factory doesnt need a init
    

    @staticmethod 
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'lvl1':                
                list_bg = []
                for i in range (4):
                    list_bg.append(Background(f'lvl1_{i}', (0,0)))
                    list_bg.append(Background(f'lvl1_{i}', (WIN_WIDTH,0)))
                return list_bg