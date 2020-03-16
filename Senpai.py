import discord
from discord.ext import commands
tokken = 'Njg4Nzc1NDQ4Mzk3NzQyMjEy.Xm8YAw.sTztDYkSkkBXcUoP36BR5txJr04'
bot = commands.Bot(command_prefix='.')
@bot.event
async def on_ready() :
    print("Sorry for my late oMo")

@bot.event
async def on_member_join(member):
    print(f'{member} has join the server.')

@bot.event
async def on_member_remove(member):
    print(f'{member} has left the server.')
     return await message.channel.send(f"{member} has left the server")


@bot.event
async def on_message(message) :
    if message.content.startswith ('Hello'):
       return await message.channel.send('hi ~ Meow ><')
bot.run(tokken)