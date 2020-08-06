from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z=mc.player.getTilePos()

number = 20

for i in range(8):
    for j in range(number):
        mc.spawnEntity(x,y,z,60)
    mc.postToChat("you spawn"+str(number)+"worm")

number *= 2    