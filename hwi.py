# usr/bin/python3
from ast import alias
import os
import random, glob
import discord
from discord.enums import Status
from dotenv import load_dotenv
from discord.ext import commands, tasks
from discord.ext.commands import Bot

from itertools import cycle

from bs4 import BeautifulSoup
import AO3

import requests
from requests.auth import HTTPBasicAuth


load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")


ACC_TOK = os.getenv("ACCESS_TOKEN")
ACC_SEC = os.getenv("ACCESS_TOKEN_SECRET")


#bot prefix command
client = commands.Bot(command_prefix='%')

target_channel_id = 836002214697893958
other_channel_id = 985026869374099456
other_other_channel = 933253388978749460
 
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('%help'))
    for guild in client.guilds:
        print(f'{guild.name} (id: {guild.id})')
    
@client.command(help='Shows the latency ( how slow stuff is ) between u and amu\'s laptop')
async def ping(ctx):
    await ctx.send(f'pong \n{round(client.latency*1000)} ms')
    

#JOP
@client.command(help='WHEN WERE JUMPING AND HOPPING WERE JOPPING')
async def jop(ctx):
    await ctx.send(f'JOP HARDER')

#ao3 command
# @client.command(help='shows ao3 account stats')
# async def ao3(ctx, pwd, user: discord.Member, *, message=None):
#     message = 'log into you account'
#     embed = discord.Embed(title = message)
#     session = AO3.Session(user, pwd)
#     session.refresh_auth_token()

    # try:
    #     user = session.get_user()
    #     stat = user.get_stats()
    #     await ctx.send(f'{user.name} has {user.works} works and {user.fandoms} fandoms')
    # except:
    #     await ctx.send('user not found')

#compability command
@client.command(aliases=['comp', 'COMP', 'compare', 'COMPARE', 'COMPATIBILITY'], help='Compares two values compability level on a scale of 1-420')
async def compatibility(ctx, arg, arg2):
    num=random.randint(1,421)
    await ctx.send(f'Compatibility between {arg} and {arg2} is {num}')

@compatibility.error
async def comp_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('please include two values in the format of: value1 value2')

    
#temp conversions    
@client.command(help='convert c to f', aliases=['CTOF', 'CtoF', 'cTOf'])
async def ftoc(ctx, temp):
    arg=int(temp)
    c = round(((arg - 32) * 5/9), 2)
    await ctx.send(f"{arg} Fahrenheit is {c} Celsius")
    
@client.command(help='convert f to c', aliases=['FTOC', 'FtoC', 'fTOc'])
async def ctof(ctx, temp):
    arg=int(temp)
    f = round(((arg * 9/5) + 32), 2)
    await ctx.send(f"{arg} Celsius is {f} Fahrenheit")

@ftoc.error
async def ftoc_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('please include the value you want converted folling the command. EX: %ftoc 32')
        
@ctof.error
async def ctof_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('please include the value you want converted folling the command. EX: %cotf 32')       


#send some nice words to a fellow member
@client.command(help='say something nice to a fellow friend', aliases=['benice'])
async def compliment(ctx, user):
    nice_phrases=[', ur doing amazing', '😊💕❤😍😎😉💋🌹🎉😘', '- keep up the good work!', 'I CODED THIS 4 U', ' love u m8 no homo bro (ok but all the homo tho)', 'u r actually the best', 'u are actually a blessing to this earth and the greatest to happen to creation since pockets', 'ur pretty neat', 'ur sexy keep it up']
    random.shuffle(nice_phrases)
    await ctx.send(f"{user} {nice_phrases[0]}")


# @client.command(help='bully amu')
# async def bully(ctx):
#     make_fun_of=['code better','spend time on smth useful today','do better']
#     await ctx.send(random.shuffle(make_fun_of))

#image sending commands
#windows syntax for files is: "./foldername\\" + random.choise(os.listdir("./foldername"))
#linux syntax is "foldername" + random.choise(os.listdir("\foldername"))

@client.command(help='sends pictures of rando skz kiddos')
async def skzpic(ctx):
    await ctx.send(file=discord.File("./skz\\" + random.choice(os.listdir("./skz"))))
    
@client.command(help='sends pictures of rando sf9 kiddos')
async def sf9pic(ctx):
    await ctx.send(file=discord.File("./sf9\\" + random.choice(os.listdir("./sf9"))))
    
@client.command(help='sends pictures of rando pentagon kiddos')
async def pentapic(ctx):
    await ctx.send(file=discord.File("./pentagon\\" + random.choice(os.listdir("./pentagon"))))

@client.command(help='sends pictures of random rabbit friend')
async def bunpic(ctx):
    await ctx.send(file=discord.File("./bunny\\" + random.choice(os.listdir("./bunny"))))




           

#sends interval pictures of skz to specified channel
@tasks.loop(hours=5)
async def daily():
    channel = client.get_channel(target_channel_id)
    await channel.send(file=discord.File("./skz\\" + random.choice(os.listdir("./skz"))))

@daily.before_loop
async def before():
    await client.wait_until_ready()
#

#error handling
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'{error} please include all required arguments')
        await ctx.send('please type a valid command. Use **%help** to see all commands')
    elif isinstance(error, commands.BotMissingRole):
        await ctx.send(f'{error} Bot does not have valid roles assigned')
    elif isinstance(error, commands.BotMissingPermissions | commands.CommandInvokeError):
        await ctx.send(f'{error} Invalid permissions. Please elevate permission and try again')
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send(f'Not a valid command - {error}. Use the **%help** command to see all valid commands')
    elif isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f'{error} Please wait {error.retry_after:.2f} seconds before trying again')
       
daily.start()
# mirage_update.start()
client.run(TOKEN)