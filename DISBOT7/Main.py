import discord, os, sys, asyncio, time, ffmpeg, aiohttp, aiofiles, base64, copy, platform, json, subprocess
from typing import Optional
from simple_chalk import chalk
from discord import app_commands
import yt_dlp as youtube_dl
import random as random_py

from gtts import gTTS
from PIL import Image
from io import BytesIO
from datetime import datetime

import modules.MineSweeperM,modules.AsciiM,modules.G2048M,modules.Puzzle15M,modules.VoiceRelatedM


CommandPrefix = "?"
#          den0620            NeNazvali          DegrOwenn          VolnyV
adminlist=[573799615074271253,547738827410898965,527505544261664798,489895341496467456]

#async def setup_hook(self):
#    self.tree.copy_global_to(guild=debug_guild)
#    await self.tree.sync(guild=debug_guild)

debug_guild=discord.Object(id=929440411758518302)
intents = discord.Intents.all()
client = discord.Client(intents=intents)
client.tree = app_commands.CommandTree(client)

colors={"black": chalk.black, "red": chalk.red, "green": chalk.green, "yellow": chalk.yellow, "blue": chalk.blue, "magenta": chalk.magenta, "cyan": chalk.cyan, "white": chalk.white, "grey": chalk.grey}


def getlen(text,mx):
    if mx<=len(text):
        return 0
    else:
        return mx-len(text)

@client.event
async def on_ready():
    text1 = f'We have logged in as {client.user}'
    try:
        sync = await client.tree.sync()
        text2 = f'Synced {len(sync)} commands'
    except Exception as E:
        text2 = f'Sync failed {E}'
    print(f'''
┌{"─"*max([len(text1),len(text2)])}┐
│{text1}{" "*getlen(text1, max([len(text1),len(text2)]))}│
│{text2}{" "*getlen(text2, max([len(text1),len(text2)]))}│
└{"─"*max([len(text1),len(text2)])}┘
''')

@client.tree.command(name="help")
async def help(interaction: discord.Interaction):
    await interaction.response.send_message('Создатели discord.py копрофилы')


@client.tree.command(name="profile")
async def profile(interaction: discord.Interaction, member: Optional[discord.Member]=None):
    if member==None:
            member=interaction.user
    MEMBER=await client.fetch_user(member.id)
    prof_color=discord.Colour(0x5865F2)
    if MEMBER.accent_color!=None: prof_color=MEMBER.accent_color
    colorpalette=[colors[i](f"{i}: ██") for i in colors]
    embed=discord.Embed(title=f"```title```", description=f"```ansi\n"+'\n'.join(colorpalette)+"```", color=prof_color)
    embed.add_field(name=f"```ansi\n{chalk.red('fieldname')}```", value=f"```ansi\n{chalk.red('fieldvalue')}```", inline=False)
    embed.set_footer(text=f"```ansi\n{chalk.red('footer')}```")
    await interaction.response.send_message(embed=embed)



with open('TOKEN.env','r') as t:
    TOKEN=str(t.read())
client.run(TOKEN)
