import discord
from discord.ext import commands,tasks
from events import intro,reminder
import time


intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True

bot = commands.Bot(command_prefix='!',intents=intents)
wakeuptimes = {'mon':'00:00','tue':'00:00','wed':'00:00','thu':'00:00','fri':'00:00','sat':'00:00','sun':'00:00',}
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

def userexists(discordId):
    return discordId in users.keys()

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

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    
#sus
@bot.command()
async def sus(ctx):
    await ctx.send('iposter')

#sends user to intro message and creates user object for them
@bot.command()
async def start(ctx,*args):
    if not userexists(ctx.author):
        users[ctx.author] = discorduser(ctx.author) # I know. This is awful. But I am tired and need sleep. The irony.
        users[ctx.author].id = ctx.author.id
        users[ctx.author].memb = await commands.MemberConverter().convert(ctx,str(users[ctx.author].id))
    await ctx.send('hi! give me your credit card information')
    await intro.main(ctx)
    if not timecheck.is_running():
        timecheck.start()

@bot.command()
async def info(ctx):
    await intro.main(ctx)

@bot.command()
async def message(ctx,*args):
    user = users[ctx.author]
    user.message.append(' '.join(args))
    await user.discord.send('custom message added')


#sets the user's wake up times
@bot.command()
async def set(ctx,*args):
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
    else:
        await ctx.send('wrong. idiot.')

#gets the users wakeup times
@bot.command()
async def get(ctx,*args):
    user = users[ctx.author] #theres gotta be a better way bro
    if len(args) == 0:
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
    users[ctx.author].counting = False
    await ctx.send('ok paused')

@bot.command()
async def play(ctx):
    users[ctx.author].counting = True
    await ctx.send('counting your minutes!')

@tasks.loop(minutes = 1)
async def timecheck():
    for user in users.keys():
        u = users[user] #I am genuinely the worst object oriented programmer on the planet
        if u.counting:
            currenttime = time.localtime()
            wday = weekdays[currenttime.tm_wday]
            minutetime = currenttime.tm_hour*60 + currenttime.tm_min
            wakeupmin = int(u.wakeuptimes[wday][0:2])*60 + int(u.wakeuptimes[wday][3:])
            if wakeupmin < minutetime:
                wday = weekdays[currenttime.tm_wday+1]
                wakeupmin = wakeupmin = (int(u.wakeuptimes[wday][0:2])+24)*60 + int(u.wakeuptimes[wday][3:])
            timediff = wakeupmin - minutetime
            pingfreq = 1
            if timediff/60 < 9:
                #print(u.memb.raw_status)
                #print(str(u.memb.raw_status) == 'online')
                #print(str(u.memb.status) == 'online')
                if (u.count%pingfreq == 0) and str(u.memb.raw_status) == 'online':
                    #check if user is active somehow
                    #if user active and timediff<mintimediff
                        #mintimediff = timediff
                    #if mintimediff - timediff > 30 and not init_nextday
                        #person is hopefully asleep
                        #initiate next day program
                        #init_nextday = true
                    await reminder.main(u,timediff) #pass status into this func
                u.count +=1
            if timediff == 0:
                u.count = 0
            print(currenttime)

#token = gettoken()
token = gettoken('/home/ubuntu/sleep-bot/sleep-bot/token.txt')
bot.run(token)