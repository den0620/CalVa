import discord,os,asyncio,time,random,subprocess,ffmpeg,json
import yt_dlp as youtube_dl

from discord import FFmpegPCMAudio
from discord.ext.commands import Bot
from discord.ext import commands
import requests as req

import MineSweeperM
import ASCIIM
import CalcV2M

PREF='$'
SCline=1
SCStatus=2
intents = discord.Intents().all()

#массив хентая
HENTAILIST=['https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/2017_Rally_Portugal_-_5.jpg/1200px-2017_Rally_Portugal_-_5.jpg','https://www.wrc.com/images/redaktion/Season-2020-NEWS/WRC/6_June/160620_-World-OttTanak-Mexico-2020_001_a7795_frz_1400x788.jpg','https://img.colleconline.com/artefactimgopt/54ae3de57a77435e81d4f0ab2563852d/modeles-reduits-voitures-2018-hyundai-i20-coupe-wrc-n-5-96672ced-800.webp','https://oracle.newpaltz.edu/wp-content/uploads/2020/10/01119013_077.jpg','https://cdn-1.motorsport.com/images/amp/0a9pQdr0/s1000/ott-tanak-martin-jarveoja-hyun.jpg','https://www.hyundai.cz/common/gfx/responsive-design/models/main-banner/main_car_wrc_overview_mobile.jpg','https://sport-auto.ch/wp-content/uploads/2019/08/50ed2767-67ea-4bff-ab4a-f9b140f85fe6.jpg']
#конец

