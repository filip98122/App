from loader import *
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

char ="!#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"

def read():
    info=end()
    return info

def write(info):
    info={'diamonds': 0, 'username': '',}
    ens(info)



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
l_terrain=[
    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww",
    "wddddddddddddgdddddddddddddddddddddddddddddddddddddddddddddddddddddddw",
    "wddgdgdddgdddgdddddddddddddgggddddgdddddddggddddgddgdddddddddddddddddw",
    "wddgggdddgdddddddddddddddddgddgddgdgdddddgddgdddgdgddddddddddddddddddw",
    "wddgdgdddgdddbd     dddddddgggddgdddgddddgddddddggdddddddddddddddddddw",
    "wddddddpbdddddd     dddddddggdddgdddgddddgddddddggdddddddddddddddddddw",
    "wdddddddddddddd     dddddddgdgdddgdgdddddgddgdddgdgddddddddddddddddddw",
    "wdddddddddddddd     dddddddgddgdddgdddddddggddddgddgdddddddddddddddddw",
    "wddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddw",
    "wddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddw",
    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww"
]
vremepre=time.time()
najvecivreme=0
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
                
                if l_terrain[i][j]=="p":
                    window.blit(s.img,(j*(HEIGHT/9)+((HEIGHT/9-HEIGHT/12)/2),i*(HEIGHT/9)))
                else:
                    if j*(HEIGHT/9)+offsetx>-1+-HEIGHT/9 and j*(HEIGHT/9)+offsetx<WIDTH and i*(HEIGHT/9)+offsety>-1+-HEIGHT/9 and i*(HEIGHT/9)+offsety<=HEIGHT and s.img!="":
                        window.blit(s.img,(j*(HEIGHT/9)+offsetx,i*(HEIGHT/9)+offsety))
if pygame.joystick.get_count()>0:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
diamonds=0
terrain=Terrain()
offsetx=0
offsety=0
camera_speed=HEIGHT/9
between=0
SVAKIH30=0
class Player:
    def __init__(s,x,y):
        s.x=x
        s.y=y
    def move(s,map):
        global diamonds
        terraincheck=map[int(s.y/(HEIGHT/9)-(offsety/(HEIGHT/9)))][int(s.x/(HEIGHT/9)-offsetx/(HEIGHT/9))]
        goback=True
        if terraincheck=="d" or terraincheck==" ":
            map[int(s.y/(HEIGHT/9)-(offsety/(HEIGHT/9)))] = replace_at(map[int(s.y/(HEIGHT/9)-(offsety/(HEIGHT/9)))], [int(s.x/(HEIGHT/9)-offsetx/(HEIGHT/9))], " ")
            goback=False
        if terraincheck=="g":
            diamonds+=1
            goback=False
            map[int(s.y/(HEIGHT/9)-(offsety/(HEIGHT/9)))] = replace_at(map[int(s.y/(HEIGHT/9)-(offsety/(HEIGHT/9)))], [int(s.x/(HEIGHT/9)-offsetx/(HEIGHT/9))], " ")
        return map,goback
def replace_at(s, index, new_char):
    return s[:index[0]] + new_char + s[index[0]+1:]


for i in range(len(l_terrain)):
    for j in range(len(l_terrain[i])):
        if l_terrain[i][j]=="p":
            player=Player(j*(HEIGHT/9),i*(HEIGHT/9))





while True:
    window.fill("Black")
    keys = pygame.key.get_pressed()
    events = pygame.event.get()
    mouseState = pygame.mouse.get_pressed()
    mousePos = pygame.mouse.get_pos()
    for event in events:
        if event.type == pygame.QUIT:
            break
        if between<=0:
                
                x = joystick.get_axis(0)
                y = joystick.get_axis(1)  # Invert Y for normal coordinate system

                magnitude = math.hypot(x, y)
                if magnitude > 0.2:  # Deadzone to avoid jitter
                    angle = math.degrees(math.atan2(-y, x))
                    angle%=360
                    preoffset=[offsetx,offsety]
                    if angle<=45 or angle>315:
                        offsetx-=camera_speed
                    elif angle>45 and angle<=135:
                        offsety+=camera_speed
                    elif angle<=225 and angle>135:
                        offsetx+=camera_speed
                    else:
                        offsety-=camera_speed
                    between=12
                    l_terrain,goback=player.move(l_terrain)
                    if goback:
                        offsetx=preoffset[0]
                        offsety=preoffset[1]
    if keys[pygame.K_ESCAPE]:
        break
    if between>0:
        between-=1
    terrain.draw(l_terrain)
    if keys[pygame.K_b]:
        breakpoint()
        
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