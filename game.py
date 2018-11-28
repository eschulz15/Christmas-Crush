import pygame
import random
from gameboard import Start, Help, Board
# The template of PygameGame is from Lukas Peraza 2015 112 Pygame Lecture
class PygameGame(object):

    def init(self):
        self.margin = max(self.height, self.width) // 8
        self.rows = self.cols = 8
        self.boxWidth = (self.width - 3 * self.margin) // self.cols
        self.boxHeight = (self.height - 2 * self.margin) // self.rows
        #initialize highlight
        self.highlightX = 0
        self.highlightY = 0
        self.startX = 0
        self.startY = 0
        #set candies
        self.peppermint = pygame.image.load("/Users/elizabethschulz/Desktop/112/term project/candy1-2.png").convert_alpha()
        self.tree = pygame.image.load("/Users/elizabethschulz/Desktop/112/term project/christmastree.png").convert_alpha()
        self.candyCane = pygame.image.load("/Users/elizabethschulz/Desktop/112/term project/candycane.png").convert_alpha()
        self.hat = pygame.image.load("/Users/elizabethschulz/Desktop/112/term project/santa.png").convert_alpha()
        self.joy = pygame.image.load("/Users/elizabethschulz/Desktop/112/term project/joy.png").convert_alpha()
        self.snowflake = pygame.image.load("/Users/elizabethschulz/Desktop/112/term project/snowflake.png").convert_alpha()
        self.hotcoco = pygame.image.load("/Users/elizabethschulz/Desktop/112/term project/hot chocolate.png").convert_alpha()
        self.candies = [self.peppermint, self.tree, self.candyCane, self.hat, self.joy]
        #create board
        self.board = []
        for row in range(self.rows):
            self.board += [[]]
            for col in range(self.cols):
                self.board[row] += [random.choice(self.candies)]

    def mousePressed(self, x, y):
        pass

    def mouseReleased(self, x, y):
        pass

    def mouseMotion(self, x, y):
        pass

    def mouseDrag(self, x, y):
        pass

    def keyPressed(self, keyCode, modifier):
        pass

    def keyReleased(self, keyCode, modifier):
        pass

    def timerFired(self, dt):
        pass

    def redrawAll(self, screen):
        pass

    def isKeyPressed(self, key):
        ''' return whether a specific key is being held '''
        return self._keys.get(key, False)

    def __init__(self, width=800, height=800, fps=50, title="Christmas Crush"):
        self.mode = "start"
        self.width = width
        self.height = height
        self.fps = fps
        self.time = 0
        self.title = title
        self.score = 0
        self.moves = 30
        self.goal = 1500
        self.grey = 192,192,192
        self.yellow = 255,255,0
        self.black = 0,0,0
        self.green = 23, 110, 10
        self.brown = 102, 51, 0
        self.red = 226,6,6
        self.white = 255,255,255
        pygame.init()

    def run(self):

        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((self.width, self.height))
        # set the title of the window
        pygame.display.set_caption(self.title)
        background = pygame.image.load("/Users/elizabethschulz/Desktop/112/term project/snow.png")
        self.bg = pygame.transform.scale(background, (self.width,
                self.height))
        # stores all the keys currently being held down
        self._keys = dict()

        # call game-specific initialization
        self.init()
        playing = True

        while playing:
            time = clock.tick(self.fps)
            self.timerFired(time)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.mousePressed(*(event.pos))
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    self.mouseReleased(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons == (0, 0, 0)):
                    self.mouseMotion(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons[0] == 1):
                    self.mouseDrag(*(event.pos))
                elif event.type == pygame.KEYDOWN:
                    self._keys[event.key] = True
                    self.keyPressed(event.key, event.mod)
                elif event.type == pygame.KEYUP:
                    self._keys[event.key] = False
                    self.keyReleased(event.key, event.mod)
                elif event.type == pygame.QUIT:
                    playing = False
            screen.fill((255, 255, 255))
            screen.blit(self.bg,(0,0))
            self.redrawAll(screen)
            pygame.display.flip()
            
        pygame.quit()
        
class Game(PygameGame):
            
    def mousePressed(self, x, y):
        if self.mode == "start":
            Start.startMousePressed(self, x, y)
        elif self.mode == "help":
            Help.helpMousePressed(self, x, y)
        elif self.mode == "winner":
            Winner.winnerMousePressed(self, x, y)
        elif self.mode == "gameOver":
            GameOver.gameOverMousePressed(self, x, y)
        else:
            Board.boardMousePressed(self,x,y)
            
    def keyPressed(self, keyCode, modifier):
        if self.mode == "start":
            Start.startKeyPressed(self, keyCode, modifier)
        elif self.mode == "help":
            Help.helpKeyPressed(self, keyCode, modifier)
        elif self.mode == "winner":
            Winner.winnerKeyPressed(self, keyCode, modifier)
        elif self.mode == "gameOver":
            GameOver.gameOverKeyPressed(self, keyCode, modifier)
        else:
            Board.boardKeyPressed(self, keyCode, modifier)
            
    def timerFired(self, dt):
        if self.mode == "start":
            Start.startTimerFired(self, dt)
        elif self.mode == "help":
            Help.helpTimerFired(self, dt)
        elif self.mode == "winner":
            Winner.winnerTimerFired(self, dt)
        elif self.mode == "gameOver":
            GameOver.gameOverTimerFired(self, dt)
        else:
            Board.boardTimerFired(self, dt)
            
    def redrawAll(self, screen):
        if self.mode == "start":
            Start.startRedrawAll(self, screen)
        elif self.mode == "help":
            Help.helpRedrawAll(self, screen)
        elif self.mode == "winner":
            Winner.winnerRedrawAll(self, screen)
        elif self.mode == "gameOver":
            GameOver.gameOverRedrawAll(self, screen)
        else:
            Board.boardRedrawAll(self, screen)
            
Game().run()