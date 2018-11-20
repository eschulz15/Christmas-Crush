import pygame
import random
from candies import GamePiece, Candy, Peppermint, Tree, Hat, CandyCane, Joy
from gameboard import Start, Board

class PygameGame(object):

    def init(self):
        pass

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
        self.title = title
        self.score = 0
        self.grey = 192,192,192
        self.yellow = 255,255,0
        self.black = 0,0,0
        pygame.init()

    def run(self):

        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((self.width, self.height))
        # set the title of the window
        pygame.display.set_caption(self.title)

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
    def init(self):
        if self.mode == "start":
            Start.init(self)
        else:
            Board.init(self)
            
    def mousePressed(self, x, y):
        if self.mode == "start":
            Start.mousePressed(self, x, y)
        else:
            Board.mousePressed(self,x,y)
            
    def keyPressed(self, keyCode, modifier):
        if self.mode == "start":
            Start.keyPressed(self, keyCode, modifier)
        else:
            Board.keyPressed(self, keyCode, modifier)
            
    def timerFired(self, dt):
        if self.mode == "start":
            Start.timerFired(self, dt)
        else:
            Board.timerFired(self, dt)
            
    def redrawAll(self, screen):
        if self.mode == "start":
            Start.redrawAll(self, screen)
        else:
            Board.redrawAll(self, screen)
            
Game().run()