import discord
from discord.ext import commands
class Status(commands.Cog):

    def __init__(self, bot : commands.bot):
        self.bot= bot

    @commands.command()
    async def ping(self, ctx: commands.Context):
        embed_var = discord.Embed(title = 'Ping',description= f"pong! {round(self.bot.latency*1000)}ms",color = discord.Color.random())
        await ctx.send(embed=embed_var)    

    @commands.command(name = "server")
    async def servers(self,ctx):
            embed_var = discord.Embed(title = 'Server',description=f"Bot is in {str(len(self.bot.guilds))} servers",color = discord.Color.random())
            await ctx.send(embed=embed_var)

def setup(bot: commands.Bot):
    bot.add_cog(Status(bot))