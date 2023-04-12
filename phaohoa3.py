class Dot(): #Những chấm theo sau mỗi viên đạn
    def __int__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
    def update(self):
        #Giảm kích thước chấm
        if self.size > 0:
            self.size -= SPEED_CHANGE_SIZE*5
        else:
            self.size = 0

    def draw(self): #vẽ một chấm
        if self.size > 0:
            pygame.draw.circle(DISPLAYSURF, self.color, (int(self.x), int(self.y), int(self.size)))
