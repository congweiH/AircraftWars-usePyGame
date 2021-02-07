import pygame
from Window import *

class Player:
    def __init__(self):
        # 加载图片精灵
        self.sprite = pygame.image.load(r'F:\workspace\AircraftWars-usePyGame\frame\Assets\me1.png')
        # 获取精灵的rect
        self.rect = self.sprite.get_rect()
        # 飞行的速度
        self.speed = 5

    def Update(self):
        pass

    def Render(self, window : Window):
        window.Draw(self.sprite, self.rect.topleft)

    def moveUp(self):
        if self.rect.top <= 0:
           self.rect.top=0
        else:
            self.rect.top -= self.speed

    def moveDown(self):
        if self.rect.top>=700-self.rect.height:
            self.rect.top=700-self.rect.height
        else:
            self.rect.top+=self.speed

    def moveLeft(self):
        if self.rect.left <= 0:
            self.rect.left=0
        else:
            self.rect.left-=self.speed

    def moveRight(self):
        if self.rect.left>=480-self.rect.width:
            self.rect.left=480-self.rect.width
        else:
            self.rect.left += self.speed
