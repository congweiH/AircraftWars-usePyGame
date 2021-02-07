from Player import *
from Window import *
import pygame

class Game:
    def __init__(self):
        # 创建窗口
        self.window = Window("飞机大战", (480, 700))

        # 创建玩家飞机
        self.player = Player()

    def HandleInput(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_UP]:
            self.player.moveUp()
        if key_pressed[pygame.K_DOWN]:
            self.player.moveDown()
        if key_pressed[pygame.K_LEFT]:
            self.player.moveLeft()
        if key_pressed[pygame.K_RIGHT]:
            self.player.moveRight()


    def Update(self):
        self.window.Update()
        ############## update here #################


        ############################################


    def Render(self):
        self.window.BeginDraw()
        ################ draw here ##################
        # 渲染玩家飞机
        self.player.Render(self.window)
        #############################################
        self.window.EndDraw()

    # get set methods
    def GetWindow(self):
        return self.window


    