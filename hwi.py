# bot.py
from ast import alias
import os, random, glob
import discord
from discord.enums import Status
from dotenv import load_dotenv
from discord.ext import commands, tasks
from discord.ext.commands import Bot

import asyncio
from itertools import cycle

load_dotenv()
TOKEN = 'ODQ4MTAyMjM1NDM0NTE2NTEw.YLHuwQ.STCbj1WrvDIrKAgtRGwVDNedFww'
GUILD = os.getenv('DISCORD_GUILD')

client = commands.Bot(command_prefix='%')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('%help'))
    for guild in client.guilds:
        print(f'{guild.name} (id: {guild.id})')
    
@client.command(help='Shows the latency ( how slow stuff is ) between u and amu\'s laptop')
async def ping(ctx):
    await ctx.send(f'pong \n{round(client.latency*1000)} ms')
    
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
    nice_phrases=[', ur doing amazing', '- keep up the good work!', 'I CODED THIS 4 U', ' love u m8 no homo bro', 'u r actually the best', 'u are actually a blessing to this earth and the greatest to happen to creation since pockets', 'ur pretty neat']
    random.shuffle(nice_phrases)
    await ctx.send(f"{user} {nice_phrases[0]}")


@client.command(help='sends pictures of rando skz kiddos')
async def skzpic(ctx):
    await ctx.send(file=discord.File("./skz\\" + random.choice(os.listdir("./skz"))))
    

@client.command(help='sends pictures of rando sf9 kiddos')
async def sf9pic(ctx):
    await ctx.send(file=discord.File("./sf9\\" + random.choice(os.listdir("./sf9"))))
    
    
@client.command(help='sends pictures of rando pentagon kiddos')
async def pentapic(ctx):
    await ctx.send(file=discord.File("./pentagon\\" + random.choice(os.listdir("./pentagon"))))
    

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('please include all required arguments')
    else:    
        await ctx.send('please type a valid command. Use %help to see all commands')
        print(error)
        

client.run(TOKEN)