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
camerax=0
cameray=0
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

#char ="!#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"

def read():
    info=end()
    return info

def write(info):
    info={'diamonds': 0, 'username': '',}
    ens(info)


def find_boulder(x,y):
    for i in range(len(l_boulders)):
        if l_boulders[i].x==x and l_boulders[i].y==y:
            return i
            break

def find_gems(x,y):
    for i in range(len(l_gems)):
        if l_gems[i].x==x and l_gems[i].y==y:
            return i
            break

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



l_explosions=[]

class Explosion:
    def __init__(s,base2,base1,delay):
        s.base2=base2
        s.base1=base1
        s.delay=delay
        s.alive=True
    def general(s,map):
        global prozor
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
                        pass
                        prozor=-1
                    elif terrainexplosion=="g":
                        gemindex=find_gems((base2+j)*tilewh,(base1+i)*tilewh)
                        if l_gems[gemindex].explodid_spawn==False and l_gems[gemindex].x!=base2*tilewh and l_gems[gemindex].y !=base1*tilewh:
                            l_explosions.append(Explosion(base2+j,base1+i   ,30))
                            l_gems[gemindex].explodid_spawn=True
                    elif terrainexplosion!="w" and terrainexplosion!="v":
                        map[base1+i][base2+j]="g"
                        l_gems.append(Diamond((base2+j)*tilewh,(base1+i)*tilewh,True))
                    if terrainexplosion=="b":
                        boulderidex=find_boulder((base2+j)*tilewh,(base1+i)*tilewh)
                        l_boulders[boulderidex].alive=False

class Terrain:
    def draw(s, map):
        for i in range(len(map)):
            for j in range(len(map[i])):
                s.img=""
                if l_terrain[i][j]=="d":
                    s.img=loaded[1]
                if l_terrain[i][j]=="p":
                    s.img=loaded[0]
                if l_terrain[i][j]=="b":
                    s.img=loaded[2]
                if l_terrain[i][j]=="w":
                    s.img=loaded[3]
                if l_terrain[i][j]=="g":
                    s.img=loaded[4]
                if l_terrain[i][j]=="v":
                    if dooropen==False:
                        s.img=loaded[5]
                    else:
                        s.img=loaded[8]
                    
                if l_terrain[i][j]=="c":
                    s.img=loaded[7]
                if l_terrain[i][j]=="p":
                    window.blit(s.img,(player.x+camerax,player.y+cameray))
                else:
                    if j*(tilewh)+offsetx+camerax>-1+-tilewh and j*(tilewh)+offsetx+camerax<WIDTH and i*(tilewh)+offsety+cameray>-1+-tilewh and i*(tilewh)+cameray+offsety<=HEIGHT and s.img!="":
                        window.blit(s.img,(j*(tilewh)+offsetx+camerax,i*(tilewh)+offsety+cameray))
