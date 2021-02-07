import pygame
from Window import *

class Player:
    def __init__(self):
        # 加载图片精灵
        self.sprite = pygame.image.load(r'F:\workspace\AircraftWars-usePyGame\frame\Assets\me1.png')
        # 获取精灵的rect
        self.rect = self.sprite.get_rect()
        # 飞行的速度
        self.speed = 15

    def Update(self):
        pass

    def Render(self, window : Window):
        window.Draw(self.sprite, self.rect.topleft)
