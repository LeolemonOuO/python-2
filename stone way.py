# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:53:37 2020

@author: SCE
"""
import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()

for i in range(123):
    mc.setBlock(x+i,y-1,z-i+1,1)
    mc.setBlock(x+i,y-1,z-i+2,1)
    mc.setBlock(x+i,y-1,z-i,1)
    time.sleep(1)
  