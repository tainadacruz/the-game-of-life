from game import Game
from grid import Grid

if __name__ == '__main__':
    grids = Grid()
    game = Game(grids)
    game.run()