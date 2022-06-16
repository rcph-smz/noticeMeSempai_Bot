import discord
import os
from random import randint
from googletrans import Translator
# import pymongo


client = discord.Client()


@client.event
async def on_ready():
    print("i have logged in as {0.user}".format(client))

listOfSenpaiStatement = [
  ["hey senpai","hmm? （；^ω^）"],
  ["senpai","Did someone call Me Sempai? ૮₍ ˃ ⤙ ˂ ₎ა "],
  ["you like me sempai","Of course I like You ˃ ⤙ ˂"],
  ["sana all","sana all"],
  ["how are you today sempai","dont worry im fine (⁄ ⁄•⁄ω⁄•⁄ ⁄)⁄"],
  ["did you eat your lunch sempai","Yup!!!, im already full (っˆڡˆς)"],
  ["hey sempai, whats my gender","i dont know tehee ^m^"],
  ["am i gay","Idk Touch Some Grass Tehee ^m^"],
  ["i like loli","should i call fbi?( ノ ゜□ ゜)ノ"],
  ["can i court you","Yes */blush"],
  ["play","Play with Me (⁄ ⁄•⁄ω⁄•⁄ ⁄)⁄"],
  ["oh nyo","Oh Nyo ~ ＾º◡º＾"],
  ["segs","Did somebody says Seggs? ૮ ˶ᵔ ᵕ ᵔ˶ ა"],
  ["goodnight","_Goodnight_ ~ <3"],
  ["cls","This is not Command Prompt (〃＾▽＾〃)"],
  ["im sad","don't worry I'm here (〃＾▽＾〃)"],
  ["uwu","_UwU_"],
  ["notice me","OkayFine ૮₍ ˃ ⤙ ˂ ₎ა"],
  ["yes","₍ ˃ ⤙ ˂ ₎"],
  ["ohayou","_Ohayou!!!_ ~ ૮ ˶ᵔ ᵕ ᵔ˶ ა <3"],
  ["oyasumi","_Oyasumi_ ~ ૮₍ ˃ ⤙ ˂ ₎ა <3"],
  ['noticeme', 'OkayFine ૮₍ ˃ ⤙ ˂ ₎ა'],
  ['nyt', 'GoodNight ~'],
  ['i love you', 'I love you too  ~'],
  ['yamete kudasai', '_Kyah_ ~  ~ YameeeTeee!!!!! _Ughhhh hmmp_'],
  ['kawaii', '૮ ˶ᵔ ᵕ ᵔ˶ ა'],
  ['kill me','Im not _"Yandere"_ _Hmmp_!!!']
]
listOfLinks = [
  ["superidol","https://c.tenor.com/dIaP-9Yp9fIAAAAd/super-idol.gif"],
  ['noticemesempai_link', 'https://discord.com/api/oauth2/authorize?client_id=964386726372065280&permissions=8&scope=bot']
]
listOfSenpaiResponse = [
  ["?",["Yesss ~","HuHuHu!!!","_Ugghhh_","No...","_?_"]]
]

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.lower().startswith("leave_server"):
      try:
        client_guild = client.get_guild(int(message.content[12:].strip()))
        await client_guild.leave()
      except:
        pass

    # help
    if message.content.lower() == 'help':
      await message.channel.send("""
Help Me Sempai :  _Innocent command ૮₍ ˃ ⤙ ˂ ₎ა_  

translate <language> - <wants to translate>

# I'm going go add more features

# and this bot has a tonnes of bugs
                                """)
                                   

  # * add<not_available> - adding your key-value preferences 
  #   ex:
  #     add <nameofkey> - <value>
  #     add NoticeMe - OkayFine ૮₍ ˃ ⤙ ˂ ₎ა
  #       // her response is OkayFine ૮₍ ˃ ⤙ ˂ ₎ა 
  # * ? - ask sempai for question
  #   ex: 
  #     <question>?
  #     can i court you? 
  #       // her response might be "Yesss ~","HuHuHu!!!","_Ugghhh_","No...","_?_"






    # translator
      # pip install googletrans==4.0.0rc1

    if(message.content.startswith("translate")):
      await message.channel.send(Translator().translate(message.content[9:].strip().split("-")[1].strip(),dest=str(message.content[9:].strip().split("-")[0].strip())).text)
     # await message.delete()
      
    # static question
    for x in listOfSenpaiStatement:
      if message.content.lower() in x:
        await message.channel.send(x[1])
    # play with sempai
    for x in listOfSenpaiResponse:
      if not message.content.lower().startswith("say") and not message.content.lower().startswith("translate") and message.content[message.content.find(x[0])] in x:
        await message.channel.send(x[1][randint(0,int(len(x[1]))) - 1])
    # links
    for x in listOfLinks:
      if message.content.lower() in x:
        await message.channel.send(x[1])
    #say <message>
    if(message.content.lower().startswith("say")):
      await message.channel.send(message.content[3:])
      # await message.delete()
        
    # special xD
       
    if message.content == "Notice Me Senpai":
      await message.channel.send("I want to Marry You, shall We? ૮₍ ˃ ⤙ ˂ ₎ა ")
    if message.content == "what's your phone number":
      await message.channel.send("09"+str(randint(0,10))+str(randint(0,10))+str(randint(0,10))+str(randint(0,10))+str(randint(0,10))+str(randint(0,10))+str(randint(0,10))+str(randint(0,10))+str(randint(0,10)))

client.run("OTY0Mzg2NzI2MzcyMDY1Mjgw.GZPbzS.5TGr1VvoTwRoco9q8h1Mk-qNgNX2M2iKMGsBYI")
