import pyxel,json
from classes import event, player, menu, rooms

event.setPyxel(pyxel)

with open("settings.json","r") as f:
    settings = json.load(f)

room = None
actualRoom = False

class App:
    def __init__(self):
        pyxel.init(settings["size"][0]*16, settings["size"][1]*16, title="The overflowing void")
        pyxel.load("textures/my_resource.pyxres")
        pyxel.playm(0, loop=True)
        pyxel.run(self.update, self.draw)
    def update(self):
        global room, actualRoom

        if menu.status == False:
            if event.simple_left():
                player.move(-1,0)
            if event.simple_right():
                player.move(1,0)
            if event.simple_down():
                player.move(0,1)
            if event.simple_up():
                player.move(0,-1)
        elif menu.win == False:
            if event.simple_down():
                menu.selected = "Quit"
            if event.simple_up():
                menu.selected = "Play"

        if event.confirm():
            if menu.status == False:
                pass
            else:
                menu.confirmed(pyxel)

        if actualRoom and rooms != []:
            rooms.pop(0)

        if rooms == []:
            menu.win = True
            menu.status = True
        else:
            room = rooms[0]
            actualRoom = room.update(player.x,player.y)
                
    def draw(self):
        global room

        pyxel.cls(0)

        if menu.status == False:
            room.draw(pyxel)
            player.draw(pyxel)
        else:
            menu.draw(pyxel)

        pyxel.text(0,0,f"({player.x},{player.y})",3)

if __name__ == "__main__":
    App()