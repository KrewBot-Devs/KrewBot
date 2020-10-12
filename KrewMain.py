import discord
from discord.ext import commands
from discord.utils import get
import classyjson as cj
import logging
import pydisbots

# set up basic logging
#logging.basicConfig(level=logging.DEBUG)

def get_prefixes(bot, message):
    with open('data/prefixes.json', 'r') as f:
        prefixes = cj.load(f)
    return prefixes[str(message.guild.id)]




bot = commands.Bot(command_prefix=get_prefixes, help_command=None)



@bot.event
async def on_guild_join(guild):
    with open('data/prefixes.json', 'r') as f:
        prefixes = cj.load(f)


    prefixes[str(guild.id)] = 'k.'

    with open('data/prefixes.json', 'w') as f:
        cj.dump(prefixes, f, indent=4)


@bot.event
async def on_guild_remove(guild):
    with open('data/prefixes.json', 'r') as f:
        prefixes = cj.load(f)

        prefixes.pop(str(guild.id))

        with open('data/prefixes.json', 'w') as f:
            cj.dump(prefixes, f, indent=4)

with open('data/keys.json', 'r') as keys_file:
    bot.key = cj.load(keys_file)

dbc = pydisbots.Client(bot, bot.key.disbotAuth, autopost_stats=True, webhook_port=8675, webhook_path='/disbotsHook')
initial_extensions = ['Cogs.Admin','Cogs.Events','Cogs.Help','Cogs.Other','Cogs.Krew','Cogs.Config', 'Cogs.Owner', 'Cogs.Uptime']

for extension in initial_extensions:
    bot.load_extension(extension)



bot.run(bot.key.discord_token)
