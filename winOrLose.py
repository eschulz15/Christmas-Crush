##############################################################################
# winner
##############################################################################

class Winner(PygameGame):
    
    def winnerMousePressed(self, x, y):
        pass
    
    def winnerKeyPressed(self, keyCode, modifier):
        if keyCode == pygame.K_r:
            Board.createBoard(self)
            self.moves = 30
            self.score = 0
            self.mode = "start"
            
    def winnerTimerFired(self, dt):
        pass
    
    def winnerRedrawAll(self, screen):
        screen.fill((255, 255, 255))
        background = pygame.image.load("/Users/elizabethschulz/Desktop/112/term project/presents.png")
        bg = pygame.transform.scale(background, (self.width,
                self.height))
        screen.blit(bg, (0,0))
        font = pygame.font.SysFont("impact", 150)
        text = font.render("YOU WIN", True, self.black)
        screen.blit(text, (self.width//5, self.height//3))
        
##############################################################################
# gameOver
##############################################################################

class GameOver(PygameGame):
    
    def gameOverMousePressed(self, x, y):
        pass
    
    def gameOverKeyPressed(self, keyCode, modifier):
        if keyCode == pygame.K_r:
            Board.createBoard(self)
            self.moves = 30
            self.score = 0
            self.mode = "start"
            
    def gameOverTimerFired(self, dt):
        pass
    
    def gameOverRedrawAll(self, screen):
        coal = pygame.image.load("/Users/elizabethschulz/Desktop/112/term project/coal.png")
        bg = pygame.transform.scale(coal, (self.width,
                self.height))
        screen.blit(bg, (0,0))
        font = pygame.font.SysFont("impact", 150)
        text = font.render("You Lost", True, self.red)
        screen.blit(text, (self.width//5, self.height//3))