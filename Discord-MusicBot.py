import discord
from discord.ext import commands
from discord.utils import get
import youtube_dl
import os

Token = 'Token here'
client = commands.Bot(command_prefix=("/"))

@client.event
async def on_ready():
    print("Bot online !")


@client.command(pass_context = True)
async def join(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()
    print("Senpai joined the voice channel")

@client.command(pass_context = True)
async def leave(ctx):
    await ctx.voice_client.disconnect()
    print("Senpai Left the voice channel")

@client.command(pass_context = True)
async def play(ctx, url):
    channel = ctx.message.author.voice.channel
    await channel.connect()
    print("Senpai joined the voice channel")
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
            print("Remove old song file")
    except PermissionError:
        print("Trying to delete song file, but it's being played")
        await ctx.send("Error")
        return

    await ctx.send("Getting everything ready")

    voice = get(client.voice_clients, guild=ctx.guild)
    ydl_opts = {
         'format': 'Bestaudio/best',
         'postprocessors':[{
             'key': 'FFmpegExtractAudio',
             'preferredcodec':'mp3',
             'preferredquality':'192',
         }]
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print("Download audio now\n")
        ydl.download([url])
    
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            name = file
            os.rename(file, "song.mp3")

    voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: print('done',))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.07


client.run(Token)