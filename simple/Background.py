# -*- coding:UTF-8 -*-

import pygame

class Background(pygame.sprite.Sprite):
    """游戏背景精灵"""

    def __init__(self, is_alt=False):
        super().__init__()
        self.image = pygame.image.load('img/background.png')
        self.rect = self.image.get_rect()
        self.speed = 1
        self.SCREEN_HEIGHT = 700
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        self.rect.y += self.speed
        # 2.判断是否移出屏幕，如果移出屏幕，将图像设置到屏幕的上方
        if self.rect.y >= self.SCREEN_HEIGHT:
            self.rect.y = -self.rect.height