import pygame

class Monster:
    def __init__(self, x, y, position):
        self.x = x
        self.y = y
        self.up = True
        self.heightCounter = 50
        self.position = position
        self.image = pygame.image.load("monster-image.png")
        self.rect = self.image.get_rect()

    def fly(self, screen):
        if self.up == True and self.heightCounter > 0:
            self.x += 1
            self.heightCounter -= 1
        elif self.up == False and self.heightCounter > 0:
            self.x -= 1
            self.heightCounter -= 1
        elif self.up == True and self.heightCounter <= 0:
            self.up = False
            self.heightCounter = 50
        elif self.up == False and self.heightCounter <= 0:
            self.up = True
            self.heightCounter = 50

        if self.y <= 800:
            if self.position == "left":
                self.x += 1
            elif self.position == "right":
                self.x -= 1

        self.y -= 1
        self.rect.center = (self.x, self.y)
        screen.blit(self.image, self.rect)
