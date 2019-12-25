# -*- coding:UTF-8 -*-
import sys
import pygame

pygame.init()   # 初始化pygame
size = width,height = 640, 480  # 设置窗口大小
screen = pygame.display.set_mode(size)  # 显示窗口

# 确保消息循环
while True:
    # 检查事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # 点击关闭按钮，则退出
            sys.exit()

pygame.quit()   # 退出pygame