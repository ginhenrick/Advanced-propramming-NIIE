import random


class Random():
    def __int__(self):
        pass

    def color(): #Tạo màu ngẫu nhiên (màu sáng)

        corlor1 = random.randint(0, 255)
        corlor2 = random.randint(0, 255)
        if corlor1 + corlor2 >= 255:
            corlor3 = random.randint(0, 255)
        else:
            corlor3 = random.randint(255 - corlor1 - corlor2, 255)
        colorList = [corlor1, corlor2, corlor3]
        random.shuffle(colorList)
        return colorList

    def num_fireworks(): #Số pháo mỗi lần bắn
        return random.randint(NUM_FIREWORKS_MIN, NUM_FIREWORKS_MAX)
    def randomBulletFlyUp_speed(): #Tốc độ viên đạn bay lên
        speed = random.uniform(SPEED_FLY_UP_MIN, SPEED_FLY_UP_MAX)
        return speed
    def randomBulletFlyUp_x(): #Vị trí viên đạn bay lên
        x = random.randint(iny(WINDOWWIDTH*0.2), int(WINDOWHEIGHT*0.8))
        return x