# -*- coding:UTF-8 -*-
from Player import *
from pygame.locals import *
from Enemy import *
from Background import *
import time
from Cover import Cover


class Main:
    def __init__(self):
        self.SCREEN_HEIGHT = 700
        self.SCREEN_WIDTH = 480
        self.AGAIN_POS = self.AGAIN_X, self.AGAIN_Y = (self.SCREEN_WIDTH/2-150, self.SCREEN_HEIGHT/2-40)
        self.GAMEOVER_POS = self.GAMEOVER_X, self.GAMEOVER_Y = (self.SCREEN_WIDTH/2-150, self.SCREEN_HEIGHT/2+30)
        # 加载图片
        self.again_img = pygame.image.load('img/again.png')
        self.gameover_img = pygame.image.load('img/gameover.png')
        self.pause_nor = pygame.image.load('img/pause_nor.png')
        self.resume_nor = pygame.image.load('img/resume_nor.png')
        self.pause_pressed = pygame.image.load('img/pause_pressed.png')
        self.resume_pressed = pygame.image.load('img/resume_pressed.png')
        self.bullet_img = pygame.image.load('img/bullet1.png')
        self.bomb_supply = pygame.image.load('img/bomb_supply.png')
        self.bullet_supply = pygame.image.load('img/bullet_supply.png')
        # 背景
        bg1 = Background()
        bg2 = Background(True)
        bg1.rect.y = 0
        bg2.rect.y = -self.SCREEN_HEIGHT
        self.back_groud = pygame.sprite.Group(bg1,bg2)

        self.time = 0
        self.starting = True
        self.score = 0
        # 玩家飞机
        self.player = Player()
        self.player_bullets = pygame.sprite.Group()

        # 炸药包
        self.bombs = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()

        # 敌机
        self.enemies1 = pygame.sprite.Group()
        self.enemies_down = pygame.sprite.Group()
        self.enemy_bullets = pygame.sprite.Group()
        self.enemy_fre = 0
        self.boss_alive = False

        self.start_time = time.time()

        pygame.init()  # 初始化pygame
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))  # 显示窗口，screen是一个surface对象
        pygame.display.set_caption("AircraftWars")  # 设置窗体标题
        pygame.display.set_icon(pygame.image.load("img/life.png"))  # 设置icon

    def run(self):
        """实现主要逻辑"""
        while True:
            # 显示封面
            Cover().run()

            while self.starting:
                # 设置游戏最大帧率为60
                pygame.time.Clock().tick(60)

                # 绘制背景
                self.background_draw()

                # 绘制玩家飞机
                self.player_draw()
                # 绘制玩家击毁动画
                self.player_destory()
                # 判断游戏是否结束
                if self.gameover() == True: break

                # 生成敌机
                self.create_enemies()
                # 移动敌机
                self.enemies_move()
                # 绘制敌机
                self.enemies1.draw(self.screen)
                # 绘制敌机击毁动画
                self.enemies_destory()

                # 显示子弹
                self.bullets_draw()
                # bomb掉下来
                self.bomb_down()
                # 获得bomb
                self.get_bomb()

                self.get_bullet()

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

            # 是否重新游戏
            while not self.starting:
                if True == self.restart():
                    break

    def get_bullet(self):
        bullets = pygame.sprite.spritecollide(self.player, self.bullets, 1, pygame.sprite.collide_mask)
        if len(bullets) > 0:
            self.player.base -= 3
            if self.player.base <= 3:
                self.player.base = 3

    def make_bomb(self):
        self.player.bomb -= 1
        for enemy in self.enemies1:
            self.enemies_down.add(enemy)
            self.enemies1.remove(enemy)

    def get_bomb(self):
        bombs = pygame.sprite.spritecollide(self.player, self.bombs, 1, pygame.sprite.collide_mask)
        if len(bombs) > 0:
            for bomb in bombs:
                self.player.bomb += 1

    def bomb_down(self):
        if self.time % 500 == 0:
            self.bombs.add(Bullet(self.bomb_supply, [random.randint(0, SCREEN_WIDTH - 50), 0],-1))
        if self.time % 600 == 0:
            self.bullets.add(Bullet(self.bullet_supply, [random.randint(0, SCREEN_WIDTH - 50), 0],-1))

        self.bullets.update()
        self.bullets.draw(self.screen)

        self.time += 1
        if self.time > 100000:
            self.time = 0

        self.bombs.update()
        self.bombs.draw(self.screen)

    def background_draw(self):
        self.screen.fill(0)
        self.screen.blit(self.pause_nor, (SCREEN_WIDTH - self.pause_nor.get_rect().width, 0))
        self.back_groud.update()
        self.back_groud.draw(self.screen)

    def player_destory(self):
        """玩家击毁"""
        if time.time() - self.start_time < 5: return False
        list = pygame.sprite.spritecollide(self.player, self.enemies1, False, pygame.sprite.collide_mask)
        if len(list) > 0:
            for i in list:
                self.enemies_down.add(i)
                self.enemies1.remove(i)
            self.player.is_hit = True

    def enemies_destory(self):
        """敌机击毁"""
        enemies1_down = pygame.sprite.groupcollide(self.enemies1, self.player_bullets, 1, 1)
        for enemy_down in enemies1_down:
            enemy_down.blood -= 1
            if enemy_down.blood<=0:
                if enemy_down.type == 0:
                    self.score += 10
                elif enemy_down.type == 1:
                    self.score += 30
                elif enemy_down.type == 2:
                    self.score += 100
                    self.boss_alive = False
                self.enemies_down.add(enemy_down)
            else:
                self.enemies1.add(enemy_down)

        for enemy_down in self.enemies_down:
            if enemy_down.down_index > 7:
                self.enemies_down.remove(enemy_down)
                continue
            enemy_down.draw(self.screen)
            enemy_down.down_index += 1

    def gameover(self) -> bool:
        """三条命没了，就结束游戏"""
        if self.player.life <= 0:
            self.starting = False
            return True
        return False

    def player_draw(self):
        """绘制玩家"""
        if not self.player.is_hit:
            if time.time() - self.start_time < 5:
                if self.time % 2 == 0:
                    self.player.draw(self.screen)
            else:
                self.player.draw(self.screen)
            self.player.draw_life_bomb(self.screen)
            self.player.fire(self.bullet_img, self.player_bullets)
        else:
            if self.player.destory(self.screen):
                self.player.life -= 1
                self.player.is_hit = False
                self.player.rect.topleft = [200, 600]
                self.player.img_index = 0
                self.player.down_index = 0
                self.player.base = 15
                self.start_time = time.time()   # 开始计时

    def create_enemies(self):
        """生成敌机"""
        if len(self.enemies1) >= 5:return
        if self.enemy_fre % 50 == 0:
            enemy1 = Enemy()
            if enemy1.type == 2:
                if self.boss_alive:
                    while enemy1.type == 2:
                        enemy1 = Enemy()
                else:
                    self.boss_alive = True
            self.enemies1.add(enemy1)
        self.enemy_fre += 1
        if self.enemy_fre >= 100:
            self.enemy_fre = 0

    def enemies_move(self):
        """移动敌机"""
        for enemy in self.enemies1:
            enemy.move()
            enemy.fire(self.bullet_img, self.enemy_bullets)
            if time.time() - self.start_time < 5: continue
            if len(pygame.sprite.spritecollide(self.player, self.enemy_bullets, False,
                                               pygame.sprite.collide_mask)) > 0:
                self.player.is_hit = True
                break

    def bullets_draw(self):
        """绘制子弹 和 清除子弹"""
        self.player_bullets.draw(self.screen)
        self.enemy_bullets.draw(self.screen)
        for bullet in self.player_bullets:
            bullet.update()
            if bullet.rect.bottom < 0:
                self.player_bullets.remove(bullet)
        for bullet in self.enemy_bullets:
            bullet.update()
            if bullet.rect.top > SCREEN_HEIGHT:
                self.enemy_bullets.remove(bullet)

    def pause_resume(self):
        """暂停"""
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
                                # 绘制暂停的画面
                                self.screen.fill(0)
                                self.back_groud.draw(self.screen)
                                self.screen.blit(self.resume_nor, (self.SCREEN_WIDTH - self.resume_nor.get_rect().width, 0))
                                self.player.draw(self.screen)
                                self.player_bullets.draw(self.screen)
                                self.enemies1.draw(self.screen)
                                self.enemy_bullets.draw(self.screen)
                                self.bombs.draw(self.screen)
                                self.player.draw_life_bomb(self.screen)
                                self.bullets.draw(self.screen)

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
            if event.type == KEYDOWN and event.key == K_x and self.player.bomb>0:
                self.make_bomb()

    def restart(self):
        """是否重新游戏"""
        self.screen.fill(0)
        self.back_groud.draw(self.screen)
        self.screen.blit(self.again_img, self.AGAIN_POS)
        self.screen.blit(self.gameover_img, self.GAMEOVER_POS)

        # 初始化
        pygame.font.init()
        # Font的第一个参数填写字体,None表示用默认字体
        myfont = pygame.font.Font(None, 60)
        # 可以理解为把文字转化为图片
        textImage = myfont.render("SCORE: "+str(self.score), True,(0,0,255))
        # 将图片显示出来
        self.screen.blit(textImage, (130, 200))

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
                    # 重新生成对象
                    self.starting = True
                    self.player = Player()
                    self.enemies1 = pygame.sprite.Group()
                    self.enemies_down = pygame.sprite.Group()
                    self.player_bullets = pygame.sprite.Group()
                    self.enemy_bullets = pygame.sprite.Group()
                    self.enemy_fre = 0
                    break

        pygame.display.update()
        return self.starting

if __name__ == '__main__':
    Main().run()