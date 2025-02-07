from constants import *
from player import Player
from ball import Ball
pygame.font.init()

WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("PONG GAME")

MAIN_FONT = pygame.font.SysFont('comicsans', 50)
BIG_MAIN_FONT = pygame.font.SysFont('comicsans', 75)

class GameInfo():
    WINNING_SCORE = 7

    def __init__(self):
        self.main_menu = True
        self.start = False
        self.score_left = 0
        self.score_right = 0
    
    def start_game(self):
        self.main_menu = False
        self.start = True
    
    def restart(self):
        self.score_left = 0
        self.score_right = 0

    def winner(self):
        if self.score_left >= self.WINNING_SCORE:
            return 1
        if self.score_right >= self.WINNING_SCORE:
            return 2

#Functions
def handle_movement(keys, player1, player2):
        
    if keys[pygame.K_w]:
        player1.move_up()

    if keys[pygame.K_s]:
        player1.move_down()

    if keys[pygame.K_UP]:
        player2.move_up()
    
    if keys[pygame.K_DOWN]:
        player2.move_down()

def main():

    #Fonts:
    main_menu_text = BIG_MAIN_FONT.render("PONG GAME", 1, 'white')
    singleplayer_text = MAIN_FONT.render('Single Player', 1, 'white')
    singleplayer_hover_text = MAIN_FONT.render('Single Player', 1, 'white', (50, 50, 50))
    multiplayer_text = MAIN_FONT.render('Multiplayer', 1, 'white')
    multiplayer_hover_text = MAIN_FONT.render('Multiplayer', 1, 'white', (50, 50, 50))
    single_player_rect = singleplayer_text.get_rect(topleft = (WIN_WIDTH/2 - singleplayer_text.get_width()/2, 500))
    multiplayer_rect = multiplayer_text.get_rect(topleft = (WIN_WIDTH/2 - multiplayer_text.get_width()/2, 600))

    #Variables and objects
    game_info = GameInfo()
    clock = pygame.time.Clock()
    run = True
    player1 = Player(True)
    player2 = Player(False)
    ball = Ball()

    def draw(win):
        WIN.fill('black')
        middle_line = pygame.Rect(WIN_WIDTH/2 - 5, 0, 10, WIN_HEIGHT)
        pygame.draw.rect(win, 'white', middle_line)
        for y in range(0,WIN_HEIGHT,WIN_HEIGHT // 10):
            pygame.draw.rect(win, 'black', (WIN_WIDTH/2 - 5, y, 10, 20))

        player1.draw(win)
        player2.draw(win)
        ball.draw(win)

        score_left_text = MAIN_FONT.render(f'{game_info.score_left}', 1, 'white')
        WIN.blit(score_left_text, (WIN_WIDTH/2 - score_left_text.get_width() - 20, 20))
        score_right_text = MAIN_FONT.render(f'{game_info.score_right}', 1, 'white')
        WIN.blit(score_right_text, (WIN_WIDTH/2 + 20, 20))
        pygame.display.update()

    while run:

        clock.tick(FPS)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
        
        if game_info.main_menu:
            clock.tick(FPS)
            WIN.fill('black')
            WIN.blit(main_menu_text, (WIN_WIDTH/2 - main_menu_text.get_width()/2, 200))
            WIN.blit(singleplayer_text, (WIN_WIDTH/2 - singleplayer_text.get_width()/2, 500))
            WIN.blit(multiplayer_text, (WIN_WIDTH/2 - multiplayer_text.get_width()/2, 600))
            pos = pygame.mouse.get_pos()
            if single_player_rect.collidepoint(pos):
                WIN.blit(singleplayer_hover_text, (WIN_WIDTH/2 - singleplayer_hover_text.get_width()/2, 500))
            elif multiplayer_rect.collidepoint(pos):
                WIN.blit(multiplayer_hover_text, (WIN_WIDTH/2 - multiplayer_hover_text.get_width()/2, 600))
            mouse_pressed = pygame.mouse.get_pressed()
            if mouse_pressed[0] and multiplayer_rect.collidepoint(pos):
                game_info.start_game()

            pygame.display.update()
        
        else:

            #Keys movements
            keys = pygame.key.get_pressed()
            handle_movement(keys, player1, player2)

            pos = pygame.mouse.get_pos()
            ball.move()
            ball.hit(player1)
            ball.hit(player2)
            ball.goal(game_info)

            draw(WIN)

            if game_info.winner():
                winner_text = MAIN_FONT.render(f'Player{game_info.winner()} wins', 1, 'white', 'black')
                WIN.blit(winner_text, (WIN_WIDTH/2 - winner_text.get_width()/2, WIN_HEIGHT/2 - winner_text.get_height()/2))
                pygame.display.update()
                pygame.time.delay(2000)
                game_info.restart()
                player1.reset()
                player2.reset()

main()