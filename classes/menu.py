class Menu:
    def __init__(self):
        self.status = True
        self.selected = "Play"
        self.win = False
    def draw(self, pxl):
        pxl.blt(4*16,1*16,1,0,32,16*8,16,0) # Show title

        if not(self.win):
            if self.selected == "Play":
                pxl.blt(16*6.5, 16*2.5, 1, 48, 0, 16*3, 16*1, 0)
                pxl.blt(16*6.5, 16*4.5, 1, 0, 16, 16*3, 16*1, 0)
            else:
                pxl.blt(16*6.5, 16*2.5, 1, 0, 0, 16*3, 16*1, 0)
                pxl.blt(16*6.5, 16*4.5, 1, 48, 16, 16*3, 16*1, 0)
        else:
            pxl.text(16*6.5, 16*2.5, "Did u really win this game ?",7)
    def confirmed(self,pxl):
        if self.selected == "Play":
            self.status = False
        else:
            exit()
menu = Menu()