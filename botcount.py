import discord
import asyncio

client = discord.Client()

async def my_background_task():
    await client.wait_until_ready()
    counter = 0
    channel = discord.Object(id='channel_id_here')
    while not client.is_closed:
        counter += 1
        await client.send_message(channel, counter)
        await asyncio.sleep(10) # task runs every 60 seconds

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.loop.create_task(my_background_task())
client.run('Njg4Nzc1NDQ4Mzk3NzQyMjEy.Xm7xeQ.-5MeGmGKfzFIKoX8w3jjkZfxN5s')