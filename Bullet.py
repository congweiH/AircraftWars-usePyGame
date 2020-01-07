# -*- coding:UTF-8 -*-
import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, bullet_img, init_pos, flag):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.midbottom = init_pos
        self.speed = 10
        self.flag = flag

    def update(self):
        if self.flag == 1:  # 我方飞机
            self.rect.top -= self.speed
        elif self.flag == -1:   # bomb
            self.rect.top += self.speed - 6
        else:   # 敌机
            self.rect.top += self.speed - 7
