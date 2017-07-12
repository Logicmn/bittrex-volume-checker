import discord
from discord.ext import commands
import main

TOKEN = 'MzM0NDU5NzY4NjcwNTE5MzEw.DEe2WQ.wLgSaebs_eBxQZ3cSsXPLQSxTok'

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
async def wall(coin, desired_multiplier):
    try:
        desired_multiplier = float(desired_multiplier)
    except:
        await bot.say("That's not a percent!")
    desired_multiplier = float("{0:.1f}".format(desired_multiplier))
    try:
        if desired_multiplier <= 2:
            await bot.say('Calculating...')
            volume = main.get_sells(coin, desired_multiplier)
            total_btc = sum(volume)
            total_btc = float("{0:.3f}".format(total_btc))
            await bot.say('Total of {0} BTC to reach a {1}x multiplier for {2}'.format(total_btc, desired_multiplier, upper(coin)))
            print('Total of {0} BTC to reach a {1}x multiplier for {2}'.format(total_btc, desired_multiplier, upper(coin)))
        else:
            await bot.say('Please use a multiplier under 2x, apparently I can\'t handle more than that.')
    except:
        await bot.say('That coin is not registered on Bittrex!')

bot.run(TOKEN)
