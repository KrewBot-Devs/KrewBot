import discord
from discord.ext import commands
from discord.utils import get
import classyjson as cj
import logging

# set up basic logging
#logging.basicConfig(level=logging.DEBUG)


bot = commands.Bot(command_prefix='!k ')
bot.remove_command('help')

with open('data/keys.json', 'r') as keys_file:
    bot.key = cj.load(keys_file)

initial_extensions = ['Cogs.Admin','Cogs.Events','Cogs.Help','Cogs.Other']

for extension in initial_extensions:
    bot.load_extension(extension)


bot.run(bot.key.discord_token)
