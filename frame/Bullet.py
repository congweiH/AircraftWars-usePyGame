import pygame
from Window import *

class Bullet:
    def __init__(self):
        
        self.sprite = pygame.image.load(r"F:\workspace\AircraftWars-usePyGame\frame\Assets\bullet1.png")

        self.rect = self.sprite.get_rect()

    def Update(self):
        pass

    def Render(self, window : Window):
        window.Draw(self.sprite, self.rect)