import discord,os,asyncio,time,ffmpeg,aiohttp,aiofiles,base64,copy,requests,platform,json#,pyttsx3
import yt_dlp as youtube_dl
import random as random_py

from gtts import gTTS
from PIL import Image
from io import BytesIO
from datetime import datetime
from discord import FFmpegPCMAudio
from discord.ui import Button,View
from discord.ext.commands import Bot
from discord.ext import commands
from datetime import datetime
#from aiohttp_socks import ProxyType,ProxyConnector,ChainProxyConnector

import MineSweeperM,ASCIIM,G2048M,PuzzleM

PREF='/'

bot = commands.Bot(intents=discord.Intents.all())
activity=discord.Activity(type=discord.ActivityType.watching, name='хентай')
status=discord.Status.online
client = discord.Bot(#debug_guilds=[981625388503531621,929440411758518302,758316954087456789,856154142183784448,884789756741951549],
    activity=activity,status=status,intents=discord.Intents.all())

with open('VolumeConf.json', 'r') as volume_dict_file:
    VolumeConf = json.load(volume_dict_file)
ydl_opts={'format':'bestaudio','noplaylist':True}
FFMPEG_opts={'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
FFMPEG_volume=0.2
adminlist=[573799615074271253,489895341496467456]
QueueList={}
LoopList=[]

bot.remove_command('help')

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
        print('We have logged in as {0.user}'.format(client))
async def async_reminder():
        await client.wait_until_ready()
        while not client.is_closed:
            TimeNow=datetime.now().strftime('%w;%H')
            FilePath=os.path.realpath(__file__)[:os.path.realpath(__file__).rfind('/')+1]
            days=['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
            if '08' in TimeNow:
                with open('RemindIds.txt','r') as doc:
                    RemindList=doc.readlines()
                for RemindChannelId in RemindList:
                    try:
                        channel=client.get_channel(int(RemindChannelId.rstrip()))
                        await channel.send(file=discord.File(rf"{FilePath}weekdays/{days[int(TimeNow[:TimeNow.find(';')])]}.JPG"))
                    except:
                        with open('RemindIds.txt','w') as doc:
                            doclines=doc.readlines()
                            doclines.remove(str(RemindChannelId)+'\n')
                            lines=''
                            for line in doclines:
                                lines+=line
                            doc.write(lines)
                await asyncio.sleep(70000)
            await asyncio.sleep(1500)
# ===
@client.command(name_localizations={'en-US': 'deafen', 'ru': 'заглушить'},description_localizations={'en-US': 'Selfdeafen bot', 'ru': 'Самозаглушить бота'})
async def deafen(message):
    if message.guild.get_member(client.user.id).voice.self_deaf: await message.guild.change_voice_state(channel=message.guild.get_member(client.user.id).voice.channel, self_mute=False, self_deaf=False); await message.respond(':white_check_mark:',ephemeral=True)
    else: await message.guild.change_voice_state(channel=message.guild.get_member(client.user.id).voice.channel, self_mute=True, self_deaf=True); await message.respond(':white_check_mark:',ephemeral=True)
# ===============UNAME===============
unameOptions=['-a','-s','-n','-r','-v','-m','-p','-i','-o']
unameFunctions={'-a': platform.platform(),'-s': platform.system(),'-n': platform.node(),'-r': platform.release(),'-v': platform.version(),'-m': platform.machine(),'-p': platform.processor(),'-i': '','-o': 'GNU/Linux'}
@client.command(name="uname",description="Hardware information")
async def uname(message,parameter: discord.Option(name="option",choices=unameOptions,required=False)):
    if parameter==None:
        message.respond(platform.system())
    else:
        unameAns=unameFunctions[parameter]
        if unameAns=='': unameAns='unknown'
        await message.respond(unameAns)
# ===============HelpCommand===============
@client.command(name_localizations={'en-US': 'help', 'ru': 'помощь'},description_localizations={'en-US': 'Show all commands', 'ru': 'Показать все команды'})
async def help(message):
        HelpPageEmbed1=await GetHelpPageEmbed1()
        button1,button2=await GetHelpPageView1()
        async def button_callback(interaction):
                await interaction.response.defer()
                await ChangeHelpPageTo2(msg)
        button1.callback=button_callback
        view=View(button2,button1)
        msg=await message.respond(embed=HelpPageEmbed1,view=view,ephemeral=True)
# ===============PROFILE===============
#@client.command(name="write",description="desc")
#async def write(message):
#    with open("prompt.txt","r") as IF:
#        lines=IF.readlines()
#        prompt="".join(lines)
#        await message.channel.send(prompt)

user=None
@client.command(name_localizations={'en-US': 'profile', 'ru': 'профиль'},description_localizations={'en-US': 'Show @member(or self) profile', 'ru': 'Показать профиль @участника(или свой)'})
async def profile(message,участника: discord.Option(discord.member.Member,name_localizations={'en-US': 'member', 'ru': 'участник'},description_localizations={'en-US': '@member', 'ru': '@участник'},required=False)):
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
# =============== Reminder ===============
@client.command(name_localizations={'en-US': 'reminder', 'ru': 'напоминание'},description_localizations={'en-US': 'Turn on/off daily morning greet', 'ru': 'Вкл/Выкл ежедневного утреннего приветствия'})
async def reminder(message):
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
@client.command(name_localizations={'en-US': 'who', 'ru': 'кто'},description_localizations={'en-US': 'Find who IS', 'ru': 'Найти кого-то'})
async def who(message,who: discord.Option(str,name_localizations={'en-US': 'whois', 'ru': 'кто-то'},description_localizations={'en-US': 'Who is member', 'ru': 'Кем является участник'})):
        MemberList=[]
        QUESTION=''
        for MEMBER in message.channel.members:
                if MEMBER.id!=573799615074271253 and not MEMBER.bot:
                        MemberList.append(MEMBER)
        if len(MemberList)>0:
                FromMemberList=random_py.choice(MemberList)
                await message.respond(f'{message.author.mention},{random_py.choice(KtoObser)} {who} - {FromMemberList.display_name} ({FromMemberList})')
        else: await message.respond('На сервере отсутствует {Obser}')
# ===============GDE===============
GdeChel=['Употребляет шестиразовое диетическое питание на 3000ккал/раз','Включает пробки после разгона','Вызывает глобальное потепление разгоном FX8350','летает над вулканом и цепляется за вертолет','цивилизованно испражняется','думает над своим поведением в обезъяннике','тонет в деревенском туалете']
@client.command(name_localizations={'en-US': 'where', 'ru': 'где'},description_localizations={'en-US': 'Find WHERE is', 'ru': 'Найти где @участник'})
async def where(message,who: discord.Option(discord.member.Member,name_localizations={'en-US': 'who', 'ru': 'кто'},description_localizations={'en-US': '@Mention member', 'ru': '@Упомяните участника'})):
        if who in message.channel.members:
                await message.respond(f'{message.author.mention},{random_py.choice(KtoObser)} {who} {random_py.choice(GdeChel)}')
        else:
                await message.respond(f'На сервере отсутствует {who}')
# ===============KOGDA===============
KogdaCheto=['Когда рак на горе свиснет','Сегодня','Завтра','Вчера','Никогда','Через год']
@client.command(name_localizations={'en-US': 'when', 'ru': 'когда'},description_localizations={'en-US': "When SOMETHING'll happen", 'ru': 'Когда произойдет что-то'})
async def when(message,event: discord.Option(str, name_localizations={'en-US': 'event', 'ru': 'событие'}, description_localizations={'en-US': "Write event", 'ru': 'Напишите событие'})):
        embed=discord.Embed(title=random_py.choice(KogdaCheto),description=event,color=0xdfe218)
        embed.set_thumbnail(url="https://cdnn21.img.ria.ru/images/15001/87/150018730_24:0:239:161_600x0_80_0_0_b26ebb09ea8bfc7df3e21dc4b00c1ab7.jpg")
        await message.respond(embed=embed)
# ===============MineSweeper===============
@client.command(name_localizations={'en-US': 'minesweeper', 'ru': 'сапер'},description_localizations={'en-US': 'Send playable minesweeper field', 'ru': 'Отправить поле игры сапера'})
async def minesweeper(message,width: discord.Option(int,name_localizations={'en-US': 'width', 'ru': 'ширина'},description_localizations={'en-US': '2<Integer<20', 'ru': '2<Целое число<20'}), height: discord.Option(int,name_localizations={'en-US': 'height', 'ru': 'высота'},description_localizations={'en-US': '2<Integer<20', 'ru': '2<Целое число<20'}), bombs: discord.Option(int,name_localizations={'en-US': 'bombs', 'ru': 'бомбы'},description_localizations={'en-US': 'Possitive integer<Width*Height', 'ru': 'Положительное целое число<Ширина*Высота'})):
        if width>20: await message.respond('Ширина слишком большая')
        elif height>20: await message.respond('Высота слишком большая')
        elif width<2: await message.respond('Ширина маленькая большая')
        elif height<2: await message.respond('Высота маленькая большая')
        elif bombs>width*height: await message.respond('Слишком много бомб')
        elif bombs<0: await message.respond('Бомб меньше нуля')
        else: await message.respond(MineSweeperM.MineSweeper(width,height,bombs))
# ===============ASCII===============
@client.command(name_localizations={'en-US': 'ascii', 'ru': 'аскии'},description_localizations={'en-US': 'Make ASCII art of url', 'ru': 'Создать арт из символов по url'})
async def ascii(message,width: discord.Option(int,name_localizations={'en-US': 'width', 'ru': 'ширина'},description_localizations={'en-US': 'Integer<150', 'ru': 'Целое число<150'}), link: discord.Option(str,name_localizations={'en-US': 'link', 'ru': 'ссылка'},description_localizations={'en-US': 'Url pic link', 'ru': 'URL ссылка на картинку'})):
        if width>150:
                await message.respond('Ширина слишком большая')
                return
        else:
                try:
                        AsciiImg=ASCIIM.ASCII(width,link)
                        await message.respond(f'```{AsciiImg}```')
                except:
                        try:
                                leng=(len(AsciiImg)+1)
                                AsciiImg1=AsciiImg[0:leng//2]
                                AsciiImg1=AsciiImg1[0:((len(AsciiImg1)+1)-(int(width)+2))]
                                AsciiImg2=AsciiImg[leng//2:]
                                AsciiImg2=AsciiImg2[(0+(int(width)+2)):]
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
@client.command(name_localizations={'en-US': '2048', 'ru': '2048'},description_localizations={'en-US': 'Play 2048', 'ru': 'Сыграть в 2048'})
async def game2048(message,width: discord.Option(int,name_localizations={'en-US': 'width', 'ru': 'ширина'},description_localizations={'en-US': 'Integer<12', 'ru': 'Целое число<12'}), height: discord.Option(int,name_localizations={'en-US': 'height', 'ru': 'высота'},description_localizations={'en-US': 'Integer<12', 'ru': 'Целое число<12'})):
    if width>12:
        await message.respond('Слишком большая ширина')
        return
    elif height>12:
        await message.respond('Слишком большая высота')
        return
    if width<0 or height<0:
        width = abs(width)
        height = abs(height)
    GameField=G2048M.CreateField(width,height)
    GameField=G2048M.GenerateNumber(GameField,width,height)
    GameField=G2048M.GenerateNumber(GameField,width,height)
    buttonUP,buttonDOWN,buttonLEFT,buttonRIGHT=await Get2048View()
    view=View(buttonUP,buttonDOWN,buttonLEFT,buttonRIGHT)
    await message.respond(f'```Игра 2048 с полем {width} на {height}```')
    msg=await message.channel.send(GameField,view=view)
    await UpdateField(msg,GameField,width,height)
# ===============15 Puzzle==============
async def GetPuzzleView():
    buttonUP=Button(style=discord.ButtonStyle.blurple, emoji='⬆')
    buttonDOWN=Button(style=discord.ButtonStyle.blurple, emoji='⬇')
    buttonLEFT=Button(style=discord.ButtonStyle.blurple, emoji='⬅')
    buttonRIGHT=Button(style=discord.ButtonStyle.blurple, emoji='➡')
    buttonCONFIRM=Button(style=discord.ButtonStyle.green, emoji='⬆')
    return (buttonUP, buttonDOWN, buttonLEFT, buttonRIGHT,buttonCONFIRM)
async def PuzzleWIN(msg):
    await msg.edit(content=f'```Вы заработали {random_py.randint(50,400)/100} TTC```', view=View())
async def PuzzleVisualize(Field,msg):
    FinalField='```'
    Width=len(Field[0])
    Height=len(Field)
    Square=Width*Height
    for i,lst in enumerate(Field):
        for j in Field[i]:
            if Square<=100:
                if j//10==0:
                    if j<=0:
                        FinalField+=f'|  '
                    else:
                        FinalField+=f'| {j}'
                else:
                    FinalField+=f'|{j}'
            else:
                if j//10==0:
                    if j<=0:
                        FinalField+=f'|   '
                    else:
                        FinalField+=f'|  {j}'
                elif j//100==0:
                    FinalField+=f'| {j}'
                else:
                    FinalField+=f'|{j}'
        FinalField+='\n'
    return FinalField+'```'
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

@client.command(name_localizations={'en-US': 'puzzle15', 'ru': 'пятнашки'},description_localizations={'en-US': 'Play 15 puzzle', 'ru': 'Сыграть в пятнашки'})
async def puzzle15(message,width: discord.Option(int,name_localizations={'en-US': 'width', 'ru': 'ширина'},description_localizations={'en-US': '2<Integer<12', 'ru': '2<Целое число<12'}),height: discord.Option(int,name_localizations={'en-US': 'height', 'ru': 'высота'},description_localizations={'en-US': '2<Integer<12', 'ru': '2<Целое число<12'})):
    if width > 12:
        await message.respond('Слишком большая ширина')
        return
    elif height > 12:
        await message.respond('Слишком большая высота')
        return
    if width < 2:
        await message.respond('Слишком маленькая ширина')
        return
    elif height < 2:
        await message.respond('Слишком маленькая высота')
        return
    Samples=(width*height)*(width+height)
    GameField=PuzzleM.CreateField(width,height)
    SolvedGameField=copy.deepcopy(GameField)
    GameField=PuzzleM.Randomize(GameField,Samples)
    buttonUP,buttonDOWN,buttonLEFT,buttonRIGHT,buttonCONFIRM=await GetPuzzleView()
    view=View(buttonUP,buttonDOWN,buttonLEFT,buttonRIGHT)
    await message.respond(f'```Пятнашки с полем {width} на {height}```')
    msg=await message.channel.send(GameField,view=view)
    await UpdatePuzzleField(msg,GameField,SolvedGameField,width,height)
# ===============RANDOM===============                                
@client.command(name_localizations={'en-US': 'random', 'ru': 'рандом'},description_localizations={'en-US': 'Generate random integer from interval', 'ru': 'Сгенерирую случайное число из промежутка'})
async def random(message,rfrom: discord.Option(int,name_localizations={'en-US':'from','ru':'от'},description_localizations={'en-US':'Integer','ru':'Целое число'}),rto: discord.Option(int,name_localizations={'en-US':'to','ru':'до'},description_localizations={'en-US':'Integer','ru':'Целое число'})): await message.respond(f'```{random_py.randint(*sorted([rfrom,rto]))}```')
# ===============QUESTION===============
AnswColors=['0xf53232','0x32ed0c']
AnswYes=['Да','Наверное','Скорее да','Точно']
AnswNo=['Нет','Наверное нет','Скорее нет','Точно нет']
@client.command(name_localizations={'en-US':'ask','ru':'спросить'},description_localizations={'en-US':'Ask a question','ru':'Задать вопрос'})
async def ask(message,question: discord.Option(str,name_localizations={'en-US':'question','ru':'вопрос'},description_localizations={'en-US':'Question itself','ru':'Сам вопрос'})):
        Color=random_py.choice(AnswColors)
        if Color=='0xf53232':
                embed=discord.Embed(title=random_py.choice(AnswNo),description=question,color=0xf53232)
                embed.set_thumbnail(url="https://i.imgur.com/4TM5Y0B.png")
                await message.respond(embed=embed)
        elif Color=='0x32ed0c':
                embed=discord.Embed(title=random_py.choice(AnswYes),description=question,color=0x32ed0c)
                embed.set_thumbnail(url='https://i.imgur.com/wzpu9SV.png')
                await message.respond(embed=embed)
# ===============PING===============
@client.command(name_localizations={'en-US':'ping','ru':'задержка'},description_localizations={'en-US':'pong','ru':'Текущая задержка бота'})
async def ping(message):
        LATENCY=int((client.latency)*1000)
        await message.respond(f'Задержка {LATENCY}мс')
# ===============SERVERS===============
@client.command(name_localizations={'en-US':'servers','ru':'сервера'},description_localizations={'en-US':'Server list','ru':'Список серверов'})
async def servers(message):
        if message.author.id==573799615074271253:
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
        POSTID=await GetPostId(RespUrl)
        return IMG,PREV,NEXT,POSTID
    try:
        None
    except:
        return(False)
async def GetImgPrevNext(HTMLresp):
    scamurl=['https://sitenable.pw/tmp/cache/f/c/a/fcabdfe26e94a380c4d95fccb184ce03.png','https://sitenable.pw/tmp/cache/7/8/4/784464ad509526695cd02d34a29853f0.png','https://sitenable.pw/tmp/cache/1/d/9/1d95a8b20b84f338f8cfc325ef7c4ab4.png','https://sitenable.pw/tmp/cache/d/6/f/d6fafec91bdbec8a7e22662d5467a897.png']
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
    PASS=False
    while not PASS:
        try:
            Base64_bytes = Base64Code.encode('utf-8')
            Params_bytes=base64.b64decode(Base64_bytes)
            PASS=True
        except:
            Base64Code=Base64Code+'a'
    Params=str(Params_bytes)[2:(len(Params_bytes)-1)]
    i=Params.find('danbooru.donmai.us/')
    i+=19
    NewParams=(Params[:i]+'posts?tags='+Tags+Params[i:])
    NewParams_bytes = NewParams.encode('ascii')
    NewParamsBase64_bytes = base64.b64encode(NewParams_bytes)
    NewParamsBase64 = NewParamsBase64_bytes.decode('ascii')
    return(NewParamsBase64)
async def AddTagsID(Base64Code,PostId,Tags=False):
    Base64_bytes=Base64Code.encode('ascii')
    PASS=False
    while not PASS:
        try:
            Base64_bytes = Base64Code.encode('utf-8')
            Params_bytes=base64.b64decode(Base64_bytes)
            PASS=True
        except:
            Base64Code=Base64Code+'a'
    Params=str(Params_bytes)[2:(len(Params_bytes)-1)]
    i=Params.find('danbooru.donmai.us/')
    i+=19
    if Tags:
        NewParams=(Params[:i]+f'posts/{PostId}?q={Tags}'+Params[i:])
    else:
        NewParams=(Params[:i]+f'posts/{PostId}'+Params[i:])
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
            PostId=Params[i:Params.find('|Python/')]
            PASS=True
        except:
            Base64Code+='a'
    return PostId
async def SearchForPics(Category,ID=False):
    try:
        a=b
    except:
        Url="https://sitenable.pw/proxify.php?proxy=c2l0ZW5hYmxlLnB3&site=aHR0cDovL2Rvbm1haS51cy8="
        async with aiohttp.ClientSession() as session:
            async with session.get(Url) as respo:
                RespUrl=str(respo.real_url)
                HTMLresp=await respo.text()
            if not ID:
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
                if i!=-1:
                    i+=24
                else:
                    i=HTMLresp.find('<img width="')
                    i=HTMLresp.find('src="/',i)
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
            else:
                i=str(RespUrl).find('&mobile=&u=')
                i+=11
                Base64Code=RespUrl[i::]+'=='
                NewParams=await AddTagsID(Base64Code,ID,Category)
                NewUrl=RespUrl[:i]+NewParams
                newUrl=NewUrl
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
        nonlocal msg,Prev,Next
        await interaction.response.defer()
        IMG,PREV,NEXT,POSTID = await ToAnotherDBpage(Prev)
        Prev,Next=PREV,NEXT
        embed=discord.Embed(title=f'Post: {POSTID}', color=0xf06c60)
        embed.set_image(url=IMG)
        view=View(PrevBut, NextBut)
        await msg.edit_original_message(content=None, embed=embed,view=view)
    async def button_callbackN(interaction):
        nonlocal msg,Prev,Next
        await interaction.response.defer()
        IMG,PREV,NEXT,POSTID=await ToAnotherDBpage(Next)
        Prev,Next=PREV,NEXT
        embed=discord.Embed(title=f'Post: {POSTID}', color=0xf06c60)
        embed.set_image(url=IMG)
        view=View(PrevBut, NextBut)
        await msg.edit_original_message(content=None, embed=embed,view=view)
    PrevBut.callback=button_callbackP
    NextBut.callback=button_callbackN
    view=View(PrevBut,NextBut)
    embed=discord.Embed(title=f'Post: {PostId}',color=0xf06c60)
    embed.set_image(url=Img)
    await msg.edit_original_message(content=None,embed=embed,view=view)
@client.command(name_localizations={'en-US':'pic','ru':'пикча'},description_localizations={'en-US':'Explore danbooru','ru':'Поиск по danbooru'})
async def pic(message,tag: discord.Option(str,name_localizations={'en-US':'tag','ru':'тег'},description_localizations={'en-US':'Search by tag','ru':'Поиск по тегу'},required=False),uid: discord.Option(str,name_localizations={'en-US':'id','ru':'айди'},description_localizations={'en-US':'Search by id','ru':'Поиск по айди'},required=False)):
    Category=tag
    MessagePostId=uid
    if True:
        if message.channel.is_nsfw() or (message.author.id in adminlist and MessagePostId!=None and MessagePostId.find('-f')!=-1):
            if MessagePostId!=None:
                if MessagePostId=='--force' or MessagePostId=='-f':
                    MessagePostId=None
                elif MessagePostId.find('--force')!=-1:
                    MessagePostId=MessagePostId.replace('--force','')
                elif MessagePostId.find('-f')!=-1:
                    MessagePostId=MessagePostId.replace('-f','')
            msg=await message.respond('''Загрузка... <a:loadingP:1055187594973036576>
```Ни бот, ни автор бота не несут отвественности за то что вы там кинули на поиск и что получили. Так же никто не претендует на авторство картинками. На текущий момент не предусмотренно никакой защиты от нежелательного контента.```''')
            if MessagePostId==None:
                IMG,PREV,NEXT,POSTID=await SearchForPics(Category)
            else: 
                IMG,PREV,NEXT,POSTID=await SearchForPics(Category,MessagePostId)
            await ChangeImgPage(msg,IMG,PREV,NEXT,POSTID)
        else:
                await message.respond('Этот канал не nsfw')
    else:
        await message.respond('У вас нет прав')
# ===============INVITE FROM ID===============
#@client.command(description=None)
#async def invite(message,guildid: discord.Option(str,description='url1')):
#    if message.author.id in adminlist:
#        Guild=client.get_guild(int(guildid))
#        for Channel in Guild.channels:
#            if str(Channel.type) == 'text':
#                Invite=await Channel.create_invite(reason='я натурал', max_age=120, max_uses=1)
#                await message.respond('invite')
#                await message.channel.send(Invite)
#                break
# ===============LEAVE FROM ID===============
#@client.command(description=None)
#async def leave(message,guildid: discord.Option(str,description='url1')):
#    if message.author.id in adminlist:
#        Guild=client.get_guild(int(guildid))
#        await Guild.leave()
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
# ================Change Volume===============
@client.command(name_localizations={'en-US':'volume','ru':'громкость'},description_localizations={'en-US':'Change server music volume (stock is 0.2)','ru':'Изменить громкость музыки на сервере (по умолчанию 0.2)'})
async def volume(message,vol: discord.Option(float,name_localizations={'en-US':'volume','ru':'громкость'},description_localizations={'en-US':'Float volume value 0.01 - 1.0','ru':'Нецелочисленное значение громкости 0.01 - 1.0'},required=False)):
    if message.guild.id == 884789756741951549 and not message.author.id in adminlist:
        await message.respond("жду пока гандоплясик извинится и мамой поклянется что не будет пинговать по всякой хуйне")
        return
    if vol!=None:
        if vol==0.2:
            if str(message.guild.id) in VolumeConf:
                VolumeConf.pop(str(message.guild.id))
                with open('VolumeConf.json', 'w') as volume_dict_file:
                    json.dump(VolumeConf, volume_dict_file)
            await message.respond(f'Громкость успешно изменена на {vol}')
        elif 0.01<=vol<=1.0:
            VolumeConf[str(message.guild.id)]=vol
            with open('VolumeConf.json', 'w') as volume_dict_file:
                json.dump(VolumeConf, volume_dict_file)
            await message.respond(f'Громкость успешно изменена на {vol}')
        else:
            await message.respond(f'Неверное число')
    else:
        if str(message.guild.id) in VolumeConf:
            await message.respond(f"Текущая громкость {VolumeConf[str(message.guild.id)]}")
        else:
            await message.respond("Текущая громкость 0.2")
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
    if str(message.guild.id) in VolumeConf:
        Voice.play(discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(URL, **FFMPEG_opts), volume=float(VolumeConf[str(message.guild.id)])))
    else:
        Voice.play(discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(URL, **FFMPEG_opts),volume=FFMPEG_volume))
    while Voice.is_playing() or Voice.is_paused():
        await asyncio.sleep(2)
    return
# =====PLAY NO GUI=====
async def PlayMusicNOGUI(message,URL):
    Voice=discord.utils.get(client.voice_clients,guild=message.guild)
    if str(message.guild.id) in VolumeConf:
        Voice.play(discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(URL, **FFMPEG_opts), volume=float(VolumeConf[str(message.guild.id)])))
    else:
        Voice.play(discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(URL, **FFMPEG_opts),volume=FFMPEG_volume))
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
@client.command(name_localizations={'en-US':'play','ru':'включи'},description_localizations={'en-US':'Play audio from video','ru':'Включу музыку с видео'})
async def play(message,link: discord.Option(str,name_localizations={'en-US':'link','ru':'ссылка'},description_localizations={'en-US':'Video link','ru':'Ссылка на видео'},required=False)):
    global ydl_opts,FFMPEG_opts,LoopList,QueueList,FFMPEG_volume
    Guild=message.guild
    if link==None:
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
        Url=link
        ConnectResult=await ConnectToVoiceChannel(message)
        if ConnectResult!='NotConnected':
            ShallTurnLoop=False
            try:
                a=b
            except:
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
            try:
                pass
            except:
                await message.respond('```Недействительный URL```')
                return
