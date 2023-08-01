import discord,os,asyncio,time,random,subprocess,ffmpeg,json
import yt_dlp as youtube_dl

from discord import FFmpegPCMAudio
from discord.ext.commands import Bot
from discord.ext import commands
import requests as req

import MineSweeperM
import ASCIIM
import CalcV2M
import MusicM

PREF='~'
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

    SCredits=['-5','-10','-15','-20','-25','-50','-100','-250','-500','-1,000','-5,000','-30,000,000']
    KtoObser=['',' все знают, что',' известно, что']
    
    if message.author==client.user:
        return
    
    Input0=str(message.content)
    if message.content.startswith(PREF):
        if message.content.startswith(str(PREF)+'сервера') and str(message.author)=='den0620#5150':
            GuildList=''
            for guild in client.guilds:
                GuildList=GuildList+str(guild)+'\n'
            await message.channel.send(GuildList)
        elif message.content.startswith(str(PREF)+'кто') or message.content.startswith(str(PREF)+'Кто') or message.content.startswith(str(PREF)+'КТО'):
            AUTHOR=str(message.author)
            Input0='Trash~'+str(Input0)
            try:
                Trash,Obser=map(str,Input0.split('~кто '))
            except:
                try:
                    Trash,Obser=map(str,Input0.split('~Кто '))
                except:
                    Trash,Obser=map(str,Input0.split('~КТО '))
            try:
                Obser,Trash=map(str,Obser.split('?'))
            except:
                None
            MemberList=[]
            channel=message.channel
            for member in channel.members:
                MemberList.append(str(member))
            try:
                MemberList.remove('den0620#5150')
            except:
                None
            MemberList.remove('CalVa#4915')
            if len(MemberList)>0:
                await message.channel.send(f'{message.author.mention},{random.choice(KtoObser)} {Obser} - {random.choice(MemberList)}')
            else:
                await message.channel.send('На сервере нету гея')
        elif message.content.startswith(str(PREF)+'MS') or message.content.startswith(str(PREF)+'ms') or message.content.startswith(str(PREF)+'Ms'):
            try:
                Trash,Input1=map(str,Input0.split('S '))
                Width,Height,Bombs=map(int,Input1.split(' '))
                await message.channel.send(MineSweeperM.MineSweeper(Width,Height,Bombs))
            except:
                if Input0.rfind('help')!=-1 or Input0.rfind('Help')!=-1 or Input0.rfind('помощь')!=-1 or Input0.rfind('Помощь')!=-1:
                    embed=discord.Embed(title="MineSweeper генератор", description="Отправлю в ответ сапера", color=0xcac412)
                    embed.set_thumbnail(url="https://i.imgur.com/zQKDNYv.png")
                    embed.add_field(name="~MS help / ~MS помощь", value="Отправлю это руководство", inline=False)
                    embed.add_field(name="~MS [ширина] [высота] [бомбы]", value='[ширина] - ширина поля в эмодзи\n (Если поле обрывается - закончилось допустимое кол-во эмодзи или спойлеров)\n [высота] - высота поля в эмодзи\n [бомбы] - кол-во бомб на поле', inline=False)
                    embed.set_footer(text="MineSweeper модифицированный 2.13")
                    await message.channel.send(embed=embed)
                else:
                    await message.channel.send('''
```diff
- Неверный ввод
Введите "~MS help" или "~MS помощь" для получения руководства по генератору```
''')
        elif message.content.startswith(str(PREF)+'music help') or message.content.startswith(str(PREF)+'Music Help') or message.content.startswith(str(PREF)+'MUSIC HELP') or message.content.startswith(str(PREF)+'помощь музыка') or message.content.startswith(str(PREF)+'Помощь Музыка') or message.content.startswith(str(PREF)+'ПОМОЩЬ МУЗЫКА'):
            embed=discord.Embed(title="Музыкальный плеер", description="Включу звук с видео на ютубе", color=0xff7b24)
            embed.set_thumbnail(url="https://i.imgur.com/iSN1F4I.png")
            embed.add_field(name="~music help / ~помощь музыка", value="Отправлю это руководство", inline=False)
            embed.add_field(name="~play", value='######', inline=False)
            #
            # ДОДЕЛАТЬ ПОМОЩЬ ПО МУЗ КОМАНДАМ
            #
            embed.set_footer(text="Плеер 0.7.2")
            await message.channel.send(embed=embed)
        elif message.content.startswith(str(PREF)+'music') or message.content.startswith(str(PREF)+'Music') or message.content.startswith(str(PREF)+'MUSIC') or message.content.startswith(str(PREF)+'музыка') or message.content.startswith(str(PREF)+'Музыка') or message.content.startswith(str(PREF)+'МУЗЫКА'):
            await message.channel.send('''
```diff
- Неверный ввод
Введите "~music help" или "~помощь музыка" для получения руководства по плееру```
''')
        elif message.content.startswith(str(PREF)+'play') or message.content.startswith(str(PREF)+'Play') or message.content.startswith(str(PREF)+'PLAY') or message.content.startswith(str(PREF)+'включи') or message.content.startswith(str(PREF)+'Включи') or message.content.startswith(str(PREF)+'ВКЛЮЧИ'):
            MusicGo=True
            try:
                Trash,Url=map(str,Input0.split(' '))
                print(Url)
            except:
                await message.channel.send('''
```diff
- Неверный ввод
Введите "~music help" или "~помощь музыка" для получения руководства по плееру```
''')
                MusicGo=False
            if MusicGo:
                #CurSong=os.path.isfile(str(message.guild.id)+'Song.mp3')
                Voice=discord.utils.get(client.voice_clients,guild=message.guild)
                try:
                    #if CurSong:
                        #os.remove(str(message.guild.id)+'Song.mp3')
                    None
                except PermissionError:
                    #await message.channel.send('Выключите играющую музыку через leave или stop')
                    #Ей похуй
                    None
                UserConnected=True
                try:
                    VoiceChannel=message.author.voice.channel
                    await VoiceChannel.connect()
                except:
                    try:
                        if Voice.is_connected():
                            await Voice.disconnect()
                            await VoiceChannel.connect()
                    except:
                        UserConnected=False
                        await message.channel.send('''
```Вы не подключены к каналу```
''') 
                Voice=discord.utils.get(client.voice_clients,guild=message.guild)
                ydl_opts={
                    'format':'bestaudio/best',
                    'noplaylist':True,
                    'keepvideo':True,
                    'postprocessors':[{
                        'key':'FFmpegExtractAudio',
                        'preferredcodec':'mp3',
                        'preferredquality':'192',
                    }],
                }
                if UserConnected:
                    try:
                        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                            VidInfo=ydl.extract_info(Url,download=False)
                        print('1')
                        F = open('LOG.txt','w')
                        F.write(VidInfo)
                        print('2')
                        if VidInfo['duration']<=3660:
                            await message.channel.send('''
```Загрузка...```
''') 
                            ydl.download([Url])
                        else:
                            await message.channel.send('''
```Видео слишком длинное (Более 1:01:00)```
''')
                            return
                        for file in os.listdir('./'):
                            if file.endswith('.mp3'):
                                FileEqualsId=0
                                for Guild in client.guilds:
                                    if file==(str(Guild.id)+'Song.mp3'):
                                        FileEqualsId+=1
                                    if file==(str(message.guild.id)+'Song.mp3'):
                                        FileEqualsId-=1
                                print(FileEqualsId)
                                if FileEqualsId==0:
                                    try:
                                        os.remove(str(message.guild.id)+'Song.mp3')
                                    except:
                                        None
                                    VideoName,Trash=map(str,file.split('.mp3'))
                                    os.rename(file,str(message.guild.id)+'Song.mp3')
                                    break
                        await message.channel.send(f'''
```Сейчас играет: {VideoName}```
''')
                        Voice.play(FFmpegPCMAudio(str(message.guild.id)+'Song.mp3'))
                    except:
                        await message.channel.send('''
```Недействительный URL```
''')
        elif message.content.startswith(str(PREF)+'leave') or message.content.startswith(str(PREF)+'Leave') or message.content.startswith(str(PREF)+'LEAVE') or message.content.startswith(str(PREF)+'выйди') or message.content.startswith(str(PREF)+'Выйди') or message.content.startswith(str(PREF)+'ВЫЙДИ'):
            Voice=discord.utils.get(client.voice_clients,guild=message.guild)
            try:
                await Voice.disconnect()
            except:
                await message.channel.send('''```
Не подключена к каналу```
''')
        elif message.content.startswith(str(PREF)+'pause') or message.content.startswith(str(PREF)+'Pause') or message.content.startswith(str(PREF)+'PAUSE') or message.content.startswith(str(PREF)+'пауза') or message.content.startswith(str(PREF)+'Пауза') or message.content.startswith(str(PREF)+'ПАУЗА'):
            Voice=discord.utils.get(client.voice_clients,guild=message.guild)
            try:
                Voice.pause()
                await message.channel.send('''
```Музыка на паузе```
''')
            except:
                await message.channel.send('''
```Ничего не играет```
''')
        elif message.content.startswith(str(PREF)+'resume') or message.content.startswith(str(PREF)+'Resume') or message.content.startswith(str(PREF)+'RESUME') or message.content.startswith(str(PREF)+'продолжи') or message.content.startswith(str(PREF)+'Продолжи') or message.content.startswith(str(PREF)+'ПРОДОЛЖИ'):
            Voice=discord.utils.get(client.voice_clients,guild=message.guild)
            try:
                Voice.resume()
                await message.channel.send('''
```Музыка продолжается```
''')
            except:
                await message.channel.send('''
```Музыка не на паузе```
''')
        elif message.content.startswith(str(PREF)+'stop') or message.content.startswith(str(PREF)+'Stop') or message.content.startswith(str(PREF)+'STOP') or message.content.startswith(str(PREF)+'выключи') or message.content.startswith(str(PREF)+'Выключи') or message.content.startswith(str(PREF)+'ВЫКЛЮЧИ'):
            Voice=discord.utils.get(client.voice_clients,guild=message.guild)
            try:
                Voice.stop()
                await message.channel.send('''
```Музыка выключена```
''')
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
                AsciiImg=ASCIIM.ASCII(NEW_WIDTH,URL)
                await message.channel.send(f'''
```
{AsciiImg}```
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
```
{AsciiImg1}```
''')
                    await message.channel.send(f'''
```
{AsciiImg2}```
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
                            embed.add_field(name="~ASCII help / ~ASCII помощь", value="Отправлю это руководство", inline=False)
                            embed.add_field(name="~ASCII [ширина] [url]", value='[ширина] - ширина арта в символах\n (Если отвечает "Неверный ввод", но все верно - уменьшите ширину)\n [url] - ссылка на изображение\n Деление сообщения происходит из-за ограничения дискордом отправки сообщения до 4000 символов\n (текущий максимум - 3 сообщшения)', inline=False)
                            embed.set_footer(text="ASCII_IMG модифицированный 3.2")
                            await message.channel.send(embed=embed)
                        else:
                            await message.channel.send('''
```diff
- Неверный ввод
Введите "~ASCII help" или "~ASCII помощь" для получения руководства по генератору```
''')
        elif Input0.rfind('RND')!=-1:
            try:
                TRASH,FIRST,LAST=map(str,Input0.split(' '))
                await message.channel.send(f'''
```
{random.randint(int(FIRST),int(LAST))}```
''')
            except:
                if Input0.rfind('help')!=-1 or Input0.rfind('Help')!=-1 or Input0.rfind('помощь')!=-1 or Input0.rfind('Помощь')!=-1:
                    embed=discord.Embed(title="Генератор рандомных чисел", description="Отправлю рандомное число", color=0xc38dce)
                    embed.set_thumbnail(url="https://i.imgur.com/jVssOCD.jpg")
                    embed.add_field(name="~RND help / ~RND помощь", value="Отправлю это руководство", inline=False)
                    embed.add_field(name="~RND [от] [до]", value='[от] - начальное число (включительно)\n [до] - конечное число (включительно)', inline=False)
                    embed.set_footer(text="RandomGenerator 0.2")
                    await message.channel.send(embed=embed)
                else:
                    await message.channel.send('''
```diff
- Неверный ввод
Введите "~RND help" или "~RND помощь" для получения руководства по генератору```
''')
        elif message.content.startswith(str(PREF)+'help') or message.content.startswith(str(PREF)+'Help') or message.content.startswith(str(PREF)+'HELP') or message.content.startswith(str(PREF)+'помощь') or message.content.startswith(str(PREF)+'Помощь') or message.content.startswith(str(PREF)+'ПОМОЩЬ'):
            embed=discord.Embed(title='Доступные команды текущей версии:',description='"~" - действительная приставка',color=0x3ae47b)
            embed.set_thumbnail(url="https://i.imgur.com/NdTbysX.png")
            embed.add_field(name='"help" - список общий команд', value='Открою список команд', inline=False)
            embed.add_field(name='"calc help" - список команд калькулятора', value='Открою calc список команд', inline=False)
            embed.add_field(name='"RND" - рандом', value='Выведу рандомное число (~RND help)', inline=False)
            embed.add_field(name='"ASCII" - арт', value='Создам арт из символов (~ASCII help)', inline=False)
            embed.add_field(name='"MS" - сапер', value='Отправлю в чат сапера (~MS help)', inline=False)
            embed.add_field(name='"кто [кто-то]"', value='Ищу [кого-то] на сервере (вопросительный знак на усмотрение)', inline=False)
            embed.add_field(name='"hentai" - хентай', value='Скину картинку', inline=False)
            embed.set_footer(text='Текущая версия: 0.6.8')
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
            await message.channel.send(embed=embed)
        elif Input0.rfind('hentai')!=-1 or Input0.rfind('Hentai')!=-1 or Input0.rfind('хентай')!=-1 or Input0.rfind('Хентай')!=-1:
            await message.channel.send(random.choice(HENTAILIST))
        else:
            Input0='trash'+str(Input0)
            Trash,Input1=Input0.split(PREF)
            ANS=CalcV2M.calculatorv2(Input1)
            if str(ANS).rfind('IQ=')!=-1:
                SCreditsR=random.choice(SCredits)
                embed=discord.Embed(title=ANS,description='вы разочаровать партия', color=0xe83030)
                embed.set_thumbnail(url='https://i.redd.it/yuzfih87wts71.jpg')
                embed.set_footer(text=f'{SCreditsR} Social credits')
                await message.channel.send(embed=embed)
            else:
                embed=discord.Embed(title=ANS,color=0x3ae47b)
                await message.channel.send(embed=embed)

f = open('TOKEN.env','r')
TOKEN=str(f.read())
client.run(TOKEN)
