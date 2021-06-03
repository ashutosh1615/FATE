import discord
from discord.ext import commands,flags
import Characters 
import random
import decorators
  



class Inventory(commands.Cog):
  def __init__(self, bot:commands.Bot):
        self.bot = bot
  #self.bot.dispatch("level_up_card",exp,lvl)

  @decorators.db_user('no')
  @commands.command()
  async def start(self,ctx):
    ls=[]
    for v in vars(Characters).values():
      if isinstance(v,type):
        ls.append(v)
    luck=random.choice(ls)
    card = luck()
    query="""INSERT INTO profiles (username,id) VALUES (%s, %s)"""
    self.bot.cur.execute(query,(f'{ctx.author.name}',ctx.author.id))
    self.bot.conn.commit()
    self.bot.cur.execute("""INSERT Into inventory (card_name,player,lvl,exp,hp,atk,def,speed,spdef,spatk,love,critical,evasion,ability,ability_desc,image_url) Values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",(card.card_name,ctx.author.id,card.lvl,card.exp,card.hp,card.atk,card.defence,card.spd,card.spdef,card.spatk,card.love,card.critical,card.evasion,card.ability,card.ability_desc,card.image))
    self.bot.conn.commit()
    embed = discord.Embed(title=f'**Welcome**',description=f"Congratulation you have entered to decide your fate check out commands and how to play guide using ```xhplay and xhelp``` you have been awarded 500g and {card.card_name} hero at starting of your journey",colour = discord.Color.random())
    await ctx.send(embed=embed)
   
  @decorators.db_user()
  @commands.command()
  async def inv(self,ctx):
    embed = discord.Embed(title="Inventory", description="use x<catagory> for further details", colour=discord.Color.random())
    embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    embed.add_field(name="Heroes", value= "all your heroes here" ,inline=False)
    embed.add_field(name="Lootboxes", value="all your lootboxes here", inline=True)
    embed.add_field(name="items", value="all your items here", inline=True)
    await ctx.send(embed=embed)
    
  @commands.is_owner()  
  @decorators.db_user()
  @commands.command()
  async def add_card(self,ctx):
    ls=[]
    for v in vars(Characters).values():
      if isinstance(v,type):
        ls.append(v)
    luck=random.choice(ls)
    card = luck()
    self.bot.cur.execute("""INSERT Into inventory (card_name,player,lvl,exp,hp,atk,def,speed,spdef,spatk,love,critical,evasion,ability,ability_desc,image_url) Values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",(card.card_name,ctx.author.id,card.lvl,card.exp,card.hp,card.atk,card.defence,card.spd,card.spdef,card.spatk,card.love,card.critical,card.evasion,card.ability,card.ability_desc,card.image))
    self.bot.conn.commit()
    await ctx.send("added boss")

  @decorators.db_user()
  @commands.command()
  async def select(self,ctx,message):
    embed=discord.Embed(name = "**Card selection**",description=f"usage xselect <card_id>",colour=discord.Color.random())
    embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    self.bot.cur.execute("select index,lvl,card_name from inventory where player=%s",(ctx.author.id,))
    ls=self.bot.cur.fetchall()
    card_id=0
    card_lvl=None
    card_name=None
    for i in range(1,len(ls)+1):
      if i == int(message):
        card_id=ls[i-1][0]
        card_lvl=ls[i-1][1]
        card_name=ls[i-1][2]

    if card_id!=0:
      self.bot.cur.execute(""" Update profiles set selection = %s where id=%s""",(card_id,ctx.author.id))
      self.bot.conn.commit()
      embed.add_field(name="**Success**",value=f"You have selected **LEVEL: {card_lvl} {card_name}** from your inventory",inline=False)  
    else:
      embed.add_field(name="**Error**",value=f"Please Provide a Valid Value That exist in your inventory",inline=False)
    await ctx.send(embed=embed)
    
  @commands.command()
  async def ihero(self,ctx,*,message):
    self.bot.cur.execute("""select card_name,series,atk,hp,def,speed,spdef,spatk,ability,ability_desc,image_url from dex where card_name ilike %s""",('%'+message+'%',))    
    ls=self.bot.cur.fetchone()
    embed=discord.Embed(name=None, title=None, color=discord.Color.random())
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.set_image(url=ls[10])
    self.bot.cur.execute("""select series_name from series where index=%s""",(ls[1],))
    series_=self.bot.cur.fetchone()[0]
    embed.add_field(name=f"{ls[0]} from Series{series_}", value=f"**HP:** {ls[3]} \n**ATK:** {ls[2]}\n**DEFENCE:** {ls[4]}\n**SPEED:** {ls[5]}\n**SPECIAL ATTACK:** {ls[6]}\n**SPECIAL DEFENCE:** {ls[7]} ", inline=False)
    embed.add_field(name="ABILITY",value=f"**{ls[8]}:** {ls[9]}",inline=False)
    await ctx.send(embed=embed)    
        
      

  @decorators.db_user()
  @commands.command(aliases = ['hero'])  
  async def heroes(self,ctx):
      
      self.bot.cur.execute("""select index,card_name,lvl,ability from inventory where player = %s""",(ctx.author.id,))
      ls = self.bot.cur.fetchall()
      pages=[]
      x=0

      for j in range((len(ls)//10)+1):
        pages.append(discord.Embed(title="Heroes", description="These are the heroes you own", colour=discord.Color.random()))
        pages[j].set_author(name=ctx.author, icon_url=ctx.author.avatar_url)  
        pages[j].set_footer(text=f"Page :{j+1}/{(len(ls)//10)+1} | Hero {(len(ls)%10)+j*10}/{len(ls)}")
      for i in range(len(ls)):
        ls_=ls[i]
        pages[x].add_field(name=f"**#{i+1} | {ls_[1]} | LVL {ls_[2]}**", value= f"Ability {ls_[3]} | id : {ls_[0]}",inline=False)
        if ((i+1) % 10) ==0:
          x=x+1   
      message = await ctx.send(embed=pages[0])
      await decorators.page(ctx,message,(len(ls)//10),pages)

  #@decorators.db_user()
  #@command.command(aliases=)    

 #   @commands.cog.listener()
  #  async def on_level_up_card(self,lvl):
  """
  @commands.is_owner()
  @commands.command()
  async def up(self,ctx):          
        for v in vars(Characters).values():
            if isinstance(v,type):
                card=v()

                self.bot.cur.execute("select exists(select ability from dex where ability =%s)",(card.ability,))
                if self.bot.cur.fetchone()[0]:
                    print("exists")
                else:
                    self.bot.cur.execute("insert into dex(card_name,series,atk,hp,def, speed,spdef ,spatk ,love ,critical ,evasion , ability ,ability_desc,image_url) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(card.card_name,card.series,card.atk,card.hp,card.defence,card.spd,card.spdef,card.spatk,card.love,card.critical,card.evasion,card.ability,card.ability_desc,card.image))
                    self.bot.conn.commit()
                    """

  @flags.add_flag('-s','--series')
  @flags.command()                  
  async def dex(self,ctx,**flags):
    
    ls=[]
    x=0
    pages=[]
    if flags['series'] !=None:
      self.bot.cur.execute("""select index from series where series_name ilike %s""",('%'+flags['series']+'%',))
      series_ = self.bot.cur.fetchone()[0]
      self.bot.cur.execute("""select index,card_name,ability,hp,atk,def,speed,spatk,spdef from dex where series = %s """,(series_,))
      ls=self.bot.cur.fetchall()
    else:
      self.bot.cur.execute("""select index,card_name,ability,hp,atk,def,speed,spatk,spdef from dex """)
      ls=self.bot.cur.fetchall()
    for j in range((len(ls)//10)+1):
      pages.append(discord.Embed(title="HERO DEX", description="These are the heroes present in game", colour=discord.Color.random()))
      pages[j].set_author(name=ctx.author, icon_url=ctx.author.avatar_url)  
      pages[j].set_footer(text=f"Page :{j+1}/{(len(ls)//10)+1}")
    for i in range(len(ls)):    
      ls_=ls[i]
      pages[x].add_field(name=f"**ID:{ls_[0]} | {ls_[1]} | Ability {ls_[2]}**", value= f"**HP:** {ls_[3]} | **Atk:** {ls_[4]} | **DEF:** {ls_[5]} | **SPD:** {ls_[6]} | **SPATK:** {ls_[7]} | **SPDEF:** {ls_[8]} ",inline=False)
      if ((i+1) % 10) ==0:
        x=x+1   
    message = await ctx.send(embed=pages[0])
    await decorators.page(ctx,message,(len(ls)//10),pages)








def setup(bot:commands.Bot):
    bot.add_cog(Inventory(bot))



