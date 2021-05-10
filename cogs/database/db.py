#importing
import psycopg2
import discord
from discord.ext import commands
from cogs.database.config import config




#connecting to the database
class PostgresBot(commands.Bot):
 def __init__(self,*args,**kwargs):
     self.cur = None
     self.conn = None
     self.params=None
     super().__init__(*args,**kwargs)  
 async def start(self, *args, **kwargs):
    try:
        #read connection parameters
        self.params=config()
        #connecting to postgresql server
        print('connecting to the postgresql database...')
        self.conn = psycopg2.connect(**self.params)
        self.cur = self.conn.cursor()
        return await super().start(*args,**kwargs)
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    
  





