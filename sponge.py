# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:53:37 2020

@author: SCE
"""
from mcpi.minecraft import Minecraft

mc = Minecraft.create()
x,y,z = mc.player.getTilePos()

block = int(input("what is the ID of the block you want to put?"))

mc.setBlock(x,y,z,block)
   
   
   