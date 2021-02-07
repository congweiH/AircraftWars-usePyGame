import pygame

class Window:
    def __init__(self, windowTitle = "Window", windowSize = (640, 480)):

        self.SetUp(windowTitle, windowSize)

    
    def SetUp(self, windowTitle, windowSize):
        """初始化窗口"""
        self.windowTitle = windowTitle
        self.windowSize = windowSize

        self.window = pygame.display.set_mode(self.windowSize)
        pygame.display.set_caption(self.windowTitle)

        self.done = False

    # 窗口事件
    def Update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True

    
    def BeginDraw(self):
        """用黑色填充清屏"""
        self.window.fill((0,0,0))

    # 在窗口中画别的东西
    def Draw(self, drawable, topleft):
        self.window.blit(drawable, topleft)


    def EndDraw(self):
        """将画的东西展示出来"""
        pygame.display.update()

    # get set method
    def GetWindowSize(self):
        return self.windowSize
    
    def IsDone(self):
        return self.done