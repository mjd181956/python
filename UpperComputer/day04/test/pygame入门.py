import pygame
import time
# 初始化pygame
pygame.init()

# 创建窗体
screen = pygame.display.set_mode((640, 480))

# 设置窗口标题
pygame.display.set_caption("贪吃蛇")

#窗口图标
icon_image = pygame.image.load("res/icon.png")
pygame.display.set_icon(icon_image)

# 设置颜色
COLOR = (180, 78, 0)
# 准备图片
plane_image = pygame.image.load("res/hero2.png")

#旋转
plane_image = pygame.transform.rotate(plane_image, 90)

# 时钟
clock = pygame.time.Clock()
# 运行无限循环
while True:
    start = time.time()
    # 处理事件，获取用户的输入事件-----------------------------
    event_list = pygame.event.get()
    # 解析处理所有事件
    for event in event_list:
        # 事件类型
        if event.type == pygame.QUIT:
            # 退出游戏
            pygame.display.quit()
            # 退出程序
            exit(0)
        elif event.type == pygame.KEYDOWN:
            print("按键被按下", event.key)
            # 上、下、左、右
            if event.key == pygame.K_UP:
                print("向上")
            if event.key == pygame.K_DOWN:
                print("向下")
            if event.key == pygame.K_LEFT:
                print("向左")
            if event.key == pygame.K_RIGHT:
                print("向右")

    # 绘制界面---------------------------------------------------
    screen.fill(COLOR)

    # 绘制图片
    screen.blit(plane_image, (30, 0))

    # 刷新界面，内存对象中的内容才能真正的界面
    pygame.display.flip()

    # time.sleep(0.1)
    # end = time.time()
    # 通过主动休眠减少刷新速度
    # duration = end - start  # 当前帧的耗时
    # if duration != 0:
    #     print(f"duration: {duration} fps:{1/duration}")

    clock.tick(10)      # 10帧每秒，每次运行，内部会确保跑足

    print("fps: ", clock.get_fps())
