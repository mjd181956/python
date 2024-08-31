"""
1、准备pygame开发环境：窗口尺寸，标题，图标
    a、准备北京图片
    b、准备蛇头

2、while True:
    a、处理用户输入事件
    b、处理游戏逻辑
    c、渲染界面
    d、控制渲染速度fps
"""


# 1、下载并导入pygame
import pygame
import random

SCREEN_WIDTH = 640
SCRREN_HEIGHT = 480
BLOCK_SIZE = 20
COLOR_GARY = (180, 180, 180)
COLOR_WHITE = (255, 255, 255)
COLOR_BLUE = (0, 0, 255)
COLOR_RED = (255, 0, 0)

# 移动方向字典
DIRECTION_DICT = {
    pygame.K_UP: (0, -BLOCK_SIZE),  # 上
    pygame.K_RIGHT: (BLOCK_SIZE, 0),  # 右
    pygame.K_DOWN: (0, BLOCK_SIZE),  # 下
    pygame.K_LEFT: (-BLOCK_SIZE, 0),  # 左
}
# 蛇头方向
HEAD_DICT = {
    pygame.K_DOWN: 0,
    pygame.K_RIGHT: 90,
    pygame.K_UP: 180,
    pygame.K_LEFT: 270,
}
# 创建一个类


class Snake:
    def __init__(self):
        self.__direction = pygame.K_RIGHT  # 0上， 1右， 2下，3左
        self.snake_body = [
            pygame.Rect(5 * BLOCK_SIZE, 3 * BLOCK_SIZE,
                        BLOCK_SIZE, BLOCK_SIZE),
            pygame.Rect(4 * BLOCK_SIZE, 3 * BLOCK_SIZE,
                        BLOCK_SIZE, BLOCK_SIZE),
            pygame.Rect(3 * BLOCK_SIZE, 3 * BLOCK_SIZE,
                        BLOCK_SIZE, BLOCK_SIZE),
        ]
        head_image = pygame.image.load("res/head-red.png")
        # 对图片大小缩放
        self.snake_head_image = pygame.transform.scale(
            head_image, (BLOCK_SIZE, BLOCK_SIZE))

        # 得分
        self.score = 0

    def move(self):
        """
        移动之前要根据输入的方向，修改移动的方向
        每一帧绘制之前都会调用move移动
        让蛇向前移动一格

        """

        # 把蛇头复制一份
        new_node = self.snake_body[0].copy()
        # 往前进的方向移动一格
        # 这里是将字典转换为元组，这样就右连个值，字典的两个值元组
        new_move = DIRECTION_DICT[self.__direction]
        new_node.x += new_move[0]
        new_node.y += new_move[1]

        # 如果超出范围，顺义
        if new_node.x >= SCREEN_WIDTH:
            new_node.x -= SCREEN_WIDTH
            # new_node.x = 0
        elif new_node.x < 0:
            new_node.x += SCREEN_WIDTH
            # new_node.x = SCREEN_WIDTH - BLOCK_SIZE
        if new_node.y < 0:
            new_node.y += SCRREN_HEIGHT
        elif new_node.y >= SCRREN_HEIGHT:
            new_node.y -= SCRREN_HEIGHT

        # 把新的蛇头放到最前面
        self.snake_body.insert(0, new_node)
        # 把蛇尾移除
        self.snake_body.pop()  # 索引不传参默认最有一个

    def draw(self, screen):
        # 绘制蛇身
        for node in self.snake_body[1:]:
            pygame.draw.rect(screen, COLOR_WHITE, node, border_radius=3)

        # 绘制蛇头
        head: pygame.Rect = self.snake_body[0]

        # 对原始头图进行选择
        # Down -> 0
        # Right -> 90
        # Up -> 180
        # Left -> 270
        head_image = pygame.transform.rotate(self.snake_head_image, HEAD_DICT[self.__direction])
        screen.blit(head_image, head)

    def grow(self):
        # 蛇尾复制一份
        new_node = self.snake_body[-1].copy()

        # 添加新的节点到尾部
        self.snake_body.append(new_node)

        # 得1分
        self.score += 1

    def is_direction_enable(self, input_key):
        """更新运动方向
            禁止水平或者垂直方向直接变换
        :param new_dir: 新的方向
        """
        if input_key not in (pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT):
            return False
        # 禁止水平或垂直方向置直接变换
        # 不能原地掉头（不能左右）
        LR = (pygame.K_LEFT, pygame.K_RIGHT)
        if self.__direction in LR and input_key in LR:
            return False
        # 不能原地掉头（不能上下）
        UD = (pygame.K_UP, pygame.K_DOWN)
        if self.__direction in UD and input_key in UD:
            return False
        return True

    def update_direction(self, input_key):

        # 符合条件，更新方向
        self.__direction = input_key

