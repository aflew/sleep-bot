import discord
from discord.ext import commands
from events import intro


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
    for i,letter in enumerate(time):
        if i == 2:
            if letter != ':':
                return False
        else:
            if not letter.isnum():
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
async def set(ctx,day,time):
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