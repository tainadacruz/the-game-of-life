from configs import *

class Grid():
    def __init__(self):
        self.__rows = []
        for r in range(LENGHT):
            col = [0]*LENGHT
            self.__rows.append(col)
        self.__grids = {"active" : self.__rows, "inactive" : self.__rows}
        self.__status = "active"
    
    def get_cell(self, r, c):
        try:
            value = self.__grids[self.__status][r][c]
        except:
            value = 0
        return value

    def set_cell(self, value=None):
        for row in range(LENGHT):
            for col in range(LENGHT):
                if value == None:
                    cell = random.choice([0,1])
                else:
                    cell = value
                self.__grids[self.__status][row][col] = cell

    @property
    def active(self):
        return self.__grids["active"]
    
    @property
    def inactive(self):
        return self.__grids["inactive"]

    @property
    def status(self):
        return self.__status

    @active.setter
    def active(self, value):
        self.__grids["active"] = value

    @inactive.setter
    def inactive(self, value):
        self.__grids["inactive"] = value

    @status.setter
    def status(self, value):
        self.__status = value
    

