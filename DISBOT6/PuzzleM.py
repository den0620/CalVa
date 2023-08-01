import random


def CreateField(Width,Height):
    Field = [[j+Width*i+1 for j in range(0,Width)] for i in range(0, Height)]
    Field[-1][-1]=0
    return (Field)


def GetPossibleMoves(Field):
    for ind1,row in enumerate(Field):
        if 0 in row:
            ind2=row.index(0)
            break
    points={}
    #-------------------------\\
    if ind1-1!=-1: points['up']=(ind1-1,ind2)
    else: points['up']=None

    if ind1<len(Field)-1: points['down']=ind1+1,ind2
    else: points['down']=None

    if ind2-1!=-1: points['left']=(ind1,ind2-1)
    else: points['left']=None

    if ind2<len(Field[0])-1: points['right']=(ind1,ind2+1)
    else: points['right']=None
    #-------------------------//
    points['space']=ind1,ind2
    return points


def Reverse(Dir):
    if Dir:
        lst1,lst2=['up','down','left','right'],['down','up','right','left']
        return lst2[lst1.index(Dir)]


def Randomize(Field,Samples):
    Dirs=['up','down','left','right']
    PrevMove=None
    for cycle in range(0,Samples):
        Rand=random.randint(0,3)
        PosWaysRand=GetPossibleMoves(Field)[Dirs[Rand]]
        while PosWaysRand==None or PosWaysRand==Reverse(PrevMove):
            Rand=random.randint(0,3)
            PosWaysRand = GetPossibleMoves(Field)[Dirs[Rand]]
        Field,PrevMove=MoveSpace(Field,GetPossibleMoves(Field),Dirs[Rand]),Dirs[Rand]
    return Field
    ...


def MoveSpace(Field,PossibleMoves,Direction):
    if Direction=='up':
        if PossibleMoves['up'] != None:
            Field[PossibleMoves['up'][0]][PossibleMoves['up'][1]], Field[PossibleMoves['space'][0]][
                PossibleMoves['space'][1]] = Field[PossibleMoves['space'][0]][PossibleMoves['space'][1]], \
                                             Field[PossibleMoves['up'][0]][PossibleMoves['up'][1]]
    elif Direction=='down':
        if PossibleMoves['down'] != None:
            Field[PossibleMoves['down'][0]][PossibleMoves['down'][1]], Field[PossibleMoves['space'][0]][
                PossibleMoves['space'][1]] = Field[PossibleMoves['space'][0]][PossibleMoves['space'][1]], \
                                             Field[PossibleMoves['down'][0]][PossibleMoves['down'][1]]
    elif Direction=='left':
        if PossibleMoves['left'] != None:
            Field[PossibleMoves['left'][0]][PossibleMoves['left'][1]], Field[PossibleMoves['space'][0]][
                PossibleMoves['space'][1]] = Field[PossibleMoves['space'][0]][PossibleMoves['space'][1]], \
                                             Field[PossibleMoves['left'][0]][PossibleMoves['left'][1]]
    elif Direction=='right':
        if PossibleMoves['right'] != None:
            Field[PossibleMoves['right'][0]][PossibleMoves['right'][1]], Field[PossibleMoves['space'][0]][
                PossibleMoves['space'][1]] = Field[PossibleMoves['space'][0]][PossibleMoves['space'][1]], \
                                             Field[PossibleMoves['right'][0]][PossibleMoves['right'][1]]
    return Field