# -*- coding:UTF-8 -*-
import sys
import pygame
from Me import *
import time

def initWin():
    pygame.init()  # 初始化pygame
    # 设置窗体
    size = width, height = 480, 700  # 设置窗口大小
    screen = pygame.display.set_mode(size)  # 显示窗口，screen是一个surface对象
    pygame.display.set_caption("AircraftWars")  # 设置窗体标题
    pygame.display.set_icon(pygame.image.load("img/life.png"))  # 设置icon

    # 设置背景图片
    background = pygame.image.load('img/background.png')
    return screen,background

def monitoringEvents(me):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 点击关闭按钮，则退出
            sys.exit()
        if event.type == pygame.KEYDOWN:  # 按空格发射子弹
            if event.key == pygame.K_SPACE:
                me.fire()
    if pygame.key.get_pressed()[pygame.K_UP]:
        me.moveUp()
    if pygame.key.get_pressed()[pygame.K_DOWN]:
        me.moveDown()
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        me.moveLeft()
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        me.moveRight()

if __name__ == '__main__':
    screen,background = initWin()

    me = Me(screen)

    # 进入消息循环
    while True:
        # 检查事件
        screen.blit(background, (0, 0))
        me.display()

        monitoringEvents(me)

        pygame.display.update()

        time.sleep(0.01)

