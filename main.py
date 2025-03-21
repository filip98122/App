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
    "wwwwwwwwwwwwwwww",
    "wddddddddddddgdw",
    "wddddddddddddgdw",
    "wddddddddddddgdw",
    "wddddddddddddgdw",
    "wddddddpbddddddw",
    "wddddddddddddddw",
    "wddddddddddddddw",
    "wddddddddddddddw",
    "wddddddddddddddw",
    "wwwwwwwwwwwwwwww"
]

class Terrain:
    def draw(s, map):
        for i in range(len(l_terrain)):
            for j in range(len(l_terrain[i])):
                if l_terrain[i][j]=="d":
                    s.img=pygame.transform.scale(loaded[1],(HEIGHT/9,HEIGHT/9))
                if l_terrain[i][j]=="p":
                    s.img=pygame.transform.scale(loaded[0],(HEIGHT/12,HEIGHT/9))
                if l_terrain[i][j]=="b":
                    s.img=pygame.transform.scale(loaded[2],(HEIGHT/9,HEIGHT/9))
                if l_terrain[i][j]=="w":
                    s.img=pygame.transform.scale(loaded[3],(HEIGHT/9,HEIGHT/9))
                if l_terrain[i][j]=="g":
                    s.img=pygame.transform.scale(loaded[4],(HEIGHT/9,HEIGHT/9))
                
                if l_terrain[i][j]=="p":
                    window.blit(s.img,(j*(HEIGHT/9)+((HEIGHT/9-HEIGHT/12)/2),i*(HEIGHT/9)))
                else:
                    window.blit(s.img,(j*(HEIGHT/9)+((HEIGHT/9-HEIGHT/12)/2),i*(HEIGHT/9)))
terrain=Terrain()
        
while True:
    window.fill("Black")
    keys = pygame.key.get_pressed()
    events = pygame.event.get()
    mouseState = pygame.mouse.get_pressed()
    mousePos = pygame.mouse.get_pos()
    for event in events:
        if event.type == pygame.QUIT:
            break
    if keys[pygame.K_ESCAPE]:
        break
    terrain.draw(l_terrain)
    pygame.display.update()
    clock.tick(60)