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
        