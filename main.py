from loader import *
from map import *
def ens(file_data):
    f=Fernet(keyE)
    encrypted_data1=json.dumps(file_data).encode('utf-8')
    encrypted_data = f.encrypt(encrypted_data1)
    with open("infojson.json", "wb") as file:
        file.write(encrypted_data)
def end():
    f=Fernet(keyE)
    with open("infojson.json", "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    decrypted_data1=json.loads(decrypted_data.decode('utf-8'))
    return decrypted_data1
def nextlevelsacusto(regen,listinfo):
    global l_boulders
    global l_explosions
    global l_gems
    global l_terrain
    global level
    global seconds
    global prozor
    global player
    global trans
    global offsetx
    global offsety
    global bar
    global diamonds
    global dooropen
    global elapsed_time
    global lives
    if regen:
        lives=3
    bar=Game_bar()
    l_terrain=listinfo["l_terrain"]
    level=listinfo["level"]
    seconds=listinfo["seconds"]
    trans=listinfo["trans"]
    diamonds=listinfo["diamonds"]
    dooropen=listinfo["dooropen"]
    elapsed_time=listinfo["elapsed_time"]
    lives=listinfo["lives"]
    prozor=1

    l_boulders=[]
    l_explosions=[]
    l_gems=[]
    global l_enemies,l_phantoms
    l_phantoms=[]
    l_enemies=[]
    
    l_boulders=[]

    for i in range(len(l_terrain)):
        for j in range(len(l_terrain[i])):
            if l_terrain[i][j]=="p":
                player=Player(j*(tilewh),i*(tilewh))
            if l_terrain[i][j]=="b":
                l_boulders.append(Boulder(j*(tilewh),i*(tilewh)))
            if l_terrain[i][j]=="g":
                l_gems.append(Diamond(j*(tilewh),i*(tilewh),False))
            if l_terrain[i][j]=="e":
                l_enemies.append(Enemy(j*(tilewh),i*(tilewh)))
            if l_terrain[i][j]=="f":
                l_phantoms.append(Ghost(j*tilewh,i*tilewh))
    
    

    
    offsety=((((HEIGHT/2)/tilewh)*tilewh)-player.y)
    offsetx=((((WIDTH/2)/tilewh)*tilewh)-player.x)
    player.x=((WIDTH/2)/tilewh)*tilewh
    player.y=((HEIGHT/2)/tilewh)*tilewh
camerax=0
cameray=0
def make_gameinfo():
    global l_boulders,l_explosions,l_gems,l_terrain,level,seconds,player,trans,offsetx,offsety,bar,diamonds,dooropen,elapsed_time,lives
    infolistallformaking={}
    infolistallformaking["l_terrain"]=l_terrain
    infolistallformaking["level"]=level
    infolistallformaking["seconds"]=seconds
    infolistallformaking["trans"]=trans
    infolistallformaking["offsetx"]=offsetx
    infolistallformaking["offsety"]=offsety
    infolistallformaking["diamonds"]=diamonds
    infolistallformaking["dooropen"]=dooropen
    infolistallformaking["elapsed_time"]=elapsed_time
    infolistallformaking["lives"]=lives
    return infolistallformaking
def init_gameinfo(gameforinfo):
    nextlevelsacusto(True,gameforinfo)
"""

    infoforgame={}
    infoforgame["l_terrain"]=l_terrain
    infoforgame["level"]=level
    infoforgame["seconds"]=seconds
    infoforgame["trans"]=trans
    infoforgame["offsetx"]=offsetx
    infoforgame["offsety"]=offsety
    infoforgame["diamonds"]=diamonds
    infoforgame["dooropen"]=dooropen
    infoforgame["elapsed_time"]=elapsed_time
    infoforgame["lives"]=lives




    l_boulders=[]
    l_explosions=[]
    l_gems=[]
    l_terrain=gameinfo["l_terrain"]
    level=gameinfo["level"]
    seconds=gameinfo["seconds"]
    trans=gameinfo["trans"]
    offsetx=gameinfo["offsetx"]
    offsety=gameinfo["offsety"]
    diamonds=gameinfo["diamonds"]
    dooropen=gameinfo["dooropen"]
    elapsed_time=gameinfo["elapsed_time"]
    lives=gameinfo["lives"]
"""
    
def collison(x1,y1,r1,x2,y2,r2):
    dx = x2 - x1
    dy = y2 - y1
    dist  = dx * dx + dy * dy
    dist = math.sqrt(dist)
    
    if dist >= r1 + r2:
        return False
    else:
        return True
def collision1(rect1 : pygame.Rect,rect2 : pygame.Rect):
    if rect1.colliderect(rect2):
        return True
    return False
def Boolflip(var):
    if var==False:
        var=True
    else:
        var=False
    return var
#char ="!#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"

def read():
    info=end()
    
    return info
info=read()
settings=info["settings"]
def save(info):
    ens(info)
save({'diamonds': 0, 'username': '', 'settings': {'Music': 0, 'Fast game': 2, 'Hardcore': False}, 'saves': {'saveslot1': {"save1":{},"save2":{},"save3":{}}, 'saveslot2': {"save1":{},"save2":{},"save3":{}}, 'saveslot3': {"save1":{},"save2":{},"save3":{}}}, 'quicksaves': {'1': {}, '2': {}, '3': {}},"newestsaves":[None,None,None]})
info = read()
def find_boulder(x,y):
    for i in range(len(l_boulders)):
        if l_boulders[i].x==x and l_boulders[i].y==y:
            return i


def find_gems(x,y):
    for i in range(len(l_gems)):
        if l_gems[i].x==x and l_gems[i].y==y:
            return i


def find_enemies(x,y):
    for i in range(len(l_enemies)):
        if l_enemies[i].x==x and l_enemies[i].y==y:
            return i
def find_ghosts(x,y):
    for i in range(len(l_phantoms)):
        if l_phantoms[i].x==x and l_phantoms[i].y==y:
            return i

def highlight(width,height,x,y,mousePos):
    if mousePos[0] > x and mousePos[0] < x + width and mousePos[1] > y and mousePos[1] < y + height:
        return True
    else:
        return False

def button_colision(width,height,x,y,mousePos,mouseState):
    """Collides the clicking of the would-be button given"""
    if mousePos[0] > x and mousePos[0] < x + width and mousePos[1] > y and mousePos[1] < y + height and mouseState[0] == True:
        return True
    else:
        return False

def checker(keys,index):
    pressed = 0
    for key in range(512):
        if keys[key]:
            pressed = key
            break
        
    if pressed!=0:
        return pressed
    else:
        return index


def list_button_class_collision(index,list):
    """Collides the clicking of the would-be button given in the list, has to be a class with a self.x, self.y,  self.width and a self.height"""
    if mousePos[0] > list[index].x and mousePos[0] < list[index].x + list[index].width and mousePos[1] > list[index].y and list[index].mousePos[1] < list[index].y + list[index].height and mouseState[0] == True:
        return True
    else:
        return False


def Vector_Normalization(x1, y1, x2, y2):
    # Calculate dx and dy with direction
    distancex = x2 - x1
    distancey = y2 - y1
    vector_lenght=math.sqrt(distancex*distancex+distancey*distancey)
    distancex=distancex/vector_lenght
    distancey=distancey/vector_lenght
    distancex*=HEIGHT/150 # For speed
    distancey*=HEIGHT/150 # For speed
    return distancex,distancey
def get_angle(dx,dy):
    angle_rad = math.atan2(dy, dx)
    angle_deg = math.degrees(angle_rad)
    return angle_deg


vremepre=time.time()
najvecivreme=0
subset=0

class Setting:
    def __init__(s,x,y,sub,img,truefalse,text,percent):
        s.x=x
        s.y=y
        s.txt=text
        s.sub=sub
        s.img=img
        s.percent=percent
        s.truefalse=truefalse
        s.t=loaded["font"].render(text,False,(255,255,255))
        s.text=pygame.transform.scale(s.t,(len(text)*(tilewh/3),s.img.get_height()-(s.img.get_height()/4.5)-(s.img.get_height()/8)))
        s.x-=s.img.get_width()
    def general(s):
        
        if s.sub==subset:
            da=0
            if s.truefalse==True:
                if button_colision(s.img.get_width()/2,s.img.get_height(),s.x,s.y,mousePos,mouseState):
                    newpercent=0
                    da=1
                elif button_colision(s.img.get_width(),s.img.get_height(),s.x,s.y,mousePos,mouseState):
                    newpercent=100
                    da=1
            for i in range(101):
                xdot=s.x+i*((s.img.get_width()-((s.img.get_width()/19.5)*2))/100)+(s.img.get_width()/19.5)
                ydot=s.y+(s.img.get_height()/2.545454545454545)
                widthdot=(s.img.get_width()-((s.img.get_width()/19.5)*2))/100
                heightdot=s.img.get_height()-(s.img.get_height()/4+s.img.get_height()/2.545454545454545)
                if i<s.percent or s.percent==100 and i!=100:
                    pygame.draw.rect(window,(255,0,0),pygame.Rect(xdot,ydot,widthdot,heightdot))
                    if i+1==s.percent:
                        window.blit(loaded[15],(xdot-widthdot/2,ydot))
                if s.percent==0 and i == 0:
                    window.blit(loaded[15],(xdot-widthdot/2,ydot))
                if button_colision((s.img.get_width()-((s.img.get_width()/19.5)*2)),(s.img.get_height()-(s.img.get_height()/4+s.img.get_height()/2.545454545454545)),s.x+i*((s.img.get_width()-((s.img.get_width()/19.5)*2))/100)+(s.img.get_width()/19.5),(s.y+(s.img.get_height()/2.545454545454545))+(s.img.get_height()-(s.img.get_height()/4+s.img.get_height()/2.545454545454545))/2,mousePos,mouseState) and s.truefalse==False:
                    newpercent=i
                    da=1
            if da==1:
                s.percent=newpercent
                if s.truefalse:
                    if s.txt=="Fast game":
                        if s.percent==0:
                            settings[s.txt]=1
                        else:
                            settings[s.txt]=2
                    elif s.txt=="Hardcore":
                        if s.percent==0:
                            settings[s.txt]=False
                        else:
                            settings[s.txt]=True
                    else:
                        settings[s.txt]=True
                else:
                    settings[s.txt]=s.percent
            window.blit(s.text,(max(0,(s.x/2)-(s.text.get_width()/2)),s.y+(s.img.get_height()-(s.img.get_height()/4.5)-(s.img.get_height()/8))/2))
            window.blit(s.img,(s.x,s.y))
if info["settings"]["Fast game"]==1:
    fast=0
else:
    fast=100
if info["settings"]["Hardcore"]==False:
    hard=0
else:
    hard=100

l_settings=[
    Setting(WIDTH,tilewh*3,0,loaded[14],False,"Music",info["settings"]["Music"]),
    Setting(WIDTH,tilewh*7,0,loaded[14],True,"Fast game",fast),
    Setting(WIDTH,tilewh*11,0,loaded[14],True,"Hardcore",hard)
]

l_explosions=[]

class Explosion:
    def __init__(s,base2,base1,delay):
        s.base2=base2
        s.base1=base1
        s.delay=delay
        s.alive=True
    def general(s,map):
        global prozor,l_gems,l_boulders,l_explosions
        if s.delay>0:
            s.delay-=1
        if s.delay==0:
            s.alive=False
            base1=s.base1
            base2=s.base2
            for i in range(-1,2):
                for j in range(-1,2):
                    terrainexplosion=map[base1+i][base2+j]
                    if terrainexplosion=="p":
                        global restart
                        restart+=1
                    elif terrainexplosion=="g":
                        gemindex=find_gems((base2+j)*tilewh,(base1+i)*tilewh)
                        if l_gems[gemindex].explodid_spawn==False and l_gems[gemindex].x!=base2*tilewh and l_gems[gemindex].y !=base1*tilewh:
                            l_explosions.append(Explosion(base2+j,base1+i   ,30/gamespeed))
                        l_gems[gemindex].explodid_spawn=True
                    elif terrainexplosion!="+" and terrainexplosion!="v":
                        map[base1+i][base2+j]="g"
                        l_gems.append(Diamond((base2+j)*tilewh,(base1+i)*tilewh,True))
                    if terrainexplosion=="b":
                        boulderidex=find_boulder((base2+j)*tilewh,(base1+i)*tilewh)
                        l_boulders[boulderidex].alive=False
                    if terrainexplosion=="e":
                        indexenemy=find_enemies((base2+j)*tilewh,(base1+i)*tilewh)
                        l_enemies[indexenemy].alive=False

class Terrain:
    def draw(s, map):
        for i in range(len(map)):
            for j in range(len(map[i])):
                s.img=""
                s.img1=""
                if trans[i][j]=="d":
                    s.img1=loaded[1]
                if trans[i][j]=="p":
                    s.img1=loaded[0]
                if trans[i][j]=="b":
                    s.img1=loaded[2]
                if trans[i][j]=="+":
                    s.img1=loaded[3]
                if trans[i][j]=="g":
                    s.img1=loaded[4]
                
                if l_terrain[i][j]=="d":
                    s.img=loaded[1]
                if l_terrain[i][j]=="p":
                    s.img=loaded[0]
                if l_terrain[i][j]=="b":
                    s.img=loaded[2]
                if l_terrain[i][j]=="+":
                    s.img=loaded[3]
                if l_terrain[i][j]=="g":
                    s.img=loaded[4]
                if l_terrain[i][j]=="v":
                    if dooropen==False:
                        s.img=loaded[5]
                    else:
                        s.img=loaded[8]
                if l_terrain[i][j]=="e":
                    s.img="1"
                if l_terrain[i][j]=="f":
                    s.img="1"
                if l_terrain[i][j]=="c":
                    s.img=loaded[7]
                if l_terrain[i][j]=="p":
                    window.blit(s.img,(player.x+camerax,player.y+cameray))
                else:
                    if j*(tilewh)+offsetx+camerax>-1+-tilewh and j*(tilewh)+offsetx+camerax<WIDTH and i*(tilewh)+offsety+cameray>-1+-tilewh and i*(tilewh)+cameray+offsety<=HEIGHT and s.img!="":
                        if l_terrain[i][j]=="e":
                            ind=find_enemies(j*(tilewh),i*(tilewh))
                            s.img=loaded[f"enemy{l_enemies[ind].direction}"]
                        if l_terrain[i][j]=="f":
                            ind=find_ghosts(j*(tilewh),i*(tilewh))
                            s.img=loaded[f"ghost{l_phantoms[ind].direction}"]
                        window.blit(s.img,(j*(tilewh)+offsetx+camerax,i*(tilewh)+offsety+cameray))
            
                    if j*(tilewh)+offsetx+camerax>-1+-tilewh and j*(tilewh)+offsetx+camerax<WIDTH and i*(tilewh)+offsety+cameray>-1+-tilewh and i*(tilewh)+cameray+offsety<=HEIGHT and s.img1!="":
                        window.blit(s.img1,(j*(tilewh)+offsetx+camerax,i*(tilewh)+offsety+cameray))
                    killtranssquare=random.randint(1,20)
                    if killtranssquare==1:
                        trans[i][j]="."  
    def draw_for_helper(s,l_terrain):
        global camerax
        global cameray
        for i in range(len(l_terrain)):
            for j in range(len(l_terrain[i])):
                s.img=""
                if l_terrain[i][j]=="d":
                    s.img=loaded[1]
                if l_terrain[i][j]=="p":
                    s.img=loaded[0]
                if l_terrain[i][j]=="b":
                    s.img=loaded[2]
                if l_terrain[i][j]=="+":
                    s.img=loaded[3]
                if l_terrain[i][j]=="g":
                    s.img=loaded[4]
                if l_terrain[i][j]=="e":
                    s.img=loaded[16]
                if l_terrain[i][j]=="v":
                    if dooropen==False:
                        s.img=loaded[5]
                    else:
                        s.img=loaded[8]
                if l_terrain[i][j]=="c":
                    s.img=loaded[7]
                if s.img!="":
                    window.blit(s.img,(j*tilewh+camerax,i*tilewh+cameray))
        if show:
            window.blit(loaded["map"],(0,0))
if pygame.joystick.get_count()>0:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
show=False
lives=3
diamonds=0
terrain=Terrain()
camera_speed=tilewh
SVAKIH30=0
l_gems=[]
l_enemies=[]
deathtime=300
offsetx=0
offsety=0
gamespeed=info["settings"]["Fast game"]
class Diamond:
    def __init__(s,x,y,explod):
        s.x=x
        s.y=y
        s.Falling=False
        s.again=20/gamespeed
        s.time=s.again
        s.alive=True
        s.explodid_spawn=explod
    def move(s,map):
        need=False
        global prozor,l_gems,l_boulders
        if s.alive:
            terraincheck=map[int(s.y/(tilewh))+1][int(s.x/(tilewh))]
            if terraincheck=="d" or terraincheck=="+" or terraincheck=="c" or terraincheck=="v":
                s.Falling=False
            elif terraincheck==".":
                need=True
                if s.time==0:
                    map[int(s.y/(tilewh))+1][int(s.x/(tilewh))]="g"
                    map[int(s.y/(tilewh))][int(s.x/(tilewh))]="."
                    s.y+=(tilewh)
                    s.time=s.again
                    s.Falling=True
            elif terraincheck=="p":
                if s.Falling==True:
                    if s.time==0:
                        global restart
                        restart+=1
                        s.alive=False
            elif terraincheck=="e":
                if s.Falling==True:
                    
                    s.explodid_spawn=True
                    base1=int(s.y/tilewh)+1
                    base2=int(s.x/tilewh)
                    s.time=s.again
                    l_explosions.append(Explosion(base2,base1,s.again))
            elif terraincheck=="f":
                ispodindex=find_ghosts(s.x,s.y+tilewh)
                if s.Falling:
                    l_phantoms[ispodindex].alive=False
                    map[int(s.y/(tilewh))+1][int(s.x/(tilewh))]="."
            elif terraincheck=="g":
                    if s.Falling==True:
                        ispodindex=find_gems(s.x,s.y+tilewh)
                        if l_gems[ispodindex].Falling==False:
                            s.Falling=False
                    else:
                    
                        ispodindex=find_gems(s.x,s.y+tilewh)
                        if ispodindex!=None:
                            if l_gems[ispodindex].Falling==False:
                                levo=map[int(s.y/(tilewh))][int(s.x/(tilewh))-1]
                                levodole=map[int(s.y/(tilewh))+1][int(s.x/(tilewh))-1]
                                desno=map[int(s.y/(tilewh))][int(s.x/(tilewh))+1]
                                desnodole=map[int(s.y/(tilewh))+1][int(s.x/(tilewh))+1]
                                if levo=="." and levodole==".":
                                    need=True
                                    if s.time==0:
                                        map[int(s.y/(tilewh))][int(s.x/(tilewh))-1]="g"
                                        map[int(s.y/(tilewh))][int(s.x/(tilewh))]="."
                                        s.Falling=True
                                        s.x-=tilewh
                                        s.time=s.again
                                elif desno==".":
                                    if desnodole==".":
                                        need=True
                                        if s.time==0:
                                            map[int(s.y/(tilewh))][int(s.x/(tilewh))+1]="g"
                                            map[int(s.y/(tilewh))][int(s.x/(tilewh))]="."
                                            s.Falling=True
                                            s.x+=tilewh
                                            s.time=s.again
            elif terraincheck=="b":
                    if s.Falling==True:
                        ispodindex=find_boulder(s.x,s.y+tilewh)
                        if l_boulders[ispodindex].Falling==False:
                            s.Falling=False
                    else:
                        need=True
                        if s.time==0:
                            #tumble
                            ispodindex=find_boulder(s.x,s.y+tilewh)
                            if l_boulders[ispodindex].Falling==False:
                                levo=map[int(s.y/(tilewh))][int(s.x/(tilewh))-1]
                                levodole=map[int(s.y/(tilewh))+1][int(s.x/(tilewh))-1]
                                desno=map[int(s.y/(tilewh))][int(s.x/(tilewh))+1]
                                desnodole=map[int(s.y/(tilewh))+1][int(s.x/(tilewh))+1]
                                if levo=="." and levodole==".":
                                    map[int(s.y/(tilewh))][int(s.x/(tilewh))-1]="g"
                                    map[int(s.y/(tilewh))][int(s.x/(tilewh))]="."
                                    s.Falling=True
                                    s.x-=tilewh
                                    s.time=s.again
                                elif desno==".":
                                    if desnodole==".":
                                        map[int(s.y/(tilewh))][int(s.x/(tilewh))+1]="g"
                                        map[int(s.y/(tilewh))][int(s.x/(tilewh))]="."
                                        s.Falling=True
                                        s.x+=tilewh
                                        s.time=s.again
            if s.time>0:
                if s.Falling==True or need:
                    s.time-=1

def die():
    window.blit(loaded[10],(0,0))
    window.blit(loaded[9],((WIDTH/2)-(loaded[9].get_width()/2),0))
class Ghost:
    def __init__(s,x,y):
        s.x=x
        s.y=y
        s.alive=True
        s.again=20/gamespeed
        s.time=s.again
        s.direction=0
        s.goforth=False
        s.turnright=False
    def find_path(s,terrain):
        if s.alive:
            global restart
            if s.direction==0:
                up=terrain[int(s.y/tilewh)-1][int(s.x/tilewh)]
                left=terrain[int(s.y/tilewh)][int(s.x/tilewh)-1]
                right=terrain[int(s.y/tilewh)][int(s.x/tilewh)+1]
            if s.direction==1:
                left=terrain[int(s.y/tilewh)-1][int(s.x/tilewh)]
                up=terrain[int(s.y/tilewh)][int(s.x/tilewh)+1]
                right=terrain[int(s.y/tilewh)+1][int(s.x/tilewh)]
            if s.direction==2:
                right=terrain[int(s.y/tilewh)][int(s.x/tilewh)-1]
                left=terrain[int(s.y/tilewh)][int(s.x/tilewh)+1]
                up=terrain[int(s.y/tilewh)+1][int(s.x/tilewh)]
            if s.direction==3:
                right=terrain[int(s.y/tilewh)-1][int(s.x/tilewh)]
                left=terrain[int(s.y/tilewh)+1][int(s.x/tilewh)]
                up=terrain[int(s.y/tilewh)][int(s.x/tilewh)-1]
            if s.time==0:
                s.direction%=4
                s.time=s.again
                if s.goforth:
                    
                    s.goforth=False
                    terrain[int(s.y/tilewh)][int(s.x/tilewh)]="."
                    if s.direction==0:
                        s.y-=tilewh
                    if s.direction==1:
                        s.x+=tilewh
                    if s.direction==2:
                        s.y+=tilewh
                    if s.direction==3:
                        s.x-=tilewh
                    if terrain[int(s.y/tilewh)][int(s.x/tilewh)]=="p":
                        restart+=1
                    terrain[int(s.y/tilewh)][int(s.x/tilewh)]="f"
                elif s.turnright:
                    s.turnright=False
                    s.direction+1
                    s.direction%=4
                elif up != "." and up != "p":
                    if left=="." or left=="p":
                        if left=="p":
                            restart+=1
                        s.direction-=1
                        s.direction%=4
                        s.goforth=True
                    elif right=="." or right=="p":
                        if right=="p":
                            restart+=1
                        s.direction+=1
                        s.direction%=4
                        s.goforth=True
                    else:
                        s.turnright=True
                        s.direction+=1
                        s.direction%=4
                elif left =="." or left=="p":
                    if left=="p":
                        restart+=1
                    s.direction-=1
                    s.direction%=4
                    s.goforth=True
                else:
                    s.direction%=4
                    terrain[int(s.y/tilewh)][int(s.x/tilewh)]="."
                    if s.direction==0:
                        if terrain[int(s.y/tilewh)-1][int(s.x/tilewh)]=="." or terrain[int(s.y/tilewh)-1][int(s.x/tilewh)]=="p":
                            s.y-=tilewh
                    if s.direction==1:
                        if terrain[int(s.y/tilewh)][int(s.x/tilewh)+1]=="." or terrain[int(s.y/tilewh)][int(s.x/tilewh)+1]=="p":
                            s.x+=tilewh
                    if s.direction==2:
                        if terrain[int(s.y/tilewh)+1][int(s.x/tilewh)]=="." or terrain[int(s.y/tilewh)+1][int(s.x/tilewh)]=="p":
                            s.y+=tilewh
                    if s.direction==3:
                        if terrain[int(s.y/tilewh)][int(s.x/tilewh)+1]=="." or terrain[int(s.y/tilewh)][int(s.x/tilewh)-1]=="p":
                            s.x-=tilewh
                    if terrain[int(s.y/tilewh)][int(s.x/tilewh)]=="p":
                        restart+=1
                    terrain[int(s.y/tilewh)][int(s.x/tilewh)]="f"
            if s.time>0:
                s.time-=1
        return terrain
class Enemy:
    def __init__(s,x,y):
        s.x=x
        s.y=y
        s.alive=True
        s.again=20/gamespeed
        s.time=s.again
        s.direction=0
        s.goforth=False
        s.turnright=False
    def find_path(s,terrain):
        if s.alive:
            global restart
            if s.direction==0:
                up=terrain[int(s.y/tilewh)-1][int(s.x/tilewh)]
                left=terrain[int(s.y/tilewh)][int(s.x/tilewh)-1]
                right=terrain[int(s.y/tilewh)][int(s.x/tilewh)+1]
            if s.direction==1:
                left=terrain[int(s.y/tilewh)-1][int(s.x/tilewh)]
                up=terrain[int(s.y/tilewh)][int(s.x/tilewh)+1]
                right=terrain[int(s.y/tilewh)+1][int(s.x/tilewh)]
            if s.direction==2:
                right=terrain[int(s.y/tilewh)][int(s.x/tilewh)-1]
                left=terrain[int(s.y/tilewh)][int(s.x/tilewh)+1]
                up=terrain[int(s.y/tilewh)+1][int(s.x/tilewh)]
            if s.direction==3:
                right=terrain[int(s.y/tilewh)-1][int(s.x/tilewh)]
                left=terrain[int(s.y/tilewh)+1][int(s.x/tilewh)]
                up=terrain[int(s.y/tilewh)][int(s.x/tilewh)-1]
            if s.time==0:
                s.direction%=4
                s.time=s.again
                if s.goforth:
                    
                    s.goforth=False
                    terrain[int(s.y/tilewh)][int(s.x/tilewh)]="."
                    if s.direction==0:
                        s.y-=tilewh
                    if s.direction==1:
                        s.x+=tilewh
                    if s.direction==2:
                        s.y+=tilewh
                    if s.direction==3:
                        s.x-=tilewh
                    if terrain[int(s.y/tilewh)][int(s.x/tilewh)]=="p":
                        restart+=1
                    terrain[int(s.y/tilewh)][int(s.x/tilewh)]="e"
                elif s.turnright:
                    s.turnright=False
                    s.direction+1
                    s.direction%=4
                elif up != "." and up != "p":
                    if left=="." or left=="p":
                        if left=="p":
                            restart+=1
                        s.direction-=1
                        s.direction%=4
                        s.goforth=True
                    elif right=="." or right=="p":
                        if right=="p":
                            restart+=1
                        s.direction+=1
                        s.direction%=4
                        s.goforth=True
                    else:
                        s.turnright=True
                        s.direction+=1
                        s.direction%=4
                elif left =="." or left=="p":
                    if left=="p":
                        restart+=1
                    s.direction-=1
                    s.direction%=4
                    s.goforth=True
                else:
                    s.direction%=4
                    terrain[int(s.y/tilewh)][int(s.x/tilewh)]="."
                    if s.direction==0:
                        if terrain[int(s.y/tilewh)-1][int(s.x/tilewh)]=="." or terrain[int(s.y/tilewh)-1][int(s.x/tilewh)]=="p":
                            s.y-=tilewh
                    if s.direction==1:
                        if terrain[int(s.y/tilewh)][int(s.x/tilewh)+1]=="." or terrain[int(s.y/tilewh)][int(s.x/tilewh)+1]=="p":
                            s.x+=tilewh
                    if s.direction==2:
                        if terrain[int(s.y/tilewh)+1][int(s.x/tilewh)]=="." or terrain[int(s.y/tilewh)+1][int(s.x/tilewh)]=="p":
                            s.y+=tilewh
                    if s.direction==3:
                        if terrain[int(s.y/tilewh)][int(s.x/tilewh)+1]=="." or terrain[int(s.y/tilewh)][int(s.x/tilewh)-1]=="p":
                            s.x-=tilewh
                    if terrain[int(s.y/tilewh)][int(s.x/tilewh)]=="p":
                        restart+=1
                    terrain[int(s.y/tilewh)][int(s.x/tilewh)]="e"
            if s.time>0:
                s.time-=1
        return terrain
class Boulder:
    def __init__(s,x,y):
        s.x=x
        s.y=y
        s.waittumble=0
        s.Falling=False
        s.again=20/gamespeed
        s.time=s.again
        s.alive=True
    def move(s,map):
        global prozor
        global l_boulders,l_gems,l_explosions
        need=False
        if s.alive==True:
            terraincheck=map[int(s.y/(tilewh))+1][int(s.x/(tilewh))]
            if terraincheck=="d" or terraincheck=="+" or terraincheck=="c" or terraincheck=="v":
                s.Falling=False
            elif terraincheck==".":
                need=True
                if s.time==0:
                    map[int(s.y/(tilewh))+1][int(s.x/(tilewh))]="b"
                    map[int(s.y/(tilewh))][int(s.x/(tilewh))]="."
                    s.y+=(tilewh)
                    s.Falling=True
                    s.time=s.again
            elif terraincheck=="p":
                if s.Falling==True:
                    if s.time==0:
                        global restart
                        restart+=1
                else:
                    s.Falling=False
                    pass
            elif terraincheck=="e":
                ispodindex=find_enemies(s.x,s.y+tilewh)
                if s.Falling:
                    l_enemies[ispodindex].alive=False
                    map[int(s.y/(tilewh))+1][int(s.x/(tilewh))]="."
            elif terraincheck=="f":
                ispodindex=find_ghosts(s.x,s.y+tilewh)
                if s.Falling:
                    l_phantoms[ispodindex].alive=False
                    map[int(s.y/(tilewh))+1][int(s.x/(tilewh))]="."
                
            elif terraincheck=="b":
                    if s.Falling==True:
                        ispodindex=find_boulder(s.x,s.y+tilewh)
                        if l_boulders[ispodindex].Falling==False:
                            s.Falling=False
                    else:
                        need=True
                        if s.time==0:
                            #tumble
                            ispodindex=find_boulder(s.x,s.y+tilewh)
                            if l_boulders[ispodindex].Falling==False:
                                levo=map[int(s.y/(tilewh))][int(s.x/(tilewh))-1]
                                levodole=map[int(s.y/(tilewh))+1][int(s.x/(tilewh))-1]
                                desno=map[int(s.y/(tilewh))][int(s.x/(tilewh))+1]
                                desnodole=map[int(s.y/(tilewh))+1][int(s.x/(tilewh))+1]
                                if levo=="." and levodole==".":
                                    map[int(s.y/(tilewh))][int(s.x/(tilewh))-1]="b"
                                    map[int(s.y/(tilewh))][int(s.x/(tilewh))]="."
                                    s.Falling=True
                                    s.x-=tilewh
                                    s.time=s.again
                                elif desno==".":
                                    if desnodole==".":
                                        map[int(s.y/(tilewh))][int(s.x/(tilewh))+1]="b"
                                        map[int(s.y/(tilewh))][int(s.x/(tilewh))]="."
                                        s.Falling=True
                                        s.x+=tilewh
                                        s.time=s.again
            elif terraincheck=="g":
                if s.Falling==True:
                    ispodindex=find_gems(s.x,s.y+tilewh)
                    if l_gems[ispodindex].Falling==False:
                        s.Falling=False
                else:
                    need=True
                    if s.time==0:
                        ispodindex=find_gems(s.x,s.y+tilewh)
                        if l_gems[ispodindex].Falling==False:
                            levo=map[int(s.y/(tilewh))][int(s.x/(tilewh))-1]
                            levodole=map[int(s.y/(tilewh))+1][int(s.x/(tilewh))-1]
                            desno=map[int(s.y/(tilewh))][int(s.x/(tilewh))+1]
                            desnodole=map[int(s.y/(tilewh))+1][int(s.x/(tilewh))+1]
                            if levo=="." and levodole==".":
                                map[int(s.y/(tilewh))][int(s.x/(tilewh))-1]="b"
                                map[int(s.y/(tilewh))][int(s.x/(tilewh))]="."
                                s.Falling=True
                                s.x-=tilewh
                                s.time=s.again
                            elif desno==".":
                                if desnodole==".":
                                    map[int(s.y/(tilewh))][int(s.x/(tilewh))+1]="b"
                                    map[int(s.y/(tilewh))][int(s.x/(tilewh))]="."
                                    s.Falling=True
                                    s.x+=tilewh
                                    s.time=s.again
            if s.time>0:
                if s.Falling==True or need:
                    s.time-=1
                



class Game_bar:
    def __init__(s):
        s.x=0
        s.y=0
        s.color=0
        s.daimonds_to_collect=s.change_d()
        s.timer=s.change_t()
        s.change=255/l_level[level-1][1]
        if l_level[level-1][1]==127:
            s.change=((255/(l_level[level-1][1]+0.5)))
        
    def general(s):
        pygame.draw.rect(window,(50,50,50),pygame.Rect(0,0,WIDTH,tilewh))
        pygame.draw.rect(window,(0,0,0),pygame.Rect(0+tilewh/10,0+tilewh/10,WIDTH-tilewh/5,tilewh-tilewh/5))
        window.blit(s.daimonds_to_collect,(WIDTH/2-tilewh*1.5-tilewh,0))
        window.blit(loaded[4],(WIDTH/2-tilewh*1.5,0))
        pygame.draw.rect(window,(min(255,s.color),max(255-s.color,0),0),pygame.Rect(WIDTH/2+tilewh/2,0,s.timer.get_width(),s.timer.get_height()))
        window.blit(s.timer,(WIDTH/2+tilewh/2,0))
        
    def change_d(s):
        if l_level[level-1][0]-diamonds<=0:
            if l_level[level-1][0]-diamonds==0:
                global dooropen
                dooropen=True
            else:
                return s.daimonds_to_collect
        return pygame.transform.scale(loaded["font"].render(f"{l_level[level-1][0]-diamonds}",False,(255,255,255)),(len(f"{l_level[level-1][0]-diamonds}")*(tilewh/3),tilewh))
    def change_t(s):
        global prozor
        if l_level[level-1][1]-seconds<=0:
            global restart
            restart+=1
            return s.timer
        return pygame.transform.scale(loaded["font"].render(f"{l_level[level-1][1]-seconds}",False,(255,255,255)),(len(f"{l_level[level-1][1]-seconds}")*(tilewh/3),tilewh))
    

dooropen=False
seconds=0
elapsed_time=900
bar=Game_bar()
restart=0
class Player:
    def __init__(s,x,y):
        s.x=x
        s.y=y
        s.time=12
    def move(s,map,direction,A):
        global cameray
        global camerax
        global l_boulders
        global l_gems
        global l_explosions
        global offsetx
        global offsety
        if camerax!=0 or cameray!=0:
            camerax=0
            cameray=0
            goback=True
            player.time=16/gamespeed
            return map,goback
        global diamonds
        terraincheck=map[int(s.y/tilewh-(offsety/tilewh))][int(s.x/tilewh-offsetx/tilewh)]
        goback=True
        if A:
            if terraincheck=="d":
                map[int(s.y/tilewh-(offsety/tilewh))][int(s.x/tilewh-offsetx/tilewh)]="."
                s.time=16/gamespeed
            elif terraincheck=="g":
                igems=find_gems(s.x-offsetx,s.y-offsety)
                l_gems[igems].alive=False
                diamonds+=1
                bar.daimonds_to_collect=bar.change_d()
                map[int(s.y/tilewh-(offsety/tilewh))][int(s.x/tilewh-offsetx/tilewh)]="."
                s.time=16/gamespeed
        elif terraincheck=="d" or terraincheck==".":
            map[indexpre1][indexpre2]="."
            map[int(s.y/(tilewh)-(offsety/(tilewh)))][int(s.x/(tilewh)-offsetx/(tilewh))]="p"
            goback=False
        elif terraincheck=="g":
            goback=False
            igems=find_gems(s.x-offsetx,s.y-offsety)
            if l_gems[igems].Falling==True:
                global restart
                restart+=1
            l_gems[igems].alive=False
            diamonds+=1
            map[indexpre1][indexpre2]="."
            map[int(s.y/(tilewh)-(offsety/(tilewh)))][int(s.x/(tilewh)-offsetx/(tilewh))]="p"
            bar.daimonds_to_collect=bar.change_d()
            
        elif terraincheck=="b":
            if s.time==-6:
                if direction==1:
                    if map[indexpre1][indexpre2+2]==".":
                        iboulder=find_boulder((indexpre2+1)*tilewh,indexpre1*tilewh)
                        if l_boulders[iboulder].Falling==False:
                            map[indexpre1][indexpre2+1]="p"
                            map[indexpre1][indexpre2] = "."
                            map[indexpre1][indexpre2+2]="b"
                            l_boulders[iboulder].x +=tilewh
                            goback=False
                elif direction==3:
                    if map[indexpre1][indexpre2-2]==".":
                        iboulder=find_boulder((indexpre2-1)*tilewh,indexpre1*tilewh)
                        if l_boulders[iboulder].Falling==False:
                            map[indexpre1][indexpre2-1]="p"
                            map[indexpre1][indexpre2]="."
                            map[indexpre1][indexpre2-2]="b"
                            l_boulders[iboulder].x-=tilewh
                            goback=False
        elif terraincheck=="e":
            restart+=1
        elif terraincheck=="f":
            restart+=1
        elif terraincheck=="v" and dooropen==True:
            goback=False
            l_boulders,map,l_gems,l_explosions,offsety,offsetx = nextlevel(True)
        return map,goback
def replace_at(s, index, new_char):
    s[index[0]]=new_char
    return s
l_boulders=[]
vartest=0
l_phantoms=[]
for i in range(len(l_terrain)):
    for j in range(len(l_terrain[i])):
        if l_terrain[i][j]=="p":
            player=Player(j*(tilewh),i*(tilewh))
        if l_terrain[i][j]=="b":
            l_boulders.append(Boulder(j*(tilewh),i*(tilewh)))
        if l_terrain[i][j]=="g":
            l_gems.append(Diamond(j*(tilewh),i*(tilewh),False))
        if l_terrain[i][j]=="e":
            l_enemies.append(Enemy(j*tilewh,i*tilewh))
        if l_terrain[i][j]=="f":
            l_phantoms.append(Ghost(j*tilewh,i*tilewh))
            
class Button:
    def __init__(s,x,y,img,purpose,prozor,restart,save,dele,slot):
        s.x=x
        s.y=y
        s.saveimg=img
        s.img=loaded[img]
        s.restart =restart
        s.dele=dele
        s.purpose=purpose
        s.prozor=prozor
        s.save=save
        s.forcedel=False
        s.forcemove=False
        s.x-=s.img.get_width()/2
        s.y-=s.img.get_height()/2
        s.slot=slot
    def genearl(s):
        
        global prozor
        global saveslot
        if s.prozor==prozor:
            global mouseuse
            if button_colision(s.img.get_width(),s.img.get_height(),s.x,s.y,mousePos,mouseState) and mouseuse:
                prozor=s.purpose
                if s.saveimg=="delete":
                    s.forcedel=True
                if s.saveimg==12:
                    s.forcemove=True
                mouseuse=False
                if s.slot==True:
                    saveslot=s.save
                
                if s.save!=None and s.slot==False:
                    global l_boulders,l_explosions,l_gems,l_terrain,seconds,player,trans,offsetx,offsety,bar,diamonds,dooropen,elapsed_time,level,info
                    if s.forcemove:
                        s.forcemove=False
                        init_gameinfo(info['saves'][f'saveslot{saveslot}'][f'save{s.save}'])
                    elif s.save!=None:
                        if info["newestsaves"][s.save-1]==None or s.forcedel:
                            info["quicksaves"][f"{s.save}"]={}
                            info['saves'][f'saveslot{s.save}'][f'save1']={}
                            info['saves'][f'saveslot{s.save}'][f'save2']={}
                            info['saves'][f'saveslot{s.save}'][f'save3']={}
                            info["newestsaves"][s.save-1]=1
                            s.forcedel=False
                            level=0
                            l_boulders,l_terrain,l_gems,l_explosions,offsety,offsetx = nextlevel(True)
                            info['saves'][f'saveslot{s.save}'][f'save1']=make_gameinfo()
                            init_gameinfo(info['saves'][f'saveslot{s.save}'][f'save1'])
                            saveslot=s.save
                        else:
                            prozor=-5
                            
                    
            window.blit(s.img,(s.x,s.y))
height4=HEIGHT/4
height5=HEIGHT/5
width2=WIDTH/2
class Buttonsforsave:
    def __init__(s,x,y,load,img,prozor,purpose,save):
        s.x=x
        s.y=y
        s.load=load
        s.img=img
        s.width=s.img.get_width()
        s.height=s.img.get_height()
        s.prozor=prozor
        s.purpose=purpose
        s.save=save
    def general(s):
        global prozor
        global saveslot
        if s.prozor==prozor:
            global mouseuse
            if button_colision(s.img.get_width(),s.img.get_height(),s.x,s.y,mousePos,mouseState) and mouseuse:
                prozor=s.purpose #for save == -2 pa onda nek bude instead of ako treba da se replacuje, ali ako nije full onda samo minimenu
                mouseuse=False
                if s.load==1:
                    init_gameinfo(info['saves'][f'saveslot{saveslot}'][f'save{s.save}'])
                    prozor=-10
                elif s.load==0:
                    if info['saves'][f'saveslot{saveslot}'][f'save{s.save}']:
                        pass
l_buttonsforsave=[
    
    
    
]





l_buttons=[
    Button(width2,height4*1.5,11,-5,0, False,None,None,False),
    Button(width2,height4*2.5,13,-2,0,False ,None,None,False),
    Button(width2,height5*1,"saveslot1",-6,-5,False,1,None,True),
    Button(width2,height5*2,"saveslot2",-6,-5,False,2,None,True),
    Button(width2,height5*3,"saveslot3",-6,-5,False,3,None,True),
    
    Button(width2,height5*1,"save1",-7,-6,False,1,None,False),
    Button(width2,height5*2,"save2",-7,-6,False,2,None,False),
    Button(width2,height5*3,"save3",-7,-6,False,3,None,False),

    
    Button(width2-loaded["delete"].get_height()/2,height5*2,"delete",1,-7,False,0,4,False),
    Button(width2-loaded[12].get_height()/2,height5*3,12,1,-7,False,0,5,False)
    
    
]
banw=0
def background(img):
    window.blit(img,(0,0))
A_for_player=False
def create_trans(listt:list):
    trans=[]
    for i in range(len(listt)):
        red=[]
        for j in range(len(listt[i])):
            if listt[i][j]=="p":
                red.append(".")
                continue
            red.append("+")
        trans.append(red)
    return trans
musicpos=0
trans=create_trans(l_terrain)
for i in range(len(trans)):
    for j in range(len(trans[i])):
        trans[i][j]="."
def nextlevel(regen):
    global l_boulders
    global l_explosions
    global l_gems
    global l_terrain
    global level
    global seconds
    global prozor
    global player
    global trans
    global offsetx
    global offsety
    global bar
    global diamonds
    global dooropen
    global elapsed_time
    global lives
    elapsed_time=900
    if regen:
        lives=3
    
    
    seconds=0
    level+=1
    prozor=1
    if level==len(l_level)+1:
        prozor=-5
        level=1
        #game done
        info["saves"][f"save{saveslot}"]={}
        info["quicksaves"][saveslot]
    l_terrain=copy.deepcopy(l_level[level-1][2])
    
    trans=create_trans(l_terrain)
    l_boulders=[]
    l_explosions=[]
    l_gems=[]
    global l_enemies,l_phantoms
    l_phantoms=[]
    l_enemies=[]
    
    l_boulders=[]

    for i in range(len(l_terrain)):
        for j in range(len(l_terrain[i])):
            if l_terrain[i][j]=="p":
                player=Player(j*(tilewh),i*(tilewh))
            if l_terrain[i][j]=="b":
                l_boulders.append(Boulder(j*(tilewh),i*(tilewh)))
            if l_terrain[i][j]=="g":
                l_gems.append(Diamond(j*(tilewh),i*(tilewh),False))
            if l_terrain[i][j]=="e":
                l_enemies.append(Enemy(j*(tilewh),i*(tilewh)))
            if l_terrain[i][j]=="f":
                l_phantoms.append(Ghost(j*tilewh,i*tilewh))
    
    

    dooropen=False
    diamonds=0
    bar=Game_bar()
    offsety=((((HEIGHT/2)/tilewh)*tilewh)-player.y)
    offsetx=((((WIDTH/2)/tilewh)*tilewh)-player.x)
    player.x=((WIDTH/2)/tilewh)*tilewh
    player.y=((HEIGHT/2)/tilewh)*tilewh
    return l_boulders,l_terrain,l_gems,l_explosions,offsety,offsetx

prozor=0
offsety=((((HEIGHT/2)/tilewh)*tilewh)-player.y)
offsetx=((((WIDTH/2)/tilewh)*tilewh)-player.x)
player.x=((WIDTH/2)/tilewh)*tilewh
player.y=((HEIGHT/2)/tilewh)*tilewh
trans=create_trans(l_terrain)
mouseuse=True
escapeuse=True
timeset = time.time()
music=loaded["music"]

delayforskip=0
saveslot=1

music.play()
exitsde=False
zamena=" "
musictime=0

while True:
    window.fill("Black")
    keys = pygame.key.get_pressed()
    events = pygame.event.get()
    mouseState = pygame.mouse.get_pressed()
    mousePos = pygame.mouse.get_pos()
    music.set_volume(info["settings"]["Music"]/100)
    
    if mouseState[0]==False:
        mouseuse=True
    if keys[pygame.K_ESCAPE]==False:
        escapeuse=True
    times=clock.get_time()
    musictime+=times
    if prozor==1:
        elapsed_time += times*gamespeed
    gamespeed=settings["Fast game"]
    if musictime>=500:
        musictime-=500
        musicpos+=1
        if musicpos==157:
            
            music.stop()
            music.play()
            musicpos=0
    if elapsed_time >= 1000:
        #secondpassed
        bar.color+=bar.change
        bar.timer=bar.change_t()
        seconds+=1
        elapsed_time -= 1000
        
    if prozor==1:
        went=False
        if keys[pygame.K_x]:
            quickinfo=make_gameinfo()
            info['quicksaves'][f"{saveslot}"]=copy.deepcopy(quickinfo)
        if keys[pygame.K_l]:
            if info['quicksaves'][f"{saveslot}"]!={}:
                init_gameinfo(copy.deepcopy(info['quicksaves'][f"{saveslot}"]))
        for event in events:
            if event.type == pygame.QUIT:
                prozor=-5
            if event.type == pygame.JOYBUTTONDOWN:
                if pygame.joystick.get_count()>0:
                    if event.button==0:
                        A_for_player=True
        if keys[pygame.K_0] and keys[pygame.K_1] and delayforskip==0:
            
            l_boulders,map,l_gems,l_explosions,offsety,offsetx = nextlevel(True)
            delayforskip=60
        if delayforskip>0:
            delayforskip-=1
        if keys[pygame.K_q]:
            A_for_player=True
        else:
            if pygame.joystick.get_count()>0:
                if joystick.get_button(0)==False:
                    A_for_player=False
            else:
                A_for_player=False
                    
        for i in range(len(l_boulders)):
            l_boulders[i].move(l_terrain)
        indexdelete=0
        for i in range(len(l_boulders)):
            if l_boulders[indexdelete].alive==False:
                del l_boulders[indexdelete]
                indexdelete-=1
            indexdelete+=1

        if player.time<=0:
            indexpre1=int(player.y/(tilewh)-((offsety/tilewh)))
            indexpre2=int(player.x/(tilewh)-((offsetx/tilewh)))
            preoffset=[offsetx,offsety]
            if pygame.joystick.get_count()>0:
                try:
                    a=joystick.get_axis(0)
                except:
                    joystick=pygame.joystick.Joystick(0)
                    joystick.init()
                x = joystick.get_axis(0)
                y = joystick.get_axis(1)  # Invert Y for normal coordinate system
                magnitude = math.hypot(x, y)
                if magnitude > 0.4:  # Deadzone to avoid jitter
                    angle = math.degrees(math.atan2(-y, x))
                    angle%=360
                    went=True
                    if angle<=45 or angle>315:
                        offsetx-=camera_speed
                        direction=1
                    elif angle>45 and angle<=135:
                        offsety+=camera_speed
                        direction=2
                    elif angle<=225 and angle>135:
                        offsetx+=camera_speed
                        direction=3
                    else:
                        offsety-=camera_speed
                        direction=4
            if keys[pygame.K_d]:
                if went==False:
                    offsetx-=camera_speed
                    went=True
                    direction=1
            elif keys[pygame.K_s]:
                if went==False:
                    offsety-=camera_speed
                    went=True
                    direction=4
            elif keys[pygame.K_a]:
                if went==False:
                    offsetx+=camera_speed
                    went=True
                    direction=3
            elif keys[pygame.K_w]:
                if went==False:
                    direction=2
                    offsety+=camera_speed
                    went=True
            if went==True:
                l_terrain,goback=player.move(l_terrain,direction,A_for_player)
                if goback:
                    offsetx=preoffset[0]
                    offsety=preoffset[1]
                else:
                    player.time=16
        
        if keys[pygame.K_ESCAPE] and escapeuse:
            prozor=10
            escapeuse=False
        if keys[pygame.K_UP]:
            cameray+=camera_speed/5
        if keys[pygame.K_DOWN]:
            cameray-=camera_speed/5
        if keys[pygame.K_RIGHT]:
            camerax-=camera_speed/5
        if keys[pygame.K_LEFT]:
            camerax+=camera_speed/5
        
        
        
        
        
        
        
        
        
        if player.time>-6:
            player.time-=(1*gamespeed)
        indexdelete=0
        for i in range(len(l_gems)):
            if l_gems[indexdelete].alive==False:
                
                del l_gems[indexdelete]
                indexdelete-=1
            else:
                if len(l_explosions)==0:
                    l_gems[indexdelete].explodid_spawn=False
            indexdelete+=1
            
        for i in range(len(l_gems)):
            l_gems[i].move(l_terrain)
        indexdelete=0
        for i in range(len(l_gems)):
            if l_gems[indexdelete].alive==False:
                del l_gems[indexdelete]
                indexdelete-=1
            indexdelete+=1
        indexdelete=0
        for i in range(len(l_explosions)):
            l_explosions[indexdelete].general(l_terrain)
            if l_explosions[indexdelete].alive==False:
                del l_explosions[indexdelete]
                indexdelete-=1
            indexdelete+=1
            
        for i in range(len(l_enemies)):
            l_terrain=l_enemies[i].find_path(l_terrain)
        for i in range(len(l_phantoms)):
            l_terrain=l_phantoms[i].find_path(l_terrain)
        
        
        indexdelete=0
        for i in range(len(l_phantoms)):
            if l_phantoms[indexdelete].alive==False:
                del l_phantoms[indexdelete]
                indexdelete-=1
            indexdelete+=1
        
        indexdelete=0
        for i in range(len(l_enemies)):
            if l_enemies[indexdelete].alive==False:
                del l_enemies[indexdelete]
                indexdelete-=1
            indexdelete+=1


        terrain.draw(l_terrain)
        bar.general()
        if restart>0:
            restart=0
            lives-=1
            if info["settings"]["Hardcore"] or lives==0:
                prozor=-1
                info["saves"][f"save{saveslot}"]={}
            else:
                level-=1
                l_boulders,map,l_gems,l_explosions,offsety,offsetx = nextlevel(False)
    if prozor==-5:
        background(loaded[6])
        if keys[pygame.K_ESCAPE] and escapeuse:
            escapeuse=False
            prozor=0
        for event in events:
            if event.type == pygame.QUIT:
                exitsde=True
        if exitsde:
            exitsde=False
            prozor=0
    if prozor==-6:
        background(loaded[6])
        if keys[pygame.K_ESCAPE] and escapeuse:
            escapeuse=False
            prozor=0
        for event in events:
            if event.type == pygame.QUIT:
                exitsde=True
        if exitsde:
            exitsde=False
            prozor=0
        
    if prozor==0:
        
        
        background(loaded[6])
        for event in events:
            if event.type == pygame.QUIT:
                exitsde=True
        if exitsde:
            exitsde=False
            break
        if keys[pygame.K_q] and keys[pygame.K_w] and keys[pygame.K_e]:
            prozor=-10
            prazan=[]
            prazan=adder(prazan,"levels/sveprazno.txt")
            l_terrain=prazan[0]
        if keys[pygame.K_ESCAPE] and escapeuse:
            escapeuse=False
            break
    if prozor==10:
        background(loaded[16])
        if keys[pygame.K_ESCAPE] and escapeuse:
            escapeuse=False
            prozor=-5
            gameinfo=make_gameinfo()
            info['saves'][f"save{saveslot}"]=gameinfo
    if prozor==-10:
        if keys[pygame.K_UP]:
            cameray+=camera_speed/5
        if keys[pygame.K_DOWN]:
            cameray-=camera_speed/5
        if keys[pygame.K_RIGHT]:
            camerax-=camera_speed/5
        if keys[pygame.K_LEFT]:
            camerax+=camera_speed/5
        terrain.draw_for_helper(l_terrain)
        if keys[pygame.K_d]:
            zamena="d"
        if keys[pygame.K_p]:
            zamena="p"
        if keys[pygame.K_b]:
            zamena="b"
        if keys[pygame.K_w]:
            zamena="+"
        if keys[pygame.K_g]:
            zamena="g"
        if keys[pygame.K_v]:
            zamena="v"
        if keys[pygame.K_c]:
            zamena="c"
        if keys[pygame.K_SPACE]:
            zamena="."
        if keys[pygame.K_w]:
            if banw==0:
                show=Boolflip(show)
                banw=30
        if banw>0:
            banw-=1
        if mouseState[0]==True:
            for i in range(len(l_terrain)):
                for j in range(len(l_terrain[i])):
                    if j*tilewh<=mousePos[0]-camerax and tilewh*(j+1)>mousePos[0]-camerax and i*tilewh<=mousePos[1]-cameray and tilewh*(i+1)>mousePos[1]-cameray:
                        l_terrain[i][j]=zamena
        if keys[pygame.K_ESCAPE]:
            acronym=input()
            if acronym!="n":
                imezafile=f"levels/map{acronym}.txt"
                writeintxt(l_terrain,imezafile)
            prozor=0
            escapeuse=False
    if prozor==-2:
        #background(loaded[6])
        for event in events:
            if event.type == pygame.QUIT:
                prozor=0
        if keys[pygame.K_ESCAPE] and escapeuse:
            escapeuse=False
            prozor=0
        for i in range(len(l_settings)):
            l_settings[i].general()
    if prozor==-1:
        die()
        if deathtime>0:
            deathtime-=1
        else:
            deathtime=300
            level=0
            l_boulders,l_terrain,l_gems,l_explosions,offsety,offsetx = nextlevel(True)
            prozor=-5
    for i in range(len(l_buttons)):
        l_buttons[i].genearl()
    pygame.display.update()
    clock.tick(60)
    SVAKIH30+=1
    if SVAKIH30==30:
        SVAKIH30=0
        if time.time()-vremepre>najvecivreme:
            najvecivreme=time.time()-vremepre
        
        print(time.time()-vremepre)
        vremepre=time.time()

print(najvecivreme)
print(30/najvecivreme)
info["settings"]=settings
save(info)