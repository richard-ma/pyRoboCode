#! /usr/bin/python
#-*- coding: utf-8 -*-

import os
import math
from pygame.math import Vector2
from Objects.movingObj import MovingObj


class Bullet(MovingObj):
    def __init__(self, power, bot):
        super().__init__()
        self.setPower(power)
        self.setBsize(power)
        self.robot = bot

    def setPower(self, power):
        power = max(0.5, min(power, 10)) # 0.5 <= power <= 10
        self.power = power

    def setBsize(self, bsize):
        bsize = max(4, min(bsize, 10)) # 4 <= bsize <= 10
        self.bsize = bsize
        
    # def setColour(self, color):
    #     mask = self.pixmap.createMaskFromColor(self.maskColor,  1)
    #     p = QPainter(self.pixmap)
    #     p.setPen(color)
    #     p.drawPixmap(self.pixmap.rect(), mask, mask.rect())
    #     p.end()
    #     self.setPixmap(self.pixmap)
    #     self.maskColor = color
        
    # def advance(self):
    #     if self.isfired:
    #         pos = self.pos
    #         x, y = pos.x, pos.y
    #         dx = - math.sin(math.radians(self.angle))*10.0
    #         dy = math.cos(math.radians(self.angle))*10.0
    #         self.setPos(x+dx, y+dy)
    #         if x < 0 or y < 0 or x > self.scene.width or y > self.scene.height:
    #             self.robot.onBulletMiss(id(self))
    #             self.scene.removeItem(self)
    #             self.robot.removeMyProtectedItem(self)

        
            
            
            
            
            
            
            
