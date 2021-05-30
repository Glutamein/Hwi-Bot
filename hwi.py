# bot.py
import os
import random
import glob
import discord
from dotenv import load_dotenv
from discord.ext import commands

DIS_TOKEN = "ODQ4MTAyMjM1NDM0NTE2NTEw.YLHuwQ.JO-cK6WHnqkYzyDPsE32IiZi4Pc"
GUILD_TOKEN = "841920524514099231"

load_dotenv()
TOKEN = (DIS_TOKEN)
GUILD = (GUILD_TOKEN)

bot = commands.Bot(command_prefix='%')

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name} (id: {guild.id})'
    )

#annoying birthday
@client.event
async def on_message(message):
    responce = 'happy Birthday! 🎈🎉'
    if message.author == client.user:
        return

    if message.content.lower() == 'happy birthday':
        await message.channel.send(responce)


#pic sender
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    #turn this into a folder of pictures
    skz_kiddos = [
        'Chan',
        'Minho',
        "Changbin",
        'Hyunjin',
        'Felix',
        'Jisung',
        'Seungmin',
        "IN",
    ]

    # path = "C:\\Users\\Amu\\Downloads\\skz\\*.*"
  
    file_path_type = ["C:\\Users\\Amu\\Downloads\\skz\\*.png", "C:\\Users\\Amu\\Downloads\\skz\\*.jpg"]
    images = glob.glob(random.choice(file_path_type))
    random_image = random.choice(images)

    if message.content == 'skz':
        response = random.choice(random_image)
        #response = random.choice(pics)
        #pics = [dictonary of pics / folder path]
        await message.channel.send(response)

    elif message.content == 'raise-exception':
       raise discord.DiscordException


client.run(TOKEN)