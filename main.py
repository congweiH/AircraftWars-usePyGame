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
AGAIN_POS = AGAIN_X, AGAIN_Y = (SCREEN_WIDTH/2-150, SCREEN_HEIGHT/2-40)
GAMEOVER_POS = GAMEOVER_X, GAMEOVER_Y = (SCREEN_WIDTH/2-150, SCREEN_HEIGHT/2+30)


pygame.init()  # 初始化pygame
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # 显示窗口，screen是一个surface对象
pygame.display.set_caption("AircraftWars")  # 设置窗体标题
pygame.display.set_icon(pygame.image.load("img/life.png"))  # 设置icon
background_img = pygame.image.load('img/background.png')

again_img = pygame.image.load('img/again.png')
gameover_img = pygame.image.load('img/gameover.png')

pause_nor = pygame.image.load('img/pause_nor.png')
resume_nor = pygame.image.load('img/resume_nor.png')

pause_pressed = pygame.image.load('img/pause_pressed.png')
resume_pressed = pygame.image.load('img/resume_pressed.png')

# 玩家飞机
player = Player()

# 子弹
bullet_img = pygame.image.load('img/bullet1.png')

# 敌机
enemies1 = pygame.sprite.Group()
enemies_down = pygame.sprite.Group()
bullets = pygame.sprite.Group()
enemy_fre = 0

start = True

def restart():
    global start
    global enemies1
    global enemies_down
    global enemy_fre
    global player
    global bullets
    if start == True:
        return False
    screen.fill(0)
    screen.blit(background_img,(0,0))
    screen.blit(again_img, AGAIN_POS)
    screen.blit(gameover_img, GAMEOVER_POS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == MOUSEBUTTONDOWN:
            M_X, M_Y = event.pos
            if GAMEOVER_X < M_X and M_X < GAMEOVER_X + gameover_img.get_rect().width and \
                    GAMEOVER_Y < M_Y and M_Y < GAMEOVER_Y + gameover_img.get_rect().height:
                pygame.quit()
                exit()
            if AGAIN_X < M_X and M_X < AGAIN_X + again_img.get_rect().width and AGAIN_Y < M_Y and \
                    M_Y < AGAIN_Y + again_img.get_rect().height:
                start = True
                player = Player()
                enemies1 = pygame.sprite.Group()
                enemies_down = pygame.sprite.Group()
                bullets = pygame.sprite.Group()
                enemy_fre = 0
                break

    pygame.display.update()

def pause_resume():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN and event.key == K_SPACE:
            # 当时状态是播放，需要改成暂停
            while True:
                screen.blit(pause_pressed, (SCREEN_WIDTH - pause_pressed.get_rect().width, 0))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    if event.type == KEYUP and event.key == K_SPACE:
                        while True:
                            screen.fill(0)
                            screen.blit(background_img, (0, 0))
                            screen.blit(resume_nor, (SCREEN_WIDTH - resume_nor.get_rect().width, 0))
                            player.draw(screen)
                            player.bullets.draw(screen)
                            enemies1.draw(screen)
                            for enemy in enemies1:
                                enemy.bullets.draw(screen)

                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    pygame.quit()
                                    exit()
                                if event.type == KEYDOWN and event.key == K_SPACE:
                                    while True:
                                        screen.blit(resume_pressed, (SCREEN_WIDTH - resume_pressed.get_rect().width, 0))
                                        for event in pygame.event.get():
                                            if event.type == KEYUP and event.key == K_SPACE:
                                                return True
                                        pygame.display.update()
                            pygame.display.update()
                pygame.display.update()

while True:
    if start == False:
        while True:
            if restart() == False:
                break
    else:
        while True:
            # 设置游戏最大帧率为60
            pygame.time.Clock().tick(60)
            # 绘制背景
            screen.fill(0)
            screen.blit(background_img, (0,0))
            screen.blit(pause_nor, (SCREEN_WIDTH - pause_nor.get_rect().width,0))
            # screen.blit(resume_nor, (SCREEN_WIDTH - resume_nor.get_rect().width, pause_pressed.get_rect().height))
            # 绘制玩家飞机
            if not player.is_hit:
                player.draw(screen)
                player.fire(bullet_img)
                player.bullets.draw(screen)
                # for bullet in player.bullets:
                #     bullets.add(bullet)
            else:
                if player.destory(screen):
                    player.life -= 1
                    player.is_hit = False
                    player.rect.topleft = [200, 600]
                    player.img_index = 0
                    player.down_index = 0
            if player.life <= 0:
                start = False
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
                # for bullet in enemy.bullets:
                #     bullets.add(bullet)
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
            # bullets.draw(screen)
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

            pause_resume()      # 暂停功能

            pygame.display.update()