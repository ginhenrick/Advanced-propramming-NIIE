class BulletFlyUp(): #Viên đạn bay lên trước khi nổ
    def __int__(self, speed, x):
        self.speed = speed
        self.x = x
        self.y = WINDOWHEIGHT
        self.dots = [] #Một list các chấm theo sau
        self.size = SIZE/2
        self.color = (255,255,100)

    def update(self):
        self.dots.append(Dot(self.x, self.y, self.size, self.color)) #Mỗi lần đạn đi qua sẽ có một chấm thêm vào
        #Xác định lại vị trí viên đạn
        self.y -= self.speed
        self.speed -= A_FALL*0.1
        #update từng chấm
        for i in range(len(self.dots)):
            self.dots[i].update()
        #Xóa những chấm có kích thước <= 0
        i = 0
        while i < len(self.dots):
            if self.dots[i].size <= 0:
                self.dots.pop(i)
            else:
                i += 1

    def draw(self):
        pygame.draw.circle(DISPLAYSURF, self.color, (int(self.x), int(self.y), int(self.size))) #Vẽ viên đạn
        #Vẽ từng chấm
        for i in range(len(self.dots)):
            self.dots[i].draw()