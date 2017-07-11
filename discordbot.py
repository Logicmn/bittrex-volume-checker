import discord
from discord.ext import commands
import main

TOKEN = ''

description = '''Logicmn made this.'''
bot = commands.Bot(command_prefix='!', description=description)

@bot.event
async def on_ready():
    print('----------------------------')
    print('Connected!')
    print('Logged in as: {0}'.format(bot.user.name))
    print('Bot ID: {0}'.format(bot.user.id))
    print('----------------------------')

@bot.command()
async def hello():
    """Says world"""
    await bot.say("world")

@bot.command()
async def wall(coin):
    all_btc, multiplier = main.main(coin)
    await bot.say('Total of {0}BTC to reach a {1}x multiplier'.format(all_btc, multiplier))

bot.run(TOKEN)
