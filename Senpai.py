import discord
from discord.ext import commands

tokken = 'Njg4Nzc1NDQ4Mzk3NzQyMjEy.Xm8YAw.sTztDYkSkkBXcUoP36BR5txJr04'
client = commands.Bot(command_prefix='.')

@client.event
async def on_ready() :
    print("Bot online.")

@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()

client.run(tokken)