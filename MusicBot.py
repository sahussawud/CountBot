import discord
from discord.ext import commands
from discord.utils import get
import youtube_dl
import os
Token = 'Njg4Nzc1NDQ4Mzk3NzQyMjEy.Xm-coQ.POYkWJ9gO3DUbjY2U64kCJT09YA'
client = commands.Bot(command_prefix=("/"))
@client.event
async def on_ready():
    print("Bot online !")
client.run(Token)
@client.command(pass_context = True)
async def join(ctx):
