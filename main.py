import discord
from discord.ext import commands
import intro

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!',intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def sus(ctx):
    await ctx.send('iposter')

@bot.command()
async def start(ctx):
    await ctx.send('hi! give me your credit card information')
    await intro.main(bot)

bot.run('MTAzODUxNjcwMjY0NTg1ODM0NA.GfqTZb.3iecHuyKhVpkKalrw6YGODYzGyw9UvC0ASyNi0')