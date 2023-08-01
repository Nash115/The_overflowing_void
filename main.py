import pyxel
from classes import event, player, menu

event.setPyxel(pyxel)

class App:
    def __init__(self):
        pyxel.init(160, 120, title="The overflowing void")
        pyxel.run(self.update, self.draw)
    def update(self):
        if menu.status == False:
            if event.left():
                player.move(-1,0)
            if event.right():
                player.move(1,0)
            if event.down():
                player.move(0,1)
            if event.up():
                player.move(0,-1)
        else:
            if event.simple_left():
                print("Déplacement simple")
            if event.simple_right():
                print("Déplacement simple")
            if event.simple_down():
                print("Déplacement simple")
            if event.simple_up():
                print("Déplacement simple")

        if event.confirm():
            print("Confirmation")

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(player.x,player.y,8,8,3)

App()