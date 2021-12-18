import os
from discord.ext import commands
from dotenv import load_dotenv
from embeds import *


load_dotenv()
bot = commands.Bot(command_prefix='/')


@bot.command(name='p')
async def profile(ctx):
    embed = embeds_profile(ctx)
    await ctx.send(embed=embed)


@bot.command(name='i')
async def inventory(ctx):
    await ctx.send("show inventory")


@bot.command(name='r')
async def register(ctx):
    file = open('data.json', 'w+')
    data = '{' + f"\"{ctx.message.author.id}\": {{}}" + '}'
    file.write(data)
    await ctx.send("you have been registered")


bot.run(os.getenv("TOKEN"))
