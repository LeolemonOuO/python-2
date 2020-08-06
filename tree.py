#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 14:34:07 2017

@author: sam0225
"""


from mcpi.minecraft import Minecraft

mc = Minecraft.create()

x,y,z=mc.player.getTilePos()

mc.setBlocks(x-3,y+2,z-2,x+1,y+4,z+2,20)
mc.setBlocks(x,y+4,z,x,y,z,30)
 
       


