from configs import *

class Game():
    def __init__(self, grid):
        pg.init()
        self.__screen = SCREEN
        self.__clock = CLOCK
        self.__grids = grid
        self.__active = self.__grids.active
        self.__inactive = self.__grids.inactive
        self.__status = self.__grids.status
        self.__grids.set_cell()

    def draw_grid(self):
        for row in range(LENGHT):
            for col in range(LENGHT):
                if self.__status == "active":
                    if (self.__active[row][col] == 1):
                        color = WHITE
                    elif (self.__active[row][col] == 0):
                        color = BLACK
                elif self.__status == "inactive":
                    if (self.__inactive[row][col] == 1):
                        color = WHITE
                    elif (self.__inactive[row][col] == 0):
                        color = BLACK
                pg.draw.rect(self.__screen, color, (row*10, col*10, TILE, TILE))

    def change_status(self):
        if self.__status == "active":
            self.__grids.status = "inactive"
            self.__status = "inactive"
        elif self.__status == "inactive":
            self.__grids.status = "active"
            self.__status = "active"

    def check_neighbours(self, row, col):
        neighbours_alive = 0
        neighbours_alive += self.__grids.get_cell(row-1, col-1)
        neighbours_alive += self.__grids.get_cell(row-1, col)
        neighbours_alive += self.__grids.get_cell(row-1, col+1)
        neighbours_alive += self.__grids.get_cell(row, col-1)
        neighbours_alive += self.__grids.get_cell(row, col+1)
        neighbours_alive += self.__grids.get_cell(row+1, col-1)
        neighbours_alive += self.__grids.get_cell(row+1, col)
        neighbours_alive += self.__grids.get_cell(row+1, col+1)

        if neighbours_alive > 3 or neighbours_alive < 2:
            return 0

        if self.__status == "active":
            if self.__active[row][col] == 0 and neighbours_alive == 3:
                return 1
            if self.__active[row][col] == 1 and (neighbours_alive == 2 or neighbours_alive == 3):
                return 1
            else:
                return 0
        elif self.__status == "inactive":
            if self.__inactive[row][col] == 0 and neighbours_alive == 3:
                return 1
            if self.__inactive[row][col] == 1 and (neighbours_alive == 2 or neighbours_alive == 3):
                return 1
            else: 
                return 0
        
    def update_generation(self):
        for row in range(LENGHT):
            for col in range(LENGHT):
                next_state = self.check_neighbours(row,col)
                if self.__status == "inactive":
                    self.__active[row][col] = next_state
                elif self.__status == "active":
                    self.__inactive[row][col] = next_state

    def handle_events(self):
        for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()

    def run(self):
        while True:
            self.__clock.tick(7)
            self.handle_events()
            self.draw_grid()
            self.update_generation()
            self.change_status()
            print(self.__status)
            pg.display.flip()