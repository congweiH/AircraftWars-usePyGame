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
player_down_index = 16

# 子弹
fire_fre = 0    # 发射的频率
bullet_img = pygame.image.load('img/bullet1.png')

# 敌机
enemy1_img = pygame.image.load('img/enemy1.png')
enemy1_down_imgs = []
enemy1_down_imgs.append(pygame.image.load('img/enemy1_down1.png'))
enemy1_down_imgs.append(pygame.image.load('img/enemy1_down2.png'))
enemy1_down_imgs.append(pygame.image.load('img/enemy1_down3.png'))
enemy1_down_imgs.append(pygame.image.load('img/enemy1_down4.png'))
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
        screen.blit(player.image[player.img_index], player.rect)
        # player.img_index = fire_fre
    else:
        player.img_index=player_down_index
        screen.blit(player.image[player.img_index], player.rect)
        player_down_index += 1
        if player_down_index>47:
            break

    # 控制发射子弹和频率并发射子弹
    if not player.is_hit:
        if fire_fre % 15 == 0:
            player.fire(bullet_img)
        fire_fre += 1
        if fire_fre>=15:
            fire_fre = 0
    # 移动子弹，若超出窗口范围则删除
    for bullet in player.bullets:
        bullet.move()
        if bullet.rect.bottom<0:
            player.bullets.remove(bullet)
    # 绘制子弹
    player.bullets.draw(screen)
    # 生成敌机
    if enemy_fre % 50 == 0:
        enemy1_pos = [random.randint(0, SCREEN_WIDTH-enemy1_img.get_rect().width), 0]
        enemy1 = Enemy(enemy1_img, enemy1_down_imgs, enemy1_pos)
        enemies1.add(enemy1)
    enemy_fre += 1
    if enemy_fre>=100:
        enemy_fre = 0
    # 移动敌机
    for enemy in enemies1:
        enemy.move()
        # 判断玩家是否被击中
        if pygame.sprite.collide_circle(enemy, player):
            enemies_down.add(enemy)
            enemies1.remove(enemy)
            player.is_hit = True
            break
        if enemy.rect.top > SCREEN_HEIGHT:
            enemies1.remove(enemy)
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
        screen.blit(enemy_down.down_imgs[enemy_down.down_index // 2],enemy_down.rect)
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