# ===============QUEUE COMMAND===============
@client.command(name_localizations={'en-US':'queue','ru':'очередь'},description_localizations={'en-US':'Add video in queue','ru':'Добавлю трек в очередь'})
async def queue(message,link: discord.Option(str,name_localizations={'en-US':'link','ru':'ссылка'},description_localizations={'en-US':'Video link','ru':'Ссылка на видео'})):
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info=ydl.extract_info(link, download=False)
        try:
            UrlList=QueueList[str(message.guild.id)]
        except:
            UrlList=[]
        UrlList.append(link)
        QueueList[str(message.guild.id)]=UrlList
        await message.respond('```Добавлено в очередь```')
    except:
        await message.respond('```Недействительный URL```')
        return
# ===============LEAVE COMMAND===============
@client.command(name_localizations={'en-US':'leave','ru':'выйди'},description_localizations={'en-US':'Leave from voice channel','ru':'Выйду из голосового канала'})
async def leave(message):
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
@client.command(name_localizations={'en-US':'pause','ru':'пауза'},description_localizations={'en-US':'Pause player','ru':'Приостановлю воспроизведение'})
async def pause(message):
    Voice=discord.utils.get(client.voice_clients,guild=message.guild)
    try:
        Voice.pause()
        await message.respond('```Музыка приостановлена```')
    except:
        await message.respond('```Ничего не играет```')
        return
