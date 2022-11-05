import discord
from discord.ext import commands,tasks
from events import intro
import time


intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!',intents=intents)
wakeuptimes = {'mon':None,'tue':None,'wed':None,'thu':None,'fri':None,'sat':None,'sun':None}
weekdays = wakeuptimes.keys() #as in, days of the week, not just mon-fri

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
    timecheck.start()

#sus
@bot.command()
async def sus(ctx):
    await ctx.send('iposter')

#sends user to intro message
@bot.command()
async def start(ctx):
    await ctx.send('hi! give me your credit card information')
    await intro.main(ctx,bot)

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

@tasks.loop(minutes=1)
async def timecheck():
    currenttime = time.localtime()

    print(currenttime)
    pass


bot.run('MTAzODUxNjcwMjY0NTg1ODM0NA.GfqTZb.3iecHuyKhVpkKalrw6YGODYzGyw9UvC0ASyNi0')