class Food:

    def __init__(self, node) -> None:
        self.node = node

    def draw(self, screen):
        pygame.draw.rect(screen, COLOR_BLUE, self.node, border_radius=3)

    @staticmethod #声明为静态函数
    def gen_food_position(snake: Snake) -> tuple:
        """根据屏幕宽高、蛇身信息生成新的食物的x, y坐标

        :param snake: 蛇对象
        :return: 坐标的x, y元组 (32,24)
        """
        while True:
            x = random.randint(0, SCREEN_WIDTH // BLOCK_SIZE - 1)
            y = random.randint(0, SCRREN_HEIGHT // BLOCK_SIZE - 1)

            # 如果在蛇身上，重新生成
            new_food_node = pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE,
                                        BLOCK_SIZE, BLOCK_SIZE)
            if new_food_node not in snake.snake_body:
                # 新的食物不在蛇身 & 蛇头
                return new_food_node


class Game:
    def __init__(self):

        # 1、初始化pygame
        pygame.init()

        # 2、设置窗体大小，获取Surface对象
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCRREN_HEIGHT))

        # 3、设置标题
        pygame.display.set_caption("贪吃蛇大作战 V1.0")

        # 4、设置图标
        icon = pygame.image.load("res/icon.png")
        pygame.display.set_icon(icon)

        # 7、加载背景图片 并 图片的拉伸缩放
        self.bg_image = pygame.image.load("res/bg.png")
        self.bg_image = pygame.transform.scale(
            self.bg_image, (SCREEN_WIDTH, SCRREN_HEIGHT))

    def start(self):
        # 8、创建一个蛇对象
        snake = Snake()
        # 9、创建一个食物对象
        food = Food(Food.gen_food_position(snake))
        is_game_over = False
        # 6、时钟
        clock = pygame.time.Clock()

        # 5、进入死循环，让窗口显示，并处理事件
        while True:
            new_dir = None
            # a、处理用户输入事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("点击了关闭")
                    self.quit_game()
                elif event.type == pygame.KEYDOWN:
                    if is_game_over:
                        if event.key == pygame.K_q:
                            self.quit_game()
                        elif event.key == pygame.K_KP_ENTER:
                            # 重启游戏
                            is_game_over = False
                            snake = Snake()
                            food = Food(Food.gen_food_position(snake))

                    # 上、下、左、右
                    # if event.key == pygame.K_UP:
                    #     print("向上")
                    #     print("向右")
                    #     print("向下")
                    #     print("向左")
                    #     snake.update_direction(pygame.K_UP)
                    # elif event.key == pygame.K_RIGHT:
                    #     print("按键被按下：", event.key)
                    #     snake.update_direction(pygame.K_RIGHT)
                    # elif event.key == pygame.K_DOWN:
                    #     print("按键被按下：", event.key)
                    #     snake.update_direction(pygame.K_DOWN)
                    # elif event.key == pygame.K_LEFT:
                    #     print("按键被按下：", event.key)
                    #     snake.update_direction(pygame.K_LEFT)
                    elif event.key == pygame.K_ESCAPE:
                        self.quit_game()
                    elif snake.is_direction_enable(event.key):
                        new_dir = event.key

            if new_dir is not None:
                snake.update_direction(new_dir)
            # b、处理游戏逻辑---------------------------
            if not is_game_over:
                #   a)、蛇移动
                snake.move()
                #   b)、遇到食物，吃掉食物，蛇身长一节
                snake_head = snake.snake_body[0]
                if snake_head == food.node:
                    # x, y = gen_food_position(snake)
                    food = Food(Food.gen_food_position(snake))
                    # 蛇身长一节
                    snake.grow()
                #   c)、碰到墙壁
                if snake_head.x < 0 or snake_head.x >= SCREEN_WIDTH  \
                        or snake_head.y < 0 or snake_head.y >= SCRREN_HEIGHT:
                    is_game_over = True

                #   d)、碰到自己
                if snake_head in snake.snake_body[1:]:
                    is_game_over = True

            # c、渲染界面
            #   a)、背景图
            self.screen.blit(self.bg_image, (0, 0))
            #   b)、绘制网格线
            # pygame.draw.line(screen, COLOR_GARY, (0, 0), (SCREEN_WIDTH, SCRREN_HEIGHT), 1)
            # 绘制所有的横线， h = 480// 20 = 12[0, 20, 40 .... 120)
            for y in range(0, SCRREN_HEIGHT, BLOCK_SIZE):
                start_pos = (0, y)
                end_pos = (SCREEN_WIDTH, y)
                pygame.draw.line(self.screen, COLOR_GARY,
                                 start_pos, end_pos, 1)
            # 绘制所有的竖线， v = 640 // 20 = 23[0, 20, 40 .... 480)
            for x in range(0, SCREEN_WIDTH, BLOCK_SIZE):
                start_pos = (x, 0)
                end_pos = (x, SCRREN_HEIGHT)
                pygame.draw.line(self.screen, COLOR_GARY,
                                 start_pos, end_pos, 1)

            #   c)、绘制蛇身
            snake.draw(self.screen)

            #   d)、绘制食物
            food.draw(self.screen)

            # 绘制得分和fps
            self.show_text(f"Score：{snake.score}", 20, 10, 10)

            fps = clock.get_fps()  # 获取真实的每秒帧率fps
            self.show_text("FPS:{:.2f}".format(fps), 20, SCREEN_WIDTH - 110, 10)

            # 根据游戏是否结束，渲染文字
            if is_game_over:
                self.show_text("游戏结束", 50, SCREEN_WIDTH // 3, SCRREN_HEIGHT // 4)
                self.show_text(f"得分：{snake.score}", 24, SCREEN_WIDTH // 3, SCRREN_HEIGHT // 4 + 70)
                self.show_text("按任意键重新开始", 24, SCREEN_WIDTH // 3, SCRREN_HEIGHT // 4 + 100)
                self.show_text("按Q退出游戏", 24, SCREEN_WIDTH // 3, SCRREN_HEIGHT // 4 + 130)



            # d、控制渲染速度fps
            # 设定fps----------------------------------------------------------
            clock.tick(12)

            # 刷新界面，内存对象中的内容才能真正的界面
            # pygame.display.flip()
            pygame.display.update()

    def quit_game(self):
        pygame.display.quit()
        exit(0)

    def show_text(self, text, font_size, x, y):
        font1 = pygame.font.SysFont("SimHei", font_size)
        text = font1.render(text, True, COLOR_RED)
        self.screen.blit(text, (x, y))


game = Game()
game.start()
