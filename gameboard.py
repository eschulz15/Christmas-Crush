# The template is from Lecture Notes about animations
import pygame
from game import PygameGame
import random
        
##############################################################################
# gameboard
##############################################################################

# template from Lukas Peraza 2015
        
class Board(PygameGame):
    def init(self):
        super().init(self)
        
    def createBoard(self):
        self.board = []
        for row in range(self.rows):
            self.board += [[]]
            for col in range(self.cols):
                self.board[row] += [random.choice(self.candies)]
    
    def updateScore(self, screen):
        font = pygame.font.SysFont("brushscriptmt", 40)
        text1 = font.render("Score:", True, self.black)
        text2 = font.render("%d" % self.score, True, self.black)
        screen.blit(text1, (self.width - 13*self.margin//8,
                self.margin + self.boxHeight))
        screen.blit(text2, (self.width - 11*self.margin//8,
                (3/2)*self.margin + self.boxHeight))
    
    def updateMoves(self, screen):
        font = pygame.font.SysFont("brushscriptmt", 40)
        text1 = font.render("Moves", True, self.black)
        text2 = font.render("Left:", True, self.black)
        text3 = font.render("%d" % self.moves, True, self.black)
        screen.blit(text1, (self.width - 13*self.margin//8,
                2*self.margin + self.boxHeight))
        screen.blit(text2, (self.width - 25*self.margin//16,
                2*self.margin + self.boxHeight + 40))
        screen.blit(text3, (self.width - 11*self.margin//8,
                5*self.margin//2 + self.boxHeight + 50))
                
    def findRowMatches(self, row):
        #check all the rows for matches
        if row == len(self.board):
            return self.board
        elements = set()
        match = 1
        #goes through elements in each row
        for element in range(len(self.board[row])):
            if self.board[row][element] != 0:
                if elements == set():
                    elements.add(self.board[row][element])
                    continue
                elif self.board[row][element] in elements:
                    match += 1
                    #check if there is a match that includes last element in row
                    if element == len(self.board[row])-1:
                        if match == 3:
                            for i in range(match):
                                self.board[row][element-i] = 0
                        elif match == 4:
                            for i in range(match):
                                if i == 2:
                                    self.board[row][element-i] = self.snowflake
                                else:
                                    self.board[row][element-i] = 0
                        elif match >= 5:
                            for i in range(match):
                                if i == 3:
                                    self.board[row][element-i] = self.hotcoco
                                else:
                                    self.board[row][element-i] = 0
                #determine whether or not there is a match in middle of row
                else:
                    if match == 3:
                        for i in range(1,match+1):
                            self.board[row][element-i] = 0
                    elif match == 4:
                        for i in range(1,match+1):
                            if i == 2:
                                self.board[row][element-i] = self.snowflake
                            else:
                                self.board[row][element-i] = 0
                    elif match >= 5:
                        for i in range(1,match+1):
                            if i == 3:
                                self.board[row][element-i] = self.hotcoco
                            else:
                                self.board[row][element-i] = 0
                    match = 1
                    elements = set([self.board[row][element]])
        #reset elements before next recursive step
        elements = set()
        return Board.findRowMatches(self, row+1)
                    
    def findColMatches(self, col):
        if col == len(self.board[0]):
            return self.board
        elements = set()
        match = 1
        for element in range(len(self.board)):
            if self.board[element][col] != 0:
                if elements == set():
                    elements.add(self.board[element][col])
                    continue
                elif self.board[element][col] in elements:
                    match += 1
                    #checks if there is a match containing last element in col
                    if element == len(self.board)-1:
                        if match == 3:
                            for i in range(match):
                                self.board[element-i][col] = 0
                        elif match == 4:
                            for i in range(match):
                                if i == 2:
                                    self.board[element-i][col] = self.snowflake
                                else:
                                    self.board[element-i][col] = 0
                        elif match >= 5:
                            for i in range(match):
                                if i == 3:
                                    self.board[element-i][col] = self.hotcoco
                                else:
                                    self.board[element-i][col] = 0
                #checks if there is a match in middle of the col
                else:
                    if match == 3:
                        for i in range(1,match+1):
                            self.board[element-i][col] = 0
                    elif match == 4:
                        for i in range(1,match+1):
                            if i == 2:
                                self.board[element-i][col] = self.snowflake
                            else:
                                self.board[element-i][col] = 0
                    elif match >= 5:
                        for i in range(1,match+1):
                            if i == 3:
                                self.board[element-i][col] = self.hotcoco
                            else:
                                self.board[element-i][col] = 0
                    match = 1
                    elements = set([self.board[element][col]])
        elements = set()
        return Board.findColMatches(self, col+1)
    
    def isLegalMove(self, keyCode, modifier):
        currX = self.startX
        currY = self.startY
        #sets the row/col of selected element
        col = (currX)//self.boxWidth
        row = (currY)//self.boxHeight
        if keyCode == pygame.K_UP:
            if 1 <= col <= self.cols-2 and self.board[row][col] == self.board[row-1][col+1] and self.board[row][col] == self.board[row-1][col-1]:
                return True
            elif col <= self.cols-3 and self.board[row][col] == self.board[row-1][col+1] and self.board[row][col] == self.board[row-1][col+2]:
                return True
            elif col >= 2 and self.board[row][col] == self.board[row-1][col-1] and self.board[row][col] == self.board[row-1][col-2]:
                return True
            elif row >= 3 and self.board[row][col] == self.board[row-2][col] and self.board[row][col] == self.board[row-3][col]:
                return True
        if keyCode == pygame.K_DOWN:
            if 1 <= col <= self.cols-2 and self.board[row][col] == self.board[row+1][col+1] and self.board[row][col] == self.board[row+1][col-1]:
                return True
            elif col <= self.cols-3 and self.board[row][col] == self.board[row+1][col+1] and self.board[row][col] == self.board[row+1][col+2]:
                return True
            elif col >= 2 and self.board[row][col] == self.board[row+1][col-1] and self.board[row][col] == self.board[row+1][col-2]:
                return True
            elif row <= self.rows-4 and self.board[row][col] == self.board[row+2][col] and self.board[row][col] == self.board[row+3][col]:
                return True
        if keyCode == pygame.K_RIGHT:
            if 1 <= row <= self.rows-2 and self.board[row][col] == self.board[row-1][col+1] and self.board[row][col] == self.board[row+1][col+1]:
                return True
            elif row >= 2 and self.board[row][col] == self.board[row-1][col+1] and self.board[row][col] == self.board[row-2][col+1]:
                return True
            elif row <= self.rows-3 and self.board[row][col] == self.board[row+1][col+1] and self.board[row][col] == self.board[row+2][col+1]:
                return True
            elif col <= self.cols-4 and self.board[row][col] == self.board[row][col+2] and self.board[row][col] == self.board[row][col+3]:
                return True
        if keyCode == pygame.K_LEFT:
            if 1 <= row <= self.rows-2 and self.board[row][col] == self.board[row-1][col-1] and self.board[row][col] == self.board[row+1][col-1]:
                return True
            elif row >= 2 and self.board[row][col] == self.board[row-1][col-1] and self.board[row][col] == self.board[row-2][col-1]:
                return True
            elif row <= self.rows-3 and self.board[row][col] == self.board[row+1][col-1] and self.board[row][col] == self.board[row+2][col-1]:
                return True
            elif col >= 3 and self.board[row][col] == self.board[row][col-2] and self.board[row][col] == self.board[row][col-3]:
                return True
        return False
        
    def boardMousePressed(self, x, y):
        if 150 >= ((self.width-x)**2 + (y)**2)**.5:
            self.mode = "help"
        row = (y - self.margin) // self.boxHeight
        col = (x - self.margin) // self.boxWidth
        row = min(self.rows - 1, max(0,row))
        col = min(self.cols - 1, max(0,col))
        self.highlightX = col * self.boxWidth
        self.highlightY = row * self.boxHeight
        self.startX = self.highlightX
        self.startY = self.highlightY
        
    def boardKeyPressed(self, keyCode, modifier):
        currX = self.startX
        currY = self.startY
        #sets the row/col of selected element
        col = (self.highlightX)//self.boxWidth
        row = (self.highlightY)//self.boxHeight
        if keyCode == pygame.K_UP or keyCode == pygame.K_DOWN or keyCode == pygame.K_RIGHT or keyCode == pygame.K_LEFT:
            self.moves -= 1
        #what to do if there are no powerups involved
        if self.board[row][col] != self.snowflake and self.board[row][col] != self.hotcoco:
            #switch with candy above
            if keyCode == pygame.K_UP:
                if self.highlightY > 0 and row > 0 and Board.isLegalMove(self, keyCode, modifier):
                    self.highlightY -= self.boxHeight
                    tmp = self.board[row][col]
                    self.board[row][col] = self.board[row-1][col]
                    self.board[row-1][col] = tmp
                    if self.highlightY < currY - self.boxHeight or\
                            self.highlightX != currX:
                        self.moves += 1
                        self.highlightY += self.boxHeight
                        tmp = self.board[row-1][col]
                        self.board[row-1][col] = self.board[row][col]
                        self.board[row][col] = tmp
                else:
                    self.moves += 1
            #switch with candy below
            if keyCode == pygame.K_DOWN:
                if self.highlightY < self.height and row < len(self.board)-1 and Board.isLegalMove(self, keyCode, modifier):
                    self.highlightY += self.boxHeight
                    tmp = self.board[row][col]
                    self.board[row][col] = self.board[row+1][col]
                    self.board[row+1][col] = tmp
                    if self.highlightY > currY + self.boxHeight or\
                            self.highlightX != currX:
                        self.highlightY -= self.boxHeight
                        self.moves += 1
                        tmp = self.board[row+1][col]
                        self.board[row+1][col] = self.board[row][col]
                        self.board[row][col] = tmp
                else:
                    self.moves += 1
            #switch with candy to the right
            if keyCode == pygame.K_RIGHT:
                if self.highlightX < self.width and col < len(self.board[row])-1 and Board.isLegalMove(self, keyCode, modifier):
                    self.highlightX += self.boxWidth
                    tmp = self.board[row][col]
                    self.board[row][col] = self.board[row][col+1]
                    self.board[row][col+1] = tmp
                    if self.highlightX > currX + self.boxWidth or\
                            self.highlightY != currY:
                        self.highlightX -= self.boxWidth
                        self.moves += 1
                        tmp = self.board[row][col+1]
                        self.board[row][col+1] = self.board[row][col]
                        self.board[row][col] = tmp
                else:
                    self.moves += 1
            #switch with candy to the left
            if keyCode == pygame.K_LEFT:
                if self.highlightX > 0 and col > 0 and Board.isLegalMove(self, keyCode, modifier):
                    self.highlightX -= self.boxWidth
                    tmp = self.board[row][col]
                    self.board[row][col] = self.board[row][col-1]
                    self.board[row][col-1] = tmp
                    if self.highlightX < currX - self.boxWidth or\
                            self.highlightY != currY:
                        self.highlightX += self.boxWidth
                        self.moves += 1
                        tmp = self.board[row][col-1]
                        self.board[row][col-1] = self.board[row][col]
                        self.board[row][col] = tmp
                else:
                    self.moves += 1
        #eliminate rows/cols
        elif self.board[row][col] == self.snowflake:
            #remove row above
            if keyCode == pygame.K_UP:
                if self.highlightY > 0 and row > 0:
                    self.highlightY -= self.boxHeight
                    for element in range(len(self.board[row-1])):
                        self.board[row-1][element] = 0
                    for element in range(len(self.board)):
                        self.board[element][col] = 0
                    if self.highlightY < currY - self.boxHeight or\
                            self.highlightX != currX:
                        self.highlightY += self.boxHeight
                        self.moves += 1
                else:
                    self.moves += 1
            #remove row below
            if keyCode == pygame.K_DOWN:
                if self.highlightY < self.height and row < len(self.board)-1:
                    self.highlightY += self.boxHeight
                    for element in range(len(self.board[row+1])):
                        self.board[row+1][element] = 0
                    for element in range(len(self.board)):
                        self.board[element][col] = 0
                    if self.highlightY > currY + self.boxHeight or\
                            self.highlightX != currX:
                        self.highlightY -= self.boxHeight
                        self.moves += 1
                else:
                    self.moves += 1
            #remove col to the right
            if keyCode == pygame.K_RIGHT:
                if self.highlightX < self.width and col < len(self.board[row])-1:
                    self.highlightX += self.boxWidth
                    for element in range(len(self.board[row])):
                        self.board[row][element] = 0
                    for element in range(len(self.board)):
                        self.board[element][col+1] = 0
                    if self.highlightX > currX + self.boxWidth or\
                            self.highlightY != currY:
                        self.highlightX -= self.boxWidth
                        self.moves += 1
                else:
                    self.moves += 1
            #remove col to the left
            if keyCode == pygame.K_LEFT:
                if self.highlightX > 0 and col > 0:
                    self.highlightX -= self.boxWidth
                    for element in range(len(self.board[row])):
                        self.board[row][element] = 0
                    for element in range(len(self.board)):
                        self.board[element][col-1] = 0
                    if self.highlightX < currX - self.boxWidth or\
                            self.highlightY != currY:
                        self.highlightX += self.boxWidth
                        self.moves += 1
                else:
                    self.moves += 1
        #eliminate candy type
        elif self.board[row][col] == self.hotcoco:
            self.score *= 2
            #remove the candy above
            if keyCode == pygame.K_UP:
                if self.highlightY > 0 and row > 0:
                    self.highlightY -= self.boxHeight
                    eliminate = self.board[row-1][col]
                    self.board[row][col] = 0
                    for i in range(len(self.board)):
                        for j in range(len(self.board[i])):
                            if self.board[i][j] == eliminate:
                                self.board[i][j] = 0
                    if self.highlightY < currY - self.boxHeight or\
                            self.highlightX != currX:
                        self.highlightY += self.boxHeight
                        self.moves += 1
                else:
                    self.moves += 1
            #remove the candy below
            if keyCode == pygame.K_DOWN:
                if self.highlightY < self.height and row < len(self.board)-1:
                    self.highlightY += self.boxHeight
                    eliminate = self.board[row+1][col]
                    self.board[row][col] = 0
                    for i in range(len(self.board)):
                        for j in range(len(self.board[i])):
                            if self.board[i][j] == eliminate:
                                self.board[i][j] = 0
                    if self.highlightY > currY + self.boxHeight or\
                            self.highlightX != currX:
                        self.highlightY -= self.boxHeight
                        self.moves += 1
                else:
                    self.moves += 1
            #remove candy to the right
            if keyCode == pygame.K_RIGHT:
                if self.highlightX < self.width and col < len(self.board[row])-1:
                    self.highlightX += self.boxWidth
                    eliminate = self.board[row][col+1]
                    self.board[row][col] = 0
                    for i in range(len(self.board)):
                        for j in range(len(self.board[i])):
                            if self.board[i][j] == eliminate:
                                self.board[i][j] = 0
                    if self.highlightX > currX + self.boxWidth or\
                            self.highlightY != currY:
                        self.highlightX -= self.boxWidth
                        self.moves += 1
                else:
                    self.moves += 1
            #remove candy to the left
            if keyCode == pygame.K_LEFT:
                if self.highlightX > 0 and col > 0:
                    self.highlightX -= self.boxWidth
                    eliminate = self.board[row][col-1]
                    self.board[row][col] = 0
                    for i in range(len(self.board)):
                        for j in range(len(self.board[i])):
                            if self.board[i][j] == eliminate:
                                self.board[i][j] = 0
                    if self.highlightX < currX - self.boxWidth or\
                            self.highlightY != currY:
                        self.highlightX += self.boxWidth
                        self.moves += 1
                else:
                    self.moves += 1
        if keyCode == pygame.K_s:
            self.mode = "start"
        if keyCode == pygame.K_h:
            self.mode = "help"
        if keyCode == pygame.K_r:
            self.score = 0
            self.moves = 30
    
    def boardTimerFired(self, dt):
        pass
        
    def drawGrid(self, screen):
        for row in range(self.rows):
            for col in range(self.cols):
                pygame.draw.rect(screen, self.black,
                (self.margin + col*self.boxWidth, self.margin + row*self.boxHeight, self.boxWidth,self.boxHeight),4)
                
    def drawCandies(self, screen):
        for row in range(self.rows):
            for col in range(self.cols):
                x, y = self.margin + col*self.boxWidth + 5, self.margin + row*self.boxHeight + 10
                if self.board[row][col] != 0:
                    screen.blit(self.board[row][col], (x,y))
    
    def boardRedrawAll(self, screen):
        pygame.draw.rect(screen, self.yellow, (self.highlightX + self.margin,self.highlightY + self.margin, self.boxWidth, self.boxHeight))
        if self.moves == 30:
            self.score = 0
        Board.findRowMatches(self, 0)
        Board.findColMatches(self, 0)
        Board.drawGrid(self, screen)
        for row in range(len(self.board)-1,-1,-1):
            for col in range(len(self.board[row])):
                x, y = self.margin + col*self.boxWidth + 5, self.margin + row*self.boxHeight + 10
                if self.board[row][col] == 0:
                    self.score += 1
                    if row == 0:
                        self.board[row][col] = random.choice(self.candies)
                    elif row != 0 and self.board[row-1][col] != 0:
                        centerY = self.margin + (row-1)*self.boxHeight
                        if self.moves != 30:
                            while centerY < y:
                                centerY+=10
                                screen.blit(self.bg,(0,0))
                                pygame.draw.rect(screen, self.black, (self.width - 7*self.margin//4,self.margin + self.boxHeight, 5*self.margin//4,self.height - 2 * self.margin - 2 * self.boxHeight), 4)
                                Board.updateScore(self, screen)
                                Board.updateMoves(self, screen)
                                pygame.draw.rect(screen, self.yellow, (self.highlightX + self.margin,self.highlightY + self.margin, self.boxWidth, self.boxHeight))
                                font = pygame.font.SysFont("brushscriptmt", 40)
                                font2 = pygame.font.SysFont("trattatello", 40)
                                text1 = font.render("Goal:", True, self.black)
                                text2 = font.render("%d" % self.goal, True, self.black)
                                screen.blit(text1, (self.width - 13*self.margin//8,
                                        (7/2)*self.margin + self.boxHeight))
                                screen.blit(text2, (self.width - 3*self.margin//2,
                                        (4)*self.margin + self.boxHeight))
                                pygame.draw.circle(screen, self.yellow, (self.width, 0), 150)
                                pygame.draw.circle(screen, self.black, (self.width, 0), 150, 4)
                                text3 = font2.render("HELP", True, self.black)
                                screen.blit(text3, (self.width-self.margin, self.margin//4))
                                Board.drawGrid(self, screen)
                                Board.drawCandies(self, screen)
                                screen.blit(self.board[row-1][col],(x,centerY)) 
                                pygame.display.update()
                        self.board[row][col] = self.board[row-1][col]
                        self.board[row-1][col] = 0
                    elif row != 0 and self.board[row-1][col] == 0:
                        for j in range(row-1, -1, -1):
                            if self.board[j][col] != 0:
                                centerY = self.margin + (j)*self.boxHeight
                                if self.moves != 30:
                                    while centerY < y:
                                        centerY+=10
                                        screen.blit(self.bg,(0,0))
                                        pygame.draw.rect(screen, self.black, (self.width - 7*self.margin//4,self.margin + self.boxHeight, 5*self.margin//4,self.height - 2 * self.margin - 2 * self.boxHeight), 4)
                                        Board.updateScore(self, screen)
                                        Board.updateMoves(self, screen)
                                        pygame.draw.rect(screen, self.yellow, (self.highlightX + self.margin,self.highlightY + self.margin, self.boxWidth, self.boxHeight))
                                        font = pygame.font.SysFont("brushscriptmt", 40)
                                        font2 = pygame.font.SysFont("trattatello", 40)
                                        text1 = font.render("Goal:", True, self.black)
                                        text2 = font.render("%d" % self.goal, True, self.black)
                                        screen.blit(text1, (self.width - 13*self.margin//8,
                                                (7/2)*self.margin + self.boxHeight))
                                        screen.blit(text2, (self.width - 3*self.margin//2,
                                                (4)*self.margin + self.boxHeight))
                                        pygame.draw.circle(screen, self.yellow, (self.width, 0), 150)
                                        pygame.draw.circle(screen, self.black, (self.width, 0), 150, 4)
                                        text3 = font2.render("HELP", True, self.black)
                                        screen.blit(text3, (self.width-self.margin, self.margin//4))
                                        Board.drawGrid(self, screen)
                                        Board.drawCandies(self, screen)
                                        screen.blit(self.board[j][col], (x, centerY))
                                        pygame.display.update()
                                self.board[row][col] = self.board[j][col]
                                self.board[j][col] = 0
                                break
                            elif j == 0 and self.board[j][col] == 0:
                                self.board[row][col] = random.choice(self.candies)
                else:
                    screen.blit(self.board[row][col], (x,y))
        pygame.draw.rect(screen, self.black, (self.width - 7*self.margin//4,
                self.margin + self.boxHeight, 5*self.margin//4, 
                self.height - 2 * self.margin - 2 * self.boxHeight), 4)
        Board.updateScore(self, screen)
        Board.updateMoves(self, screen)
        font = pygame.font.SysFont("brushscriptmt", 40)
        font2 = pygame.font.SysFont("trattatello", 40)
        text1 = font.render("Goal:", True, self.black)
        text2 = font.render("%d" % self.goal, True, self.black)
        screen.blit(text1, (self.width - 13*self.margin//8,
                (7/2)*self.margin + self.boxHeight))
        screen.blit(text2, (self.width - 3*self.margin//2,
                (4)*self.margin + self.boxHeight))
        pygame.draw.circle(screen, self.yellow, (self.width, 0), 150)
        pygame.draw.circle(screen, self.black, (self.width, 0), 150, 4)
        text3 = font2.render("HELP", True, self.black)
        screen.blit(text3, (self.width-self.margin, self.margin//4))
        pygame.display.flip()
        if self.moves == 0:
            if self.score >= self.goal:
                self.mode = "winner"
            else:
                self.mode = "gameOver"