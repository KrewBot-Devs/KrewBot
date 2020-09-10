import discord
from discord.ext import commands
from discord.utils import get

bot = commands.Bot(command_prefix='!k ')

class Other(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name="info", aliases=["information"])
    async def information(self, ctx):
        info_msg = discord.Embed(color=discord.Color.orange())
        info_msg.add_field(name="Command Prefix", value=ctx.prefix, inline=True)
        info_msg.add_field(name="Creators", value="Emerald#8617 &\n Sh-wayz#4749", inline=True)
        info_msg.add_field(name="Total Servers", value=str(len(self.bot.guilds)), inline=True)
        info_msg.add_field(name="Total Users", value=str(len(self.bot.users)), inline=True)
        info_msg.add_field(name="Source Code", value="https://github.com/Sh-wayz/krewbot", inline=True)
        info_msg.set_author(name="Krew Bot Information",)
        await ctx.send(embed=info_msg)




def setup(bot):
    bot.add_cog(Other(bot))
