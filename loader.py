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
        loaded[14]=pygame.transform.scale(pygame.image.load("textures/bar.png"),(tilewh*14,tilewh*1.5))
        loaded[15]=pygame.transform.scale(pygame.image.load("textures/dot.png"),(loaded[14].get_height()-(loaded[14].get_height()/4+loaded[14].get_height()/2.545454545454545),loaded[14].get_height()-(loaded[14].get_height()/4+loaded[14].get_height()/2.545454545454545)))
        loaded[16]=pygame.transform.scale(pygame.image.load("textures/minimenu.png"),(WIDTH,HEIGHT))
        
        loaded["enemy0"]=pygame.transform.scale(pygame.image.load("textures/enemy0.png"),(tilewh,tilewh))
        loaded["enemy1"]=pygame.transform.scale(pygame.image.load("textures/enemy1.png"),(tilewh,tilewh))
        loaded["enemy2"]=pygame.transform.scale(pygame.image.load("textures/enemy2.png"),(tilewh,tilewh))
        loaded["enemy3"]=pygame.transform.scale(pygame.image.load("textures/enemy3.png"),(tilewh,tilewh))
        
        loaded["ghost0"]=pygame.transform.scale(pygame.image.load("textures/ghost0.png"),(tilewh,tilewh))
        loaded["ghost1"]=pygame.transform.scale(pygame.image.load("textures/ghost1.png"),(tilewh,tilewh))
        loaded["ghost2"]=pygame.transform.scale(pygame.image.load("textures/ghost2.png"),(tilewh,tilewh))
        loaded["ghost3"]=pygame.transform.scale(pygame.image.load("textures/ghost3.png"),(tilewh,tilewh))

        loaded["saveslot1"]=pygame.transform.scale(pygame.image.load("textures/saveslot1.png"),(tilewh*7,tilewh*3))
        loaded["saveslot2"]=pygame.transform.scale(pygame.image.load("textures/saveslot2.png"),(tilewh*7,tilewh*3))
        loaded["saveslot3"]=pygame.transform.scale(pygame.image.load("textures/saveslot3.png"),(tilewh*7,tilewh*3))

        loaded["save1"]=pygame.transform.scale(pygame.image.load("textures/save1.png"),(tilewh*7,tilewh*3))
        loaded["save2"]=pygame.transform.scale(pygame.image.load("textures/save2.png"),(tilewh*7,tilewh*3))
        loaded["save3"]=pygame.transform.scale(pygame.image.load("textures/save3.png"),(tilewh*7,tilewh*3))

        loaded["delete"]=pygame.transform.scale(pygame.image.load("textures/delete.png"),(tilewh*7,tilewh*3))
        loaded["music"]=pygame.mixer.Sound("textures/Game music.mp3")
        loaded["map"]=pygame.transform.scale(pygame.image.load("textures/map.png"),(WIDTH,HEIGHT))
        return loaded
loader=Loader()
loaded=loader.load()