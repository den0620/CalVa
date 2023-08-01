import discord,os,asyncio,time,random,ffmpeg,aiohttp,base64,copy
import yt_dlp as youtube_dl

from discord import FFmpegPCMAudio
from discord.ui import Button,View
from discord.ext.commands import Bot
from discord.ext import commands
from datetime import datetime
#from aiohttp_socks import ProxyType,ProxyConnector,ChainProxyConnector

import MineSweeperM,ASCIIM,G2048M,PuzzleM

PREF='/'

bot = commands.Bot(intents=discord.Intents.all())
client = discord.Bot(debug_guilds=[981625388503531621,929440411758518302,758316954087456789,856154142183784448,884789756741951549,1042423377341726800],intents=discord.Intents.all())

ydl_opts={'format':'bestaudio','noplaylist':True}
FFMPEG_opts={'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
adminlist=[573799615074271253,547738827410898965,489895341496467456,374558482525061122]
QueueList={}
LoopList=[]

bot.remove_command('help')

HelpCommands=client.create_group('помощь','Помощь по командам')
GameCommands=client.create_group('игра','Игры')
GreetCommands=client.create_group('напоминание','Ежедневное напоминание дня недеди')

async def GetHelpPageEmbed1():
    HelpPageEmbed01=discord.Embed(title='[Добавить бота]',url='https://discord.com/api/oauth2/authorize?client_id=968795473068560395&permissions=0&scope=applications.commands%20bot',description=f'"{PREF}" - действительная приставка',color=0x3ae47b)
    HelpPageEmbed01.set_author(name='Страница 1/2')
    HelpPageEmbed01.set_thumbnail(url=client.user.avatar)
    HelpPageEmbed01.add_field(name='Список команд:',value=f'''
"{PREF}помощь список" - Открою список всех команд
"{PREF}помощь музыка" - Открою список команд музыки
"{PREF}профиль" - Открою ваш профиль
"{PREF}рандом" - Генератор случайных чисел
"{PREF}аскии" - Создам арт''',inline=False)
    HelpPageEmbed01.set_image(url='https://i.imgur.com/N74YGKW.png')
    HelpPageEmbed01.set_footer(text='Написан den0620#5150 на Python 3.9.2 (Pycord)')
    return(HelpPageEmbed01)
async def GetHelpPageEmbed2():
    HelpPageEmbed02=discord.Embed(title='[Добавить бота]',url='https://discord.com/api/oauth2/authorize?client_id=968795473068560395&permissions=0&scope=applications.commands%20bot',description=f'"{PREF}" - действительная приставка',color=0x3ae47b)
    HelpPageEmbed02.set_author(name='Страница 2/2')
    HelpPageEmbed02.set_thumbnail(url=client.user.avatar)
    HelpPageEmbed02.add_field(name='Список команд:',value=f'''"{PREF}кто [кто-то]" - Скажу кто [такой-то]
"{PREF}где @упомянутый" - Скажу где @участник
"{PREF}когда [что-то]" - Скажу когда произойдет [что-то]
"{PREF}игра список" - Список игр (не работает)
"{PREF}игра сапер" - Игра сапер
"{PREF}игра в2048" - Игра 2048''',inline=False)
    HelpPageEmbed02.set_image(url='https://i.imgur.com/N74YGKW.png')
    HelpPageEmbed02.set_footer(text='Написан den0620#5150 на Python 3.9.2 (Pycord)')
    return(HelpPageEmbed02)
async def GetHelpPageView1():
        button1=Button(label='Вперед',style=discord.ButtonStyle.green,emoji='▶')
        button2=Button(label='Назад',style=discord.ButtonStyle.green,emoji='◀',disabled=True)
        return(button1,button2)
async def GetHelpPageView2():
        button2=Button(label='Вперед',style=discord.ButtonStyle.green,emoji='▶',disabled=True)
        button1=Button(label='Назад',style=discord.ButtonStyle.green,emoji='◀')
        return(button1,button2)
async def Get2048View():
        buttonUP=Button(style=discord.ButtonStyle.green,emoji='⬆')
        buttonDOWN=Button(style=discord.ButtonStyle.green,emoji='⬇')
        buttonLEFT=Button(style=discord.ButtonStyle.green,emoji='⬅')
        buttonRIGHT=Button(style=discord.ButtonStyle.green,emoji='➡')
        return(buttonUP,buttonDOWN,buttonLEFT,buttonRIGHT)
# ===============OpenHelpPages===============
async def ChangeHelpPageTo1(msgOld):
        HelpPageEmbed1=await GetHelpPageEmbed1()
        button1,button2=await GetHelpPageView1()
        async def button_callback(interaction):
                await interaction.response.defer()
                await ChangeHelpPageTo2(msgOld)
        button1.callback=button_callback
        view=View(button2,button1)
        msg=await msgOld.edit_original_message(embed=HelpPageEmbed1,view=view)
async def ChangeHelpPageTo2(msgOld):
        HelpPageEmbed2=await GetHelpPageEmbed2()
        button1,button2=await GetHelpPageView2()
        async def button_callback(interaction):
                await interaction.response.defer()
                await ChangeHelpPageTo1(msgOld)
        button1.callback=button_callback
        view=View(button1,button2)
        msg=await msgOld.edit_original_message(embed=HelpPageEmbed2,view=view)
# ===============READY OUTPUT===============
@client.event
async def on_ready():
        await client.change_presence(activity=(discord.Activity(type=discord.ActivityType.watching, name='хентай')))
        print('We have logged in as {0.user}'.format(client))
        while True:
            DataTimeNow=datetime.now()
            TimeNow=DataTimeNow.strftime('%w;%H')
            if TimeNow.rfind('08')!=-1:
                if TimeNow.find('0;')!=-1:
                    print('sun')
                    with open('RemindIds.txt','r') as doc:
                        for RemindChannelId in doc:
                            channel=client.get_channel(int(RemindChannelId))
                            await channel.send(file=discord.File(r"E:\DISBOT5\weekdays\sunday.JPG"))
                    await asyncio.sleep(70000)
                if TimeNow.find('1;')!=-1:
                    print('mon')
                    with open('RemindIds.txt','r') as doc:
                        for RemindChannelId in doc:
                            channel=client.get_channel(int(RemindChannelId))
                            await channel.send(file=discord.File(r"E:\DISBOT5\weekdays\monday.JPG"))
                    await asyncio.sleep(70000)
                if TimeNow.find('2;')!=-1:
                    print('tue')
                    with open('RemindIds.txt','r') as doc:
                        for RemindChannelId in doc:
                            channel=client.get_channel(int(RemindChannelId))
                            await channel.send(file=discord.File(r"E:\DISBOT5\weekdays\tuesday.JPG"))
                    await asyncio.sleep(70000)
                if TimeNow.find('3;')!=-1:
                    print('wed')
                    with open('RemindIds.txt','r') as doc:
                        for RemindChannelId in doc:
                            channel=client.get_channel(int(RemindChannelId))
                            await channel.send(file=discord.File(r"E:\DISBOT5\weekdays\wednesday.JPG"))
                    await asyncio.sleep(70000)
                if TimeNow.find('4;')!=-1:
                    print('thu')
                    with open('RemindIds.txt','r') as doc:
                        for RemindChannelId in doc:
                            channel=client.get_channel(int(RemindChannelId))
                            await channel.send(file=discord.File(r"E:\DISBOT5\weekdays\thursday.JPG"))
                    await asyncio.sleep(70000)
                if TimeNow.find('5;')!=-1:
                    print('fri')
                    with open('RemindIds.txt','r') as doc:
                        for RemindChannelId in doc:
                            channel=client.get_channel(int(RemindChannelId))
                            await channel.send(file=discord.File(r"E:\DISBOT5\weekdays\friday.JPG"))
                    await asyncio.sleep(70000)
                if TimeNow.find('6;')!=-1:
                    print('sat')
                    with open('RemindIds.txt','r') as doc:
                        for RemindChannelId in doc:
                            channel=client.get_channel(int(RemindChannelId))
                            await channel.send(file=discord.File(r"E:\DISBOT5\weekdays\saturday.JPG"))
                    await asyncio.sleep(70000)
            await asyncio.sleep(1500)
# ===============HelpCommand===============
@HelpCommands.command(description="Список команд")
async def список(message):
        HelpPageEmbed1=await GetHelpPageEmbed1()
        button1,button2=await GetHelpPageView1()
        async def button_callback(interaction):
                await interaction.response.defer()
                await ChangeHelpPageTo2(msg)
        button1.callback=button_callback
        view=View(button2,button1)
        msg=await message.respond(embed=HelpPageEmbed1,view=view,ephemeral=True)
@HelpCommands.command(description="Помощь по проигрывателю")
async def музыка(message):
        embed=discord.Embed(title="Проигрыватель звука с видео на YouTube",url='https://shorturl.at/CRV01',description="Включу звук с видео на ютубе", color=0xff7b24)
        embed.set_author(name='Страница 1/1')
        embed.add_field(name='Список команд:',value=f'''"{PREF}помощь музыка" - Отправлю это руководство
"{PREF}включи [URL]" - Включить звук с видео по URL YouTube
"{PREF}включи (без url)" - Включу следующее в очереди (как скип)
"{PREF}выключи" - Выключу играющую музыку
"{PREF}пауза" - Поставлю играющую музыку на паузу
"{PREF}продолжи" - Сниму играющую музыку с паузы
"{PREF}выйди" - Выйду из ГС и выключу играющую музыку
"{PREF}очередь" - Добавлю видео в очередь
"{PREF}повтор" - Включу/Выключу повтор играющей музыки''', inline=False)
        await message.respond(embed=embed,ephemeral=True)
# ===============PROFILE===============
user=None
@client.command(description="Покажу ваш профиль")
async def профиль(message,участника: discord.Option(discord.member.Member,description='Покажу профиль @участника',required=False)):
        if участника==None:
                участника=message.author
        MEMBER=await client.fetch_user(участника.id)
        is_bot='не бот'
        if MEMBER.bot: is_bot='ботяра'
        prof_color=discord.Colour(0x5865F2)
        if MEMBER.accent_color!=None: prof_color=MEMBER.accent_color
        user_hypesquad='отсутствует'
        if MEMBER.public_flags.hypesquad_balance: user_hypesquad='Balance <:balance:1001070326635048992>'
        elif MEMBER.public_flags.hypesquad_bravery: user_hypesquad='Bravery <:bravery:1001070344762839121>'
        elif MEMBER.public_flags.hypesquad_brilliance: user_hypesquad='Brilliance <:briliance:1001070354812391455>'
        embed=discord.Embed(title=f"Профиль участника {MEMBER.display_name}",color=prof_color)
        embed.add_field(name=f'Имя: {MEMBER}',value=f'ID: {MEMBER.id}\n{MEMBER.mention} {is_bot}\nХайпсквад {user_hypesquad}',inline=False)
        embed.set_thumbnail(url=str(MEMBER.avatar))
        embed.set_footer(text=f"footer")
        await message.respond(embed=embed)
# ===============Week day reminder status===============
@GreetCommands.command(description='Покажу включено или выключено напоминание в канале')
async def состояние(message):
        with open('RemindIds.txt','r') as doc:
            if (str(message.channel.id)+'\n') in doc:
                await message.respond('Сейчас напоминание включено')
            else:
                await message.respond('Сейчас напоминание выключено')
@GreetCommands.command(description='Вкл/Выкл ежедневного утреннего приветствия')
async def переключить(message):
        with open('RemindIds.txt','r') as doc:
            doclines=doc.readlines()
        if (str(message.channel.id)+'\n') in doclines:
            with open('RemindIds.txt','w') as doc:
                doclines.remove(str(message.channel.id)+'\n')
                lines=''
                for line in doclines:
                    lines+=line
                doc.write(lines)
                await message.respond('Напоминание выключено')
        else:
            with open('RemindIds.txt','w') as doc:
                doclines.append(str(message.channel.id)+'\n')
                lines=''
                for line in doclines:
                    lines+=line
                doc.write(lines)
                await message.respond('Напоминание включено')
# ===============KTO===============
KtoObser=['',' все знают, что',' известно, что']
@client.command(description='Находит кого-то')
async def кто(message,кто: discord.Option(str,description='Введите кем является участник')):
        MemberList=[]
        QUESTION=''
        if кто.rfind('?')==(len(кто)-1): WHO=кто[:(len(кто)-1)]
        else: WHO=кто
        for MEMBER in message.channel.members:
                if MEMBER.id!=573799615074271253 and not MEMBER.bot:
                        MemberList.append(MEMBER)
        if len(MemberList)>0:
                FromMemberList=random.choice(MemberList)
                await message.respond(f'{message.author.mention},{random.choice(KtoObser)} {WHO} - {FromMemberList.display_name} ({FromMemberList})')
        else: await message.respond('На сервере отсутствует {Obser}')
# ===============GDE===============
GdeChel=['Употребляет шестиразовое диетическое питание на 3000ккал/раз','Включает пробки после разгона','Вызывает глобальное потепление разгоном FX8350','летает над вулканом и цепляется за вертолет','цивилизованно испражняется','думает над своим поведением в обезъяннике','тонет в деревенском туалете']
@client.command(description='Найду где @участник')
async def где(message,кто: discord.Option(discord.member.Member,description='@Упомяните участника')):
        if кто in message.channel.members:
                await message.respond(f'{message.author.mention},{random.choice(KtoObser)} {кто} {random.choice(GdeChel)}')
        else:
                await message.respond('На сервере отсутствует {кто}')
# ===============KOGDA===============
KogdaCheto=['Когда рак на горе свиснет','Сегодня','Завтра','Вчера','Никогда','Через год']
@client.command(description='Скажу когда произойдет что-то')
async def когда(message,событие: discord.Option(str,description='Напишите событие')):
        embed=discord.Embed(title=random.choice(KogdaCheto),description=событие,color=0xdfe218)
        embed.set_thumbnail(url="https://cdnn21.img.ria.ru/images/15001/87/150018730_24:0:239:161_600x0_80_0_0_b26ebb09ea8bfc7df3e21dc4b00c1ab7.jpg")
        await message.respond(embed=embed)
# ===============MineSweeper===============
@GameCommands.command(description='Отправлю поле игры сапера')
async def сапер(message,ширина: discord.Option(int,description='Целое число<20'), высота: discord.Option(int,description='Целое число<20'), бомбы: discord.Option(int,description='Целое число')):
        if ширина>20:
                await message.respond('Ширина слишком большая')
                return
        elif высота>20:
                await message.respond('Высота слишком большая')
                return
        else:
                await message.respond(MineSweeperM.MineSweeper(ширина,высота,бомбы))
# ===============ASCII===============
@client.command(description='Создам арт из символов')
async def аскии(message,ширина: discord.Option(int,description='Целое число<150'), ссылка: discord.Option(str,description='URL ссылка на картинку')):
        if ширина>150:
                await message.respond('Ширина слишком большая')
                return
        else:
                try:
                        AsciiImg=ASCIIM.ASCII(ширина,ссылка)
                        await message.respond(f'```{AsciiImg}```')
                except:
                        try:
                                leng=(len(AsciiImg)+1)
                                AsciiImg1=AsciiImg[0:leng//2]
                                AsciiImg1=AsciiImg1[0:((len(AsciiImg1)+1)-(int(ширина)+2))]
                                AsciiImg2=AsciiImg[leng//2:]
                                AsciiImg2=AsciiImg2[(0+(int(ширина)+2)):]
                                await message.respond(f'```{AsciiImg1}```')
                                await message.channel.send(f'```{AsciiImg2}```')
                        except:
                                await message.respond('```Недействительная ссылка или ширина слишком большая```')
# ===============2048===============
async def G2048WIN(msg):
    await msg.edit(content=f'```Вы выиграли```',view=View())
async def G2048LOSE(msg):
    await msg.edit(content=f'```Вы проиграли```',view=View())
async def Visualize(GameField,msg):
    Height=len(GameField[0])
    Width=len(GameField)
    FinalField=''
    for y in range(0,Height):
            for x in range(0,Width):
                if GameField[x][y]==0:
                    FinalField+=':o2:'
                elif GameField[x][y]==2:
                    if Width*Height<=1:
                        await G2048WIN(msg)
                        return(1)
                    FinalField+=':two:'
                elif GameField[x][y]==4:
                    if Width*Height<=2:
                        await G2048WIN(msg)
                        return(1)
                    FinalField+=':four:'
                elif GameField[x][y]==8:
                    if Width*Height<=3:
                        await G2048WIN(msg)
                        return(1)
                    FinalField+=':eight:'
                elif GameField[x][y]==16:
                    if Width*Height<=4:
                        await G2048WIN(msg)
                        return(1)
                    FinalField+='<:sixteen:1008126187144478843>'
                elif GameField[x][y]==32:
                    if Width*Height<=5:
                        await G2048WIN(msg)
                        return(1)
                    FinalField+='<:thirtytwo:1008126198104199350>'
                elif GameField[x][y]==64:
                    if Width*Height<=6:
                        await G2048WIN(msg)
                        return(1)
                    FinalField+='<:sixtytwo:1008126209059721358>'
                elif GameField[x][y]==128:
                    if Width*Height<=7:
                        await G2048WIN(msg)
                        return(1)
                    FinalField+='<:hundredtwintyeight:1008126219318984764>'
                elif GameField[x][y]==256:
                    if Width*Height<=8:
                        await G2048WIN(msg)
                        return(1)
                    FinalField+='<:twohundredfiftysix:1008126229469216769>'
                elif GameField[x][y]==512:
                    if Width*Height<=9:
                        await G2048WIN(msg)
                        return(1)
                    FinalField+='<:fivehundredtwelve:1008126240177270794>'
                elif GameField[x][y]==1024:
                    if Width*Height<=10:
                        await G2048WIN(msg)
                        return(1)
                    FinalField+='<:thousandtwentyfour:1008126251397025833>'
                elif GameField[x][y]==2048:
                    await G2048WIN(msg)
                    return(1)
            FinalField+='\n'
    return(FinalField)
async def UpdateField(msg,GameField,Width,Height):
    Field=GameField
    WaitingForButton=True
    buttonUP,buttonDOWN,buttonLEFT,buttonRIGHT=await Get2048View()
    async def button_callback_up(interaction):
        nonlocal Field
        await interaction.response.defer()
        NewField=G2048M.Move(Field,'up',Width,Height)
        if not G2048M.FindSpace(Field,Width,Height):
            await G2048LOSE(msg)
            return
        NewField=G2048M.GenerateNumber(Field,Width,Height)
        Field=NewField
        Visual=await Visualize(Field,msg)
        if Visual==1:
            return
        await msg.edit(content=Visual,view=view)
    async def button_callback_down(interaction):
        nonlocal Field
        await interaction.response.defer()
        NewField=G2048M.Move(Field,'down',Width,Height)
        if not G2048M.FindSpace(Field,Width,Height):
            await G2048LOSE(msg)
            return
        NewField=G2048M.GenerateNumber(Field,Width,Height)
        Field=NewField
        Visual=await Visualize(Field,msg)
        if Visual==1:
            return
        await msg.edit(content=Visual,view=view)
    async def button_callback_left(interaction):
        nonlocal Field
        await interaction.response.defer()
        NewField=G2048M.Move(Field,'left',Width,Height)
        if not G2048M.FindSpace(Field,Width,Height):
            await G2048LOSE(msg)
            return
        NewField=G2048M.GenerateNumber(Field,Width,Height)
        Field=NewField
        Visual=await Visualize(Field,msg)
        if Visual==1:
            return
        await msg.edit(content=Visual,view=view)
    async def button_callback_right(interaction):
        nonlocal Field
        await interaction.response.defer()
        NewField=G2048M.Move(Field,'right',Width,Height)
        if not G2048M.FindSpace(Field,Width,Height):
            await G2048LOSE(msg)
            return
        NewField=G2048M.GenerateNumber(Field,Width,Height)
        Field=NewField
        Visual=await Visualize(Field,msg)
        if Visual==1:
            return
        await msg.edit(content=Visual,view=view)
    buttonUP.callback=button_callback_up
    buttonDOWN.callback=button_callback_down
    buttonLEFT.callback=button_callback_left
    buttonRIGHT.callback=button_callback_right
    view=View(buttonUP,buttonDOWN,buttonLEFT,buttonRIGHT)
    await msg.edit(content=await Visualize(Field,msg),view=view)
@GameCommands.command(description='Сыграть в 2048')
async def в2048(message,ширина: discord.Option(int,description='Целое число<12'), высота: discord.Option(int,description='Целое число<12')):
    Width=ширина
    Height=высота
    if Width>12:
        await message.respond('Слишком большая ширина')
        return
    elif Height>12:
        await message.respond('Слишком большая высота')
        return
    GameField=G2048M.CreateField(Width,Height)
    GameField=G2048M.GenerateNumber(GameField,Width,Height)
    GameField=G2048M.GenerateNumber(GameField,Width,Height)
    buttonUP,buttonDOWN,buttonLEFT,buttonRIGHT=await Get2048View()
    view=View(buttonUP,buttonDOWN,buttonLEFT,buttonRIGHT)
    await message.respond(f'```Игра 2048 с полем {Width} на {Height}```')
    msg=await message.channel.send(GameField,view=view)
    await UpdateField(msg,GameField,Width,Height)
# ===============15 Puzzle==============
async def GetPuzzleView():
    buttonUP=Button(style=discord.ButtonStyle.blurple, emoji='⬆')
    buttonDOWN=Button(style=discord.ButtonStyle.blurple, emoji='⬇')
    buttonLEFT=Button(style=discord.ButtonStyle.blurple, emoji='⬅')
    buttonRIGHT=Button(style=discord.ButtonStyle.blurple, emoji='➡')
    buttonCONFIRM=Button(style=discord.ButtonStyle.green, emoji='⬆')
    return (buttonUP, buttonDOWN, buttonLEFT, buttonRIGHT,buttonCONFIRM)
async def PuzzleWIN(msg):
    await msg.edit(content=f'```Вы заработали {random.randint(50,400)/100} TTC```', view=View())
async def PuzzleVisualize(Field,msg):
    icons=[':o2:',':one:',':two:',':three:',':four:',':five:',':six:',':seven:',':eight:',':nine:',
           ':keycap_ten:','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25']
    FinalField=''
    for i,lst in enumerate(Field):
        for j in Field[i]:
            FinalField+=icons[j]
        FinalField+='\n'
    return FinalField
async def UpdatePuzzleField(msg,Field,SolvedField,Width,Height):
    buttonUP,buttonDOWN,buttonLEFT,buttonRIGHT,buttonCONFIRM=await GetPuzzleView()
    async def button_callback_up(interaction):
        nonlocal Field
        await interaction.response.defer()
        NewField=PuzzleM.MoveSpace(Field,PuzzleM.GetPossibleMoves(Field),'up')
        Field=NewField
        Visual=await PuzzleVisualize(Field,msg)
        await msg.edit(content=Visual,view=view)
    async def button_callback_down(interaction):
        nonlocal Field
        await interaction.response.defer()
        NewField = PuzzleM.MoveSpace(Field, PuzzleM.GetPossibleMoves(Field), 'down')
        Field = NewField
        Visual = await PuzzleVisualize(Field, msg)
        await msg.edit(content=Visual, view=view)
    async def button_callback_left(interaction):
        nonlocal Field
        await interaction.response.defer()
        NewField = PuzzleM.MoveSpace(Field, PuzzleM.GetPossibleMoves(Field), 'left')
        Field = NewField
        Visual = await PuzzleVisualize(Field, msg)
        await msg.edit(content=Visual, view=view)
    async def button_callback_right(interaction):
        nonlocal Field
        await interaction.response.defer()
        Field = PuzzleM.MoveSpace(Field, PuzzleM.GetPossibleMoves(Field), 'right')
        Visual = await PuzzleVisualize(Field, msg)
        await msg.edit(content=Visual, view=view)
    async def button_callback_confirm(interaction):
        nonlocal Field,SolvedField
        await interaction.response.defer()
        if Field[:]==SolvedField[:]:
            await PuzzleWIN(msg)
            return
    buttonUP.callback=button_callback_up
    buttonDOWN.callback=button_callback_down
    buttonLEFT.callback=button_callback_left
    buttonRIGHT.callback=button_callback_right
    buttonCONFIRM.callback=button_callback_confirm
    view=View(buttonUP,buttonDOWN,buttonLEFT,buttonRIGHT,buttonCONFIRM)
    await msg.edit(content=await PuzzleVisualize(Field,msg),view=view)

@GameCommands.command(description='Сыграть в пятнашки')
async def пятнашки(message,ширина: discord.Option(int,description='Целое число<12'),высота: discord.Option(int,description='Целое число')):
    Width=ширина
    Height=высота
    if Width > 12:
        await message.respond('Слишком большая ширина')
        return
    elif Height > 12:
        await message.respond('Слишком большая высота')
        return
    Samples=300
    GameField=PuzzleM.CreateField(Width,Height)
    SolvedGameField=copy.deepcopy(GameField)
    GameField=PuzzleM.Randomize(GameField,Samples)
    buttonUP,buttonDOWN,buttonLEFT,buttonRIGHT,buttonCONFIRM=await GetPuzzleView()
    view=View(buttonUP,buttonDOWN,buttonLEFT,buttonRIGHT)
    await message.respond(f'```Пятнашки с полем {Width} на {Height}```')
    msg=await message.channel.send(GameField,view=view)
    await UpdatePuzzleField(msg,GameField,SolvedGameField,Width,Height)
# ===============RANDOM===============                                
@client.command(description='Сгенерирую случайное число из промежутка')
async def рандом(message,от: discord.Option(int,description='Целое число'),до: discord.Option(int,description='Целое число')):
        try:
                await message.respond(f'```{random.randint(int(от),int(до))}```')
        except:
                await message.respond(f'```{random.randint(int(до),int(от))}```')
# ===============QUESTION===============
AnswColors=['0xf53232','0x32ed0c']
AnswYes=['Да','Наверное','Скорее да','Точно']
AnswNo=['Нет','Наверное нет','Скорее нет','Точно нет']
@client.command(description='Задать мне вопрос')
async def вопрос(message,вопрос: discord.Option(str,description='Сам вопрос')):
        Color=random.choice(AnswColors)
        if Color=='0xf53232':
                embed=discord.Embed(title=random.choice(AnswNo),description=вопрос,color=0xf53232)
                embed.set_thumbnail(url="https://i.imgur.com/4TM5Y0B.png")
                await message.respond(embed=embed)
        elif Color=='0x32ed0c':
                embed=discord.Embed(title=random.choice(AnswYes),description=вопрос,color=0x32ed0c)
                embed.set_thumbnail(url='https://i.imgur.com/wzpu9SV.png')
                await message.respond(embed=embed)
# ===============PING===============
@client.command(description='Текущий пинг бота')
async def пинг(message):
        LATENCY=int((client.latency)*1000)
        await message.respond(f'Задержка {LATENCY}мс')
# ===============SERVERS===============
@client.command(description='Список серверов')
async def сервера(message):
        if str(message.author)=='den0620#5150':
                GuildList=''
                for guild in client.guilds:
                        GuildList=GuildList+str(guild)+' '+str(guild.id)+'\n'
                await message.respond(f'```{GuildList}```')
        else:
                await message.respond('У вас нет прав на запрос этой команды')
# ===============AIOHTTP===============
async def ToAnotherDBpage(PAGE):
    try:
        a=b
    except:
        async with aiohttp.ClientSession() as session:
            async with session.get(PAGE) as respo:
                RespUrl=str(respo.real_url)
                HTMLresp=await respo.text()
        IMG,PREV,NEXT=await GetImgPrevNext(HTMLresp)
        POSTID=await GetPostId(PAGE)
        return IMG,PREV,NEXT,POSTID
    try:
        None
    except:
        return(False)
async def GetImgPrevNext(HTMLresp):
    scamurl=['https://sitenable.pw/tmp/cache/7/8/4/784464ad509526695cd02d34a29853f0.png','https://sitenable.pw/tmp/cache/1/d/9/1d95a8b20b84f338f8cfc325ef7c4ab4.png']
    IMG='https://sitenable.pw'+HTMLresp[
            HTMLresp.find('/tmp/cache',HTMLresp.find('<section class="image-container note-container"')):
            HTMLresp.find('"',HTMLresp.find('/tmp/cache',HTMLresp.find('<section class="image-container note-container"')))
            ]
    IMG=IMG.replace(';','&')
    if IMG in scamurl:
        IMG='https://sitenable.pw'+HTMLresp[
            HTMLresp.find('/o.php',HTMLresp.find('<section class="image-container note-container"')):
            HTMLresp.find('"',HTMLresp.find('/o.php',HTMLresp.find('<section class="image-container note-container"')))
            ]
        IMG=IMG.replace(';','&')
        Base64Code=IMG[IMG.find('&amp&u=')+7:]+'=='
        B64pass=False
        while not B64pass:
            try:
                Base64_bytes=Base64Code.encode('utf-8')
                Params_bytes=base64.b64decode(Base64_bytes)
                Params=str(Params_bytes)[2:(len(Params_bytes)-1)]
                B64pass=True
            except:
                Base64Code=Base64Code[:len(Base64Code)-1]
        i=Params.find('|s://')
        i+=1
        IMG='http'+Params[
            Params.find('|s://')+1:
            Params.find('|Python')
            ]
    PREV='https://sitenable.pw'+HTMLresp[
            HTMLresp.find('/o.php',HTMLresp.find('class="prev"')):
            HTMLresp.find('"',HTMLresp.find('/o.php',HTMLresp.find('class="prev"')))
            ]
    PREV=PREV.replace(';','&')
    NEXT='https://sitenable.pw'+HTMLresp[
            HTMLresp.find('/o.php',HTMLresp.find('class="next"')):
            HTMLresp.find('"',HTMLresp.find('/o.php',HTMLresp.find('class="next"')))
            ]
    NEXT=NEXT.replace(';','&')
    return IMG,PREV,NEXT
async def AddTags(Base64Code,Tags):
    Base64_bytes=Base64Code.encode('ascii')
    Params_bytes=base64.b64decode(Base64_bytes)
    Params=str(Params_bytes)[2:(len(Params_bytes)-1)]
    i=Params.find('danbooru.donmai.us/')
    i+=19
    NewParams=(Params[:i]+'posts?tags='+Tags+Params[i:])
    print('newparams',NewParams)
    NewParams_bytes = NewParams.encode('ascii')
    NewParamsBase64_bytes = base64.b64encode(NewParams_bytes)
    NewParamsBase64 = NewParamsBase64_bytes.decode('ascii')
    return(NewParamsBase64)
async def GetPostId(Url):
    if str(Url).find('&mobile=&amp&u=')!=-1:
        i=str(Url).find('&mobile=&amp&u=')
        i+=15
    else:
        i=str(Url).find('&mobile=&u=')
        i+=11
    Base64Code=Url[i::]
    PASS=False
    while not PASS:
        try:
            Base64_bytes=Base64Code.encode('ascii')
            Params_bytes=base64.b64decode(Base64_bytes)
            Params=str(Params_bytes)[2:(len(Params_bytes)-1)]
            i=Params.find('/posts/')
            i+=7
            PostId=Params[i:Params.find('|Python/')]
            PASS=True
        except:
            Base64Code+='a'
    return PostId
async def SearchForPics(Category):
    try:
        a=b
    except:
        Url="https://sitenable.pw/proxify.php?proxy=c2l0ZW5hYmxlLnB3&site=aHR0cDovL2Rvbm1haS51cy8="
        async with aiohttp.ClientSession() as session:
            async with session.get(Url) as respo:
                RespUrl=str(respo.real_url)
                HTMLresp=await respo.text()
            if Category!=None:
                i=str(RespUrl).find('&mobile=&u=')
                i+=11
                Base64Code=RespUrl[i::]+'=='
                NewParams=await AddTags(Base64Code,Category)
                NewUrl=RespUrl[:i]+NewParams
                async with session.get(NewUrl) as resp:
                    HTMLresp=await resp.text()
            # =====
            HTMLresp=str(HTMLresp)
            i=HTMLresp.find('draggable="false" href="/')
            i+=24
            Href=''
            while HTMLresp[i]!='"':
                Href+=HTMLresp[i]
                i+=1
            j=Href.find('&amp;u=')
            href=Href[(j+7):]
            i=str(RespUrl).find('&mobile=&u=')
            i+=11
            newUrl=RespUrl[:i]+href
            # =====
            async with session.get(newUrl) as resp:
                HTMLresp=await resp.text()
        IMG,PREV,NEXT=await GetImgPrevNext(HTMLresp)
        POSTID=await GetPostId(newUrl)
        return(IMG,PREV,NEXT,POSTID)
    try:
        None
    except:
        return(False)
# ===============GETIMGS COMMAND===============
async def ChangeImgPage(msg,Img,Prev,Next,PostId):
    PrevBut=Button(label='Назад',style=discord.ButtonStyle.green,emoji='◀')
    NextBut=Button(label='Вперед',style=discord.ButtonStyle.green,emoji='▶')
    async def button_callbackP(interaction):
        await interaction.response.defer()
        IMG,PREV,NEXT,POSTID=await ToAnotherDBpage(Prev)
        await ChangeImgPage(msg,IMG,PREV,NEXT,POSTID)
    async def button_callbackN(interaction):
        await interaction.response.defer()
        IMG,PREV,NEXT,POSTID=await ToAnotherDBpage(Next)
        await ChangeImgPage(msg,IMG,PREV,NEXT,POSTID)
    PrevBut.callback=button_callbackP
    NextBut.callback=button_callbackN
    view=View(PrevBut,NextBut)
    embed=discord.Embed(title=f'Post: {PostId}',color=0xf06c60)
    embed.set_image(url=Img)
    await msg.edit_original_message(content=None,embed=embed,view=view)
@client.command(description='search')
async def dbsearch(message,категория: discord.Option(str,description='Поиск по тегу',required=False),айди: discord.Option(str,description='Поиск по айди',required=False)):
    Category=категория
    if message.author.id in adminlist:
        if message.channel.is_nsfw():
            if айди==None:
                msg=await message.respond('loading...')
                IMG,PREV,NEXT,POSTID=await SearchForPics(Category)
                await ChangeImgPage(msg,IMG,PREV,NEXT,POSTID)
            else:
                pass
        else:
                await message.respond('Этот канал не nsfw')
# ===============INVITE FROM ID===============
@client.command(description=None)
async def invite(message,guildid: discord.Option(str,description='url1')):
    if message.author.id in adminlist:
        Guild=client.get_guild(int(guildid))
        for Channel in Guild.channels:
            if str(Channel.type) == 'text':   
                Invite=await Channel.create_invite(reason='я ебу собак', max_age=120, max_uses=1)
                await message.respond('invite')
                await message.channel.send(Invite)
                break
# ===============LEAVE FROM ID===============
@client.command(description=None)
async def leave(message,guildid: discord.Option(str,description='url1')):
    if message.author.id in adminlist:
        Guild=client.get_guild(int(guildid))
        await Guild.leave()
# ==============1000-7==============
#@client.command(description='1000-7')
#async def ghoul(message):
#    if message.author.id in adminlist:
#        await message.respond('1000-7')
#        for i in range(7,993,7):
#            await message.channel.send(f'{1000-i}-7')
#            await asyncio.sleep(1)
#        await message.channel.send(f'{1000-i-7}')
# ================MUSIC=====COMMANDS===============
# =====PLAY GUI=====
async def PlayMusicGUI(message,Url):
    Voice=discord.utils.get(client.voice_clients,guild=message.guild)
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info=ydl.extract_info(Url, download=False)
        URL=info['formats'][5]['url']
        ICON=info['thumbnail']
        TITLE=info['title']
        LENG=int(info['duration'])
    LENGTH=time.strftime('%H:%M:%S',time.gmtime(LENG))
    embed=discord.Embed(title=f"{TITLE}", url=f"{Url}", description=f"Продолжительность: {LENGTH}", color=0x33ad4f)
    embed.set_author(name="Сейчас играет:")
    embed.set_thumbnail(url=f"{ICON}")
    try:
        await message.respond(embed=embed)
    except:
        await message.channel.send(embed=embed)
    Voice.play(discord.FFmpegPCMAudio(URL, **FFMPEG_opts))
    while Voice.is_playing() or Voice.is_paused():
        await asyncio.sleep(2)
    return
# =====PLAY NO GUI=====
async def PlayMusicNOGUI(message,URL):
    Voice=discord.utils.get(client.voice_clients,guild=message.guild)
    Voice.play(discord.FFmpegPCMAudio(URL, **FFMPEG_opts))
    while Voice.is_playing() or Voice.is_paused():
        await asyncio.sleep(2)
    return
# =====CONNECT TO VOICE CHANNEL=====
async def ConnectToVoiceChannel(message):
    try:
        VoiceChannel=message.author.voice.channel
        await VoiceChannel.connect()
        Voice=discord.utils.get(client.voice_clients,guild=message.guild)
        return('Directly')
    except:
        try:
            Voice=message.author.guild.get_member(client.user.id).voice.channel
            if Voice==VoiceChannel:
                Voice=discord.utils.get(client.voice_clients,guild=message.guild)
                Voice.stop()
                return('AlreadyIn')
            else:
                Voice=discord.utils.get(client.voice_clients,guild=message.guild)
                await Voice.disconnect()
                await VoiceChannel.connect()
            return('Moved')
        except:
            await message.respond('```Вы не подключены к каналу```')
            return('NotConnected')
# ===== MAIN =====
@client.command(description='Включу музыку с видео')
async def включи(message,ссылка: discord.Option(str,description='Ссылка на видео',required=False)):
    global ydl_opts,FFMPEG_opts,LoopList,QueueList
    Guild=message.guild
    if ссылка==None:
        if (str(Guild.id) in QueueList) and (len(QueueList[str(Guild.id)])>0):
            ConnectResult=await ConnectToVoiceChannel(message)
            if ConnectResult!='NotConnected':
                while (str(Guild.id) in LoopList) or (len(QueueList[str(Guild.id)])>0):
                    if str(Guild.id) in LoopList:
                        Url=QueueList[str(message.guild.id)][0]
                        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                            info=ydl.extract_info(Url, download=False)
                            URL=info['formats'][5]['url']
                        while str(Guild.id) in LoopList:
                            await PlayMusicNOGUI(message,Url)
                    else:
                        UrlList=QueueList[str(Guild.id)]
                        Url=UrlList[0]
                        await PlayMusicGUI(message,Url)
                        if not (str(Guild.id) in LoopList):
                            UrlList.pop(0)
        else:
            await message.respond('```Ничего нет в очереди```')
            return
    else:
        Url=ссылка
        ConnectResult=await ConnectToVoiceChannel(message)
        if ConnectResult!='NotConnected':
            ShallTurnLoop=False
            try:
                Voice=discord.utils.get(client.voice_clients,guild=message.guild)
                if str(message.guild.id) in LoopList:
                    LoopList.remove(str(message.guild.id))
                    ShallTurnLoop=True
                if Voice.is_playing:
                    Voice.stop()
                await PlayMusicGUI(message,Url)
                if ShallTurnLoop: LoopList.append(str(message.guild.id))
                try:
                    while (str(Guild.id) in LoopList) or (len(QueueList[str(Guild.id)])>0):
                        if str(Guild.id) in LoopList:
                            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                                info=ydl.extract_info(Url, download=False)
                                URL=info['formats'][5]['url']
                            while str(Guild.id) in LoopList:
                                await PlayMusicNOGUI(message,URL)
                        else:
                            UrlList=QueueList[str(Guild.id)]
                            Url=UrlList[0]
                            UrlList.pop(0)
                            await PlayMusicGUI(message,Url)
                except:
                    None
            except:
                await message.respond('```Недействительный URL```')
                return
# ===============QUEUE COMMAND===============
@client.command(description='Добавлю трек в очередь')
async def очередь(message,ссылка: discord.Option(str,description='Ссылка на видео')):
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info=ydl.extract_info(ссылка, download=False)
        try:
            UrlList=QueueList[str(message.guild.id)]
        except:
            UrlList=[]
        UrlList.append(ссылка)
        QueueList[str(message.guild.id)]=UrlList
        await message.respond('```Добавлено в очередь```')
    except:
        await message.respond('```Недействительный URL```')
        return
# ===============LEAVE COMMAND===============
@client.command(description='Выйду из голосового канала')
async def выйди(message):
    Voice=discord.utils.get(client.voice_clients,guild=message.guild)
    if message.guild.id in LoopList:
        LoopList.remove(str(message.guild.id))
    try:
        await message.respond(content='```Вышла```')
        await Voice.disconnect()
    except:
        await message.respond('```Не подключена к каналу```')
        return
# ===============PAUSE COMMAND===============
@client.command(description='Приостановлю воспроизведение')
async def пауза(message):
    Voice=discord.utils.get(client.voice_clients,guild=message.guild)
    try:
        Voice.pause()
        await message.respond('```Музыка приостановлена```')
    except:
        await message.respond('```Ничего не играет```')
        return
# ===============RESUME COMMAND===============
@client.command(description='Продолжу воспроизведение')
async def продолжи(message):
    Voice=discord.utils.get(client.voice_clients,guild=message.guild)
    try:
        Voice.resume()
        await message.respond('```Музыка продолжается```')
    except:
        await message.respond('```Музыка не приостановлена```')
        return
# ===============STOP COMMAND===============
@client.command(description='Выключу музыку')
async def выключи(message):
    Voice=discord.utils.get(client.voice_clients,guild=message.guild)
    if str(message.guild.id) in LoopList:
        LoopList.remove(str(message.guild.id))
    try:
        Voice.stop()
        await message.respond('```Музыка выключена```')
    except:
        await message.respond('```Не подключена или ничего не играет```')
# ===============LOOP COMMAND==============
@client.command(description='Включу/Выключу повтор играющего трека')
async def повтор(message):
    if str(message.guild.id) in LoopList:
        LoopList.remove(str(message.guild.id))
        await message.respond('```Повтор выключен```')
    else:
        LoopList.append(str(message.guild.id))
        await message.respond('```Повтор включен```')







@client.event
async def on_voice_state_update(member,before,after):
        if after.channel==None:
                try:
                        VoiceChannel=member.guild.voice_client.channel
                        Voice=discord.utils.get(client.voice_clients,guild=member.guild)
                        if Voice!=None:
                                if len(VoiceChannel.members)<=1:
                                        await Voice.disconnect()
                except:
                        None
t=open('TOKEN.env','r')
TOKEN=str(t.read())
t.close
client.run(TOKEN)
