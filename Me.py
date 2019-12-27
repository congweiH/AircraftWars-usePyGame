# -*- coding:UTF-8 -*-
import pygame
from Bullet import *

class Me:
    def __init__(self, screen, posx=200, posy=450):
        self.posx = posx
        self.posy = posy
        self.life = 3   # 生命值
        self.speed = 5
        self.screen = screen
        self.me2 = pygame.image.load('img/me2.png')
        self.bullet_list = []


    def display(self):
        self.screen.blit(self.me2,(self.posx, self.posy))

        bullet_list_out = []
        for bullet in self.bullet_list:
            bullet.move()
            bullet.display()
            if bullet.isOut():
                bullet_list_out.append(bullet)
        for bullet in bullet_list_out:
            self.bullet_list.remove(bullet)

    def moveUp(self):
        self.posy -= self.speed
        if self.posy <= 0:
            self.posy = 0

    def moveDown(self):
        self.posy += self.speed
        if self.posy + self.me2.get_height() >= 700:
            self.posy = 700 - self.me2.get_height()

    def moveLeft(self):
        self.posx -= self.speed
        if self.posx <= 0:
            self.posx = 0

    def moveRight(self):
        self.posx += self.speed
        if self.posx + self.me2.get_width() >= 480:
            self.posx = 480 - self.me2.get_width()

    def fire(self):
        self.bullet_list.append(Bullet(self.screen,self.posx + self.me2.get_width()/2,self.posy))
