import discord
import asyncio
from discord.ext.commands import Bot
import secrets
import random


description = '''My very first Discord bot'''

bot = Bot(command_prefix='!', description=description)
client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@bot.event
async def on_ready():
    print("Client logged in!")

@bot.command()
async def hello(*args):
    return await bot.say("Hello, world!")

@bot.command()
async def add(left : int, right : int):
    '''Adds two numbers together.'''
    await bot.say(left + right)


bot.run(secrets.BOT_TOKEN)
client.run(secrets.CLIENT_SECRET)
