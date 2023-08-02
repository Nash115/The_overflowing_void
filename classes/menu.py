class Menu:
    def __init__(self):
        self.status = True
        self.selected = "Play"
    def draw(self, pxl):
        pxl.blt(0,0,1,0,32,16*8,16,0) # Show title
        pxl.text(16*1.5, 16*0.5, "The overflowing void_", 7)

        if self.selected == "Play":
            pxl.blt(16*2.5, 16*1.5, 1, 48, 0, 16*3, 16*1, 0)
            pxl.blt(16*2.5, 16*3.5, 1, 0, 16, 16*3, 16*1, 0)
        else:
            pxl.blt(16*2.5, 16*1.5, 1, 0, 0, 16*3, 16*1, 0)
            pxl.blt(16*2.5, 16*3.5, 1, 48, 16, 16*3, 16*1, 0)
    def confirmed(self,pxl):
        if self.selected == "Play":
            self.status = False
        else:
            exit()
menu = Menu()