if pygame.joystick.get_count()>0:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
diamonds=0
terrain=Terrain()
camera_speed=tilewh
SVAKIH30=0
l_gems=[]
deathtime=300
offsetx=0
offsety=0
class Diamond:
    def __init__(s,x,y,explod):
        s.x=x
        s.y=y
        s.Falling=False
        s.again=20
        s.time=s.again
        s.alive=True
        s.explodid_spawn=explod
    def move(s,map):
        global prozor
        if s.alive:
            terraincheck=map[int(s.y/(tilewh))+1][int(s.x/(tilewh))]
            if terraincheck=="d" or terraincheck=="w":
                s.Falling=False
            elif terraincheck==" ":
                if s.time==0:
                    map[int(s.y/(tilewh))+1][int(s.x/(tilewh))]="g"
                    map[int(s.y/(tilewh))][int(s.x/(tilewh))]=" "
                    s.y+=(tilewh)
                    s.time=s.again
                    s.Falling=True
            elif terraincheck=="p":
                if s.Falling==True:
                    if s.time==0:
                        prozor=-1
                        s.alive=False
            elif terraincheck=="g":
                    if s.Falling==True:
                        ispodindex=find_gems(s.x,s.y+tilewh)
                        if l_gems[ispodindex].Falling==False:
                            s.Falling=False
                    else:
                        if s.time==0:
                            ispodindex=find_gems(s.x,s.y+tilewh)
                            if ispodindex!=None:
                                if l_gems[ispodindex].Falling==False:
                                    levo=map[int(s.y/(tilewh))][int(s.x/(tilewh))-1]
                                    levodole=map[int(s.y/(tilewh))+1][int(s.x/(tilewh))-1]
                                    desno=map[int(s.y/(tilewh))][int(s.x/(tilewh))+1]
                                    desnodole=map[int(s.y/(tilewh))+1][int(s.x/(tilewh))+1]
                                    if levo==" " and levodole==" ":
                                        map[int(s.y/(tilewh))][int(s.x/(tilewh))-1]="g"
                                        map[int(s.y/(tilewh))][int(s.x/(tilewh))]=" "
                                        s.Falling=True
                                        s.x-=tilewh
                                        s.time=s.again
                                    elif desno==" ":
                                        if desnodole==" ":
                                            map[int(s.y/(tilewh))][int(s.x/(tilewh))+1]="g"
                                            map[int(s.y/(tilewh))][int(s.x/(tilewh))]=" "
                                            s.Falling=True
                                            s.x+=tilewh
                                            s.time=s.again
            elif terraincheck=="b":
                    if s.Falling==True:
                        ispodindex=find_boulder(s.x,s.y+tilewh)
                        if l_boulders[ispodindex].Falling==False:
                            s.Falling=False
                    else:
                        if s.time==0:
                            #tumble
                            ispodindex=find_boulder(s.x,s.y+tilewh)
                            if l_boulders[ispodindex].Falling==False:
                                levo=map[int(s.y/(tilewh))][int(s.x/(tilewh))-1]
                                levodole=map[int(s.y/(tilewh))+1][int(s.x/(tilewh))-1]
                                desno=map[int(s.y/(tilewh))][int(s.x/(tilewh))+1]
                                desnodole=map[int(s.y/(tilewh))+1][int(s.x/(tilewh))+1]
                                if levo==" " and levodole==" ":
                                    map[int(s.y/(tilewh))][int(s.x/(tilewh))-1]="g"
                                    map[int(s.y/(tilewh))][int(s.x/(tilewh))]=" "
                                    s.Falling=True
                                    s.x-=tilewh
                                    s.time=s.again
                                elif desno==" ":
                                    if desnodole==" ":
                                        map[int(s.y/(tilewh))][int(s.x/(tilewh))+1]="g"
                                        map[int(s.y/(tilewh))][int(s.x/(tilewh))]=" "
                                        s.Falling=True
                                        s.x+=tilewh
                                        s.time=s.again
            if s.time>0:
                s.time-=1

def die():
    window.blit(loaded[10],(0,0))
    window.blit(loaded[9],((WIDTH/2)-(loaded[9].get_width()/2),0))




