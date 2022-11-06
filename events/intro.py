from asyncio import sleep
async def main(ctx):
    await ctx.author.send('Welcome to Sleep Bot! \n Sleep Bot is a simple bot that will remind you to go to sleep. \nWhether the time slipped away from you, or you have forgotten the consequences of a poor sleep, Sleep Bot will be there to remind you its time get to bed')
    await sleep(1.5)
    await ctx.author.send('\nWe do this in 3 simple ways. \
    \n1. Starting 9 hours from your wake up time, Sleep Bot will send you a reminder every 20 minutes to get to bed \
    \n2. If you wake up after a bad sleep, we encourage you to input at "!message" with a testimonial of how you feel \
    \n3. On future nights, if you are still active <5 hours from your wakeup time, it will then send one of your random testimonials.\n \n')
    await sleep(1.5)
    await ctx.author.send('You initiated Sleep Bot by inputting "!start" you can also initiate and suppress intro with "!start -". If you would like to remove Sleep Bot and its data, input "!cancel". \
    \nIf you would like to pause sleep bot for any given amount of time, input "!pause" to stop the service and "!play" to restart it.\n')
    await ctx.author.send('To resend the introduction, input "!info"\n')
    await sleep(1.5)
    await ctx.author.send('To begin, what time would you like to wake up each day? \n(format: !set mon 06:30)')
    await ctx.author.send('You can change your wake up times at any point using the same format. \n Use the input "!get" to see what times you have set for the whole week \n\
    or "!get <day>" (ex. "!get mon") for specific days.')
    await ctx.author.send('\nNote: We use a 24 hour clock')

    
    