# ===============RESUME COMMAND===============
@client.command(name_localizations={'en-US':'resume','ru':'продолжи'},description_localizations={'en-US':'Resume playing','ru':'Продолжу воспроизведение'})
async def resume(message):
    Voice=discord.utils.get(client.voice_clients,guild=message.guild)
    try:
        Voice.resume()
        await message.respond('```Музыка продолжается```')
    except:
        await message.respond('```Музыка не приостановлена```')
        return
# ===============STOP COMMAND===============
@client.command(name_localizations={'en-US':'stop','ru':'выключи'},description_localizations={'en-US':'Stop playing','ru':'Выключу музыку'})
async def stop(message):
    Voice=discord.utils.get(client.voice_clients,guild=message.guild)
    if str(message.guild.id) in LoopList:
        LoopList.remove(str(message.guild.id))
    try:
        Voice.stop()
        await message.respond('```Музыка выключена```')
    except:
        await message.respond('```Не подключена или ничего не играет```')
# ===============LOOP COMMAND==============
@client.command(name_localizations={'en-US':'loop','ru':'повтор'},description_localizations={'en-US':'Turn on/off loop','ru':'Включу/Выключу повтор играющего трека'})
async def loop(message):
    if str(message.guild.id) in LoopList:
        LoopList.remove(str(message.guild.id))
        await message.respond('```Повтор выключен```')
    else:
        LoopList.append(str(message.guild.id))
        await message.respond('```Повтор включен```')
