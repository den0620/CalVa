import random
#==========
def CreateField(Width,Height):
    Field=[]
    for i in range(0,Width):
        Field.append([0]*Height)
    return(Field)
#==========
def FindSpace(Field,Width,Height):
    for x in range(0,Width):
        for y in range(0,Height):
            if Field[x][y]==0: return(True)
    return(False)
#==========
def GenerateNumber(Field,Width,Height):
    IsFreeSpace=FindSpace(Field,Width,Height)
    x=random.randint(0,Width-1)
    y=random.randint(0,Height-1)
    while Field[x][y]!=0 and IsFreeSpace:
        x=random.randint(0,Width-1)
        y=random.randint(0,Height-1)
    if IsFreeSpace:
        Field[x][y]=2
    return(Field)
#==========
def Move(Field,Direction,Width,Height):
    if Direction=='up':
        for i in range(0,Height):
            for RowIndex in range(0,Width):
                for NumIndex in range(0,Height-1):
                    if Field[RowIndex][NumIndex]==0 and Field[RowIndex][NumIndex+1]!=0: Field[RowIndex][NumIndex],Field[RowIndex][NumIndex+1]=Field[RowIndex][NumIndex+1],0
                    elif Field[RowIndex][NumIndex]==Field[RowIndex][NumIndex+1] and Field[RowIndex][NumIndex]!=0: Field[RowIndex][NumIndex+1],Field[RowIndex][NumIndex]=0,Field[RowIndex][NumIndex]*2
    if Direction=='down':
        for i in range(0,Height):
            for RowIndex in range(0,Width):
                for NumIndex in range(Height-1,0,-1):
                    if Field[RowIndex][NumIndex]==0 and Field[RowIndex][NumIndex-1]!=0: Field[RowIndex][NumIndex],Field[RowIndex][NumIndex-1]=Field[RowIndex][NumIndex-1],0
                    elif Field[RowIndex][NumIndex]==Field[RowIndex][NumIndex-1] and Field[RowIndex][NumIndex]!=0: Field[RowIndex][NumIndex-1],Field[RowIndex][NumIndex]=0,Field[RowIndex][NumIndex]*2
    if Direction=='left':
        for i in range(0,Width):
            for NumIndex in range(0,Height):
                for RowIndex in range(0,Width-1):
                    if Field[RowIndex][NumIndex]==0 and Field[RowIndex+1][NumIndex]!=0: Field[RowIndex][NumIndex],Field[RowIndex+1][NumIndex]=Field[RowIndex+1][NumIndex],0
                    elif Field[RowIndex][NumIndex]==Field[RowIndex+1][NumIndex] and Field[RowIndex][NumIndex]!=0: Field[RowIndex+1][NumIndex],Field[RowIndex][NumIndex]=0,Field[RowIndex][NumIndex]*2
    if Direction=='right':
        for i in range(0,Width):
            for NumIndex in range(0,Height):
                for RowIndex in range(Width-1,0,-1):
                    if Field[RowIndex][NumIndex]==0 and Field[RowIndex-1][NumIndex]!=0: Field[RowIndex][NumIndex],Field[RowIndex-1][NumIndex]=Field[RowIndex-1][NumIndex],0
                    elif Field[RowIndex][NumIndex]==Field[RowIndex-1][NumIndex] and Field[RowIndex][NumIndex]!=0: Field[RowIndex-1][NumIndex],Field[RowIndex][NumIndex]=0,Field[RowIndex][NumIndex]*2
    return(Field)
