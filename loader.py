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
        loaded[7]=pygame.transform.scale(pygame.image.load("textures/brick.png"),(tilewh,tilewh))
        loaded[8]=pygame.transform.scale(pygame.image.load("textures/dooro.png"),(tilewh,tilewh))
        loaded["font"]=pygame.sysfont.SysFont("S",90)
        loaded[9]=pygame.transform.scale(loaded["font"].render(f"You Failed",False,(255,255,255)),(10*(tilewh/3),tilewh))
        loaded[10]=pygame.transform.scale(pygame.image.load("textures/death.png"),(WIDTH,HEIGHT))
        loaded[11]=pygame.transform.scale(pygame.image.load("textures/play.png"),(tilewh*7,tilewh*3))
        loaded[12]=pygame.transform.scale(pygame.image.load("textures/continue.png"),(tilewh*7,tilewh*3))
        loaded[13]=pygame.transform.scale(pygame.image.load("textures/options.png"),(tilewh*7,tilewh*3))

        return loaded
loader=Loader()
loaded=loader.load()