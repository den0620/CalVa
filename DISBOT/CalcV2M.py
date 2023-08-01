import random
#начало калькулятора
def calculatorv2(N):
    ANSWERS=['Да','Нет','Да нет','Вроде','Может','Точно','Точно нет','Не знаю']
    h=random.randint(-9,47)
    c=f'Ввод неверный ваш IQ={h}'
    if N.rfind('?')!=-1:
        N=str(N)+'&'
        ANSWER=random.choice(ANSWERS)
        if ANSWER=='Да' or ANSWER=='Вроде' or ANSWER=='Может' or ANSWER=='Точно':
            c=str(N)+str(ANSWER)+'&'+'0x3ae47b'
        elif ANSWER=='Нет' or ANSWER=='Да нет' or ANSWER=='Точно нет':
            c=str(N)+str(ANSWER)+'&'+'0xe83030'
        elif ANSWER=='Не знаю':
            c=str(N)+str(ANSWER)+'&'+'0xf4ec0b'
    elif N.rfind('=')!=-1:
        a,b=map(str,N.split('='))
        a=a.replace('-','')
        b=b.replace('-','')
        if a[::-1]==b or a==b:
            c='Верно'
        else:
            c='Схуяли'
    elif N.rfind('+')!=-1:
        a,b=map(str,N.split('+'))
        c=a+b
    elif N.rfind('^')!=-1:
        a,b=map(str,N.split('^'))
        try:
            c=''
            a=int(float(a))
            b=float(b)
            if int(b)>=1:
                c=str(a)
                for i in range(1,int(b)):
                    c=str(c)*int(a)
                if c=='':
                    c=float(b)
            elif float(b)<0:
                for i in range(0,abs(int(b))):
                    c=str(c)+str(a)*len(str(a))
                c='-0'+'.'+str(c)
            else:
                c='Функция V для кого обалдуй'
        except:
            avg=0
            for i in b:
                avg=avg+ord(i)
            avg=avg//len(b)
            ans=''
            for i in range(0,avg):
                ans=ans+str(a)
            length=len(ans)//256
            c=''
            if length>0:
                for i in range(0,252):
                    c=c+ans[i]
                c+='...'
            else:
                c=ans
    elif N.rfind('V')!=-1:
        N=' '+str(N)
        b,a=map(str,N.split('V'))
        if b==' ':
            b=1
        else:
            b=int(float(b))-1
        OA=''
        for i in a:
            if OA.rfind(i)==-1:
                OA=str(OA)+str(i)
        if len(a)==int(float(OA))**b:
            c=OA
        else:
            c=float(int(float(a))*int(float(OA))%1000)/100
        if float(a)<0:
            c=str(abs(float(a))**0.5)+'i'
    elif N.rfind('-')!=-1:
        a,b=map(str,N.split('-'))
        if len(a)>len(b):
            h=0
            c=''
            for i in a:
                if h>=len(a)-len(b):
                    break
                c+=i
                h+=1
            c+=str(b)
        elif len(b)>len(a):
            h=0
            c=''
            for i in b:
                if h>=len(b)-len(a):
                    break
                c+=i
                h+=1
            c='-'+str(c)+str(a)
        elif len(a)==len(b):
            c=0
    elif N.rfind('*')!=-1:
        if N.rfind(']')!=-1:
            a0,b0=map(str,N.split('*'))
            if a0.rfind(']')!=-1 and b0.rfind(']')!=-1:
                a0=a0.replace(']','')
                b0=b0.replace(']','')
                z,a=map(int,a0.split('['))
                z,b=map(int,b0.split('['))
                c=a*b
            elif b0.rfind(']')==-1:
                a0=a0.replace(']','')
                z,a=map(float,a0.split('['))
                b0==float(b0)
                if float(b0)==float(0):
                    c=a
                else:
                    c=0
            elif a0.rfind(']')==-1:
                b0=b0.replace(']','')
                z,b=map(float,b0.split('['))
                if float(a0)==float(0):
                    c=b
                else:
                    c=0
        elif N.rfind(']')==-1:
            try:
                a,b=map(float,N.split('*'))
                if int(a)==a:
                    a=int(a)
                c=str(a)*int(b)
            except:
                a,b=map(str,N.split('*'))
                try:
                    c=str(a)*int(b)
                except:
                    avg=0
                    for i in b:
                        avg=avg+ord(i)
                    avg=int(avg)//len(b)
                    ans=str(a)*int(avg)
                    c=''
                    if len(ans)>255:
                        for i in range(0,252):
                            c=c+ans[i]
                        c=str(c)+str('...')
                    else:
                        c=ans
    elif N.rfind('/')!=-1:
        a,b=map(str,N.split('/'))
        b=float(b)
        a=float(a)
        if int(a)==a:
            a=int(a)
        if int(b)==b:
            b=int(b)
        if b==0:
            c='0['+str(a)+']'
        else:
            c=len(str(a))/len(str(b))+((int(a)*5.3/(int(b)/2))%10)/10
            if int(c)==int(b):
                c=int(c)
    elif N.rfind(':')!=-1:
        a,b=map(str,N.split(':'))
        b=float(b)
        a=float(a)
        if int(a)==a:
            a=int(a)
        if int(b)==b:
            b=int(b)
        if b==0:
            c='0['+str(a)+']'
        else:
            c=len(str(a))/len(str(b))+((int(a)*5.3/(int(b)/2))%10)/10
            if int(c)==int(b):
                c=int(c)
    return(c)

#конец