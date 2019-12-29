# -*- coding:UTF-8 -*-
import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemy_img, enemy_down_imgs, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.rect.topleft = init_pos
        self.down_imgs = enemy_down_imgs
        self.speed = 2
        self.down_index = 0
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        self.rect.top += self.speed