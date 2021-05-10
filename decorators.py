import discord
from discord.ext import commands 



def db_user(need="yes"):
    async def check_user(ctx):   
     ctx.bot.cur.execute('''select exists(select id from profiles where id=%s)''',(ctx.message.author.id,))
     if ctx.bot.cur.fetchone()[0]:
        if need=="yes":
          return True
        elif need=="no":
          embed=discord.Embed(title='Already registered in game',description='Use ```Xhelp and xhplay``` for knowing more about the game',colour=discord.Color.random())
          await ctx.send(embed=embed)  
          return False  
     else:
          if need == "yes":
            embed=discord.Embed(title='Not registered in game',description='Use ```Xstart``` for registering the game',colour=discord.Color.random())
            await ctx.send(embed=embed)  
            return False
          elif need=="no":
            return True       
    return commands.check(check_user)

async def page(ctx,message,number,pages):
    await message.add_reaction('⏮')
    await message.add_reaction('◀')
    await message.add_reaction('▶')
    await message.add_reaction('🗑')
    def check(reaction, user):
        return user == ctx.author
    i = 0
    reaction = None
  
    while True:  
        if str(reaction) == '⏮':
            i = 0
            await message.edit(embed = pages[i])
        elif str(reaction) == '◀':
            if i > 0:
                i -= 1
                await message.edit(embed = pages[i])
        elif str(reaction) == '▶':
            if i <= number:
                i += 1
                await message.edit(embed = pages[i])
        elif str(reaction) == '🗑':
            await message.delete()
        
        try:
            reaction, user = await ctx.bot.wait_for('reaction_add', timeout = 30.0, check = check)
            await message.remove_reaction(reaction, user)
        except:
            break
    await message.clear_reactions()
