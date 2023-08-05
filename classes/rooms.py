import json

with open("textures/textures_data.json","r") as f:
    data = json.load(f)

class Room:
    def __init__(self):
        self.plate = [
            ["NW","N","N","N","N","N","N","N","N","N","N","N","N","N","N","NE"],
            ["W","g","g","g","g","g","g","g","g","g","g","g","g","g","g","E"],
            ["W","g","g","g","g","g","g","g","g","g","g","g","g","g","g","E"],
            ["W","g","g","g","g","g","g","g","g","g","g","g","g","g","g","E"],
            ["W","g","g","g","g","g","g","g","g","g","g","g","g","g","end","E"],
            ["W","g","g","g","g","g","g","g","g","g","g","g","g","g","g","E"],
            ["W","g","g","g","g","g","g","g","g","g","g","g","g","g","g","E"],
            ["W","g","g","g","g","g","g","g","g","g","g","g","g","g","g","E"],
            ["SW","S","S","S","S","S","S","S","S","S","S","S","S","S","S","SE"]
        ]
        self.finished = False
        self.number = 0
    def checkMove(self, xPlayer, yPlayer, xDirection, yDirection) -> bool:
        collisions = ["W","E","N","S","NW","NE","SW","SE","wall"]
        if self.plate[yPlayer+yDirection][xPlayer+xDirection] in collisions:
            return False
        else:
            return True
    def draw(self, pxl) -> None:
        for line in range(len(self.plate)):
            for column in range(len(self.plate[line])):
                if self.plate[line][column] != 0:
                    pxl.blt(column*16,line*16, 0, data[self.plate[line][column]][0], data[self.plate[line][column]][1], data[self.plate[line][column]][2], data[self.plate[line][column]][3], data[self.plate[line][column]][4])

# The update method of puzzles classes return False while the level is not finished
rooms = []

class Puzzle1(Room):
    def __init__(self):
        super().__init__()
        with open("levels/lv1.json","r") as f:
            self.plate = json.load(f)
        self.number = 1
    def update(self,xPlayer,yPlayer) -> None:
        if xPlayer == 15 and yPlayer == 4:
            return [1,1]
        else:
            return False
rooms.append(Puzzle1())

class Puzzle2(Room):
    def __init__(self):
        super().__init__()
        with open("levels/lv2.json","r") as f:
            self.plate = json.load(f)
        self.number = 2
    def update(self,xPlayer,yPlayer) -> None:
        if xPlayer == 15 and yPlayer == 5:
            return [1,1]
        else:
            return False
rooms.append(Puzzle2())