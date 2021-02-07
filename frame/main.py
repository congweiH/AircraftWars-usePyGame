from Game import *


class main:
    def __init__(self):
        pygame.init()

        game = Game()

        while not game.GetWindow().IsDone():
            # 设置游戏最大帧率为60
            pygame.time.Clock().tick(60)
            game.HandleInput()
            game.Update()
            game.Render()


if __name__ == "__main__":
    main()