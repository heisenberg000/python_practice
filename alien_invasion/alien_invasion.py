# -*- encoding: utf-8 -*-
'''
@File    :   alien_invasion.py
@Time    :   2021/10/15 23:17:44
@Author  :   James 
@Version :   1.0
@Desc    :   射击小游戏学习
'''

import sys,pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
  '''管理游戏资源和行为的类'''
  def __init__(self):
    '''初始化游戏并创建游戏资源'''
    pygame.init()
    self.settings = Settings()
    # 设置屏幕大小
    # self.screen = pygame.display.set_mode((self.settings.width,self.settings.height))
    # 设置全屏
    self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
    self.settings.screen_width = self.screen.get_rect().width
    self.settings.screen_height = self.screen.get_rect().height
    pygame.display.set_caption('Alien Invasion')
    # 初始化飞船对象
    self.ship = Ship(self)
    self.bullets = pygame.sprite.Group()
    self.aliens = pygame.sprite.Group()

    self._create_fleet()

  def _check_events(self):
    '''响应键盘和鼠标事件'''
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
      elif event.type == pygame.KEYDOWN:
        self._check_keydown_events(event)
      elif event.type == pygame.KEYUP:
        self._check_keyup_events(event)

  def _check_keydown_events(self,event):
    '''响应按键'''
    if event.key == pygame.K_RIGHT:
      self.ship.moving_right = True
    elif event.key == pygame.K_LEFT:
      self.ship.moving_left = True
    elif event.key == pygame.K_ESCAPE:
      sys.exit()
    elif event.key == pygame.K_SPACE:
      self._fire_bullet()

  def _check_keyup_events(self,event):
    '''响应松开'''
    if event.key == pygame.K_RIGHT:
      self.ship.moving_right = False
    elif event.key == pygame.K_LEFT:
      self.ship.moving_left = False

  def _fire_bullet(self):
    '''创建一颗子弹，并将其加入到编组bullets中'''
    if len(self.bullets) < self.settings.bullet_allowed:
      new_bullet = Bullet(self)
      self.bullets.add(new_bullet)
  
  def _create_fleet(self):
    '''创建外星人群'''
    alien = Alien(self)
    self.aliens.add(alien)

  def _update_screen(self):
    '''更新屏幕上的图像，并切换到新屏幕'''
    self.screen.fill(self.settings.bg_color)
    self.ship.blitme()
    for bullet in self.bullets.sprites():
      bullet.draw_bullet()
    self.aliens.draw(self.screen)
    pygame.display.flip()
  
  def _update_bullet(self):
    '''更新子弹位置并删除消失的子弹'''
    # 更新子弹位置
    self.bullets.update()
    # 删除消失的子弹
    for bullet in self.bullets.copy():
      if bullet.rect.bottom <= 0:
        self.bullets.remove(bullet)

  def run_game(self):
    '''开始游戏的主循环'''
    while True:
      self._check_events()
      self.ship.update()
      self._update_bullet()
      self._update_screen()
     
if __name__ == '__main__':
  # 创建游戏实例并运行
  ai = AlienInvasion()
  ai.run_game()
    
    