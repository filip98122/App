from General_info import *
timeslist=[
[19,255],
[18,255],
[34,127],
[23,510],
[0,255]
]

levels=len(timeslist)
level=1
l_level=[]
def adder(list,filename):
    f=open(filename)
    listoflists=[]
    lines=f.readlines()
    for i in range(len(lines)):
        linestr=lines[i].strip()
        line=[]
        for j in range(len(linestr)):
            line.append(str(linestr[j]))
        listoflists.append(line)
    list.append(listoflists)
    f.close()
    return list

def writeintxt(list,filename):
    f=open(filename,"w")
    for i in range(len(list)):
        for j in range(len(list[i])):
            f.write(list[i][j])
        if i!=len(list)-1:
            f.write("\n")
    f.close()



for i in range(levels):
    filenamestr=f"levels/map{i+1}.txt"
    listfor=adder(timeslist[i],filenamestr)

    l_level.append(listfor)
l_terrain=copy.deepcopy(l_level[level-1][2])
