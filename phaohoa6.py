def main():
    global FPSLOCK, DISPLAYSURF
    pygame.init()
    FPSLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    fireWorks = []
    time = TIME_CREAT_FW
    bulletFlyUps = []

    while True:
        DISPLAYSURF.fill((0,0,0)) #Xóa nền
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
        if time == TIME_CREAT_FW: #Tạo (những) viên đạn bay lên sau khoảng thời gian xác định
            for i in range(Random.num_fireworks()):
                bulletFlyUps.append(BulletFlyUp(Random.randomBulletFlyUp_speed(), Random.randomBulletFlyUp_x()))

        for i in range(len(bulletFlyUps)):
            bulletFlyUps[i].draw()
            bulletFlyUps[i].update()

        for i in range(len(fireWorks)):
            fireWorks[i].draw()
            fireWorks[i].update()

        i = 0
        while i < len(bulletFlyUps):
            if bulletFlyUps[i].speed <= 0: # viên đạn bay lên đạt độ cao tối đa
                fireWorks.append(FireWork(bulletFlyUps[i].x, bulletFlyUps[i].y)) # Tạo quả pháo ngay vị trí viên đạn
                bulletFlyUps.pop(i) #Xóa viên đạn đó
            else:
                i += 1
        #Xóa quả pháo hoa khi kích thước những viên đạn <= 0
        i = 0
        while i < len(fireWorks):
            if fireWorks[i].bullets[0].size <= 0:
                fireWorks.pop(i)
            else:
                i += 1

        #Đếm khoảng thời gian bắn
        if time <= TIME_CREAT_FW:
            time += 1
        else:
            time = 0
        pygame.display.update()
        FPSLOCK.tick(FPS)

if __name__ == '__main__':
    main()