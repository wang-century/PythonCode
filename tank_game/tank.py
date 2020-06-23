"""
    坦克大战
        主逻辑类
        坦克类（我方坦克，敌方坦克）
        子弹类
        爆炸类
        音效类
"""
import pygame
from pygame import display as _display
from pygame import event as _event
import random


class MainGame():
    """
        主逻辑类
    """
    SCREEN_WIDTH = 900
    SCREEN_HEIGHT = 550
    window = None  # 窗口对象
    PI_TANK = None  # 坦克
    enemy_tank_list = []    # 敌方坦克列表
    enemy_tank_count = 5    # 敌方坦克数量

    def start_game(self):
        """开始游戏"""
        # 加载游戏窗口
        _display.init()
        MainGame.window = _display.set_mode((MainGame.SCREEN_WIDTH, MainGame.SCREEN_HEIGHT))
        # 设置游戏标题
        _display.set_caption('坦克大战v1.0')
        # 创建坦克
        MainGame.PI_TANK = Tank(430, 450)
        # 创建敌方坦克
        self.create_enemy_tank()

        while True:
            MainGame.window.fill((0, 0, 0))  # 渲染背景，填充黑色
            self.handle_event()  # 调用事件处理
            MainGame.window.blit(self.draw_text('敌方剩余坦克{}辆'.format(1)), (5, 5))  # 将剩余坦克数量显示在主窗口
            MainGame.PI_TANK.display_tank()  # 加载我方坦克
            # 将敌方坦克加入窗口
            for enemy_tank in MainGame.enemy_tank_list:
                enemy_tank.display_tank()
            if not MainGame.PI_TANK.stop:  # 控制坦克是否移动
                MainGame.PI_TANK.move_tank(MainGame.PI_TANK)
            _display.update()  # 刷新屏幕

    def create_enemy_tank(self):
        """创建敌方坦克"""
        for i in range(MainGame.enemy_tank_count):
            random_left = random.randint(1, 8)  # 横坐标范围为100-800
            random_speed = random.randint(1, 3)  # 敌方坦克速度1-3
            enemy_tank = EnemyTank(random_left * 100, speed=random_speed)
            MainGame.enemy_tank_list.append(enemy_tank)


    def handle_event(self):
        """事件处理"""
        event_list = _event.get()  # 获取所有事件
        for event in event_list:
            if event.type == pygame.QUIT:  # 退出按钮
                print('退出游戏')
                self.close_game()
            if event.type == pygame.KEYDOWN:  # 事件类型为按键按下
                # 判断按键并作出处理
                if event.key == pygame.K_LEFT:  # 左按钮
                    print('向左移动')
                    MainGame.PI_TANK.direction = 'left'  # 坦克朝向左
                    MainGame.PI_TANK.stop = False  # 坦克开始移动
                elif event.key == pygame.K_RIGHT:  # 右按钮
                    print('向右移动')
                    MainGame.PI_TANK.direction = 'right'  # 坦克朝向右
                    MainGame.PI_TANK.stop = False
                elif event.key == pygame.K_UP:  # 上按钮
                    print('向上移动')
                    MainGame.PI_TANK.direction = 'up'  # 坦克朝向上
                    MainGame.PI_TANK.stop = False

                elif event.key == pygame.K_DOWN:  # 下按钮
                    print('向下移动')
                    MainGame.PI_TANK.direction = 'down'  # 坦克朝向下
                    MainGame.PI_TANK.stop = False
                elif event.key == pygame.K_SPACE:  # 空格按钮
                    print('开炮')
            if event.type == pygame.KEYUP:  # 事件类型为按键抬起
                MainGame.PI_TANK.stop = True  # 坦克移动停止

    def draw_text(self, text):
        """给定字符串，返回包含字符串内容的surface"""
        pygame.font.init()  # 字体模块初始化
        # fonts_list = pygame.font.get_fonts()  # 返回系统可用字体（列表）
        # print(fonts_list)
        font = pygame.font.SysFont('kaiti', 16)  # 创建字体对象
        text_surface = font.render(text, True, pygame.Color(255, 0, 0))  # 使用字体渲染内容
        # 返回包含内容的surface
        return text_surface

    def close_game(self):
        """关闭游戏"""
        exit()


class Tank(pygame.sprite.Sprite):
    """
        坦克类（继承精灵类）
    """

    def __init__(self, point_x, point_y):
        """初始化坦克"""
        pygame.sprite.Sprite.__init__(self)
        # 坦克的四个朝向图片
        self.images = {'up': pygame.image.load('images/p1tankU.gif'), 'down': pygame.image.load('images/p1tankD.gif'),
                       'left': pygame.image.load('images/p1tankL.gif'),
                       'right': pygame.image.load('images/p1tankR.gif')}
        self.direction = 'up'  # 坦克的朝向
        self.image = self.images[self.direction]  # 坦克的图片
        self.rect = self.image.get_rect()  # 坦克的形状
        self.rect.left = point_x
        self.rect.top = point_y
        self.speed = 1  # 坦克的速度
        self.stop = True  # 控制坦克是否移动

    def display_tank(self):
        """显示坦克"""
        self.image = self.images[self.direction]  # 设置坦克图片
        MainGame.window.blit(self.image, self.rect)

    def move_tank(self, tank):
        """移动坦克"""
        if tank.direction == 'up':
            if tank.rect.top > 0:  # 设置边界
                tank.rect.top -= tank.speed
        elif tank.direction == 'down':
            if tank.rect.top <= MainGame.SCREEN_HEIGHT - tank.rect.height:  # 设置边界
                tank.rect.top += tank.speed
        elif tank.direction == 'left':
            if tank.rect.left > 0:  # 设置边界
                tank.rect.left -= tank.speed
        elif tank.direction == 'right':
            if tank.rect.left <= MainGame.SCREEN_WIDTH - tank.rect.width:  # 设置边界
                tank.rect.left += tank.speed


class MyTank():
    """
        我方坦克类
    """
    pass


class EnemyTank(pygame.sprite.Sprite):
    """
        敌方坦克类
    """

    def __init__(self, point_x,speed,point_y=100):
        """生成敌方坦克"""
        pygame.sprite.Sprite.__init__(self)
        # 坦克的四个朝向图片
        self.images = {'up': pygame.image.load('images/enemy2U.gif'), 'down': pygame.image.load('images/enemy2D.gif'),
                       'left': pygame.image.load('images/enemy2L.gif'),
                       'right': pygame.image.load('images/enemy2R.gif')}
        self.direction = self.random_direction()  # 坦克的朝向随机
        self.image = self.images[self.direction]  # 坦克的图片
        self.rect = self.image.get_rect()  # 坦克的形状
        self.rect.left = point_x
        self.rect.top = point_y
        self.speed = speed  # 坦克的速度
        self.stop = False  # 控制坦克是否移动

    def random_direction(self):
        """生成随即方向"""
        directions = ['up', 'down', 'left', 'right']
        direction = random.choice(directions)
        return direction

    def display_tank(self):
        """显示坦克"""
        self.image = self.images[self.direction]  # 设置坦克图片
        MainGame.window.blit(self.image, self.rect)

class Bullet():
    """
        子弹类
    """
    pass


class Explode():
    """
        爆炸类
    """
    pass


class Music():
    """
        音效类
    """
    pass


if __name__ == '__main__':
    game = MainGame()
    game.start_game()
    # game.draw_text('你好世界')
