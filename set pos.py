# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:53:37 2020

@author: SCE
"""


from mcpi.minecraft import Minecraft

mc = Minecraft.create()

x=300
y=10000
z=100

mc.player.setTilePos(x,y,z)