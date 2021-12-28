import os
from discord.ext import commands
from dotenv import load_dotenv
from embeds import *
from classes.session import Session
from db_parameters import check_if_data_exist
from classes.character import Character


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
    if check_if_data_exist(table=Session, field=Session.id_discord, value=str(ctx.message.author.id)):
        await ctx.send("you are already register")
    else:
        Character(id_session=0, id_discord=str(ctx.message.author.id))
        await ctx.send("you have been register")


bot.run(os.getenv("TOKEN"))
