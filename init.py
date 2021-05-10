import discord
from discord.ext import commands
from cogs.database.db import PostgresBot

activity = discord.Activity(name='Fate Pre Alpha 0.1.5', type=discord.ActivityType.watching)
prefix = ["x","X","x ","X "]

bot = PostgresBot(command_prefix=prefix, case_insensitive=True,activity=activity)
bot.load_extension('cogs.Status')
bot.load_extension('cogs.client')
bot.load_extension('cogs.Pvp')
bot.load_extension('cogs.Inventory')
bot.load_extension('cogs.Economy')
#@bot.command()
#async def Fate(ctx):
#    embed=discord.Embed(name="__Message__",value=None,colour=discord.Color.random())
#    embed.add_field(name="__Message__",value="Please Give your suggestions for new bot Fate Here. It is in pre Alpha Right now . \nyou can also give bot logo too as an suggestion \n ||Already added many commands and characters||",inline=False)
#    embed.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
#    await ctx.send(embed=embed)


bot.run("ODI5MzM3MzA0ODYxNjM4Njk3.YG2qjQ.zD63-hog4TAUY_mNUEMkzNbIbpM") 
