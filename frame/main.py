from Game import *


class main:
    def __init__(self):
        pygame.init()

        game = Game()

        while not game.GetWindow().IsDone():
            game.HandleInput()
            game.Update()
            game.Render()


if __name__ == "__main__":
    main()