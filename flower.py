# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:53:37 2020

@author: SCE
"""
import time
import random
from mcpi.minecraft import Minecraft

mc = Minecraft.create()
N=0
while N!= 50:
    x,y,z = mc.player.getTilePos()
    F=random.randrange(8)
    mc.setBlock(x,y,z,38,F)
    N+=1
    time.sleep(0.1)