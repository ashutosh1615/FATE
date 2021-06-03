import discord
from discord.ext import commands
import Characters
import math,random,time

def ability_check(card_bt):
    for v in vars(Characters).values():
        if isinstance(v,type):
            card=v()
            if card.card_name==card_bt.card_name:
                return card.ability_worker(card_bt)


      
def dmg(r,cardatk,carddef):
    if r == 100:
        return int(round((((cardatk.atk/carddef.defence)*(cardatk.spatk/carddef.spdef)*(cardatk.atk+cardatk.spatk))/3*(150/100)*cardatk.lvl),1)) 
    else:
        return int(round((((cardatk.atk/carddef.defence)+(cardatk.spatk/carddef.spdef)*(cardatk.atk+cardatk.spatk))/3),1)) 
class Battler():
    def __init__(self,card_name,card_owner,lvl,atk,hp,defence,spd,spdef,spatk,evasion,critical,image,ability):
        self.card_name=card_name
        self.card_owner=card_owner
        self.lvl=lvl
        self.procc=1
        self.atk=int(atk+(lvl**0.75))
        self.hp=int((hp+(lvl**0.75))*10)
        self.defence=int(defence+(lvl**0.75))
        self.spd=int(spd+(lvl**0.75))
        self.spdef=int(spdef+(lvl**0.75))
        self.spatk=int(spatk+(lvl**0.75))
        self.evasion=evasion
        self.critical = critical
        self.image=image
        self.ability=ability
        self.critical=False

        self.hp_base=int((hp+(lvl**0.75))*10)
        self.atk_base=int(atk+(lvl**0.75))
        self.defence_base=int(defence+(lvl**0.75))
        self.spatk_base=int(spatk+(lvl**0.75))
        self.spdef_base=int(spdef+(lvl**0.75))


    def check_turn(self,enemy,user):
        if enemy.spd >= user.spd:
            card1=enemy
            card2=user
        else:
            card1=user
            card2=enemy
        return [card1,card2]


    def calculate(self,cardatk,carddef):
        damage=0
 
        r=random.randint(cardatk.critical,100)
        if r==100:
            cardatk.critical=True
        e=random.randint(carddef.evasion,100)
        damage=dmg(r,cardatk,carddef)

        if e==100:
            damage=0                         
        if carddef.hp<damage:
                damage=carddef.hp
                carddef.hp=0
        else:   
                carddef.hp=carddef.hp-damage
              
        return damage
       
                   



            




