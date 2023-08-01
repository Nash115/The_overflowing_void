class Player:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 8 # The "hitbox" of the player is a square
        self.speed = 1
        self.hitbox = []
    def move(self, xDirection, yDirection):
        self.x += xDirection*self.speed
        self.y += yDirection*self.speed
    def adaptHitbox(self):
        self.hitbox = []
        self.hitbox.append((self.x,self.y),(self.x+self.size,self.y+self.size))
player = Player()