# ===============CalVaTTS===============
@client.command(name_localizations={'en-US':'cvtts','ru':'квттс'},description_localizations={'en-US':'Text To Speech','ru':'Текст в речь'})
async def cvtts(message,text: discord.Option(str,name_localizations={'en-US':'text','ru':'текст'},description_localizations={'en-US':'Text','ru':'Текст'}),lang: discord.Option(str,name_localizations={'en-US':'lang','ru':'язык'},description_localizations={'en-US':'IETF lang (default is "ru")','ru':'Язык по IETF (по умолчанию "ru")'})='ru'):
    if True: #message.author.id in adminlist
        if await ConnectToVoiceChannel(message)!='NotConnected':
            Voice=discord.utils.get(client.voice_clients,guild=message.guild)
            msg=await message.respond(f'```"{text}" (ожидание)```')
            tts=gTTS(text,lang=lang)
            #engine=pyttsx3.init()
            #engine.setProperty('volume', 10.0)
            #engine.setProperty('rate', 100)
            tts.save(f"{os.path.realpath(__file__)[:os.path.realpath(__file__).rfind('/')+1]}cvtts/cvtts{msg.id}.mp3")
            #engine.save_to_file(text,f'CVTTS{msg.id}.mp3')
            #engine.runAndWait()
            Voice.play(discord.FFmpegPCMAudio(f"{os.path.realpath(__file__)[:os.path.realpath(__file__).rfind('/')+1]}cvtts/cvtts{msg.id}.mp3"))
            while Voice.is_playing() or Voice.is_paused():
                await asyncio.sleep(1)
            await msg.edit_original_message(content=f'```"{text}" (выполнено)```')
            os.remove(f"{os.path.realpath(__file__)[:os.path.realpath(__file__).rfind('/')+1]}cvtts/cvtts{msg.id}.mp3")
        else:
            pass
    else:
        await message.respond('Недостаточно прав')

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

with open('TOKEN.env','r') as t:
    TOKEN=str(t.read())
client.loop.create_task(async_reminder())
client.run(TOKEN)
