from General_info import *
class Loader:
    def load(s):
        loaded={}
        loaded[0]=pygame.image.load("player.png")
        loaded[1]=pygame.image.load("dirt.png")
        loaded[2]=pygame.image.load("boulder.png")
        loaded[3]=pygame.image.load("wall.png")
        loaded[4]=pygame.image.load("diamond.png")
        return loaded
loader=Loader()
loaded=loader.load()