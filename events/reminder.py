from math import trunc
async def main(user,timediff):
    await user.discord.send(f'{trunc(timediff/60)}:{timediff%60} before you have to wake up')
    if timediff < 300:
        await user.discord.send('I am rapidly approaching your location')
        await user.discord.send('you should go to sleep NOW')
    pass