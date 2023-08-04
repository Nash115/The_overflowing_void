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
            ["W","g","g","g","g","g","g","g","g","g","g","g","g","g","g","E"],
            ["W","g","g","g","g","g","g","g","g","g","g","g","g","g","g","E"],
            ["W","g","g","g","g","g","g","g","g","g","g","g","g","g","g","E"],
            ["W","g","g","g","g","g","g","g","g","g","g","g","g","g","g","E"],
            ["SW","S","S","S","S","S","S","S","S","S","S","S","S","S","S","SE"]
        ]
        self.finished = False
    def draw(self, pxl) -> None:
        for line in range(len(self.plate)):
            for column in range(len(self.plate[line])):
                if self.plate[line][column] != 0:
                    pxl.blt(column*16,line*16, 0, data[self.plate[line][column]][0], data[self.plate[line][column]][1], data[self.plate[line][column]][2], data[self.plate[line][column]][3], data[self.plate[line][column]][4])


class Puzzle1(Room):
    def __init__(self):
        super().__init__()
        with open("levels/lv1.json","r") as f:
            self.plate = json.load(f)
    def update(self) -> None:
        pass

rooms = [
    Puzzle1(),
]
