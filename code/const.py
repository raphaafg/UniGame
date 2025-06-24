#code criado para centralizar as constantes do jogo - os números mágicos - usados para definir o tamanho da janela, cores, etc.
#constantes devem ser escritas em letras maiúsculas
#boas praticas: separar as constantes pelas iniciais
import pygame


#C
COLOR_PURPLE = (187, 50, 214)  # RGB color for purple
COLOR_BLUESKY = (167, 236, 255)  # RGB color for sky blue
COLOR_BLUESPACE = (80, 50, 255)  # RGB color for yellow
COLOR_ORANGEFIRE = (230, 165, 0)  # RGB color for orange fire
COLOR_DARKGREEN = (0, 100, 0)  # RGB color for dark green

#E
ENTITY_SPEED = {
    'lvl1_0': 0,
    'lvl1_1': 0,
    'lvl1_2': 4,
    'lvl1_3': 5,
    'lvl2_0': 1,
    'lvl2_1': 0,
    'lvl2_2': 2,
    'Player1_DLC':4,
    'Player2_DLC':5,
    'Enemy1': 3,
    'Enemy2': 2,
    'Player1_DLCShot': 7,
    'Player2_DLCShot': 5,
    'Enemy1Shot': 4,
    'Enemy2Shot': 7,

}
ENEMY_SPAWN = pygame.USEREVENT + 1 
EVENT_TIMEOUT = pygame.USEREVENT + 2 #it has to be +2 because +1 is already used by ENEMY_SPAWN

ENTITY_HEALTH = {
    'lvl1_0': 999,
    'lvl1_1': 999,
    'lvl1_2': 999,
    'lvl1_3': 999,
    'lvl2_0': 999,
    'lvl2_1': 999,
    'lvl2_2': 999,
    'Player1_DLC': 300,
    'Player1_DLCShot': 1,
    'Player2_DLC': 300,
    'Player2_DLCShot': 1,
    'Enemy1': 40,
    'Enemy2': 65,
    'Enemy1Shot': 1,
    'Enemy2Shot': 1,
}

ENTITY_SHOT_DELAY = {
    'Player1_DLC': 20,
    'Player2_DLC': 30,
    'Enemy1': 90,
    'Enemy2': 150,
}

ENTITY_DAMAGE = {
    'lvl1_0': 0,
    'lvl1_1': 0,
    'lvl1_2': 0,
    'lvl1_3': 0,
    'lvl2_0': 0,
    'lvl2_1': 0,
    'lvl2_2': 0,
    'Player1_DLC': 5,
    'Player2_DLC': 5,
    'Enemy1': 10,
    'Enemy2': 15,
    'Player1_DLCShot': 20,
    'Player2_DLCShot': 25,
    'Enemy1Shot': 20,
    'Enemy2Shot': 30,
}

ENTITY_SCORE = {
    'lvl1_0': 0,
    'lvl1_1': 0,
    'lvl1_2': 0,
    'lvl1_3': 0,
    'lvl2_0': 0,
    'lvl2_1': 0,
    'lvl2_2': 0,
    'Player1_DLC': 0,
    'Player2_DLC': 0,
    'Enemy1': 100,
    'Enemy2': 150,
    'Player1_DLCShot': 0,
    'Player2_DLCShot': 0,
    'Enemy1Shot': 0,
    'Enemy2Shot': 0,
}


#F
FONT_TITLE_SIZE = 60  # Font size for the menu text
FONT_OPTION_SIZE = 18  # Font size for the menu options

#
HIT_COOLDOWN = 40 

#M
MENU_OPTION = ( 'NEW GAME - 1P > ARCADE',
                'NEW GAME - 2P > COOPERATIVE',
                'NEW GAME - 2P > COMPETITIVE',
                'SCORE',
                'CONTROLS',
                'EXIT')

#P
PLAYER_KEY_UP = {'Player1_DLC': pygame.K_UP, 'Player2_DLC': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1_DLC': pygame.K_DOWN, 'Player2_DLC': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1_DLC': pygame.K_LEFT, 'Player2_DLC': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1_DLC': pygame.K_RIGHT, 'Player2_DLC': pygame.K_d}
PLAYER_KEY_SHOOT = {'Player1_DLC': pygame.K_SPACE, 'Player2_DLC': pygame.K_g}  

#S
SPAWN_TIME = 1300 #1.8s
STEP_TIMEOUT = 100  #0.1s
STAGE_TIMEOUT = 25000  #25s

#W
WIN_WIDTH = 800  # Width of the game window
WIN_HEIGHT = 500  # Height of the game window

WIN_SCORE_POS = { 'Title': (WIN_WIDTH/2, 50),
                 'EnterName': (WIN_WIDTH/2, 90),
                 'Label': (WIN_WIDTH/2, 100),
                 'Name': (WIN_WIDTH/2, 110),
                 0: (WIN_WIDTH/2, 130), #0 a 9 referente ao index do lista ordenada
                 1: (WIN_WIDTH/2, 150),
                 2: (WIN_WIDTH/2, 170),
                 3: (WIN_WIDTH/2, 190),
                 4: (WIN_WIDTH/2, 210),
                 5: (WIN_WIDTH/2, 230),
                 6: (WIN_WIDTH/2, 250),
                 7: (WIN_WIDTH/2, 270),
                 8: (WIN_WIDTH/2, 290),
                 9: (WIN_WIDTH/2, 310),            

}
