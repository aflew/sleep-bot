
async def main(ctx):
    await ctx.send('Welcome to Sleep Bot! \n Sleep Bot is a simple bot that will remind you to go to sleep. Whether the time slipped away from you, or you have forgotten the consequences of a poor sleep, Sleep Bot will be there to remind you its time to sleep')
    await ctx.send('We do this in 3 simple ways. \
    \n1. Starting 9 hours from your wake up time, Sleep Bot will send you a reminder every 20 minutes to get to bed \
    \n2. If sleep bot notices that you were active < 6 hours before your wake up time, it will prompt you the next day and ask you how you feel\
    \n3. On future nights, if Sleep Bot has sent 4 notifications and you are still active, it will then send a random testimonial from yourself about how you felt after a bad sleep')
    await ctx.send('You initiated Sleep Bot by inputting "!start". If you would like to remove Sleep Bot and its data, input "!cancel". \
    If you would like to pause sleep bot for any given amount of time, input "!pause" to stop the service and "!play" to restart it.')
    await ctx.send('To begin, What time would you like to wake up each day?')
    await ctx.send('Use this format: !set mon 06:30')
    await ctx.send('You can change your wake up times at any point using the same format. \n Use the input "!get" to see what times you have set for the whole week \
    or "!get (day)" (ex. "!get mon") for specific days.')
    await ctx.send('To resend the introduction, input "!intro".')
    
    