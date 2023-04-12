import math


class Bullet(): #Viên đạn sau khi nổ
    def __int__(self, x, y, speed, angle, color):
        self.x = x
        self.y = y
        self.speed = speed
        self.angle = angle #Góc hợp bởi viên đạn phương ngang
        self.size = SIZE
        self.color = color

    def update(self):
        #xác định tốc độ theo 2 phương
        speedX = self.speed * math.cos(self.angle*RAD)
        speedY = self.speed * -math.sin(self.angle*RAD)
        #Xác định lại vị trí viên đạn
        self.x += speedX
        self.y += speedY
        self.y += A_FALL
        #Giảm tốc độ đạn
        if self.size > 0:
            self.size -= SPEED_CHANGE_SIZE
        else:
            self.size = 0
        #Giảm kích thước đạn
        if self.speed > 0:
            self.speed -= CHANGE_SPEED
        else:
            self.speed = 0

    def draw(self): #Vẽ 1 viên đạn
        if self.size > 0:
            pygame.draw.circle(DISPLAYSURF, self.color, (int(self.x), int(self.y), int(self.size)))
