import random


class FireWork(): #Quả pháo hoa
    def __int__(self, x, y):
        self.x = x
        self.y = y
        self.dots = [] #List các chấm theo sau mỗi viên đạn

    def creatBullets(): #tạo list các viên đạn
        bullets = []
        color = Random.color()
        for i in range(NUM_BULLET):
            angle = (360/NUM_BULLET)*i
            speed = random.uniform(SPEED_MIN, SPEED_MAX)
            bullets.append(Bullet(self.x, self.y, speed, angle, color))
        return bullets
    self.bullets = creatBullets();

    def update(self):
        for i in range(len(self.bullets)): #update từng viên đạn
            self.bullets[i].update()
            self.dots.append(Dot(self.bullets[i].x, self.bullets[i].y, self.bullets[i].size, self.bullets[i].color))
            for i in range(len(self.dots)): #update từng chấm
                self.dots[i].update()
                #Xóa những chấm có kích thước <= 0
            i = 0
            while i < len(self.dots):
                if self.dots[i].size <= 0:
                    self.dots.pop(i)
                else:
                    i += 1

    def draw(self):
        for i in range(len(self.bullets)): #vẽ từng viên đạn
            self.bullets[i].draw()
        for i in range(len(self.dots)): #Vẽ từng chấm
            self.dots[i].draw()