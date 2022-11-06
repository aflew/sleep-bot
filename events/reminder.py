from math import trunc
async def main(user,timediff):
    person = user.discord
    if "online" == "online" and timediff != 0:
        await user.discord.send(f'{trunc(timediff/60)}:{timediff%60} before you have to wake up')
        if timediff >= 420 and timediff <540:
            await user.discord.send('You should probably get to bed')
        if timediff >=300 and timediff < 420:
            await user.discord.send('You should go to sleep - for real this time')
        if timediff < 300:
            await user.discord.send('I am rapidly aproaching your location \nGo to sleep NOW')
    pass
