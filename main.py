# -*- coding:UTF-8 -*-
import sys
import pygame
from Player import *
from pygame.locals import *
import time
import random
from Enemy import *

SCREEN_HEIGHT = 700
SCREEN_WIDTH = 480


pygame.init()  # 初始化pygame
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # 显示窗口，screen是一个surface对象
pygame.display.set_caption("AircraftWars")  # 设置窗体标题
pygame.display.set_icon(pygame.image.load("img/life.png"))  # 设置icon
background_img = pygame.image.load('img/background.png')

# 玩家飞机
player = Player()

# 子弹
bullet_img = pygame.image.load('img/bullet1.png')

# 敌机
enemies1 = pygame.sprite.Group()
enemies_down = pygame.sprite.Group()
enemy_fre = 0

while True:
    # 设置游戏最大帧率为60
    pygame.time.Clock().tick(60)
    # 绘制背景
    screen.fill(0)
    screen.blit(background_img, (0,0))
    # 绘制玩家飞机
    if not player.is_hit:
        player.draw(screen)
        player.fire(bullet_img)
        player.bullets.draw(screen)
    else:
        if player.destory(screen):
            break
    # 生成敌机
    if enemy_fre % 50 == 0:
        enemy1 = Enemy()
        enemies1.add(enemy1)
    enemy_fre += 1
    if enemy_fre >= 100:
        enemy_fre = 0
    # 移动敌机
    for enemy in enemies1:
        enemy.move()
        enemy.fire(bullet_img)
        enemy.bullets.draw(screen)
        if len(pygame.sprite.spritecollide(player,enemy.bullets, False,pygame.sprite.collide_mask))>0:
            player.is_hit = True
            break
    # 判断玩家是否被击中
    list = pygame.sprite.spritecollide(player, enemies1, False, pygame.sprite.collide_mask)
    if len(list)>0:
        for i in list:
            enemies_down.add(i)
            enemies1.remove(i)
        player.is_hit = True
    # 敌机被击中
    enemies1_down = pygame.sprite.groupcollide(enemies1,player.bullets,1,1)
    for enemy_down in enemies1_down:
        enemies_down.add(enemy_down)
    # 绘制敌机
    enemies1.draw(screen)
    # 绘制击毁动画
    for enemy_down in enemies_down:
        if enemy_down.down_index > 7:
            enemies_down.remove(enemy_down)
            continue
        enemy_down.draw(screen)
        enemy_down.down_index += 1

    # 监听键盘事件
    key_pressed = pygame.key.get_pressed()
    if not player.is_hit:
        if key_pressed[K_UP]:
            player.moveUp()
        if key_pressed[K_DOWN]:
            player.moveDown()
        if key_pressed[K_LEFT]:
            player.moveLeft()
        if key_pressed[K_RIGHT]:
            player.moveRight()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()