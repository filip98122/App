from General_info import *
class Loader:
    def load(s):
        loaded={}
        loaded[0]=pygame.image.load("textures/player.png")
        loaded[1]=pygame.image.load("textures/dirt.png")
        loaded[2]=pygame.image.load("textures/boulder.png")
        loaded[3]=pygame.image.load("textures/wall.png")
        loaded[4]=pygame.image.load("textures/diamond.png")
        loaded[0]=pygame.transform.scale(loaded[0],(tilewh,tilewh))
        loaded[1]=pygame.transform.scale(loaded[1],(tilewh,tilewh))
        loaded[2]=pygame.transform.scale(loaded[2],(tilewh,tilewh))
        loaded[3]=pygame.transform.scale(loaded[3],(tilewh,tilewh))
        loaded[4]=pygame.transform.scale(loaded[4],(tilewh,tilewh))
        loaded[6]=pygame.transform.scale(pygame.image.load("textures/backgroundmenu.png"),(WIDTH,HEIGHT))
        loaded[5]=pygame.transform.scale(pygame.image.load("textures/door.png"),(tilewh,tilewh))
        return loaded
loader=Loader()
loaded=loader.load()