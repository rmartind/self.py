import discord
import logging
import asyncio
import uvloop
import conf


asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
client = discord.Client()


@client.event
async def on_ready():
    print(client.user.name)


async def del_msg(chan):
    max_del = 1000000
    count = 0
    async for x in client.logs_from(chan, limit=max_del):
        try:
            if count < max_del and x.author == client.user:
                await client.delete_message(x)
                count += 1
        except Exception as e:
            logging.exception(str(e))


@client.event
async def on_message(msg):
    if msg.author != client.user:
        return 
    
    if msg.content.startswith('?del'):
        await del_msg(msg.channel)

    elif msg.content.startswith('?prvdel'):
        for chan in client.private_channels:
            await del_msg(chan)

client.run(conf.token['token'], bot=False)
