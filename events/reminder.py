from math import trunc
from random import randint
async def main(user,timediff):
    if timediff != 0:
        await user.discord.send(f"{trunc(timediff/60):0>2}:{timediff%60:0>2} before you have to wake up")
        if timediff >= 420 and timediff <540:
            await user.discord.send(f'<@{user.id}> You should probably get to bed')
        if timediff >=300 and timediff < 420:
            await user.discord.send(f'<@{user.id}> You should go to sleep - for real this time')
        if timediff < 300:
            await user.discord.send(f'<@{user.id}> I am rapidly aproaching your location \nGo to sleep NOW')
            if user.message != []:
                await user.discord.send(f'Last time You slept this little, this is how you felt: \n"{user.message[randint(0,len(user.message)-1)]}"')