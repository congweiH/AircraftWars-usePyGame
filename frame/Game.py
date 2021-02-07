from Player import *
from Window import *

class Game:
    def __init__(self):
        # 创建窗口
        self.window = Window("飞机大战", (480, 700))

        # 创建玩家飞机
        self.player = Player()

        
    def HandleInput(self):
        pass


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


    