# -*- encoding: utf-8 -*-
'''
@File    :   alien.py
@Time    :   2021/10/25 23:48:17
@Author  :   James 
@Version :   1.0
@Desc    :   外星人类
'''

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''表示单个外星人'''
    def __init__(self, ai_game):
        '''初始化外星人并设置其初始位置'''
        super().__init__()
        self.screen = ai_game.screen

        # 加载外星人图像并设置其rect属性
        self.image = pygame.image.load(r'G:\GitWorkSpace\python_practice\alien_invasion\images\alien.bmp')
        self.rect = self.image.get_rect()

        # 每个外星人最初在左上角附近出现
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的精准水平位置
        self.x = float(self.rect.x)
