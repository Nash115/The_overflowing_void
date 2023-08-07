import json, os

with open("textures/textures_data.json","r") as f:
    data = json.load(f)

class Room:
    """
    Evry rooms have 2 plates : one for the background and one for the collisions
    (because some levels need a background and a collision plate different)
    The value of "collision" in the ".json" is null if the collision plate is the same as the background plate
    """
    def __init__(self):
        self.number = 0
        self.finished = False
        self.spawn = [1,1]
        self.winPos = [15,4]
    def load(self) -> None:
        with open(f"levels/lv{self.number}.json","r") as f:
            file = json.load(f)
            self.plate = file["plate"]
            if file["collision"] != None:
                self.collision_plate = file["collision"]
            else:
                self.collision_plate = self.plate
    def checkMove(self, xPlayer, yPlayer, xDirection, yDirection) -> bool:
        collisions = ["W","E","N","S","NW","NE","SW","SE","wall"]
        if self.collision_plate[yPlayer+yDirection][xPlayer+xDirection] in collisions:
            return False
        else:
            return True
    def draw(self, pxl) -> None:
        for line in range(len(self.plate)):
            for column in range(len(self.plate[line])):
                if self.plate[line][column] != 0:
                    pxl.blt(column*16,line*16, 0, data[self.plate[line][column]][0], data[self.plate[line][column]][1], data[self.plate[line][column]][2], data[self.plate[line][column]][3], data[self.plate[line][column]][4])
    def update(self,xPlayer,yPlayer) -> None:
        if xPlayer == self.winPos[0] and yPlayer == self.winPos[1]:
            return True
        else:
            return False

# The update method of puzzles classes return False while the level is not finished
rooms = []

# Read all ".json" files in the folder "levels"
for i in range(1, len([i for i in os.listdir("levels") if i.endswith(".json") if i.startswith("lv")])+1):
    rooms.append(Room())
    rooms[i-1].number = i

for i in rooms:
    with open(f"levels/lv{i.number}.json","r") as f:
        actualJson = json.load(f)
    i.spawn = actualJson["spawn"]
    i.winPos = actualJson["win"]
    i.load()