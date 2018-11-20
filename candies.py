import pygame

class GamePiece(pygame.sprite.Sprite):
    def __init__(self,x,y,image):
        super(GamePiece, self).__init__()
        w, h = image.get_size()
        self.x, self.y, self.image = x, y, image
        self.updateRect()

    def updateRect(self):
        w,h = self.image.get_size()
        self.w, self.h = w, h
        self.rect = pygame.Rect(self.x, self.y, w, h)
        
    def update(self, screenWidth, screenHeight):
        if self.rect.left > screenWidth:
            self.x -= screenWidth + self.w
        elif self.rect.right < 0:
            self.x += screenWidth + self.w
        if self.rect.top > screenHeight:
            self.y -= screenHeight + self.h
        elif self.rect.bottom < 0:
            self.y += screenHeight + self.h
        self.updateRect()
        
class Candy(GamePiece):
        
    def update(self, keysDown, screenWidth, screenHeight, changeX, changeY):
        if keysDown(pygame.K_UP):
            self.y -= changeY
        if keysDown(pygame.K_DOWN):
            self.y += changeY
        if keysDown(pygame.K_RIGHT):
            self.x += changeX
        if keysDown(pygame.K_LEFT):
            self.x -= changeX
        super(Candy, self).update(screenWidth, screenHeight)
        
class Peppermint(Candy):
    @staticmethod
    def init():
        Peppermint.pImage = pygame.image.load("/Users/elizabethschulz/Desktop/112/term project/candy1-2.png").convert_alpha()
        
    def __init__(self, x, y):
        super(Peppermint, self).__init__(x,y,Peppermint.pImage)
        
class Tree(Candy):
    @staticmethod
    def init():
        Tree.xmasImage = pygame.image.load("/Users/elizabethschulz/Desktop/112/term project/christmastree.png").convert_alpha()
        
    def __init__(self, x, y):
        super(Tree, self).__init__(x,y,Tree.xmasImage)
        
class Hat(Candy):
    @staticmethod
    def init():
        Hat.hatImage = pygame.image.load("/Users/elizabethschulz/Desktop/112/term project/santa.png").convert_alpha()
        
    def __init__(self, x, y):
        super(Hat, self).__init__(x,y,Hat.hatImage)
        
class CandyCane(Candy):
    @staticmethod
    def init():
        CandyCane.ccImage = pygame.image.load("/Users/elizabethschulz/Desktop/112/term project/candycane.png").convert_alpha()
        
    def __init__(self, x, y):
        super(CandyCane, self).__init__(x,y,CandyCane.ccImage)
        
class Joy(Candy):
    @staticmethod
    def init():
        Joy.joyImage = pygame.image.load("/Users/elizabethschulz/Desktop/112/term project/joy.png").convert_alpha()
        
    def __init__(self, x, y):
        super(Joy, self).__init__(x,y,Joy.joyImage)