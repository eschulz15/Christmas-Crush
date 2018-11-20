# template from Lukas Peraza 2015
import pygame
import random
        
##############################################################################
# start
##############################################################################

class Start(object):
    def init(self):
        background = pygame.image.load("/Users/elizabethschulz/Desktop/112/term project/startscreen.png")
        self.bg = pygame.transform.scale(background, (self.width,
                    self.height))
    
    def mousePressed(self, x, y):
        self.mode = "board"
    
    def keyPressed(self, keyCode, modifier):
        if keyCode == pygame.K_p:
            self.mode = "board"
        
    def redrawAll(self, screen):
        pygame.draw.rect(screen, self.grey, (self.width//4, self.height//4,
         self.width//2, self.height//2))
        
##############################################################################
# gameboard
##############################################################################

# template from Lukas Peraza 2015
        
class Board(object):
    def init(self):
        background = pygame.image.load("/Users/elizabethschulz/Desktop/112/term project/winter2-2.png")
        self.bg = pygame.transform.scale(background, (self.width,
                self.height))
        self.margin = max(self.height, self.width) // 8
        self.rows = self.cols = 8
        self.boxWidth = (self.width - 3 * self.margin) // self.rows
        self.boxHeight = (self.height - 2 * self.margin) // self.cols
        self.highlightX = 0
        self.highlightY = 0
        self.x = 0
        self.y = 0
        Peppermint.init()
        Tree.init()
        CandyCane.init()
        Hat.init()
        Joy.init()
        candyCoords = []
        options = [Peppermint, Tree, CandyCane, Hat, Joy]
        for i in range(self.margin, self.height-(self.margin), 
                        self.boxHeight):
            for j in range(self.margin, 
                self.width-(2 * self.margin+self.boxWidth), self.boxWidth):
                candyCoords += [(j,i)]
        self.candies = []
        for coordinate in candyCoords:
            item = random.choice(options)
            self.candies += [item(coordinate[0],coordinate[1])]
        self.candyGroup = pygame.sprite.Group()
        for item in self.candies:
            self.candyGroup.add(item)
            
    def updateScore(self, screen):
        font = pygame.font.SysFont("brushscriptmt", 50)
        text = font.render("Score: %d" % self.score, True, (0,0,0))
        screen.blit(text, (self.width//4, 0))
    
    def mousePressed(self, x, y):
        row = (y - self.margin) // self.boxHeight
        col = (x - self.margin) // self.boxWidth
        row = min(self.rows - 1, max(0,row))
        col = min(self.cols - 1, max(0,col))
        self.highlightX = col * self.boxWidth
        self.highlightY = row * self.boxHeight
        self.x = self.highlightX
        self.y = self.highlightY
            
    def keyPressed(self, keyCode, modifier):
        currX = self.x
        currY = self.y
        if keyCode == pygame.K_UP:
            if self.highlightY > 0:
                self.highlightY -= self.boxHeight
                if self.highlightY < currY - self.boxHeight or\
                        self.highlightX != currX:
                    self.highlightY += self.boxHeight
        if keyCode == pygame.K_DOWN:
            if self.highlightY < self.height :
                self.highlightY += self.boxHeight
                if self.highlightY > currY + self.boxHeight or\
                        self.highlightX != currX:
                    self.highlightY -= self.boxHeight
        if keyCode == pygame.K_RIGHT:
            if self.highlightX < self.width:
                self.highlightX += self.boxWidth
                if self.highlightX > currX + self.boxWidth or\
                        self.highlightY != currY:
                    self.highlightX -= self.boxWidth
        if keyCode == pygame.K_LEFT:
            if self.highlightX > 0:
                self.highlightX -= self.boxWidth
                if self.highlightX < currX - self.boxWidth or\
                        self.highlightY != currY:
                    self.highlightX += self.boxWidth
                    
    def redrawAll(self, screen):
        pygame.draw.rect(screen, self.yellow, (self.highlightX + self.margin,   
            self.highlightY + self.margin, self.boxWidth, self.boxHeight))
        for row in range(self.rows):
            for col in range(self.cols):
                pygame.draw.rect(screen, self.black,
                (row * self.boxWidth + self.margin, 
                 col * self.boxHeight + self.margin, self.boxWidth,
                  self.boxHeight),2)
        self.candyGroup.draw(screen)
        pygame.draw.rect(screen, self.black, (self.width - 7*self.margin//4,
         self.margin + self.boxHeight, 5*self.margin//4, 
         self.height - 2 * self.margin - 2 * self.boxHeight), 2)