class PVP(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot



    @commands.max_concurrency(1,per=commands.BucketType.user)
    @commands.command(aliases=['tr','train'])
    async def Training(self,ctx):
        self.bot.cur.execute("""select card_name,lvl,atk,hp,def,speed,spdef,spatk,evasion,critical,image_url,ability from inventory where index=(select selection from profiles where id = %s)""",(ctx.author.id,))
        ls=self.bot.cur.fetchone()
        user_card=Battler(ls[0],f"__{ctx.author.name}__'s {ls[0]}",ls[1],ls[2],ls[3],ls[4],ls[5],ls[6],ls[7],ls[8],ls[9],ls[10],ls[11])
        ls_=[]
        for v in vars(Characters).values():
            if isinstance(v,type):
                ls_.append(v)
        luck=random.choice(ls_)
        ecard = luck()
        enemy=Battler(ecard.card_name,f"__Enemy's__ {ecard.card_name}",ls[1],ecard.atk,ecard.hp,ecard.defence,ecard.spd,ecard.spdef,ecard.spatk,ecard.evasion,ecard.critical,ecard.image,ecard.ability)
        embed=discord.Embed(Name = "Test BT", value = None,colour = discord.Color.random())
        embed.add_field(name="Test BT",value=f"{ctx.author.name}'s Level {user_card.lvl} {user_card.card_name}\n **Ability**: __{user_card.ability}__ \n **{user_card.hp}/{user_card.hp_base}<:heart_3:829286810117996555>** \n\nEnemy's Level {enemy.lvl} {enemy.card_name}\n **Ability**: __{enemy.ability}__ \n **{enemy.hp}/{enemy.hp_base}<:heart_3:829286810117996555>** ",inline=False)
        embed.set_image(url=enemy.image)
        embed.set_thumbnail(url=user_card.image)
        message=await ctx.send(embed=embed)

        for i in range (1,16):  
            cards=user_card.check_turn(enemy,user_card)
            round=[discord.Embed(Name = "Test BT", value = None,colour = discord.Color.random()),discord.Embed(Name = "Test BT", value = None,colour = discord.Color.random())]
            for j in range(0,2):
                position=""
                statement="."

                damage=user_card.calculate(cards[0],cards[1])
                round[j].set_image(url=enemy.image)
                round[j].set_thumbnail(url=user_card.image)
                statement=ability_check(cards[0])


                if j==0:
                    position="**Faster speed**"
                elif j==1:
                     position="has got his **turn**"
            
                if damage==0:
                    round[j].add_field(name="Test BT",value=f"{ctx.author.name}'s Level {user_card.lvl} {user_card.card_name}\n **Ability**: __{user_card.ability}__ \n **{user_card.hp}/{user_card.hp_base}<:heart_3:829286810117996555>** \n\nEnemy's Level {enemy.lvl} {enemy.card_name}\n **Ability**: __{enemy.ability}__ \n **{enemy.hp}/{enemy.hp_base}<:heart_3:829286810117996555>** \n\n**Round {i}** \n {cards[0].card_owner} has {position} it strikes  {statement}\n {cards[1].card_owner} evades the attack ",inline=False)
                else:
                    if cards[0].critical:
                        round[j].add_field(name="Test BT",value=f"{ctx.author.name}'s Level {user_card.lvl} {user_card.card_name}\n **Ability**: __{user_card.ability}__ \n **{user_card.hp}/{user_card.hp_base}<:heart_3:829286810117996555>** \n\nEnemy's Level {enemy.lvl} {enemy.card_name}\n **Ability**: __{enemy.ability}__ \n **{enemy.hp}/{enemy.hp_base}<:heart_3:829286810117996555>** \n\n**Round {i}** \n {cards[0].card_owner} has {position} it strikes {statement}\n {cards[0].card_owner} did a critical hit doing {damage}",inline=False)
                        cards[0].critical=False
                    else:        
                        round[j].add_field(name="Test BT",value=f"{ctx.author.name}'s Level {user_card.lvl} {user_card.card_name}\n **Ability**: __{user_card.ability}__ \n **{user_card.hp}/{user_card.hp_base}<:heart_3:829286810117996555>** \n\nEnemy's Level {enemy.lvl} {enemy.card_name}\n **Ability**: __{enemy.ability}__ \n **{enemy.hp}/{enemy.hp_base}<:heart_3:829286810117996555>** \n\n**Round {i}** \n {cards[0].card_owner} has {position} it strikes  {statement}\n {cards[0].card_owner} did {damage} ",inline=False)
                cards[0],cards[1]=cards[1],cards[0]
                await message.edit(embed = round[j])
                time.sleep(1.5)                   
            cards[0].procc+=1

            if i==15 or user_card.hp<=0 or enemy.hp<=0:
                embed_final=discord.Embed(name=None, description=None, colour=discord.Color.random())
                embed_final.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
                if user_card.hp<=0:
                    embed_final.add_field(name="Failure <:lol:813848273155915846>", value="You lose dumbo be a better hero", inline=False)
                else:
                    orb=random.randint(1,3)
                    self.bot.cur.execute(f"""update profiles set orbs=orbs+{orb} where id = {ctx.author.id}""")
                    self.bot.conn.commit()
                    embed_final.add_field(name="Success <a:LoveDance:821236689216340014>", value=f"You defeated the enemy {enemy.card_name} Nice job \n You have been awarded with {orb} orbs", inline=False)
                    #embed_final.add_field(name="Success <a:LoveDance:821236689216340014>", value=f"You defeated the enemy {enemy.card_name} Nice job", inline=False)

                await ctx.send(embed=embed_final)
                break


        

    
def setup(bot:commands.Bot):
    bot.add_cog(PVP(bot))
