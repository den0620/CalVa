import random
#начало сапера
def MineSweeper(Width,Height,Bombs):
    if Bombs>Width*Height:
        return('Головой подумой дитя афгана')
    else:
        Field=[]
        for i in range(0,Height):
            Field.append([0]*Width)
        #генерация бомб и цифр рядом
        for h in range(0,Bombs):
            i=random.randint(0,Height-1)
            j=random.randint(0,Width-1)
            while Field[i][j]=='B':
                i=random.randint(0,Height-1)
                j=random.randint(0,Width-1)
            Field[i][j]='B'
            for m in range(i-1,i+2):
                for n in range(j-1,j+2):
                    try:
                        if m>-1 and n>-1:
                            Field[m][n]+=1
                    except:
                        None
        #опрозрачивание цифр рядом с 0
        for i in range(0,Height):
            for j in range(0,Width):
                try:
                    if Field[i][j]%100==0:
                        for m in range(i-1,i+2):
                            for n in range(j-1,j+2):
                                try:
                                    if m>-1 and n>-1:
                                        Field[m][n]+=100
                                except:
                                    None
                except:
                    None
        #перевод из цифр в эмодзи
        FinalField=''
        for i in range(0,Height):
            for j in range(0,Width):
                SP=''
                if Field[i][j]=='B' or Field[i][j]<100:
                    SP='||'
                else:
                    Field[i][j]=Field[i][j]%100
                if Field[i][j]=='B':
                    Field[i][j]=f'{SP}:bomb:{SP}'
                elif Field[i][j]==0:
                    Field[i][j]=f'{SP}:o2:{SP}'
                elif Field[i][j]==1:
                    Field[i][j]=f'{SP}:one:{SP}'
                elif Field[i][j]==2:
                    Field[i][j]=f'{SP}:two:{SP}'
                elif Field[i][j]==3:
                    Field[i][j]=f'{SP}:three:{SP}'
                elif Field[i][j]==4:
                    Field[i][j]=f'{SP}:four:{SP}'
                elif Field[i][j]==5:
                    Field[i][j]=f'{SP}:five:{SP}'
                elif Field[i][j]==6:
                    Field[i][j]=f'{SP}:six:{SP}'
                elif Field[i][j]==7:
                    Field[i][j]=f'{SP}:seven:{SP}'
                elif Field[i][j]==8:
                    Field[i][j]=f'{SP}:eight:{SP}'
                FinalField+=Field[i][j]
            FinalField+='\n'
        return(FinalField)
#Конец сапера
