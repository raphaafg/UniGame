import datetime
import pygame

from code.DBProxy import DBProxy
from code.const import COLOR_BLUESKY, COLOR_BLUESPACE, COLOR_ORANGEFIRE, COLOR_PURPLE, FONT_OPTION_SIZE, FONT_TITLE_SIZE, MENU_OPTION, WIN_HEIGHT, WIN_SCORE_POS, WIN_WIDTH


class Score:

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/ScoreBg.png').convert_alpha() #load the background image
        self.rect = self.surf.get_rect(left=0, top=0)  #get the rectangle of the image setting the position (0,0 is default)
        


    def save(self, game_mode: str, player_score: list[int]):
        pygame.mixer_music.load('./asset/Sound_score.wav')
        pygame.mixer_music.play(loops=-1) # Play the background music in a loop 
        self.window.blit(source=self.surf, dest=self.rect)

        db_proxy = DBProxy('DBScore') #connectin to DB when winning game

        namePlay = ''
        clock = pygame.time.Clock()

        redraw = True
        prev_namePlay = ''
        prev_text = ''
        while True:
            updated = False

            ##--------------Check for all events--------------##
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() 
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and len(namePlay) == 4:
                        db_proxy.save({'name': namePlay, 'score': score, 'date': get_formatted_date() })
                        self.show()
                        return
                    elif event.key == pygame.K_BACKSPACE:
                        if len(namePlay) > 0:
                            namePlay = namePlay[:-1] #erase last character
                            updated = True
                    else:
                        if len(namePlay) < 4 and event.unicode.isprintable():
                            namePlay += event.unicode #add character to var namePlay that starts empty
                            updated = True

            # Determine score and prompt text based on game mode
            if game_mode == MENU_OPTION[0]: #GAME FOR 1P
                score = player_score[0]
                text = 'Player 1, enter your name (4 char) and press ENTER:'
            elif game_mode == MENU_OPTION[1]: #GAME FOR 2P COOP
                score = ((player_score[0]+player_score[1])/2)
                text = 'Players, enter your team name (4 char) and press ENTER:'
            elif game_mode == MENU_OPTION[2]: #GAME FOR 2P VS
                if player_score[0] > player_score[1]:
                    score = player_score[0]
                    text = 'Player 1, enter your name (4 char) and press ENTER:'
                elif player_score[0] < player_score[1]:
                    score = player_score[1]
                    text = 'Player 2, enter your name (4 char) and press ENTER:'
                else:  
                    score = player_score[0]
                    text = 'DRAW!!!!, enter your team name (4 char) and press ENTER:'

            # Redraw only if input or prompt text has changed, or after an event
            if updated or namePlay != prev_namePlay or text != prev_text:
                self.window.blit(source=self.surf, dest=self.rect)
                self.score_text(FONT_TITLE_SIZE, "YOU WIN!", COLOR_PURPLE, WIN_SCORE_POS['Title'] )
                self.score_text(20, text, COLOR_BLUESKY, WIN_SCORE_POS['EnterName'] )
                self.score_text(30, namePlay, COLOR_ORANGEFIRE, WIN_SCORE_POS['Name'] )
                pygame.display.flip()
                prev_namePlay = namePlay
                prev_text = text

            clock.tick(30)  # Limit to 30 frames per second
        

    def show(self):
        pygame.mixer_music.load('./asset/Sound_score.wav')
        pygame.mixer_music.play(loops=-1) # Play the background music in a loop 
        self.window.blit(source=self.surf, dest=self.rect)
        self.score_text(48, 'TOP 10 SCORE', COLOR_PURPLE, WIN_SCORE_POS['Title'])
        self.score_text(20, 'NAME        SCORE                DATE            ', COLOR_PURPLE, WIN_SCORE_POS['Label'])
        self.score_text(20, "Pess any key to return to Menu", COLOR_PURPLE,text_center_pos=((WIN_WIDTH/2), WIN_HEIGHT-30))

        db_proxy = DBProxy('DBScore')
        list_score = db_proxy.retrieve_top10() #saving data from db to list_score
        db_proxy.close()

        clock = pygame.time.Clock()

        for player_score in list_score:
            id_, name, score, date = player_score #separando atraves do index da lista o conteudo
            self.score_text(20, f'{name}         {score :05d}        {date}', COLOR_BLUESKY, WIN_SCORE_POS[list_score.index(player_score)])



        while True:
        
            ##--------------Check for all events--------------##
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() 
                    quit()
                
                if event.type == pygame.KEYDOWN:
                    return
                
            pygame.display.flip()
            clock.tick(30)  # Limit to 30 frames per second
            

    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        Font = pygame.font.SysFont(name="bauhaus93", size=text_size) #cria a fonte
        Surface = Font.render(text, True, text_color).convert_alpha() #renderiza o texto com a fonte, antialiasing e cor
        Rect = Surface.get_rect(center=text_center_pos) #centra o retangulo do texto na posicao especificada
        self.window.blit(source=Surface, dest=Rect) #blit padrao, ou seja, desenha o texto na janela

##--------------get time and date--------------##
def get_formatted_date():
    current_datetime = datetime.datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%d/%m/%y")
    return f"{current_time} - {current_date}"