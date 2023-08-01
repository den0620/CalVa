import discord,os,asyncio,time,random,ffmpeg
import yt_dlp as youtube_dl

from discord import FFmpegPCMAudio
from discord.ui import Button,View
from discord.ext.commands import Bot
from discord.ext import commands
import requests as req

import MineSweeperM,ASCIIM

PREF='~'
client = discord.Client()
client = commands.Bot(command_prefix=PREF,intents=discord.Intents.all())

ydl_opts={'format':'bestaudio','noplaylist':True}
FFMPEG_opts={'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
HelpPageEmbed1=discord.Embed(title='[Добавить бота]',url='https://discord.com/api/oauth2/authorize?client_id=968795473068560395&permissions=0&scope=bot',description=f'"{PREF}" - действительная приставка',color=0x3ae47b)
HelpPageEmbed1.set_author(name='Страница 1/2')
HelpPageEmbed1.set_thumbnail(url="https://i.imgur.com/NdTbysX.png")
HelpPageEmbed1.add_field(name='"help" - список общих команд', value='Открою список команд', inline=False)
HelpPageEmbed1.add_field(name='"profile" - ваш профиль', value='Покажу ваш профиль', inline=False)
HelpPageEmbed1.add_field(name='"music help" - команды музыки', value='Открою список команд музыки', inline=False)
HelpPageEmbed1.add_field(name=f'"rnd" - рандом', value=f'Выведу рандомное число ({PREF}rnd help)', inline=False)
HelpPageEmbed1.add_field(name=f'"ascii" - арт', value=f'Создам арт из символов ({PREF}ascii help)', inline=False)
HelpPageEmbed1.add_field(name=f'"ms" - сапер', value=f'Отправлю в чат сапера ({PREF}ms help)', inline=False)
HelpPageEmbed1.set_footer(text='Написан den0620#5150 на Python 3.9.2')

HelpPageEmbed2=discord.Embed(title='[Добавить бота]',url='https://discord.com/api/oauth2/authorize?client_id=968795473068560395&permissions=0&scope=bot',description=f'"{PREF}" - действительная приставка',color=0x3ae47b)
HelpPageEmbed2.set_author(name='Страница 2/2')
HelpPageEmbed2.set_thumbnail(url="https://i.imgur.com/NdTbysX.png")
HelpPageEmbed2.add_field(name='"ping"/"пинг"', value='Отправлю число выражающее задержку', inline=False)
HelpPageEmbed2.add_field(name='"кто [кто-то]"', value='Ищу [кого-то] на сервере (вопросительный знак на усмотрение)', inline=False)
HelpPageEmbed2.add_field(name='"где @упомянание"', value='Ищу @упомянутого на сервере (вопросительный знак на усмотрение)', inline=False)
HelpPageEmbed2.add_field(name='"когда [что-то]"', value='Когда произойдет [что-то] (вопросительный знак на усмотрение)',inline=False)
HelpPageEmbed2.set_footer(text='Написан den0620#5150 на Python 3.9.2')

QueueList={}
LoopList=[]
# ===============OpenHelpPages===============
async def OpenHelpPage1(message):
        button1=Button(label='Вперед',style=discord.ButtonStyle.green,emoji='▶')
        button2=Button(label='Назад',style=discord.ButtonStyle.green,emoji='◀',disabled=True)
        async def button_callback(interaction):
                await interaction.response.edit_message()
                await ChangeHelpPageTo2(msg)
        button1.callback=button_callback
        view=View(button2,button1)
        msg=await message.channel.send(embed=HelpPageEmbed1,view=view)
async def ChangeHelpPageTo1(msg):
        button1=Button(label='Вперед',style=discord.ButtonStyle.green,emoji='▶')
        button2=Button(label='Назад',style=discord.ButtonStyle.green,emoji='◀',disabled=True)
        async def button_callback(interaction):
                await interaction.response.edit_message()
                await ChangeHelpPageTo2(msg)
        button1.callback=button_callback
        view=View(button2,button1)
        msg=await msg.edit(embed=HelpPageEmbed1,view=view)
async def ChangeHelpPageTo2(msg):
        button1=Button(label='Назад',style=discord.ButtonStyle.green,emoji='◀')
        button2=Button(label='Вперед',style=discord.ButtonStyle.green,emoji='▶',disabled=True)
        async def button_callback(interaction):
                await interaction.response.edit_message()
                await ChangeHelpPageTo1(msg)
        button1.callback=button_callback
        view=View(button1,button2)
        msg=await msg.edit(embed=HelpPageEmbed2,view=view)
# ===============LAMBDA X:===============
async def After1(Guild,Voice,URLold,channel):
        await PlayQueue(Guild,Voice,URLold,channel)
# ===============PlayQueuedSongs/PlayLoop===============
async def PlayQueue(Guild,Voice,Urlold,channel):
        global ydl_opts,FFMPEG_opts,LoopList,QueueList
        try:
                a=b
        except:
                if str(Guild.id) in LoopList:
                        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                                info=ydl.extract_info(Urlold, download=False)
                                URL=info['formats'][5]['url']
                        Voice.play(discord.FFmpegPCMAudio(URL, **FFMPEG_opts))
                        while Voice.is_playing():
                                await asyncio.sleep(1)
                        await After1(Guild,Voice,Urlold,channel)
                else:
                        if str(Guild.id) in QueueList:
                                if len(QueueList[str(Guild.id)])>0:
                                        UrlList=QueueList[str(Guild.id)]
                                        Url=UrlList[0]
                                        UrlList.pop(0)
                                        QueueList[str(Guild.id)]=UrlList
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
                                        await channel.send(embed=embed)
                                        Voice.play(discord.FFmpegPCMAudio(URL, **FFMPEG_opts))
                                        while Voice.is_playing():
                                                await asyncio.sleep(1)
                                        await After1(Guild,Voice,Url,channel)
                                else:
                                        del QueueList[str(Guild.id)]
        try:
                None
        except:
                None
                
@client.event
async def on_ready():
        await client.change_presence(activity=(discord.Activity(type=discord.ActivityType.watching, name='хентай')))
        print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author==client.user:
        return

    global ydl_opts,FFMPEG_opts,LoopList,QueueList
    # ===============KTO LIST===============
    KtoObser=['',' все знают, что',' известно, что']
    # ===============GDE LIST===============
    GdeChel=['Употребляет шестиразовое диетическое питание на 3000ккал/раз','Включает пробки после разгона','Вызывает глобальное потепление разгоном FX8350','летает над вулканом и цепляется за вертолет','цивилизованно испражняется','думает над своим поведением в обезъяннике','тонет в деревенском туалете']
    # ===============KOGDA LIST===============
    KogdaCheto=['Когда рак на горе свиснет','Сегодня','Завтра','Вчера','Никогда','Через год']
    # ===============QUESTIONS COLORS===============
    AnswColors=['0xf53232','0x32ed0c']
    # ===============ANSWER YES===============
    AnswYes=['Да','Наверное','Скорее да','Точно']
    # ===============ANSWER NO===============
    AnswNo=['Нет','Наверное нет','Скорее нет','Точно нет']
            
    if message.content.startswith(PREF) and not message.author.bot:
        #Input0=Original Input
        Trash,Input0=map(str,message.content.split(PREF))
        # ===============PING COMMAND===============
        if Input0.startswith('ping') or Input0.startswith('пинг'):
             await message.channel.send(client.latency)   
        # ===============SERVERS COMMAND===============
        elif Input0.startswith('сервера') and str(message.author)=='den0620#5150':
            GuildList=''
            for guild in client.guilds:
                GuildList=GuildList+str(guild)+'\n'
            await message.channel.send(GuildList)
        # ===============PROFILE COMMAND===============
        elif Input0.startswith('profile') or Input0.startswith('профиль'):
            try:
                MEMBER=(message.mentions[0])
            except:
                MEMBER=message.author
            embed=discord.Embed(title=f"Профиль {MEMBER}", description=f"ID: {MEMBER.id}", color=0x93b2b4)
            embed.set_author(name=f'{message.author}: {message.content}',icon_url=message.author.avatar)
            embed.set_thumbnail(url=str(MEMBER.avatar))
            embed.set_footer(text=f"None")
            await message.channel.send(embed=embed)
        # ===============KTO COMMAND===============
        elif Input0.startswith('кто') or Input0.startswith('Кто') or Input0.startswith('КТО'):
            Input0=str(PREF)+str(Input0)
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
            for member in message.channel.members:
                if str(member)!='den0620#5150' and str(member)!='CalVa#4915':
                    MemberList.append(member)
            if len(message.channel.members)>0:
                await message.channel.send(f'{message.author.mention},{random.choice(KtoObser)} {Obser} - {random.choice(MemberList)}')
            else:
                await message.channel.send('На сервере отсутствует {Obser}')
        # ===============GDE COMMAND===============
        elif Input0.startswith('где') or Input0.startswith('Где') or Input0.startswith('ГДЕ'):
            try:
                Input0,Trash=map(str,Obser.split('?'))
            except:
                None
            try:
                if message.mentions[0] in message.channel.members:
                    await message.channel.send(f'{message.author.mention},{random.choice(KtoObser)} {message.mentions[0]} {random.choice(GdeChel)}')
                else:
                    await message.channel.send('На сервере отсутствует {message.mentions[0]}')
            except:
                await message.channel.send('```Неверный ввод\nУпомяните участника чата```')
        # ===============KOGDA COMMAND===============
        elif Input0.startswith('когда ') or Input0.startswith('Когда ') or Input0.startswith('КОГДА '):
            Input0=str(PREF)+str(Input0)
            try:
                Trash,Input0=map(str,Input0.split(f'{PREF}когда '))
            except:
                try:
                    Trash,Input0=map(str,Input0.split(f'{PREF}Когда '))
                except:
                    try:
                        Trash,Input0=map(str,Input0.split(f'{PREF}КОГДА '))
                    except:
                        await message.channel.send('```Неверный ввод\nУкажите действие```')
                        return
            try:
                Input0,Trash=map(str,Input0.split('?'))
            except:
                None
            embed=discord.Embed(title=random.choice(KogdaCheto),description=Input0,color=0xdfe218)
            embed.set_author(name=f'{message.author}: {message.content}',icon_url=message.author.avatar)
            embed.set_thumbnail(url="https://cdnn21.img.ria.ru/images/15001/87/150018730_24:0:239:161_600x0_80_0_0_b26ebb09ea8bfc7df3e21dc4b00c1ab7.jpg")
            await message.channel.send(embed=embed)
        # ===============MS COMMAND===============
        elif Input0.startswith('ms') or Input0.startswith('сапер'):
            try:
                try:
                    Trash,Input1=map(str,Input0.split('ms '))
                except:
                    Trash,Input1=map(str,Input0.split('сапер '))
                Width,Height,Bombs=map(int,Input1.split(' '))
                if Width+Height<=50:
                    await message.channel.send(MineSweeperM.MineSweeper(Width,Height,Bombs))
                else:
                    await message.channel.send('```Поле слишком большое```')
            #===============MS HELP===============
            except:
                if Input0.rfind('help')!=-1 or Input0.rfind('помощь')!=-1:
                    embed=discord.Embed(title="Генератор сапера", description="Отправлю в ответ поле", color=0xcac412)
                    embed.set_author(name=f'{message.author}: {message.content}',icon_url=message.author.avatar)
                    embed.set_thumbnail(url="https://i.imgur.com/zQKDNYv.png")
                    embed.add_field(name=f"{PREF}MS help / {PREF}MS помощь", value="Отправлю это руководство", inline=False)
                    embed.add_field(name=f"{PREF}MS [ширина] [высота] [бомбы]", value='[ширина] - ширина поля в эмодзи\n (Если поле обрывается - закончилось допустимое кол-во эмодзи или спойлеров)\n [высота] - высота поля в эмодзи\n [бомбы] - кол-во бомб на поле', inline=False)
                    embed.set_footer(text="MineSweeper модифицированный 2.13")
                else:
                    await message.channel.send(f'```Неверный ввод\nВведите "{PREF}MS help" или "{PREF}MS помощь" для получения руководства по генератору```')
        # ===============MUSIC COMMAND===============
        elif Input0.startswith('music') or Input0.startswith('музыка'):
            if Input0.rfind('help')!=-1 or Input0.rfind('помощь')!=-1:
                embed=discord.Embed(title="Музыкальный плеер", description="Включу звук с видео на ютубе", color=0xff7b24)
                embed.set_author(name=f'{message.author}: {message.content}',icon_url=message.author.avatar)
                embed.set_thumbnail(url="https://i.imgur.com/iSN1F4I.png")
                embed.add_field(name=f"{PREF}music help / {PREF}помощь музыка", value="Отправлю это руководство", inline=False)
                embed.add_field(name=f"{PREF}play [URL] / {PREF}включи [URL]", value="Включить звук с видео по URL YouTube", inline=False)
                embed.add_field(name=f"{PREF}play / {PREF}включи (без url)",value="Включу следующее в очереди\n(Еще работает как скип)",inline=False)
                embed.add_field(name=f"{PREF}stop / {PREF}выключи", value="Выключу играющую музыку", inline=False)
                embed.add_field(name=f"{PREF}pause / {PREF}пауза", value="Поставлю играющую музыку на паузу", inline=False)
                embed.add_field(name=f"{PREF}resume / {PREF}продолжи", value="Сниму играющую музыку с паузы", inline=False)
                embed.add_field(name=f"{PREF}leave / {PREF}выйди", value="Выйду из ГС и выключу играющую музыку", inline=False)
                embed.add_field(name=f"{PREF}queue / {PREF}очередь", value="Добавлю видео в очередь", inline=False)
                embed.add_field(name=f"{PREF}loop / {PREF}повтор", value="Включу/Выключу повтор играющей музыки", inline=False)
                embed.set_footer(text="Плеер 1.0.2")
                await message.channel.send(embed=embed)
            else:
                await message.channel.send(f'```Неверный вводВведите "{PREF}music help" или "{PREF}помощь музыка" для получения руководства по плееру```')
        # ===============PLAY COMMAND===============
        elif Input0.startswith('play') or Input0.startswith('включи'):
            PlayingQueue=False
            try:
                Trash,Url=map(str,Input0.split(' '))
            except:
                if Input0=='play' or Input0=='включи':
                        try:
                                Url=QueueList[str(message.guild.id)][0]
                                try:
                                        VoiceChannel=message.author.voice.channel
                                        await VoiceChannel.connect()
                                        Voice=discord.utils.get(client.voice_clients,guild=message.guild)
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
                                            await message.channel.send('```Вы не подключены к каналу```')
                                            return
                                await After1(message.guild,Voice,Url,message.channel)
                                PlayingQueue=True
                        except:
                                await message.channel.send('```Ничего нет в очереди```')
                                return
                if not PlayingQueue:
                        await message.channel.send(f'```Неправильный ввод\nВведите "{PREF}music help" или "{PREF}помощь музыка" для получения руководства по плееру```')
                        return
            if not PlayingQueue:
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
                            await message.channel.send('```Вы не подключены к каналу```')
                            return
                    Voice=discord.utils.get(client.voice_clients,guild=message.guild)
                    try:
                            a=b
                    except:
                        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                            info=ydl.extract_info(Url, download=False)
                            URL=info['formats'][5]['url']
                            ICON=info['thumbnail']
                            TITLE=info['title']
                            LENG=int(info['duration'])
                        Voice.play(discord.FFmpegPCMAudio(URL, **FFMPEG_opts))
                        LENGTH=time.strftime('%H:%M:%S',time.gmtime(LENG))
                        embed=discord.Embed(title=f"{TITLE}", url=f"{Url}", description=f"Продолжительность: {LENGTH}", color=0x33ad4f)
                        embed.set_author(name="Сейчас играет:")
                        embed.set_thumbnail(url=f"{ICON}")
                        await message.channel.send(embed=embed)
                        while Voice.is_playing():
                                await asyncio.sleep(1)
                        await After1(message.guild,Voice,Url,message.channel)
                    try:
                            None
                    except:
                        await message.channel.send('```Недействительный URL```')
                        return
        # ===============QUEUE COMMAND===============
        elif Input0.startswith('queue') or Input0.startswith('очередь'):
                try:
                        Trash,Url=map(str,Input0.split(' '))
                        try:
                                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                                        info=ydl.extract_info(Url, download=False)
                                try:
                                        UrlList=QueueList[str(message.guild.id)]
                                except:
                                        UrlList=[]
                                UrlList.append(Url)
                                QueueList[str(message.guild.id)]=UrlList
                                await message.channel.send('```Добавлено в очередь```')
                        except:
                                await message.channel.send('```Недействительный URL```')
                                return
                except:
                        await message.channel.send(f'```Неправильный ввод\nВведите "{PREF}music help" или "{PREF}помощь музыка" для получения руководства по плееру```')
                        return
        # ===============LEAVE COMMAND===============
        elif Input0.startswith('leave') or Input0.startswith('выйди'):
            Voice=discord.utils.get(client.voice_clients,guild=message.guild)
            if message.guild.id in LoopList:
                LoopList.remove(str(message.guild.id))
            try:
                await Voice.disconnect()
            except:
                await message.channel.send('```Не подключена к каналу```')
                return
        # ===============PAUSE COMMAND===============
        elif Input0.startswith('pause') or Input0.startswith('пауза'):
            Voice=discord.utils.get(client.voice_clients,guild=message.guild)
            try:
                Voice.pause()
                await message.channel.send('```Музыка приостановлена``')
            except:
                await message.channel.send('```Ничего не играет```')
                return
        # ===============RESUME COMMAND===============
        elif Input0.startswith('resume') or Input0.startswith('продолжи'):
            Voice=discord.utils.get(client.voice_clients,guild=message.guild)
            try:
                Voice.resume()
                await message.channel.send('```Музыка продолжается```')
            except:
                await message.channel.send('```Музыка не приостановлена```')
                return
        # ===============STOP COMMAND===============
        elif Input0.startswith('stop') or Input0.startswith('выключи'):
            Voice=discord.utils.get(client.voice_clients,guild=message.guild)
            if str(message.guild.id) in LoopList:
                LoopList.remove(str(message.guild.id))
            try:
                Voice.stop()
                await message.channel.send('```Музыка выключена```')
            except:
                await message.channel.send('```Не подключена или ничего не играет```')
        # ===============LOOP COMMAND==============
        elif Input0.startswith('loop') or Input0.startswith('повтор'):
            if str(message.guild.id) in LoopList:
                LoopList.remove(str(message.guild.id))
                await message.channel.send('```Повтор выключен```')
            else:
                LoopList.append(str(message.guild.id))
                await message.channel.send('```Повтор включен```')
        # ===============ASCII COMMAND===============
        elif Input0.startswith('ascii') or Input0.startswith('аскии'):
            #Первая попытка
            try:
                TRASH,NEW_WIDTH,URL=map(str,Input0.split(' '))
                if NEW_WIDTH>=150:
                    await message.channel.send('```Ширина слишком большая```')
                    return
                else:
                    AsciiImg=ASCIIM.ASCII(NEW_WIDTH,URL)
                    await message.channel.send(f'```{AsciiImg}```')
            except:
                #2 сообщения с рисунком
                try:
                    #Высота сообщения в строках
                    leng=(len(AsciiImg)+1)
                    AsciiImg1=AsciiImg[0:leng//2]
                    AsciiImg1=AsciiImg1[0:((len(AsciiImg1)+1)-(int(NEW_WIDTH)+2))]
                    AsciiImg2=AsciiImg[leng//2:]
                    AsciiImg2=AsciiImg2[(0+(int(NEW_WIDTH)+2)):]
                    await message.channel.send(f'```{AsciiImg1}```')
                    await message.channel.send(f'```{AsciiImg2}```')
                except:
                    try:
                        #3 сообщения с рисунком
                        AsciiImg1=AsciiImg[0:leng//3]
                        AsciiImg1=AsciiImg1[0:((len(AsciiImg1)+1)-(int(NEW_WIDTH)+2))]
                        AsciiImg2=AsciiImg[leng//3:(2*leng//3)]
                        AsciiImg2=AsciiImg2[(0+(int(NEW_WIDTH)+2)):(len(AsciiImg2)-(int(NEW_WIDTH)+2))]
                        AsciiImg3=AsciiImg[(2*leng//3):]
                        AsciiImg3=AsciiImg3[(0+(int(NEW_WIDTH)+2)):]
                        await message.channel.send(f'```{AsciiImg1}```')
                        await message.channel.send(f'```{AsciiImg2}```')
                        await message.channel.send(f'```{AsciiImg3}```')
                    except:
                        if Input0.rfind('help')!=-1 or Input0.rfind('помощь')!=-1:
                            embed=discord.Embed(title="ASCII арт генератор", description="Отправлю в ответ картинку из символов", color=0x1fc6ef)
                            embed.set_author(name=f'{message.author}: {message.content}',icon_url=message.author.avatar)
                            embed.set_thumbnail(url="https://i.imgur.com/uc4CH2A.png")
                            embed.add_field(name=f"{PREF}ascii help / {PREF}ascii помощь", value="Отправлю это руководство", inline=False)
                            embed.add_field(name=f"{PREF}ascii [ширина] [url]", value='[ширина] - ширина арта в символах\n (Если отвечает "Неверный ввод", но все верно - уменьшите ширину)\n [url] - ссылка на изображение\n Деление сообщения происходит из-за ограничения дискордом отправки сообщения до 4000 символов\n (текущий максимум - 3 сообщшения)', inline=False)
                            await message.channel.send(embed=embed)
                        else:
                            await message.channel.send(f'```Неверный ввод\nВведите "{PREF}ASCII help" или "{PREF}ASCII помощь" для получения руководства по генератору```')
        # ===============RND COMMAND===============
        elif Input0.startswith('rnd') or Input0.startswith('рандом'):
            try:
                TRASH,FIRST,LAST=map(str,Input0.split(' '))
                await message.channel.send(f'```{random.randint(int(FIRST),int(LAST))}```')
            except:
                try:
                    await message.channel.send(f'```{random.randint(int(LAST),int(FIRST))}```')
                except:
                    if Input0.rfind('help')!=-1 or Input0.rfind('Help')!=-1 or Input0.rfind('помощь')!=-1 or Input0.rfind('Помощь')!=-1:
                        embed=discord.Embed(title="Генератор рандомных чисел", description="Отправлю рандомное число", color=0xc38dce)
                        embed.set_author(name=f'{message.author}: {message.content}',icon_url=message.author.avatar)
                        embed.set_thumbnail(url="https://i.imgur.com/jVssOCD.jpg")
                        embed.add_field(name=f"{PREF}rnd help / {PREF}rnd помощь", value="Отправлю это руководство", inline=False)
                        embed.add_field(name=f"{PREF}rnd [от] [до]", value='[от] - начальное число (включительно)\n [до] - конечное число (включительно)', inline=False)
                        embed.set_footer(text="RandomGenerator 0.2")
                        await message.channel.send(embed=embed)
                    else:
                        await message.channel.send(f'```Неверный ввод\nВведите "{PREF}RND help" или "{PREF}RND помощь" для получения руководства по генератору```')
        # ===============HELP COMMAND===============
        elif Input0.startswith('help') or Input0.startswith('помощь'):
            await OpenHelpPage1(message)
            return
        # ===============QUESTION COMMAND===============
        elif Input0.endswith('?'):
            Color=random.choice(AnswColors)
            if Color=='0xf53232':
                embed=discord.Embed(title=random.choice(AnswNo),description=Input0,color=0xf53232)
                embed.set_author(name=f'{message.author}: {message.content}',icon_url=message.author.avatar)
                embed.set_thumbnail(url="https://i.imgur.com/4TM5Y0B.png")
                await message.channel.send(embed=embed)
            elif Color=='0x32ed0c':
                embed=discord.Embed(title=random.choice(AnswYes),description=Input0,color=0x32ed0c)
                embed.set_author(name=f'{message.author}: {message.content}',icon_url=message.author.avatar)
                embed.set_thumbnail(url='https://i.imgur.com/wzpu9SV.png')
                await message.channel.send(embed=embed)
        else:
            embed=discord.Embed(title='Неверная команда',description=f'Введите {PREF}help или {PREF}помощь\nдля получения списка команд')
            embed.set_author(name=f'{message.author}: {message.content}',icon_url=message.author.avatar)
            embed.set_thumbnail(url='https://i.imgur.com/Bf2cWnT.jpg')
            await message.channel.send(embed=embed)
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
client.run(TOKEN)
