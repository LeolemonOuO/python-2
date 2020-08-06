# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:53:37 2020

@author: SCE
"""
import time
from mcpi.minecraft import Minecraft

mc = Minecraft.create()

while True:
    x,y,z = mc.player.getTilePos()
    mc.setBlock(x,y,z,79 )
    time.sleep(0.1)