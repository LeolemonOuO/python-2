# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:53:37 2020

@author: SCE
"""


from mcpi.minecraft import Minecraft

mc = Minecraft.create()

x,y,z = mc.player.getTilePos()
mc.setBlock(x,y,z,11,3)
mc.setBlock(x,y+1,z,11,3)
mc.setBlock(x,y+2,z,11,3)
mc.setBlock(x,y+3,z,11,3)
mc.setBlock(x,y+4,z,11,3)
mc.setBlock(x,y+5,z,11,3)
mc.setBlock(x,y+6,z,11,3)
mc.setBlock(x,y+7,z,11,3)
mc.setBlock(x,y+8,z,11,3)
mc.setBlock(x,y+9,z,11,3)
mc.setBlock(x,y+10,z,11,3)
mc.setBlock(x,y+11,z,11,3)
mc.setBlock(x,y+12,z,11,3)
mc.setBlock(x,y+13,z,11,3)
mc.setBlock(x,y+14,z,11,3)
mc.setBlock(x,y+15,z,11,3)