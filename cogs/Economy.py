import discord
from discord.ext import commands


class Economy(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
    
    @commands.group(aliases=['orb','ob'],invoke_without_command=True)
    async def orbs(self,ctx):
        embed=discord.Embed(name= None, value=None, color=discord.Color.random())
        embed.add_field(name="Usage", value="```xorb sell <number of orbs>``` and ```xorb use <card no you want to enchant> [-n for specifying number of orb to use]```", inline=False)
        await ctx.send(embed=embed)
    
   # @flags.add_flag('-n','--number')
   # @orbs.command()
   # async def use(message):
   #     card=message
   #     self.bot.cur.execute("""select exists(select orbs from profiles where id=%s and orbs=%s)""",(ctx.author.id,ls[0]))
   #     if self.bot.cur.fetchone()[0]:
   #         exp=ls[0]
   #         self.bot.cur.execute(update)

    @orbs.command()
    async def sell(self,ctx,message):
        def check(reaction, user):
            return user == ctx.author
        embed=discord.Embed(name="", value="", color=discord.Color.random())
       

        self.bot.cur.execute("""select exists(select orbs from profiles where id =%s and orbs>=%s) """,(ctx.author.id,int(message)))  
        if self.bot.cur.fetchone()[0]:
            gd = int(message)*100
            reaction=None
            embed.add_field(name="__SELL__",value=f"You are Selling your {int(message)} orbs and getting {gd} __Gold__")
            selling_msg=await ctx.send(embed=embed)
            await selling_msg.add_reaction('☑')
            await selling_msg.add_reaction('❌')
            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout = 30.0, check = check) 
            except:
                await selling_msg.delete()
            
            if str(reaction)=='☑':
                self.bot.cur.execute("""update profiles set gold = gold+%s,orbs = orbs -%s where id = %s""",(gd,int(message),ctx.author.id))
                self.bot.conn.commit()
                await selling_msg.delete()
                embed_sus=discord.Embed(name=None,value=None,color=discord.Color.random())
                embed_sus.add_field(name="__SUCCESS__",value=f"You sold your {int(message)} orbs and get {gd} gold in return")           
                await ctx.send(embed=embed_sus)
            elif str(reaction)=='❌':
                await selling_msg.delete()
                
            
        else:
            embed.add_field(name="Error",value="You dont have enough __orbs__ You stated to sell")
            await ctx.send(embed=embed)

def setup(bot:commands.Bot):
    bot.add_cog(Economy(bot))