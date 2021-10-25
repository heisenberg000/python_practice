# -*- encoding: utf-8 -*-
'''
@File    :   ship.py
@Time    :   2021/10/15 23:17:12
@Author  :   James 
@Version :   1.0
@Desc    :   飞船类
'''
import pygame

class Ship:
  def __init__(self, ai_game):
    '''初始化飞船并设置其初始位置'''
    self.screen = ai_game.screen
    self.settings = ai_game.settings
    self.screen_rect = ai_game.screen.get_rect()
    
    # 加载飞船图像并获取起外接矩形
    self.image = pygame.image.load(r'G:\GitWorkSpace\python_practice\alien_invasion\images\ship.bmp')
    self.rect = self.image.get_rect()
    
    # 每艘新飞船，将其放置在屏幕底部的中央
    self.rect.midbottom = self.screen_rect.midbottom
    
    # 在飞船的属性x中存储小数值
    self.x = float(self.rect.x)

    # 移动标志
    self.moving_right = False
    self.moving_left = False
  
  def update(self):
    '''根据移动标志调整飞船的位置'''
    if self.moving_right and self.rect.right < self.screen_rect.right:
      self.x += self.settings.ship_speed
    if self.moving_left and self.rect.left > self.screen_rect.left:
      self.x -= self.settings.ship_speed
    # 根据x更新rect对象
    self.rect.x = self.x
    
  def blitme(self):
    '''在指定位置绘制飞船'''
    self.screen.blit(self.image,self.rect)