class Boulder:
    def __init__(s,x,y):
        s.x=x
        s.y=y
        s.waittumble=0
        s.Falling=False
        s.again=20
        s.time=s.again
        s.alive=True
    def move(s,map):
        global prozor
        if s.alive==True:
            terraincheck=map[int(s.y/(tilewh))+1][int(s.x/(tilewh))]
            if terraincheck=="d" or terraincheck=="w":
                s.Falling=False
            elif terraincheck==" ":
                if s.time==0:
                    map[int(s.y/(tilewh))+1][int(s.x/(tilewh))]="b"
                    map[int(s.y/(tilewh))][int(s.x/(tilewh))]=" "
                    s.y+=(tilewh)
                    s.Falling=True
                    s.time=s.again
            elif terraincheck=="p":
                if s.Falling==True:
                    if s.time==0:
                        pass
                        prozor=-1
                else:
                    s.Falling=False
                    pass
            elif terraincheck=="b":
                    if s.Falling==True:
                        ispodindex=find_boulder(s.x,s.y+tilewh)
                        if l_boulders[ispodindex].Falling==False:
                            s.Falling=False
                    else:
                        if s.time==0:
                            #tumble
                            ispodindex=find_boulder(s.x,s.y+tilewh)
                            if l_boulders[ispodindex].Falling==False:
                                levo=map[int(s.y/(tilewh))][int(s.x/(tilewh))-1]
                                levodole=map[int(s.y/(tilewh))+1][int(s.x/(tilewh))-1]
                                desno=map[int(s.y/(tilewh))][int(s.x/(tilewh))+1]
                                desnodole=map[int(s.y/(tilewh))+1][int(s.x/(tilewh))+1]
                                if levo==" " and levodole==" ":
                                    map[int(s.y/(tilewh))][int(s.x/(tilewh))-1]="b"
                                    map[int(s.y/(tilewh))][int(s.x/(tilewh))]=" "
                                    s.Falling=True
                                    s.x-=tilewh
                                    s.time=s.again
                                elif desno==" ":
                                    if desnodole==" ":
                                        map[int(s.y/(tilewh))][int(s.x/(tilewh))+1]="b"
                                        map[int(s.y/(tilewh))][int(s.x/(tilewh))]=" "
                                        s.Falling=True
                                        s.x+=tilewh
                                        s.time=s.again
            elif terraincheck=="g":
                if s.Falling==True:
                    ispodindex=find_gems(s.x,s.y+tilewh)
                    base1=int(s.y/(tilewh)+1)
                    base2=int(s.x/(tilewh))
                    if l_gems[ispodindex].Falling==False:
                        l_gems[ispodindex].explodid_spawn=True
                        l_explosions.append(Explosion(base2,base1,0))
                else:
                    if s.time==0:
                        ispodindex=find_gems(s.x,s.y+tilewh)
                        if l_gems[ispodindex].Falling==False:
                            levo=map[int(s.y/(tilewh))][int(s.x/(tilewh))-1]
                            levodole=map[int(s.y/(tilewh))+1][int(s.x/(tilewh))-1]
                            desno=map[int(s.y/(tilewh))][int(s.x/(tilewh))+1]
                            desnodole=map[int(s.y/(tilewh))+1][int(s.x/(tilewh))+1]
                            if levo==" " and levodole==" ":
                                map[int(s.y/(tilewh))][int(s.x/(tilewh))-1]="b"
                                map[int(s.y/(tilewh))][int(s.x/(tilewh))]=" "
                                s.Falling=True
                                s.x-=tilewh
                                s.time=s.again
                            elif desno==" ":
                                if desnodole==" ":
                                    map[int(s.y/(tilewh))][int(s.x/(tilewh))+1]="b"
                                    map[int(s.y/(tilewh))][int(s.x/(tilewh))]=" "
                                    s.Falling=True
                                    s.x+=tilewh
                                    s.time=s.again
            if s.time>0:
                s.time-=1
                



class Game_bar:
    def __init__(s):
        s.x=0
        s.y=0
        s.daimonds_to_collect=s.change_d()
        s.timer=s.change_t()
    def general(s):
        pygame.draw.rect(window,(50,50,50),pygame.Rect(0,0,WIDTH,tilewh))
        pygame.draw.rect(window,(0,0,0),pygame.Rect(0+tilewh/10,0+tilewh/10,WIDTH-tilewh/5,tilewh-tilewh/5))
        window.blit(s.daimonds_to_collect,(WIDTH/2-tilewh*1.5,0))
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
            prozor=-1
            return s.timer
        return pygame.transform.scale(loaded["font"].render(f"{l_level[level-1][1]-seconds}",False,(255,255,255)),(len(f"{l_level[level-1][1]-seconds}")*(tilewh/3),tilewh))
    

