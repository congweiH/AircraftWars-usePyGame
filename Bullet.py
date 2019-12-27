# -*- coding:UTF-8 -*-
import pygame


class Bullet:
    def __init__(self, screen, x, y):
        self.x = x
        self.y = y
        self.screen = screen
        self.bullet1 = pygame.image.load("img/bullet1.png")

    def display(self):
        self.screen.blit(self.bullet1, (self.x,self.y))

    def move(self):
        self.y -= 10
        self.display()

    def isOut(self):
        if self.y < 0:
            return True
        else:
            return False