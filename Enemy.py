# -*- coding:UTF-8 -*-
import pygame
from Bullet import *
import random

SCREEN_HEIGHT = 700
SCREEN_WIDTH = 480


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.enemy_img = []
        self.enemy_down_imgs = []
        self.loadImg()

        self.type = random.randint(0, 2)

        if self.type == 0:
            self.blood = 1
        elif self.type == 1:
            self.blood = 4
        else:
            self.blood = 8

        self.image = self.enemy_img[self.type]
        self.rect = self.image.get_rect()

        self.down_imgs = self.enemy_down_imgs[self.type]
        self.speed = 2
        self.down_index = 0
        self.mask = pygame.mask.from_surface(self.image)
        self.fire_fre = 0

        self.speedx = 2

        self.rect.topleft = [random.randint(0, SCREEN_WIDTH - self.image.get_rect().width), 0]

    def loadImg(self):
        self.enemy_img = [pygame.image.load('img/enemy1.png'), pygame.image.load('img/enemy2.png'),
                     pygame.image.load('img/enemy3_hit.png')]
        self.enemy_down_imgs = [[pygame.image.load('img/enemy1_down1.png'), pygame.image.load('img/enemy1_down2.png'),
                            pygame.image.load('img/enemy1_down3.png'), pygame.image.load('img/enemy1_down4.png')],
                           [pygame.image.load('img/enemy2_down1.png'), pygame.image.load('img/enemy2_down2.png'),
                            pygame.image.load('img/enemy2_down3.png'), pygame.image.load('img/enemy2_down4.png')],
                           [pygame.image.load('img/enemy3_down1.png'), pygame.image.load('img/enemy3_down2.png'),
                            pygame.image.load('img/enemy3_down3.png'), pygame.image.load('img/enemy3_down4.png'),
                            pygame.image.load('img/enemy3_down5.png'), pygame.image.load('img/enemy3_down6.png')]]

    def move(self):
        if self.type == 0 or self.type == 1:
            self.rect.top += self.speed
        elif self.type == 2:    # boss
            if self.rect.topleft == 0:
                self.rect.topleft = 0
            self.rect.x -= self.speedx
            if self.rect.x <=10:
                self.speedx = -self.speedx
            if self.rect.x >= 300:
                self.speedx = -self.speedx

    def fire(self, bullet_img, bullets):
        if self.fire_fre % 60 == 0:
            bullets.add(Bullet(bullet_img, self.rect.midbottom, 0))
        self.fire_fre += 1
        if self.fire_fre >= 60:
            self.fire_fre = 0

    def draw(self,screen):
        screen.blit(self.down_imgs[self.down_index // 2], self.rect)