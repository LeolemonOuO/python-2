# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:53:37 2020

@author: SCE
"""


from mcpi.minecraft import Minecraft

mc = Minecraft.create()

print(mc.player.getTilePos())