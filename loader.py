from General_info import *
class Loader:
    def load(s):
        loaded={}
        loaded[0]=pygame.image.load("player.png")
        loaded[1]=pygame.image.load("dirt.png")
        loaded[2]=pygame.image.load("boulder.png")
        loaded[3]=pygame.image.load("wall.png")
        loaded[4]=pygame.image.load("diamond.png")
        loaded[0]=pygame.transform.scale(loaded[0],(HEIGHT/12,HEIGHT/9))
        loaded[1]=pygame.transform.scale(loaded[1],(HEIGHT/9,HEIGHT/9))
        loaded[2]=pygame.transform.scale(loaded[2],(HEIGHT/9,HEIGHT/9))
        loaded[3]=pygame.transform.scale(loaded[3],(HEIGHT/9,HEIGHT/9))
        loaded[4]=pygame.transform.scale(loaded[4],(HEIGHT/9,HEIGHT/9))
        return loaded
loader=Loader()
loaded=loader.load()