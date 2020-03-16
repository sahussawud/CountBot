""" bot """
import discord
from discord.ext import commands
bot = commands.Bot(command_prefix='<help>')
@bot.event
async def on_ready():
    print("Sorry for my late")

@bot.event
async def on_message(message):
    if message.content.startswith('Hello'):
        await message.channel.send('hi ><')
    elif message.content.startswith('Senpai'):
        await message.channel.send('nani nani oWo')

#@bot.event

bot.run('Njg4Nzc1NDQ4Mzk3NzQyMjEy.Xm7xeQ.-5MeGmGKfzFIKoX8w3jjkZfxN5s')
