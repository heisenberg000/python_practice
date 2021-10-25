# -*- encoding: utf-8 -*-
'''
@File    :   settings.py
@Time    :   2021/10/15 23:17:28
@Author  :   James 
@Version :   1.0
@Desc    :   配置类
'''

class Settings:
  def __init__(self):
    '''初始化游戏的设置'''
    # 屏幕设置
    self.width = 1000
    self.height = 600
    self.bg_color = (230,230,230)
    # 飞船设置
    self.ship_speed = 1.5
    # 子弹设置
    self.bullet_speed = 1.0
    self.bullet_width = 3
    self.bullet_height = 15
    self.bullet_color = (60,60,60)
    # 限制最大子弹数
    self.bullet_allowed = 3