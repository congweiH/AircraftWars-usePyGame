# -*- coding:UTF-8 -*-
from Player import *
from pygame.locals import *
from Enemy import *

class Main:
    def __init__(self):
        self.SCREEN_HEIGHT = 700
        self.SCREEN_WIDTH = 480
        self.AGAIN_POS = self.AGAIN_X, self.AGAIN_Y = (self.SCREEN_WIDTH/2-150, self.SCREEN_HEIGHT/2-40)
        self.GAMEOVER_POS = self.GAMEOVER_X, self.GAMEOVER_Y = (self.SCREEN_WIDTH/2-150, self.SCREEN_HEIGHT/2+30)
        # 加载图片
        self.background_img = pygame.image.load('img/background.png')
        self.again_img = pygame.image.load('img/again.png')
        self.gameover_img = pygame.image.load('img/gameover.png')
        self.pause_nor = pygame.image.load('img/pause_nor.png')
        self.resume_nor = pygame.image.load('img/resume_nor.png')
        self.pause_pressed = pygame.image.load('img/pause_pressed.png')
        self.resume_pressed = pygame.image.load('img/resume_pressed.png')
        self.bullet_img = pygame.image.load('img/bullet1.png')

        self.start = True
        # 玩家飞机
        self.player = Player()

        # 敌机
        self.enemies1 = pygame.sprite.Group()
        self.enemies_down = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.enemy_fre = 0

        pygame.init()  # 初始化pygame
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # 显示窗口，screen是一个surface对象
        pygame.display.set_caption("AircraftWars")  # 设置窗体标题
        pygame.display.set_icon(pygame.image.load("img/life.png"))  # 设置icon

    def run(self):
        while True:
            if self.start == False:
                while True:
                    if  self.restart() == False:
                        break
            else:
                while True:
                    # 设置游戏最大帧率为60
                    pygame.time.Clock().tick(60)
                    # 绘制背景
                    self.screen.fill(0)
                    self.screen.blit(self.background_img, (0, 0))
                    self.screen.blit(self.pause_nor, (SCREEN_WIDTH - self.pause_nor.get_rect().width, 0))
                    # screen.blit(resume_nor, (SCREEN_WIDTH - resume_nor.get_rect().width, pause_pressed.get_rect().height))
                    # 绘制玩家飞机
                    if not  self.player.is_hit:
                        self.player.draw(self.screen)
                        self.player.fire(self.bullet_img)
                        self.player.bullets.draw(self.screen)
                        # for bullet in player.bullets:
                        #     bullets.add(bullet)
                    else:
                        if self.player.destory(self.screen):
                            self.player.life -= 1
                            self.player.is_hit = False
                            self.player.rect.topleft = [200, 600]
                            self.player.img_index = 0
                            self.player.down_index = 0
                    if self.player.life <= 0:
                        start = False
                        break
                    # 生成敌机
                    if self.enemy_fre % 50 == 0:
                        enemy1 = Enemy()
                        self.enemies1.add(enemy1)
                    self.enemy_fre += 1
                    if self.enemy_fre >= 100:
                        enemy_fre = 0
                    # 移动敌机
                    for enemy in self.enemies1:
                        enemy.move()
                        enemy.fire(self.bullet_img)
                        enemy.bullets.draw(self.screen)
                        # for bullet in enemy.bullets:
                        #     bullets.add(bullet)
                        if len(pygame.sprite.spritecollide(self.player, enemy.bullets, False,
                                                           pygame.sprite.collide_mask)) > 0:
                            self.player.is_hit = True
                            break
                    # 判断玩家是否被击中
                    list = pygame.sprite.spritecollide(self.player, self.enemies1, False, pygame.sprite.collide_mask)
                    if len(list) > 0:
                        for i in list:
                            self.enemies_down.add(i)
                            self.enemies1.remove(i)
                        self.player.is_hit = True
                    # 敌机被击中
                    enemies1_down = pygame.sprite.groupcollide(self.enemies1, self.player.bullets, 1, 1)
                    for enemy_down in enemies1_down:
                        self.enemies_down.add(enemy_down)
                    # 绘制敌机
                    self.enemies1.draw(self.screen)
                    # bullets.draw(screen)
                    # 绘制击毁动画
                    for enemy_down in self.enemies_down:
                        if enemy_down.down_index > 7:
                            self.enemies_down.remove(enemy_down)
                            continue
                        enemy_down.draw(self.screen)
                        enemy_down.down_index += 1
                    # 监听键盘事件
                    key_pressed = pygame.key.get_pressed()
                    if not self.player.is_hit:
                        if key_pressed[K_UP]:
                            self.player.moveUp()
                        if key_pressed[K_DOWN]:
                            self.player.moveDown()
                        if key_pressed[K_LEFT]:
                            self.player.moveLeft()
                        if key_pressed[K_RIGHT]:
                            self.player.moveRight()

                    self.pause_resume()  # 暂停功能

                    pygame.display.update()

    def pause_resume(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN and event.key == K_SPACE:
                # 当时状态是播放，需要改成暂停
                while True:
                    self.screen.blit(self.pause_pressed, (self.SCREEN_WIDTH - self.pause_pressed.get_rect().width, 0))
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            exit()
                        if event.type == KEYUP and event.key == K_SPACE:
                            while True:
                                self.screen.fill(0)
                                self.screen.blit(self.background_img, (0, 0))
                                self.screen.blit(self.resume_nor, (self.SCREEN_WIDTH - self.resume_nor.get_rect().width, 0))
                                self.player.draw(self.screen)
                                self.player.bullets.draw(self.screen)
                                self.enemies1.draw(self.screen)
                                for enemy in self.enemies1:
                                    enemy.bullets.draw(self.screen)

                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        exit()
                                    if event.type == KEYDOWN and event.key == K_SPACE:
                                        while True:
                                            self.screen.blit(self.resume_pressed,
                                                        (SCREEN_WIDTH - self.resume_pressed.get_rect().width, 0))
                                            for event in pygame.event.get():
                                                if event.type == KEYUP and event.key == K_SPACE:
                                                    return True
                                            pygame.display.update()
                                pygame.display.update()
                    pygame.display.update()

    def restart(self):
        if self.start == True:
            return False
        self.screen.fill(0)
        self.screen.blit(self.background_img, (0, 0))
        self.screen.blit(self.again_img, self.AGAIN_POS)
        self.screen.blit(self.gameover_img, self.GAMEOVER_POS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == MOUSEBUTTONDOWN:
                M_X, M_Y = event.pos
                if self.GAMEOVER_X < M_X and M_X < self.GAMEOVER_X + self.gameover_img.get_rect().width and \
                        self.GAMEOVER_Y < M_Y and M_Y < self.GAMEOVER_Y + self.gameover_img.get_rect().height:
                    pygame.quit()
                    exit()
                if self.AGAIN_X < M_X and M_X < self.AGAIN_X + self.again_img.get_rect().width and self.AGAIN_Y < M_Y and \
                        M_Y < self.AGAIN_Y + self.again_img.get_rect().height:
                    self.start = True
                    self.player = Player()
                    self.enemies1 = pygame.sprite.Group()
                    self.enemies_down = pygame.sprite.Group()
                    self.bullets = pygame.sprite.Group()
                    self.enemy_fre = 0
                    break

        pygame.display.update()

if __name__ == '__main__':
    Main().run()