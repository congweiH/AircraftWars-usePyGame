# -*- coding:UTF-8 -*-
import pygame
from Bullet import *

SCREEN_HEIGHT = 700
SCREEN_WIDTH = 480


class Player(pygame.sprite.Sprite):
    def __init__(self, init_pos=None):
        pygame.sprite.Sprite.__init__(self)
        if init_pos is None:
            init_pos = [200, 600]
        self.image = self.loadImage()
        self.speed = 8
        self.rect = self.image[0].get_rect()
        self.rect.topleft = init_pos
        self.bullets = pygame.sprite.Group()
        self.img_index = 0
        self.is_hit = False

    def loadImage(self):
        image = []
        image.append(pygame.image.load('img/me1.png'))
        image.append(pygame.image.load('img/me2.png'))
        image.append(pygame.image.load('img/me_destroy_1.png'))
        image.append(pygame.image.load('img/me_destroy_2.png'))
        image.append(pygame.image.load('img/me_destroy_3.png'))
        image.append(pygame.image.load('img/me_destroy_4.png'))
        return image

    def fire(self, bullet_img):
        bullet = Bullet(bullet_img, self.rect.midtop)
        self.bullets.add(bullet)

    def moveUp(self):
        if self.rect.top <= 0:
           self.rect.top=0
        else:
            self.rect.top -= self.speed

    def moveDown(self):
        if self.rect.top>=SCREEN_HEIGHT-self.rect.height:
            self.rect.top=SCREEN_HEIGHT-self.rect.height
        else:
            self.rect.top+=self.speed

    def moveLeft(self):
        if self.rect.left <= 0:
            self.rect.left=0
        else:
            self.rect.left-=self.speed

    def moveRight(self):
        if self.rect.left>=SCREEN_WIDTH-self.rect.width:
            self.rect.left=SCREEN_WIDTH-self.rect.width
        else:
            self.rect.left += self.speed
