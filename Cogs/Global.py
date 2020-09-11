
import arrow
import discord
import classyjson as cj
from discord.ext import commands


class Global(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.startTime = arrow.utcnow()


        with open('data/stuff.json','r') as maininfo:
            self.bot.d = cj.load(maininfo)


        with open('data/keys.json', 'r') as keys_file:
            self.bot.d.key = cj.load(keys_file)

def setup(bot):
    bot.add_cog(Global(bot))
