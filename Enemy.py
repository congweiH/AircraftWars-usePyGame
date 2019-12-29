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
        r = random.randint(0,2)
        self.image = self.enemy_img[r]
        self.rect = self.image.get_rect()
        self.rect.topleft = [random.randint(0, SCREEN_WIDTH - self.image.get_rect().width), 0]
        self.down_imgs = self.enemy_down_imgs[r]
        self.speed = 2
        self.down_index = 0
        self.mask = pygame.mask.from_surface(self.image)
        self.bullets = pygame.sprite.Group()
        self.fire_fre = 0

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
        self.rect.top += self.speed

    def fire(self, bullet_img):
        if self.fire_fre % 15 == 0:
            self.bullets.add(Bullet(bullet_img, self.rect.midtop, 0))
        self.fire_fre += 1
        if self.fire_fre >= 15:
            self.fire_fre = 0
        # 清除子弹
        for bullet in self.bullets:
            bullet.move()
            if bullet.rect.top > SCREEN_HEIGHT:
                self.bullets.remove(bullet)

    def draw(self,screen):
        screen.blit(self.down_imgs[self.down_index // 2], self.rect)