import discord
from discord.ext import commands
from discord.utils import get
import arrow
import asyncio

bot = commands.Bot(command_prefix='!k ')
class Uptime(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.g = arrow.utcnow()
        self.db = self.bot.get_cog("Database")



    @commands.command(name="uptime", aliases=['up'])
    async def get_uptime(self, ctx):
        async with ctx.typing():
            await asyncio.sleep(1)
            p = arrow.utcnow()
            diff = (p - self.g)
            days = diff.days
            hours = int(diff.seconds / 3600)
            minutes = int(diff.seconds / 60) % 60
            if days == 1:
                dd = "day"
            else:
                dd = "days"
            if hours == 1:
                hh = "hour"
            else:
                hh = "hours"
            if minutes == 1:
                mm = "minute"
            else:
                mm = "minutes"
            await ctx.send(embed=discord.Embed(color=discord.Color.orange(),
                                               description="Bot has been online for " + str(days) + " " + dd + ", " + str(
                                                   hours) + " " + hh + ", and " + str(minutes) + " " + mm + "!"))

def setup(bot):
    bot.add_cog(Uptime(bot))
