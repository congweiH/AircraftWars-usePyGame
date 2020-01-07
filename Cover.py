# -*- coding:UTF-8 -*-
import pygame
from pygame.locals import *

class Cover:
    def __init__(self):
        self.SCREEN_HEIGHT = 700
        self.SCREEN_WIDTH = 480
        pygame.init()  # 初始化pygame
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))  # 显示窗口，screen是一个surface对象
        pygame.display.set_caption("AircraftWars")  # 设置窗体标题
        pygame.display.set_icon(pygame.image.load("img/life.png"))  # 设置icon

        self.bg = pygame.image.load('img/background.png')
        # 初始化
        pygame.font.init()
        # Font的第一个参数填写字体,None表示用默认字体
        self.myfont = pygame.font.Font("STCAIYUN.TTF", 60)
        # 可以理解为把文字转化为图片
        self.play = self.myfont.render("play", True, (255, 255, 255))
        self.help = self.myfont.render("help", True, (255, 255, 255))
        self.about = self.myfont.render("about", True, (255, 255, 255))

        self.is_quit = False

        self.play_pos = (150,200)
        self.help_pos = (150, 300)
        self.about_pos = (150, 400)

    def run(self):

        while True:

            self.screen.fill(0)
            self.screen.blit(self.bg, (0, 0))
            self.screen.blit(self.play, self.play_pos)
            self.screen.blit(self.help, self.help_pos)
            self.screen.blit(self.about, self.about_pos)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == MOUSEBUTTONDOWN:
                    M_x,M_y = event.pos
                    if M_x>self.play_pos[0] and M_y>self.play_pos[1] and M_x<self.play_pos[0]+self.play.get_rect().width \
                            and M_y<self.play_pos[1]+self.play.get_rect().height:
                        self.is_quit = True
                        break
                    elif M_x>self.help_pos[0] and M_y>self.help_pos[1] and M_x<self.help_pos[0]+self.help.get_rect().width \
                            and M_y<self.help_pos[1]+self.help.get_rect().height:
                        self.Help()
                    elif M_x>self.about_pos[0] and M_y>self.about_pos[1] and M_x<self.about_pos[0]+self.about.get_rect().width \
                            and M_y<self.about_pos[1]+self.about.get_rect().height:
                        self.About()

            if self.is_quit:
                break

            pygame.display.update()

    def Help(self):
        self.myfont = pygame.font.Font("STCAIYUN.TTF", 30)
        content1 = "up: player move up"
        content2 = "down: player move down"
        content3 = "left: player move left"
        content4 = "right: player move right"
        content5 = "space: for pause"
        content6 = "    x: make bomb to take effect"
        content1 = self.myfont.render(content1, True, (255,255,255))
        content2 = self.myfont.render(content2, True, (255,255,255))
        content3 = self.myfont.render(content3, True, (255,255,255))
        content4 = self.myfont.render(content4, True, (255,255,255))
        content5 = self.myfont.render(content5, True, (255,255,255))
        content6 = self.myfont.render(content6, True, (255,255,255))
        back = self.myfont.render("back", True, (255, 0, 0))
        while True:
            self.screen.fill(0)
            self.screen.blit(self.bg, (0, 0))
            self.screen.blit(content1, (0,0))
            self.screen.blit(content2, (0, 50))
            self.screen.blit(content3, (0, 100))
            self.screen.blit(content4, (0, 150))
            self.screen.blit(content5, (0, 200))
            self.screen.blit(content6, (0, 250))
            self.screen.blit(back, (400, 650))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == MOUSEBUTTONDOWN:
                    M_x, M_y = event.pos
                    if M_x>400 and M_y>650 and M_x<400+back.get_rect().width \
                            and M_y<650+back.get_rect().height:
                        return

            pygame.display.update()

    def About(self):

        self.myfont = pygame.font.Font("STCAIYUN.TTF", 30)
        content1 = "author: Congwei Huang"
        content2 = "Email: congwei_huang@163.com"
        content1 = self.myfont.render(content1, True, (255, 255, 255))
        content2 = self.myfont.render(content2, True, (255, 255, 255))
        back = self.myfont.render("back", True, (255, 0, 0))
        while True:
            self.screen.fill(0)
            self.screen.blit(self.bg, (0, 0))
            self.screen.blit(content1, (0, 0))
            self.screen.blit(content2, (0, 50))
            self.screen.blit(back, (400, 650))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == MOUSEBUTTONDOWN:
                    M_x, M_y = event.pos
                    if M_x > 400 and M_y > 650 and M_x < 400 + back.get_rect().width \
                            and M_y < 650 + back.get_rect().height:
                        return

            pygame.display.update()

if __name__ == '__main__':
    Cover().run()