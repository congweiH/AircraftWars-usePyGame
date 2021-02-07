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
        self.img_index = 0
        self.down_index = 0
        self.is_hit = False
        self.fire_fre = 0
        self.life = 3
        self.bomb = 0
        self.base = 15
        self.life_img = pygame.image.load('img/life.png')
        self.bomb_img = pygame.image.load('img/bomb.png')
        self.mask = pygame.mask.from_surface(self.image[0])

    def loadImage(self):
        image = [pygame.image.load('img/me1.png'), pygame.image.load('img/me2.png'),
                 pygame.image.load('img/me_destroy_1.png'), pygame.image.load('img/me_destroy_2.png'),
                 pygame.image.load('img/me_destroy_3.png'), pygame.image.load('img/me_destroy_4.png')]
        return image

    def draw(self,screen):
        screen.blit(self.image[self.img_index], self.rect)

    def draw_life_bomb(self,screen):
        delta = self.life_img.get_rect().width
        for i in range(self.life):
            screen.blit(self.life_img, (i * delta, 0))
        delta = self.bomb_img.get_rect().height
        for i in range(self.bomb):
            screen.blit(self.bomb_img, (0, SCREEN_HEIGHT - delta - i * delta))

    def destory(self, screen):
        self.img_index=self.down_index
        if self.down_index>5:
            return True
        self.draw(screen)
        self.down_index += 1

    def fire(self, bullet_img, bullets):
        if self.fire_fre % self.base == 0:
            bullets.add(Bullet(bullet_img, self.rect.midtop, 1))
        self.fire_fre += 1
        if self.fire_fre >= self.base:
            self.fire_fre = 0

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