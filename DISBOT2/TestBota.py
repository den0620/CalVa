import discord,asyncio
from discord.ext.commands import Bot
from discord.ext import commands

PREF='~'
client = discord.Client()
client = commands.Bot(command_prefix=PREF,intents=discord.Intents.all())

@client.event
async def on_message(message):
    if message.content.startswith('$greet'):
        channel = message.channel
        await channel.send('Say hello!')

        def check(m):
            return m.content == 'hello' and m.channel == channel

        msg = await client.wait_for('message', check=check)
        await channel.send('Hello {.author}!'.format(msg))

t=open('TOKEN.env','r')
TOKEN=str(t.read())
client.run(TOKEN)
