import pyxel,json
from classes import event, player, menu

event.setPyxel(pyxel)

with open("settings.json","r") as f:
    settings = json.load(f)

class App:
    def __init__(self):
        pyxel.init(settings["size"][0]*16, settings["size"][1]*16, title="The overflowing void")
        pyxel.load("my_resource.pyxres")
        pyxel.playm(0, loop=True)
        pyxel.run(self.update, self.draw)
    def update(self):
        if menu.status == False:
            if event.simple_left():
                player.move(-1,0)
            if event.simple_right():
                player.move(1,0)
            if event.simple_down():
                player.move(0,1)
            if event.simple_up():
                player.move(0,-1)
        else:
            if event.simple_down():
                menu.selected = "Quit"
            if event.simple_up():
                menu.selected = "Play"

        if event.confirm():
            if menu.status == False:
                pass
            else:
                menu.confirmed(pyxel)
                
    def draw(self):
        pyxel.cls(0)

        if menu.status == False:
            player.draw(pyxel)
        else:
            menu.draw(pyxel)

App()