dooropen=False
seconds=0
elapsed_time=0
bar=Game_bar()

class Player:
    def __init__(s,x,y):
        s.x=x
        s.y=y
        s.time=12
    def move(s,map,direction,A):
        global cameray
        global camerax
        if camerax!=0 or cameray!=0:
            camerax=0
            cameray=0
            goback=True
            player.time=15
            return map,goback
        global diamonds
        terraincheck=map[int(s.y/tilewh-(offsety/tilewh))][int(s.x/tilewh-offsetx/tilewh)]
        goback=True
        if A:
            if terraincheck=="d":
                map[int(s.y/tilewh-(offsety/tilewh))][int(s.x/tilewh-offsetx/tilewh)]=" "
                s.time=15
            elif terraincheck=="g":
                igems=find_gems(s.x-offsetx,s.y-offsety)
                l_gems[igems].alive=False
                diamonds+=1
                bar.daimonds_to_collect=bar.change_d()
                map[int(s.y/tilewh-(offsety/tilewh))][int(s.x/tilewh-offsetx/tilewh)]=" "
                s.time=15
        elif terraincheck=="d" or terraincheck==" ":
            map[indexpre1][indexpre2]=" "
            map[int(s.y/(tilewh)-(offsety/(tilewh)))][int(s.x/(tilewh)-offsetx/(tilewh))]="p"
            goback=False
        elif terraincheck=="g":
            goback=False
            igems=find_gems(s.x-offsetx,s.y-offsety)
            if l_gems[igems].Falling==True:
                global prozor
                prozor=-1
            l_gems[igems].alive=False
            diamonds+=1
            map[indexpre1][indexpre2]=" "
            map[int(s.y/(tilewh)-(offsety/(tilewh)))][int(s.x/(tilewh)-offsetx/(tilewh))]="p"
            bar.daimonds_to_collect=bar.change_d()
            
        elif terraincheck=="b":
            if s.time==-6:
                if direction==1:
                    if map[indexpre1][indexpre2+2]==" ":
                        iboulder=find_boulder((indexpre2+1)*tilewh,indexpre1*tilewh)
                        if l_boulders[iboulder].Falling==False:
                            map[indexpre1][indexpre2+1]="p"
                            map[indexpre1][indexpre2] = " "
                            map[indexpre1][indexpre2+2]="b"
                            l_boulders[iboulder].x +=tilewh
                            goback=False
                elif direction==3:
                    if map[indexpre1][indexpre2-2]==" ":
                        iboulder=find_boulder((indexpre2-1)*tilewh,indexpre1*tilewh)
                        if l_boulders[iboulder].Falling==False:
                            map[indexpre1][indexpre2-1]="p"
                            map[indexpre1][indexpre2]=" "
                            map[indexpre1][indexpre2-2]="b"
                            l_boulders[iboulder].x-=tilewh
                            goback=False
        return map,goback
def replace_at(s, index, new_char):
    s[index[0]]=new_char
    return s
l_boulders=[]

for i in range(len(l_terrain)):
    for j in range(len(l_terrain[i])):
        if l_terrain[i][j]=="p":
            player=Player(j*(tilewh),i*(tilewh))
        if l_terrain[i][j]=="b":
            l_boulders.append(Boulder(j*(tilewh),i*(tilewh)))
        if l_terrain[i][j]=="g":
            l_gems.append(Diamond(j*(tilewh),i*(tilewh),False))
class Button:
    def __init__(s,x,y,img,purpose):
        s.x=x
        s.y=y
        s.img=loaded[img]
        s.purpose=purpose
    def draw(s):
        window.blit(s.img,(s.x,s.ys))

def background(img):
    window.blit(img,(0,0))
A_for_player=False

