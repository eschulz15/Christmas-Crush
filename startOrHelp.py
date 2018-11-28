##############################################################################
# start
##############################################################################

class Start(PygameGame):
        
    def startMousePressed(self, x, y):
        #expert
        if 265 <= x <= 531 and 191 <= y <= 294:
            self.mode = "board"
        #intermediate
        elif 194 <= x <= 604 and 317 <= y <= 418:
            self.mode = "board"
        #beginner
        elif 123 <= x <= 677 and 441 <= y <= 543:
            self.mode = "board"
        #help
        elif 338 <= x <= 450 and 566 <= y <= 668:
            self.mode = "help"
            
    def startKeyPressed(self, keyCode, modifier):
        if keyCode == pygame.K_p:
            self.mode = "board"
        if keyCode == pygame.K_h:
            self.mode = "help"
    
    def startTimerFired(self, dt):
        pass
        
    def startRedrawAll(self, screen):
        tree = pygame.image.load("/Users/elizabethschulz/Desktop/112/term project/levels.png").convert_alpha()
        level = pygame.transform.scale(tree, (self.width - self.margin,
                self.height+2*self.margin))
        screen.blit(level, (3*self.margin/4, self.margin))
        font = pygame.font.SysFont("trattatello", 110)
        text = font.render("Christmas Crush", True, self.black)
        screen.blit(text, (self.width//8, self.margin//4))
        
##############################################################################
# help
##############################################################################

class Help(PygameGame):
    def instructions(self,screen):
        font1 = pygame.font.SysFont("timesnewroman", 60)
        text = font1.render("How To Play:", True, self.black)
        screen.blit(text, (self.width//4, self.height//5))
        font2 = pygame.font.SysFont("timesnewroman", 20)
        text1 = font2.render("1. Click on a candy to highlight it.", True, (0,0,0))
        text2 = font2.render("2. Move the arrow keys to switch two candies.", True, (0,0,0))
        text3 = font2.render("i. Candies will only be switched if they create a match.", True, (0,0,0))
        text4 = font2.render("3. Get 3 or more of the same candies in a row to earn points!", True, (0,0,0))
        text5 = font2.render("i. Candies near the bottom of the board will earn more points.", True, (0,0,0))
        text6 = font2.render("This candy will appear if 4 candies are matched.", True, (0,0,0))
        text7 = font2.render("When this candy is switched, it will", True, (0,0,0))
        text8 = font2.render("clear the column and row that it is in.", True, (0,0,0))
        text9 = font2.render("This candy will appear if 5 candies are matched.", True, (0,0,0))
        text10 = font2.render("When this candy is switched, it will clear", True, (0,0,0))
        text11 = font2.render("all of the candies it is switched with and the score will double.", True, (0,0,0))
        text12 = font2.render("Press 'h' any time to get to the help screen.", True, (0,0,0))
        text13 = font2.render("Press 'r' any time to restart the game.", True, (0,0,0))
        text14 = font2.render("Press 'p' to play.", True, (0,0,0))
        screen.blit(text1, (self.width//5, self.height//3))
        screen.blit(text2,(self.width//5, self.height//3 + 20))
        screen.blit(text3,(self.width//5 + self.margin//2, self.height//3 + 40))
        screen.blit(text4, (self.width//5, self.height//3 + 60))
        screen.blit(text5,(self.width//5 + self.margin//2, self.height//3 + 80))
        screen.blit(text6,(self.width//5 + self.margin, self.height//3 + 120))
        screen.blit(text7, (self.width//5 + self.margin, self.height//3 + 140))
        screen.blit(text8,(self.width//5 + self.margin, self.height//3 + 160))
        screen.blit(text9,(self.width//5 + self.margin, self.height//3 + 200))
        screen.blit(text10,(self.width//5 + self.margin, self.height//3 + 220))
        screen.blit(text11,(self.width//5 + self.margin, self.height//3 + 240))
        screen.blit(self.snowflake, (self.width//5 + self.margin//3, self.height//3 + 120))
        screen.blit(self.hotcoco, (self.width//5 + self.margin//3, self.height//3 + 200))
        screen.blit(text12, (self.width//5, self.height//3 + 260))
        screen.blit(text13,(self.width//5, self.height//3 + 280))
        screen.blit(text14,(self.width//5, self.height//3 + 300))
        
    def helpMousePressed(self, x, y):
        pass
        
    def helpTimerFired(self, dt):
        pass
    
    def helpKeyPressed(self, keyCode, modifier):
        if keyCode == pygame.K_p:
            self.mode = "board"
        if keyCode == pygame.K_s:
            self.mode = "start"
            
    def helpRedrawAll(self, screen):
        Help.instructions(self,screen)