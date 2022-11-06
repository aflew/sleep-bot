from math import trunc
from random import randint
import discord
async def main(user,timediff):
    neutral = [' before you have to wake up',' until the next day begins',' before the cycle begins anew'," before your planned time to wake up"]
    stern = ['You should probably get to bed','Your precious hours of sleep are dwindling','Going to sleep now would really be nice for you',
             'Think about how nice it will feel after a full sleep']
    mad = ['You should go to sleep - for real this time',"You're going to regret this, bozo",
           '"Surely nothing will go wrong if I stay up this late"- WRONG']
    custom = ['Last time you slept this little, this is how you felt:',"Here's a message from the past:",
              "There's no one you can trust more than yourself:","This is how you're going to be feeling when you wake up:"]
    if timediff != 0:
        await user.discord.send(f"{trunc(timediff/60):0>2}:{timediff%60:0>2}{neutral[randint(0,len(neutral)-1)]}")
        if timediff >= 420 and timediff <540:
            await user.discord.send(f'<@{user.id}> {stern[randint(0,len(stern)-1)]}\n\n ')
        if timediff >=300 and timediff < 420:
            await user.discord.send(f'<@{user.id}> {mad[randint(0,len(mad)-1)]}\n\n ')
        if timediff < 300:
            await user.discord.send(f'<@{user.id}> I am rapidly aproaching your location \nGo to sleep NOW\n\n ')
            if user.message != []:
                await user.discord.send(f'{custom[randint(0,len(custom)-1)]} \n"{user.message[randint(0,len(user.message)-1)]}"\n\n ')
    if randint(1,100) == 100:
        await user.discord.send(file=discord.File('/home/ubuntu/sleep-bot/sleep-bot/saul.gif'))