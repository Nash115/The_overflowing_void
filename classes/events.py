# C:\Users\...\AppData\Local\Programs\Python\Python311\Lib\site-packages\pyxel\__init__.pyi

class Event:
    def __init__(self):
        self.pxl = None
    def setPyxel(self,pxl):
        self.pxl = pxl
    def up(self):
        return self.pxl.btn(self.pxl.KEY_UP) or (self.pxl.btnv(self.pxl.GAMEPAD1_AXIS_LEFTY) < -10000)
    def down(self):
        return self.pxl.btn(self.pxl.KEY_DOWN) or (self.pxl.btnv(self.pxl.GAMEPAD1_AXIS_LEFTY) > 10000)
    def left(self):
        return self.pxl.btn(self.pxl.KEY_LEFT) or (self.pxl.btnv(self.pxl.GAMEPAD1_AXIS_LEFTX) < -10000)
    def right(self):
        return self.pxl.btn(self.pxl.KEY_RIGHT) or (self.pxl.btnv(self.pxl.GAMEPAD1_AXIS_LEFTX) > 10000)
    
    def simple_up(self):
        return self.pxl.btnp(self.pxl.KEY_UP) or (self.pxl.btnv(self.pxl.GAMEPAD1_AXIS_LEFTY) < -10000) or self.pxl.btnp(self.pxl.GAMEPAD1_BUTTON_DPAD_UP)
    def simple_down(self):
        return self.pxl.btnp(self.pxl.KEY_DOWN) or (self.pxl.btnv(self.pxl.GAMEPAD1_AXIS_LEFTY) > 10000) or self.pxl.btnp(self.pxl.GAMEPAD1_BUTTON_DPAD_DOWN)
    def simple_left(self):
        return self.pxl.btnp(self.pxl.KEY_LEFT) or (self.pxl.btnv(self.pxl.GAMEPAD1_AXIS_LEFTX) < -10000) or self.pxl.btnp(self.pxl.GAMEPAD1_BUTTON_DPAD_LEFT)
    def simple_right(self):
        return self.pxl.btnp(self.pxl.KEY_RIGHT) or (self.pxl.btnv(self.pxl.GAMEPAD1_AXIS_LEFTX) > 10000) or self.pxl.btnp(self.pxl.GAMEPAD1_BUTTON_DPAD_RIGHT)

    def confirm(self):
        return self.pxl.btnp(self.pxl.KEY_RETURN) or self.pxl.btnp(self.pxl.GAMEPAD1_BUTTON_A)
event = Event()