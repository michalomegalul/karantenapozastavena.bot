import discord
from discord.ext import commands, tasks
from keep_alive import keep_alive
import datetime
datetime.datetime.now()
datetime.datetime(2012, 3, 23, 23, 24, 55, 173504)
import requests
import json
import random
from replit import db
import os
import requests
import json
import asyncio
from itertools import cycle
from random import randint


from main_cog import main_cog
from music_cog import music_cog


bot = commands.Bot(command_prefix='!')
x = 0

#x=(datetime.datetime.now().day)
#x = x +0
#Y =(datetime.datetime.now().month)
#Z = x , Y
#Cas1 =1, 11
#Cas2 =8, 11
#Cas3 =15, 11 
#Cas4 =27, 11 
#Cas5 =3, 12
@bot.command()
#async def like(msg):
#  if  (Z == Cas1):
#    await msg.send("Ye Dnes je Like house")
#     
#  elif(Z == Cas2):
#    await msg.send("Ye Dnes je Like house")
#     
#  elif(Z == Cas3):
#    await msg.send("Ye Dnes je Like house")
#     
#  elif(Z == Cas4):
#    await msg.send("Ye Dnes je Like house")
#     
#  elif(Z == Cas5):
#    await msg.send("Ye Dnes je Like house")
#    
#  else:
#    await msg.send("Ye Dnes neni Like house")
async def xd(msg):
  for x in range(1000000):
    x = x +1
    print ("Ten bot to napsal uz>",x)
    await msg.send("@everyone https://tenor.com/view/yourmom-forsen-bttv-twitch-gif-20397354 ")

#if (d1 < d2):
#    async defhttps://tenor.com/view/yourmom-forsen-bttv-twitch-gif-20397354 l(msg):
#      await msg.send("Dnes je like house ye!")
#else:
#    async def l(msg):
#      await msg.send("Dnes neni like house ye!")
async def like(msg):
  await msg.send("Každý den lol")
@bot.command(pass_context=True)
async def test(msg):
    await msg.send('funguj!', file=discord.File('social-credit-sad-spongebob.gif'))
client = discord.Client()

async def my_background_task():
    await client.wait_until_ready()
    counter = 0
    channel = client.get_channel(id=903410860884631592) # replace with channel_id
    while not client.is_closed():
        counter += 1
        await channel.send(counter)
        await asyncio.sleep(1) # task runs every 60 seconds



bot.add_cog(main_cog(bot))
bot.add_cog(music_cog(bot))

keep_alive()



bot.run(os.environ["bot.exe"])