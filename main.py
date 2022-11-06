import discord
from discord.ext import commands,tasks
from events import intro,reminder
import time


intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True

bot = commands.Bot(command_prefix='!',intents=intents)
wakeuptimes = {'mon':'00:00','tue':'00:00','wed':'00:00','thu':'00:00','fri':'00:00','sat':'00:00','sun':'00:00',} #obsolete
weekdays = list(wakeuptimes.keys()) #as in, days of the week, not just mon-fri

users = {} #users is a dictionary where the Discord User objects are the keys that are mapped to
#the corresponding custom discorduser class (not to be confused with Discord.User) object that has the Discord.User object as one
#of its attributes
#lol


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

def gettoken(filename='C:\\Users\\malle\\sleep-bot\\events\\token.txt'):
    f = open(filename)
    token = f.readline()
    return token

def userexists(discorduser): #checks if there is a discorduser corresponding to the ctx.author usually
    return discorduser in users.keys()


# I am so sorry about this one
#self.wakeuptimes for user's wakeuptimes
#self.discord is the built-in Discord User class
#self.memb is the built-in Discord Member class
class discorduser():
    def __init__(self,discorduser):
        self.wakeuptimes = {'mon':'08:00','tue':'08:00',
                            'wed':'08:00','thu':'08:00',
                            'fri':'08:00','sat':'08:00',
                            'sun':'08:00',}
        self.count = 0
        self.discord = discorduser
        self.counting = True
        self.message = []
        self.mintime = 24*60

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    
#sus
@bot.command()
async def sus(ctx):
    await ctx.send('iposter')

#sends user to intro message and creates user object for them if it doesn't exist
#if the user includes the arguement "-" it will supress the output of intro
#starts timecheck loop if not running already
#user must use this command before bot can work
@bot.command()
async def start(ctx,*args):
    if not userexists(ctx.author):
        users[ctx.author] = discorduser(ctx.author) # I know. This is awful. But I am tired and need sleep. The irony.
        users[ctx.author].id = ctx.author.id
        users[ctx.author].memb = await commands.MemberConverter().convert(ctx,str(users[ctx.author].id))
   #await ctx.author.send('hi! give me your credit card information')
    start_suppress = False
    if len(args) == 1:
        if str(args[0]) == '-' :
            start_suppress = True
    if not start_suppress:
        await intro.main(ctx)
    if not timecheck.is_running():
        timecheck.start()

@bot.command()
async def info(ctx):
    await intro.main(ctx)

@bot.command()
async def message(ctx,*args):
    if not userexists(ctx.author):
        return
    user = users[ctx.author]
    user.message.append(' '.join(args))
    await user.discord.send('custom message added')


#sets the user's wake up times
@bot.command()
async def set(ctx,*args):
    if not userexists(ctx.author):
        return
    user = users[ctx.author]
    if len(args) != 2:
        await ctx.send('usage: !set <day> <time>')
        return
    day,time = args[0],args[1]
    fullday = {'mon':'monday','tue':'tuesday',
               'wed':'wednesday','thu':'thursday',
               'fri':'friday','sat':'saturday',
               'sun':'sunday'}
    if checkvalidset(day,time):
        user.wakeuptimes[day] = time
        await ctx.author.send(f'set wakeup time for {fullday[day]} to {time}')
    elif day == 'all':
        for d in user.wakeuptimes.keys():
            user.wakeuptimes[d] = time
        await ctx.author.send(f'set wakeup time for all to {time}')
    else:
        await ctx.send('usage: !set <day> <time>')

#gets the users wakeup times
@bot.command()
async def get(ctx,*args):
    if not userexists(ctx.author):
        return
    user = users[ctx.author] #theres gotta be a better way bro
    if len(args) == 0 or 'all' in args:
        for day in user.wakeuptimes.keys():
            await ctx.send(f'{day}: {user.wakeuptimes[day]}')
    for day in args:
        try:
            await ctx.send(f'{day}: {user.wakeuptimes[day]}')
        except:
            await ctx.send('!get <day> for any number of days \n or just !get for all 7 days')
            return

@bot.command()
async def pause(ctx):
    if not userexists(ctx.author):
        return
    users[ctx.author].counting = False
    await ctx.send('ok paused')

@bot.command()
async def play(ctx):
    if not userexists(ctx.author):
        return
    users[ctx.author].counting = True
    await ctx.send('counting your minutes!')

@bot.command()
async def cancel(ctx):
    if not userexists(ctx.author):
        await ctx.send('??? at least give us a chance (!start)')
        return
    await ctx.send('Goodbye. Type !start to restart services')
    del users[ctx.author]

@bot.command()
async def reset(ctx,*args):
    if not userexists(ctx.author):
        return
    user = users[ctx.author]
    if len(args)==0:
        args = 'all'
    for a in args:
        if a in ['all','message']: #me being quirky and doing a similar thing in entirely different ways across functions
            user.message = []
            await ctx.send('Reset messages')
        if a in ['all','times']:
            user.wakeuptimes = {'mon':'08:00','tue':'08:00','wed':'08:00',
                                'thu':'08:00','fri':'08:00','sat':'08:00',
                                'sun':'08:00',}
            await ctx.send('Reset times')

#uhhh dont worry about these commands
@bot.command()
async def saul(ctx):
    await ctx.send(file=discord.File('/home/ubuntu/sleep-bot/sleep-bot/saul.gif'))

@bot.command()
async def ltg(ctx):
    await ctx.send(file=discord.File('/home/ubuntu/sleep-bot/sleep-bot/ltg.gif'))

@tasks.loop(minutes = 1)
async def timecheck():
    for user in users.keys(): # what even is this
        u = users[user] #I am genuinely the worst object oriented programmer on the planet <-- future me here, scratch the oo part
        if u.counting:
            currenttime = time.localtime()
            wday = weekdays[currenttime.tm_wday]
            minutetime = currenttime.tm_hour*60 + currenttime.tm_min
            wakeupmin = int(u.wakeuptimes[wday][0:2])*60 + int(u.wakeuptimes[wday][3:])
            if wakeupmin < minutetime: #if the wakeuptime for the current day has already passed, use the next day's wakeuptime + 24h
                if wday != 'sun':
                    wday = weekdays[currenttime.tm_wday+1]
                else:
                    wday = 'mon'
                wakeupmin = wakeupmin = (int(u.wakeuptimes[wday][0:2])+24)*60 + int(u.wakeuptimes[wday][3:]) #what the fuck
                #         ^I could    ^just fix this but like genuinely what is going on here
            timediff = wakeupmin - minutetime #time in minutes to next wakeuptime
            pingfreq = 20 #how often the bot will bother you (minutes)
            if timediff/60 < 9: #annoyances start 9 hours from wakeup
                if (u.count%pingfreq == 0) and str(u.memb.raw_status) == 'online': #only pings if user is online (assumes online = awake)
                    if timediff < u.mintime: #keeps track of how close you were to your wakeuptime
                        u.mintime = timediff
                    await reminder.main(u,timediff)
                u.count +=1
            if timediff == 0:
                u.count = 0 #don't know why we do this actually
            print(currenttime)
            if wday == weekdays[currenttime.tm_wday] and minutetime == wakeupmin and u.mintime < 300: 
                # if you were awake less than 5 hours before waketime, prompts you for message at wakeuptime
                await u.discord.send(f'<@{u.id}> Noticed you had a rough sleep, you should leave a message for yourself \nUse "!message"')
                u.mintime = 24*60
        


#token = gettoken()
token = gettoken('/home/ubuntu/sleep-bot/sleep-bot/token.txt')
bot.run(token)