client = discord.Client()
client = commands.Bot(command_prefix=PREF,intents=discord.Intents.all())

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='хентай'))
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):

    global SCline
    global SCStatus
    def GetCurStatus(SC):
        # +SocialCredits
        if -100<SC<200:
            return('Новичек')
        elif 200<=SC<400:
            return('Уже смешарик')
        elif 400<=SC<1000:
            return('Опытный')
        elif 1000<=SC<2000:
            return('Умный')
        elif 2000<=SC<4000:
            return('Гуру')
        elif 4000<=SC<7000:
            return('Натурал')
        elif 7000<=SC<12000:
            return('Мега натурал')
        elif 12000<=SC<20000:
            return('СУПЕР натурал')
        elif 20000<=SC<30000:
            return('ГИПЕР НАТУРАЛ')
        # -SocialCredits
        elif -300<SC<=-100:
            return('Глупый')
        elif -500<SC<=-300:
            return('Дурной')
        elif -1000<SC<=-500:
            return('Очумелый')
        elif -2000<SC<=-1000:
            return('Первобытник')
        else:
            return('Ограничение пробито')
            
    SCredits=['-5','-5','-5','-5','-5','-5','-5','-5','-5','-5','-5','-5','-5','-5','-5','-5','-5','-5','-5','-5','-5','-5','-5','-5','-5','-5','-5','-5','-5','-5','-5','-5',
              '-10','-10','-10','-10','-10','-10','-10','-10','-10','-10','-10','-10','-10','-10','-10','-10',
              '-15','-15','-15','-15','-15','-15','-15','-15',
              '-20','-20','-20','-20',
              '-30','-30',
              '-50',]
    KtoObser=['',' все знают, что',' известно, что']
    
    if message.author==client.user:
        return

    SCreditsADD=True
    SCreditsREM=False
    SCreditsDIF=None

    Input0=str(message.content)
    if message.content.startswith(PREF):
        if message.content.startswith(str(PREF)+'сервера') and str(message.author)=='den0620#5150':
            GuildList=''
            for guild in client.guilds:
                GuildList=GuildList+str(guild)+'\n'
            await message.channel.send(GuildList)
        elif message.content.startswith(str(PREF)+'profile') or message.content.startswith(str(PREF)+'Profile') or message.content.startswith(str(PREF)+'PROFILE') or message.content.startswith(str(PREF)+'профиль') or message.content.startswith(str(PREF)+'Профиль') or message.content.startswith(str(PREF)+'ПРОФИЛЬ'):
            try:
                MEMBER=message.mentions[0]
                MEMBERID=MEMBER.id
            except:
                MEMBER=message.author
                MEMBERID=MEMBER.id
            try:
                f=open(str(MEMBERID)+'INFO.dat','r')
                lines=f.readlines()
                f.close
                CurSCredits=lines[SCline-1]
                CurSCStatus=lines[SCStatus-1]
                embed=discord.Embed(title=f"Профиль {MEMBER}", description=f"ID: {MEMBERID}", color=0x93b2b4)
                embed.set_thumbnail(url=str(MEMBER.avatar_url))
                embed.add_field(name="Социальные кредиты:", value=f"{CurSCredits}", inline=False)
                embed.add_field(name="Статус:", value=f"{CurSCStatus}", inline=False)
                if int(MEMBERID)==int(968795473068560395):
                    embed.add_field(name="Характеристики хоста:", value="2C/4T Intel Core i3-6100 3700Mhz\nCrucial CT8G4DFS824A.M8FE x2 DDR4-2400 CL21\nOS Windows 10 Pro 64bit 19044", inline=False)
                embed.set_footer(text=f"Подробнее о получении Social Credits {PREF}SC help")
                await message.channel.send(embed=embed)
            except:
                await message.channel.send('''
```Пользователь еще не отправил ни одной команды```
''')
        elif message.content.startswith(str(PREF)+'SC help'):
            embed=discord.Embed(title='Руководство по Социальным кредитам',color=0xe63700)
            embed.add_field(name='Кредиты дают за:',value='Правильно введеные команды',inline=False)
            embed.add_field(name='Кредиты забирают за:',value='Неправильно введеные команды\nили ответы об ошибке',inline=False)
            embed.add_field(name='На кредиты не влияют:',value='Ответы "неправильный ввод" ссылающиеся на команды help',inline=False)
            embed.add_field(name="Награды:", value=f"От 20.000 Социальных кредитов\n-Статус ГИПЕР НАТУРАЛ\n-На вас не действует команда {PREF}кто", inline=False)
            await message.channel.send(embed=embed)
        elif message.content.startswith(str(PREF)+'кто') or message.content.startswith(str(PREF)+'Кто') or message.content.startswith(str(PREF)+'КТО'):
            AUTHOR=str(message.author)
            Input0=f'Trash{PREF}'+str(Input0)
            try:
                Trash,Obser=map(str,Input0.split(f'{PREF}кто '))
            except:
                try:
                    Trash,Obser=map(str,Input0.split(f'{PREF}Кто '))
                except:
                    Trash,Obser=map(str,Input0.split(f'{PREF}КТО '))
            try:
                Obser,Trash=map(str,Obser.split('?'))
            except:
                None
            MemberList=[]
            channel=message.channel
            for member in channel.members:
                MemberList.append(member)
            def proverka(OBOSRAN):
                global SCStatus
                try:
                    f=open(str(OBOSRAN.id)+'INFO.dat','r')
                    lines=f.readlines()
                    f.close()
                    CurSCredits,Trash=map(str,lines[SCline-1].split('\n'))
                    CurSCredits=int(CurSCredits)
                    if CurSCredits>=20000:
                        return('VIP')
                    else:
                        return(str(OBOSRAN))
                except:
                    return(str(OBOSRAN))
            neVIP=True
            while neVIP and len(MemberList)>0:
                OBOSRAN=random.choice(MemberList)
                if proverka(OBOSRAN)=='VIP':
                    MemberList.remove(OBOSRAN)
                else:
                    neVIP=False
            if len(MemberList)>0:
                await message.channel.send(f'{message.author.mention},{random.choice(KtoObser)} {Obser} - {OBOSRAN}')
            else:
                await message.channel.send('На сервере отсутствует {Obser}')
        elif message.content.startswith(str(PREF)+'MS') or message.content.startswith(str(PREF)+'ms') or message.content.startswith(str(PREF)+'Ms'):
            try:
                Trash,Input1=map(str,Input0.split('S '))
                Width,Height,Bombs=map(int,Input1.split(' '))
                if Width+Height<=50:
                    await message.channel.send(MineSweeperM.MineSweeper(Width,Height,Bombs))
                else:
                    await message.channel.send('''
```Поле слишком большое```
''')
                    SCreditsADD=False
                    SCreditsREM=True
            except:
                if Input0.rfind('help')!=-1 or Input0.rfind('Help')!=-1 or Input0.rfind('помощь')!=-1 or Input0.rfind('Помощь')!=-1:
                    embed=discord.Embed(title="MineSweeper генератор", description="Отправлю в ответ сапера", color=0xcac412)
                    embed.set_thumbnail(url="https://i.imgur.com/zQKDNYv.png")
                    embed.add_field(name=f"{PREF}MS help / {PREF}MS помощь", value="Отправлю это руководство", inline=False)
                    embed.add_field(name=f"{PREF}MS [ширина] [высота] [бомбы]", value='[ширина] - ширина поля в эмодзи\n (Если поле обрывается - закончилось допустимое кол-во эмодзи или спойлеров)\n [высота] - высота поля в эмодзи\n [бомбы] - кол-во бомб на поле', inline=False)
                    embed.set_footer(text="MineSweeper модифицированный 2.13")
                    await message.channel.send(embed=embed)
                else:
                    await message.channel.send(f'''
```diff
- Неверный ввод
Введите "{PREF}MS help" или "{PREF}MS помощь" для получения руководства по генератору```
''')
                    SCreditsADD=False
        elif message.content.startswith(str(PREF)+'music help') or message.content.startswith(str(PREF)+'Music Help') or message.content.startswith(str(PREF)+'MUSIC HELP') or message.content.startswith(str(PREF)+'помощь музыка') or message.content.startswith(str(PREF)+'Помощь Музыка') or message.content.startswith(str(PREF)+'ПОМОЩЬ МУЗЫКА'):
            embed=discord.Embed(title="Музыкальный плеер", description="Включу звук с видео на ютубе", color=0xff7b24)
            embed.set_thumbnail(url="https://i.imgur.com/iSN1F4I.png")
            embed.add_field(name=f"{PREF}music help / {PREF}помощь музыка", value="Отправлю это руководство", inline=False)
            embed.add_field(name=f"{PREF}play [URL] / {PREF}включи [URL]", value="Включить звук с видео по URL YouTube", inline=False)
            embed.add_field(name=f"{PREF}stop / {PREF}выключи", value="Выключу играющую музыку", inline=False)
            embed.add_field(name=f"{PREF}pause / {PREF}пауза", value="Поставлю играющую музыку на паузу", inline=False)
            embed.add_field(name=f"{PREF}resume / {PREF}продолжи", value="Сниму играющую музыку с паузы", inline=False)
            embed.add_field(name=f"{PREF}leave / {PREF}выйди", value="Выйду из ГС и выключу играющую музыку", inline=False)
            embed.add_field(name=f"#НЕРАБОТАЕТ {PREF}queue [URL] / {PREF}очередь [URL]", value="Добавлю видео в очередь",inline=False)
            embed.add_field(name=f"#НЕРАБОТАЕТ {PREF}skip / {PREF}пропусти", value="Пропущу играющую музыку", inline=False)
            embed.add_field(name=f"#НЕРАБОТАЕТ {PREF}loop / {PREF}повтор", value="Включу/Выключу повтор играющей музыки", inline=False)
            #                        /|\
            # ДОДЕЛАТЬ МУЗ КОМАНДЫ 3  |
            #                         |
            embed.set_footer(text="Плеер 0.8.9")
            await message.channel.send(embed=embed)
        elif message.content.startswith(str(PREF)+'music') or message.content.startswith(str(PREF)+'Music') or message.content.startswith(str(PREF)+'MUSIC') or message.content.startswith(str(PREF)+'музыка') or message.content.startswith(str(PREF)+'Музыка') or message.content.startswith(str(PREF)+'МУЗЫКА'):
            await message.channel.send(f'''
```diff
- Неверный ввод
Введите "{PREF}music help" или "{PREF}помощь музыка" для получения руководства по плееру```
''')
            SCreditsADD=False
        elif message.content.startswith(str(PREF)+'play') or message.content.startswith(str(PREF)+'Play') or message.content.startswith(str(PREF)+'PLAY') or message.content.startswith(str(PREF)+'включи') or message.content.startswith(str(PREF)+'Включи') or message.content.startswith(str(PREF)+'ВКЛЮЧИ'):
            MusicGo=True
            try:
                Trash,Url=map(str,Input0.split(' '))
            except:
                await message.channel.send(f'''
```diff
- Неверный ввод
Введите "{PREF}music help" или "{PREF}помощь музыка" для получения руководства по плееру```
''')
                SCreditsADD=False
                MusicGo=False
            if MusicGo:
                UserConnected=True
                try:
                    VoiceChannel=message.author.voice.channel
                    await VoiceChannel.connect()
                except:
                    try:
                        Voice=message.author.guild.get_member(client.user.id).voice.channel
                        if Voice==VoiceChannel:
                            Voice=discord.utils.get(client.voice_clients,guild=message.guild)
                            Voice.stop()
                        else:
                            Voice=discord.utils.get(client.voice_clients,guild=message.guild)
                            await Voice.disconnect()
                            await VoiceChannel.connect()
                    except:
                        UserConnected=False
                        await message.channel.send('''
```Вы не подключены к каналу```
''')
                        SCreditsREM=True
                        SCreditsADD=False
                Voice=discord.utils.get(client.voice_clients,guild=message.guild)        
                ydl_opts={'format':'bestaudio','noplaylist':True}
                FFMPEG_opts={'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
                if UserConnected:
                    try:
                        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                            info = ydl.extract_info(Url, download=False)
                            URL = info['formats'][5]['url']
                            ICON = info['thumbnail']
                            TITLE = info['title']
                            LENG = int(info['duration'])
                        Voice.play(discord.FFmpegPCMAudio(URL, **FFMPEG_opts))
                        LENGTH=time.strftime('%H:%M:%S', time.gmtime(LENG))
                        embed=discord.Embed(title=f"{TITLE}", url=f"{Url}", description=f"Продолжительность: {LENGTH}", color=0x33ad4f)
                        embed.set_author(name="Сейчас играет:")
                        embed.set_thumbnail(url=f"{ICON}")
                        await message.channel.send(embed=embed)
                        print(TITLE)
                    except:
                        await message.channel.send('''
```Недействительный URL```
''')
                        SCreditsREM=True
                        SCreditsADD=False
        elif message.content.startswith(str(PREF)+'leave') or message.content.startswith(str(PREF)+'Leave') or message.content.startswith(str(PREF)+'LEAVE') or message.content.startswith(str(PREF)+'выйди') or message.content.startswith(str(PREF)+'Выйди') or message.content.startswith(str(PREF)+'ВЫЙДИ'):
            Voice=discord.utils.get(client.voice_clients,guild=message.guild)
            try:
                await Voice.disconnect()
            except:
                await message.channel.send('''```
Не подключена к каналу```
''')
                SCreditsREM=True
                SCreditsADD=False
        elif message.content.startswith(str(PREF)+'pause') or message.content.startswith(str(PREF)+'Pause') or message.content.startswith(str(PREF)+'PAUSE') or message.content.startswith(str(PREF)+'пауза') or message.content.startswith(str(PREF)+'Пауза') or message.content.startswith(str(PREF)+'ПАУЗА'):
            Voice=discord.utils.get(client.voice_clients,guild=message.guild)
            try:
                Voice.pause()
                await message.channel.send('''
```Музыка на паузе```
''')
                SCreditsADD=False
                SCreditsADD=False
            except:
                await message.channel.send('''
```Ничего не играет```
''')
                SCreditsREM=True
                SCreditsADD=False
        elif message.content.startswith(str(PREF)+'resume') or message.content.startswith(str(PREF)+'Resume') or message.content.startswith(str(PREF)+'RESUME') or message.content.startswith(str(PREF)+'продолжи') or message.content.startswith(str(PREF)+'Продолжи') or message.content.startswith(str(PREF)+'ПРОДОЛЖИ'):
            Voice=discord.utils.get(client.voice_clients,guild=message.guild)
            try:
                Voice.resume()
                await message.channel.send('''
```Музыка продолжается```
''')
                SCreditsADD=False
                SCreditsADD=False
            except:
                await message.channel.send('''
```Музыка не на паузе```
''')
                SCreditsREM=True
                SCreditsADD=False
        elif message.content.startswith(str(PREF)+'stop') or message.content.startswith(str(PREF)+'Stop') or message.content.startswith(str(PREF)+'STOP') or message.content.startswith(str(PREF)+'выключи') or message.content.startswith(str(PREF)+'Выключи') or message.content.startswith(str(PREF)+'ВЫКЛЮЧИ'):
            Voice=discord.utils.get(client.voice_clients,guild=message.guild)
            try:
                Voice.stop()
                await message.channel.send('''
```Музыка выключена```
''')
                SCreditsADD=False
                SCreditsADD=False
            except:
                await message.channel.send('''
```Бот не подключен или ничего не играет```
''')
        elif Input0.rfind('?')!=-1:
            Input0='trash'+str(Input0)
            Trash,Input1=Input0.split(PREF)
            QueAnsCol=CalcV2M.calculatorv2(Input1)
            que,ans,col=map(str,QueAnsCol.split('&'))
            if col=='0x3ae47b':
                embed=discord.Embed(title=ans,description=que,color=0x3ae47b)
                embed.set_thumbnail(url='https://static5.depositphotos.com/1029663/395/i/600/depositphotos_3955476-stock-photo-green-check-mark.jpg')
            elif col=='0xf4ec0b':
                embed=discord.Embed(title=ans,description=que,color=0xf4ec0b)
                embed.set_thumbnail(url='https://www.seekpng.com/png/full/49-493201_atlanta-air-conditioning-sunglasses-fun-fixed-smiling-thumbs.png')
            else:
                embed=discord.Embed(title=ans,description=que,color=0xe83030)
                embed.set_thumbnail(url='https://avatarko.ru/img/kartinka/5/chelovechek_4172.jpg')
            await message.channel.send(embed=embed)
        elif Input0.rfind('ASCII')!=-1:
            #Первая попытка
            try:
                TRASH,NEW_WIDTH,URL=map(str,Input0.split(' '))
                if NEW_WIDTH<=150:
                    await message.channel.send('''
```Ширина слишком большая```
''')
                AsciiImg=ASCIIM.ASCII(NEW_WIDTH,URL)
                await message.channel.send(f'''
```{AsciiImg}```
''')
                print(AsciiImg)
            except:
                #2 сообщения с рисунком
                try:
                    #Высота сообщения в строках
                    leng=(len(AsciiImg)+1)
                    AsciiImg1=AsciiImg[0:leng//2]
                    AsciiImg1=AsciiImg1[0:((len(AsciiImg1)+1)-(int(NEW_WIDTH)+2))]
                    AsciiImg2=AsciiImg[leng//2:]
                    AsciiImg2=AsciiImg2[(0+(int(NEW_WIDTH)+2)):]
                    await message.channel.send(f'''
```{AsciiImg1}```
''')
                    await message.channel.send(f'''
```{AsciiImg2}```
''')
                except:
                    try:
                        #3 сообщения с рисунком
                        AsciiImg1=AsciiImg[0:leng//3]
                        AsciiImg1=AsciiImg1[0:((len(AsciiImg1)+1)-(int(NEW_WIDTH)+2))]
                        AsciiImg2=AsciiImg[leng//3:(2*leng//3)]
                        AsciiImg2=AsciiImg2[(0+(int(NEW_WIDTH)+2)):(len(AsciiImg2)-(int(NEW_WIDTH)+2))]
                        AsciiImg3=AsciiImg[(2*leng//3):]
                        AsciiImg3=AsciiImg3[(0+(int(NEW_WIDTH)+2)):]
                        await message.channel.send(f'''
```
{AsciiImg1}```
''')
                        await message.channel.send(f'''
```
{AsciiImg2}```
''')
                        await message.channel.send(f'''
```
{AsciiImg3}```
''')
                    except:
                        if Input0.rfind('help')!=-1 or Input0.rfind('Help')!=-1 or Input0.rfind('помощь')!=-1 or Input0.rfind('Помощь')!=-1:
                            embed=discord.Embed(title="ASCII арт генератор", description="Отправлю в ответ картинку из символов", color=0x1fc6ef)
                            embed.set_thumbnail(url="https://i.imgur.com/uc4CH2A.png")
                            embed.add_field(name=f"{PREF}ASCII help / {PREF}ASCII помощь", value="Отправлю это руководство", inline=False)
                            embed.add_field(name=f"{PREF}ASCII [ширина] [url]", value='[ширина] - ширина арта в символах\n (Если отвечает "Неверный ввод", но все верно - уменьшите ширину)\n [url] - ссылка на изображение\n Деление сообщения происходит из-за ограничения дискордом отправки сообщения до 4000 символов\n (текущий максимум - 3 сообщшения)', inline=False)
                            embed.set_footer(text="ASCII_IMG модифицированный 3.2")
                            await message.channel.send(embed=embed)
                        else:
                            await message.channel.send(f'''
```diff
- Неверный ввод
Введите "{PREF}ASCII help" или "{PREF}ASCII помощь" для получения руководства по генератору```
''')
                            SCreditsADD=False
        elif Input0.rfind('RND')!=-1:
            try:
                TRASH,FIRST,LAST=map(str,Input0.split(' '))
                await message.channel.send(f'''
```
{random.randint(int(FIRST),int(LAST))}```
''')
            except:
                try:
                    await message.channel.send(f'''
```
{random.randint(int(LAST),int(FIRST))}```
''')
                except:
                    if Input0.rfind('help')!=-1 or Input0.rfind('Help')!=-1 or Input0.rfind('помощь')!=-1 or Input0.rfind('Помощь')!=-1:
                        embed=discord.Embed(title="Генератор рандомных чисел", description="Отправлю рандомное число", color=0xc38dce)
                        embed.set_thumbnail(url="https://i.imgur.com/jVssOCD.jpg")
                        embed.add_field(name=f"{PREF}RND help / {PREF}RND помощь", value="Отправлю это руководство", inline=False)
                        embed.add_field(name=f"{PREF}RND [от] [до]", value='[от] - начальное число (включительно)\n [до] - конечное число (включительно)', inline=False)
                        embed.set_footer(text="RandomGenerator 0.2")
                        await message.channel.send(embed=embed)
                    else:
                        await message.channel.send(f'''
```diff
- Неверный ввод
Введите "{PREF}RND help" или "{PREF}RND помощь" для получения руководства по генератору```
''')
                    SCreditsADD=False
        elif message.content.startswith(str(PREF)+'help') or message.content.startswith(str(PREF)+'Help') or message.content.startswith(str(PREF)+'HELP') or message.content.startswith(str(PREF)+'помощь') or message.content.startswith(str(PREF)+'Помощь') or message.content.startswith(str(PREF)+'ПОМОЩЬ'):
            embed=discord.Embed(title='[Добавить бота]',url='https://discord.com/api/oauth2/authorize?client_id=968795473068560395&permissions=0&scope=bot',description=f'"{PREF}" - действительная приставка',color=0x3ae47b)
            embed.set_author(name='Написан den0620#5150 на Python 3.9.2', icon_url='https://cdn.discordapp.com/avatars/573799615074271253/8da4f16d28f9859f93a01634dbe35ba8.webp?size=1024')
            embed.set_thumbnail(url="https://i.imgur.com/NdTbysX.png")
            embed.add_field(name='"help" - список общих команд', value='Открою список команд', inline=False)
            embed.add_field(name='"profile" - ваш профиль', value='Покажу ваш профиль', inline=False)
            embed.add_field(name='"calc help" - список команд калькулятора', value='Открою calc список команд', inline=False)
            embed.add_field(name='"music help" - команды музыки', value='Открою список команд музыки', inline=False)
            embed.add_field(name=f'"RND" - рандом', value='Выведу рандомное число ({PREF}RND help)', inline=False)
            embed.add_field(name=f'"ASCII" - арт', value='Создам арт из символов ({PREF}ASCII help)', inline=False)
            embed.add_field(name=f'"MS" - сапер', value='Отправлю в чат сапера ({PREF}MS help)', inline=False)
            embed.add_field(name='"кто [кто-то]"', value='Ищу [кого-то] на сервере (вопросительный знак на усмотрение)', inline=False)
            embed.add_field(name='"hentai" - хентай', value='Скину картинку', inline=False)
            embed.set_footer(text='Текущая версия: 0.7.5')
            await message.channel.send(embed=embed)
        elif message.content.startswith(str(PREF)+'calc help') or message.content.startswith(str(PREF)+'Calc Help') or message.content.startswith(str(PREF)+'CALC HELP'):
            embed=discord.Embed(title='Команды калькулятора:',description='CalculatorV2',color=0xbdc7bc)
            embed.set_thumbnail(url="https://i.imgur.com/X6O5mep.png")
            embed.add_field(name='"+" - сложение', value='Сложу два числа', inline=False)
            embed.add_field(name='"-" - вычитание', value='Вычту из одного числа другое', inline=False)
            embed.add_field(name='"*" - умножение', value='Умножу одно число на другое', inline=False)
            embed.add_field(name='"/" или ":" - деление', value='Поделю одно число на другое', inline=False)
            embed.add_field(name='"^" - степень', value='Возведу одно число в степень другого', inline=False)
            embed.add_field(name='"V" - корень', value='Найду корень из числа', inline=False)
            embed.add_field(name='"=" - сравнение', value='Сравню два числа', inline=False)
            embed.set_footer(text='Текущая версия: 2.3.1')
            await message.channel.send(embed=embed)
        elif Input0.rfind('hentai')!=-1 or Input0.rfind('Hentai')!=-1 or Input0.rfind('хентай')!=-1 or Input0.rfind('Хентай')!=-1:
            await message.channel.send(random.choice(HENTAILIST))
        else:
            Input0='trash'+str(Input0)
            Trash,Input1=Input0.split(PREF)
            ANS=CalcV2M.calculatorv2(Input1)
            if str(ANS).rfind('IQ=')!=-1:
                SCreditsADD=False
                SCreditsREM=True
                SCreditsDIF=random.choice(SCredits)
                embed=discord.Embed(title=ANS,description='вы разочаровать партия', color=0xe83030)
                embed.set_thumbnail(url='https://i.redd.it/yuzfih87wts71.jpg')
                embed.set_footer(text=f'{SCreditsDIF} Social credits')
                await message.channel.send(embed=embed)
            else:
                embed=discord.Embed(title=ANS,color=0x3ae47b)
                await message.channel.send(embed=embed)
        if SCreditsDIF==None:
            SCreditsDIF=random.choice(SCredits)
        if SCreditsADD:
            if os.path.isfile('./'+str(message.author.id)+'INFO.dat'):
                None
            else:
                f=open(str(message.author.id)+'INFO.dat','w')
                f.close
            f=open(str(message.author.id)+'INFO.dat','r')
            lines=f.readlines()
            f.close
            try:
                CurSCredits=int(lines[SCline-1])
            except:
                lines=[0,'Новичек']
                CurSCredits=0
            try:
                NewSCredits=int(CurSCredits)-int(SCreditsDIF)
            except:
                NewSCredits=-int(SCreditsDIF)
            f=open(str(message.author.id)+'INFO.dat','w')
            lines[SCline-1]=NewSCredits
            #Статус
            CurStatus=GetCurStatus(NewSCredits)
            lines[SCStatus-1]=CurStatus
            #Конец статуса
            for line in lines:
                f.write(str(line)+'\n')
            f.close
        if SCreditsREM:
            if os.path.isfile('./'+str(message.author.id)+'INFO.dat'):
                None
            else:
                f=open(str(message.author.id)+'INFO.dat','w')
                f.close
            f=open(str(message.author.id)+'INFO.dat','r')
            lines=f.readlines()
            f.close
            try:
                CurSCredits=int(lines[SCline-1])
            except:
                lines=[0,'Новичек']
                CurSCredits=0
            try:
                NewSCredits=int(CurSCredits)+int(SCreditsDIF)
            except:
                NewSCredits=-int(SCreditsDIF)
            f=open(str(message.author.id)+'INFO.dat','w')
            lines[SCline-1]=NewSCredits
            #Статус
            CurStatus=GetCurStatus(NewSCredits)
            lines[SCStatus-1]=CurStatus
            #Конец статуса
            for line in lines:
                f.write(str(line)+'\n')
            f.close
            

t = open('TOKEN.env','r')
TOKEN=str(t.read())
client.run(TOKEN)
