import discord
from discord.ext import commands,tasks
from events import intro,reminder
#import pymongo
#from pymongo import MongoClient
#import intro
import time


intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!',intents=intents)
wakeuptimes = {'mon':'00:00','tue':'00:00','wed':'00:00','thu':'00:00','fri':'00:00','sat':'00:00','sun':'00:00',}
weekdays = list(wakeuptimes.keys()) #as in, days of the week, not just mon-fri


def checkvalidset(day,time):
    if day not in weekdays:
        return False
    if len(time) != 5:
        return False
    if int(time[0:2]) > 23:
        return False
    if int(time[3:]) > 59:
        return False
    if time[2] != ':':
        return False
    return True


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    

#sus
@bot.command()
async def sus(ctx):
    await ctx.send('iposter')

#sends user to intro message
@bot.command()
async def start(ctx):
    await ctx.send('hi! give me your credit card information')
    await intro.main(ctx,bot)
    count = 0
    timecheck.start(1)

#sets the user's wake up times
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

#gets the users wakeup times
@bot.command()
async def get(ctx,*args):
    if len(args) == 0:
        for day in wakeuptimes.keys():
            await ctx.send(f'{day}: {wakeuptimes[day]}')
    for day in args:
        try:
            await ctx.send(f'{day}: {wakeuptimes[day]}')
        except:
            await ctx.send('!gettimes <day> for any number of days \n or just !gettimes for all 7 days')
            return

@bot.command()
async def pause(ctx):
    timecheck.cancel()

@tasks.loop(seconds = 10)
async def timecheck(count):
    currenttime = time.localtime()
    wday = weekdays[currenttime.tm_wday]
    minutetime = currenttime.tm_hour*60 + currenttime.tm_min
    wakeupmin = int(wakeuptimes[wday][0:2])*60 + int(wakeuptimes[wday][3:])
    if wakeupmin < minutetime:
        wday = weekdays[currenttime.tm_wday+1]
        wakeupmin = wakeupmin = (int(wakeuptimes[wday][0:2])+24)*60 + int(wakeuptimes[wday][3:])
    timediff = wakeupmin - minutetime
    if timediff/60 < 9 and timediff > 0:
        if count % 5 == 0:
            await reminder.main(bot)
        count +=1
    if timediff == 0:
        count = 0
    print(currenttime)


bot.run('MTAzODUxNjcwMjY0NTg1ODM0NA.GfqTZb.3iecHuyKhVpkKalrw6YGODYzGyw9UvC0ASyNi0')