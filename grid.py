from configs import *

class Grid():
    def __init__(self):
        self.__grids = {"active" : [[0]*30]*30, "inactive" : [[0]*30]*30}            

    def set_cell(self, value=None):
        for row in range(30):
            for tile in range(30):
                if value == None:
                    cell = random.choice([0,1])
                else:
                    cell = value
                self.__grids["active"][row][tile] = cell

    @property
    def active(self):
        return self.__grids["active"]
    
    @property
    def inactive(self):
        return self.__grids["inactive"]

    @active.setter
    def active(self, value):
        self.__grids["active"] = value

    @inactive.setter
    def inactive(self, value):
        self.__grids["inactive"] = value

    def update(self):
        pass
        '''row_count = 0
        for row in self.__grids["active"]:
            col_count = 0
            for tile in row:

                if col_count != 0:
                    if self.__matrix[row][tile-1]:
                        pass

                if col_count != 29:
                    if self.__matrix[row][tile+1]:
                        pass

                if row_count != 0:
                    if self.__matrix[row-1][tile] == 1:
                        pass
                    if self.__matrix[row-1][tile-1] == 1:
                        pass
                    if self.__matrix[row-1][tile+1] == 1:
                        pass

                if row_count != 29:
                    if self.__matrix[row+1][tile] == 1:
                        pass
                    if self.__matrix[row+1][tile-1] == 1:
                        pass
                    if self.__matrix[row+1][tile+1] == 1:
                        pass

                if tile == 0:
                    pass
                elif tile == 1:
                    pass
            
            col_count += 1
        row_count += 1
    '''
