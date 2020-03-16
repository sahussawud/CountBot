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
bot.run('tokken')