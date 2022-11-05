import discord
from discord.ext import commands
from events import intro
#import pymongo
#from pymongo import MongoClient
#import intro

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!',intents=intents)
wakeuptimes = {'mon':None,'tue':None,'wed':None,'thu':None,'fri':None,'sat':None,'sun':None}

def checkvalidset(day,time):
    if day not in wakeuptimes.keys():
        return False
    if len(time) != 5:
        return False
    if int(time[0:2]) > 23:
        return False
    if int(time[3:-1]) > 59:
        return False
    if time[3] != ':':
        return False
    return True


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def sus(ctx):
    await ctx.send('iposter')

@bot.command()
async def start(ctx):
    await ctx.send('hi! give me your credit card information')
    await intro.main(ctx,bot)

@bot.command()
async def set(ctx,*args):
    if len(args) != 2:
        await ctx.send('usage: !set <day> <time>')
        return
    day,time = args[0],args[1]
    fullday = {'mon':'monday','tue':'tuesday',
              'wed':'wednesday','thu':'thursday',
              'fri':'friday','sat':'saturday',
              'sun':'sunday'}
    if checkvalidset(day,time):
        wakeuptimes[day] = time
        await ctx.send(f'set wakeup time for {fullday[day]} to {time}')
    else:
        await ctx.send('wrong. idiot.')


bot.run('MTAzODUxNjcwMjY0NTg1ODM0NA.GfqTZb.3iecHuyKhVpkKalrw6YGODYzGyw9UvC0ASyNi0')