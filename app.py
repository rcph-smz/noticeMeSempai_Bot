import discord
from discord.ext import commands
import os
from random import randint
import random
from googletrans import Translator
import requests
# import pymongo

client = commands.Bot(command_prefix="./")
client.remove_command("help")

@client.event
async def on_ready():
  print(f'I have been login as {client.user}')


get_list = ["guild_id","author","ping","quote","hold_book"]

req = requests.get("https://type.fit/api/quotes")

def get_command(ctx,k,i):
  index = get_list.index(k)
  ctx_list = [ctx.guild.id,ctx.author,f'{round(client.latency * 1000)}ms',random.choice(req.json())['text'],"https://rcph-smz.github.io/noticeMeSempai_Bot/preview.html"]

  return ctx_list[index]
  
  

@client.command()
async def get(ctx, *args):
  for i in args:
    for k in get_list:
      if k in i:
        await ctx.send(get_command(ctx,k,i))

@client.command()
async def translate(ctx, language , *args):
  await ctx.send(Translator().translate(" ".join(args),dest=language).text)

@client.command()
async def say(ctx,*message):
  await ctx.send(" ".join(message))

field_list = [["guild_id","./get guild_id"],["author","./get author"],["ping","./get ping"],["translate","./translate <language> <argument>"],["say","./say <argument/message>"],["hold_book","./hold_book"],["quote","./get quote"]]
@client.group(invoke_without_command=True)
async def help(ctx):
  em = discord.Embed(title = "commands", value = "use ./help command to see all stuff", color = discord.Color.from_rgb(198,175,165))

  for flist in field_list:
    em.add_field(name=flist[0],value=flist[1])

  await ctx.send(embed = em)

@client.command()
async def hold_book(ctx):
  em = discord.Embed(color = discord.Color.from_rgb(198,175,165))
  with open("./anime_holding_a_book.txt","r") as bk:
    em.set_image(url=f'https://rcph-smz.github.io/Anime-Girls-Holding-Programming-Books/{random.choice(bk.readlines())}')

    await ctx.send(embed = em)
    
try:
  with open("./noticeMe.txt","r") as noticeMe:
    for i in noticeMe.readlines():
      client.run(i)
except:
  client.run(os.environ["noticeMe"])