px=((WIDTH/2)/tilewh)*tilewh
py=((HEIGHT/2)/tilewh)*tilewh
prozor=1
offsety=((((HEIGHT/2)/tilewh)*tilewh)-player.y)
offsetx=((((WIDTH/2)/tilewh)*tilewh)-player.x)
player.x=((WIDTH/2)/tilewh)*tilewh
player.y=((HEIGHT/2)/tilewh)*tilewh
fps = []
while True:
    if prozor==1:
        window.fill("Black")
        keys = pygame.key.get_pressed()
        events = pygame.event.get()
        mouseState = pygame.mouse.get_pressed()
        mousePos = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.QUIT:
                break
            if event.type == pygame.JOYBUTTONDOWN:
                if pygame.joystick.get_count()>0:
                    if event.button==0 and keys[pygame.K_q]==False:
                        A_for_player=True
            if event.type==pygame.JOYBUTTONUP:
                if pygame.joystick.get_count()>0:
                    if event.button==0:
                        A_for_player=False
        if keys[pygame.K_q]:
            A_for_player=True
        for i in range(len(l_boulders)):
            l_boulders[i].move(l_terrain)
        indexdelete=0
        for i in range(len(l_boulders)):
            if l_boulders[indexdelete].alive==False:
                del l_boulders[indexdelete]
                indexdelete-=1
            indexdelete+=1
        elapsed_time += clock.get_time()

        if elapsed_time >= 1000:
            #secondpassed
            bar.timer=bar.change_t()
            seconds+=1
            elapsed_time -= 1000
        if player.time<=0:
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
                    indexpre1=int(player.y/(tilewh)-((offsety/tilewh)))
                    indexpre2=int(player.x/(tilewh)-((offsetx/tilewh)))
                    preoffset=[offsetx,offsety]
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
                    l_terrain,goback=player.move(l_terrain,direction,A_for_player)
                    if goback:
                        offsetx=preoffset[0]
                        offsety=preoffset[1]
                    else:
                        player.time=15
            else:
                preoffset=[offsetx,offsety]
                went=False
                indexpre1=int(player.y/(tilewh)-offsety/tilewh)
                indexpre2=int(player.x/(tilewh)-offsetx/tilewh)
                if keys[pygame.K_d]:
                    offsetx-=camera_speed
                    went=True
                    direction=1
                elif keys[pygame.K_s]:
                    offsety-=camera_speed
                    went=True
                    direction=4
                elif keys[pygame.K_a]:
                    offsetx+=camera_speed
                    went=True
                    direction=3
                elif keys[pygame.K_w]:
                    direction=2
                    offsety+=camera_speed
                    went=True
                if went==True:
                    l_terrain,goback=player.move(l_terrain,direction,A_for_player)
                    if goback:
                        offsetx=preoffset[0]
                        offsety=preoffset[1]
                    else:
                        player.time=15
        
        if keys[pygame.K_ESCAPE]:
            break
        if keys[pygame.K_UP]:
            cameray+=camera_speed/5
        if keys[pygame.K_DOWN]:
            cameray-=camera_speed/5
        if keys[pygame.K_RIGHT]:
            camerax-=camera_speed/5
        if keys[pygame.K_LEFT]:
            camerax+=camera_speed/5
        
        
        
        
        
        
        
        
        
        if player.time>-6:
            player.time-=1
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
        terrain.draw(l_terrain)
        bar.general()
    if prozor==0:
        window.fill("Black")
        background(loaded[6])
        keys = pygame.key.get_pressed()
        events = pygame.event.get()
        mouseState = pygame.mouse.get_pressed()
        mousePos = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.QUIT:
                break
        if keys[pygame.K_ESCAPE]:
            break
    if prozor==-1:
        window.fill("Black")
        die()
        keys = pygame.key.get_pressed()
        events = pygame.event.get()
        mouseState = pygame.mouse.get_pressed()
        mousePos = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.QUIT:
                break
        if keys[pygame.K_ESCAPE]:
            break
        if deathtime>0:
            deathtime-=1
        else:
            prozor=0
            deathtime=300
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