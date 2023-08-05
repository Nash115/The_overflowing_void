import json

with open("settings.json","r") as f:
    settings = json.load(f)

class Player:
    def __init__(self):
        self.x = 1
        self.y = 1
        self.size = 16 # Assume that the player is a square
        self.speed = 1
    def move(self, xDirection, yDirection):
        if self.x + xDirection < 0:
            return False
        if self.x + xDirection > settings["size"][0]-1:
            return False
        if self.y + yDirection < 0:
            return False
        if self.y + yDirection > settings["size"][1]-1:
            return False
        self.x += xDirection*self.speed
        self.y += yDirection*self.speed
        return True
    def draw(self,pxl):
        pxl.rect(player.x*16,player.y*16,16,16,3)
player = Player()