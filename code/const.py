#code criado para centralizar as constantes do jogo - os números mágicos - usados para definir o tamanho da janela, cores, etc.
#constantes devem ser escritas em letras maiúsculas
#boas praticas: separar as constantes pelas iniciais



#C
import pygame


COLOR_PURPLE = (187, 50, 214)  # RGB color for purple
COLOR_BLUESKY = (167, 236, 255)  # RGB color for sky blue
COLOR_BLUESPACE = (80, 50, 255)  # RGB color for yellow

#E
ENTITY_SPEED = {
    'lvl1_0': 0,
    'lvl1_1': 0,
    'lvl1_2': 4,
    'lvl1_3': 5,
    'Player1_DLC':4,
    'Player2_DLC':4,
    'Enemy1': 3,
    'Enemy2': 2,
}
ENEMY_SPAWN = pygame.USEREVENT + 1 
#F
FONT_TITLE_SIZE = 60  # Font size for the menu text
FONT_OPTION_SIZE = 18  # Font size for the menu options



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
SPAWN_TIME = 5500

#W
WIN_WIDTH = 800  # Width of the game window
WIN_HEIGHT = 500  # Height of the game window
