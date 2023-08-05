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
                if room.checkMove(player.x,player.y,-1,0):
                    player.move(-1,0)
            if event.simple_right():
                if room.checkMove(player.x,player.y,1,0):
                    player.move(1,0)
            if event.simple_down():
                if room.checkMove(player.x,player.y,0,1):
                    player.move(0,1)
            if event.simple_up():
                if room.checkMove(player.x,player.y,0,-1):
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

        if (actualRoom != False) and rooms != []:
            rooms.pop(0)
            player.x = actualRoom[0]
            player.y = actualRoom[1]

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

        if menu.status == False:
            pyxel.text(0,0,f"> Room_{room.number}",3)

        pyxel.text(0,6,f"({player.x},{player.y})",3)

if __name__ == "__main__":
    App()