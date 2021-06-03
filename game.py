from configs import *

class Game():
    def __init__(self, grid):
        pg.init()
        self.__screen = SCREEN
        self.__grids = grid
        self.__active = self.__grids.active
        self.__inactive = self.__grids.inactive

    def draw_grid(self):
        for row in range(30):
            for tile in range(30):
                if self.__active[row][tile] == 1:
                    color = WHITE
                elif self.__active[row][tile] == 0:
                    color = BLACK
                pg.draw.rect(self.__screen, color, (row*20,tile*20, TILE, TILE))

    def update_generation(self):
        self.__grids.set_cell(None)

    def handle_events(self):
        for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()

    def run(self):
        while True:
            self.handle_events()
            #self.__screen.fill(BLACK)
            self.__grids.set_cell()
            self.draw_grid()
            pg.display.flip()