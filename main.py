# -*- coding:UTF-8 -*-
import sys
import pygame

pygame.init()   # 初始化pygame
# 设置窗体
size = width, height = 480, 700  # 设置窗口大小
screen = pygame.display.set_mode(size)  # 显示窗口，screen是一个surface对象
pygame.display.set_caption("AircraftWars")  # 设置窗体标题
pygame.display.set_icon(pygame.image.load("img/life.png"))  # 设置icon

# 加载图片
background = pygame.image.load('img/background.png')
screen.blit(background, background.get_rect())
me2 = pygame.image.load('img/me2.png')
me1 = pygame.image.load('img/me1.png')
me1Rect = me1.get_rect()
me2Rect = me2.get_rect()

posx, posy = (200, 450)

# 进入消息循环

pygame.display.flip()
while True:
    # 检查事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # 点击关闭按钮，则退出
            sys.exit()
    # screen.fill((255, 255, 255))
    if pygame.key.get_pressed()[pygame.K_UP]:
        posy -= 10
        if(posy<=0): posy = 0
        screen.blit(background, (0, 0))
        screen.blit(me2, (posx, posy))
        pygame.display.update()
    if pygame.key.get_pressed()[pygame.K_DOWN]:
        posy += 10
        if(posy+me2.get_height()>=700): posy = 700 - me2.get_height()
        screen.blit(background, (0, 0))
        screen.blit(me2, (posx, posy))
        pygame.display.update()
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        posx -= 10
        if posx<=0: posx = 0
        screen.blit(background, (0, 0))
        screen.blit(me2, (posx, posy))
        pygame.display.update()
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        posx += 10
        if posx+me2.get_width()>=480: posx = 480 - me2.get_width()
        screen.blit(background, (0, 0))
        screen.blit(me2, (posx, posy))
        pygame.display.update()


    screen.blit(me1, (posx, posy))
    pygame.display.flip()

pygame.quit()   # 退出pygame
