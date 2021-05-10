import discord
import math,random
import decorators 
from discord.ext import commands
  

class clients(commands.Cog):
  def __init__(self,bot : commands.Bot):
    self.bot=bot  



 


  
  
  @commands.command(aliases = ['p','player'])
  @decorators.db_user()
  async def profile(self,ctx):
    self.bot.cur.execute('''SELECT username,gold,exp,lvl,selection,orbs From profiles where id = %s''',(ctx.author.id,))
    ls =  self.bot.cur.fetchone()
    embed = discord.Embed(title=f'**{ls[0]}\' Profile**',description=None,colour = discord.Color.random())
    embed.add_field(name="**Lvl**",value=f"{ls[3]}")
    embed.add_field(name=f"**Exp**",value=f"{ls[2]}/{math.floor(20*(ls[3]**1.5))}")
    embed.add_field(name="**Gold**",value=f"{ls[1]}<:gold:832880401365204992>",inline=False)
    embed.add_field(name="**Orbs**",value=f"{ls[5]} <:orb:832881276889071646>",inline=False)
    self.bot.cur.execute('''select card_name from inventory where index = %s''',(ls[4],))
    ls_ = self.bot.cur.fetchone()
    if ls_ == None:
      embed.add_field(name="**Selected Card**",value=f"{ls_}")
    else:
      embed.add_field(name="**Selected Card**",value=f"{ls_[0]}")
    await ctx.send(embed=embed)
      


"""


  @commands.Cog.listener()
  async def on_levelup(self):
    if exp >= 20*(self.lvl**1.5):
      self.lvl=self.lvl + 1
      exp=exp-(20*self.lvl**1.5)
    
  @commands.command()
  async def select(self,ctx,*):
    


  @commands.Cog.listener()
  async def on_exp(self):
    pass"""




def setup(bot:commands.Bot):
  bot.add_cog(clients(bot))
