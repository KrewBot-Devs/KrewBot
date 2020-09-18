import discord
from discord.ext import commands
from discord.utils import get
import arrow



bot = commands.Bot(command_prefix='!k ')



class Other(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.g = arrow.utcnow()
        self.db = self.bot.get_cog("Database")


    @commands.command(name="info", aliases=["information"])
    async def information(self, ctx):
        info_msg = discord.Embed(color=discord.Color.orange())
        info_msg.add_field(name="Command Prefix", value=ctx.prefix, inline=True)
        info_msg.add_field(name="Creators", value="Emerald#8617 &\n Sh-wayz#4749", inline=True)
        info_msg.add_field(name="Total Servers", value=str(len(self.bot.guilds)), inline=True)
        info_msg.add_field(name="Total Users", value=str(len(self.bot.users)), inline=True)
        info_msg.add_field(name="Disbots Link", value='[disbots.gg](https://disbots.gg/bot/752948048669442228)', inline=True)
        info_msg.add_field(name="Source Code", value="[github.com](https://github.com/KrewBot-Devs/KrewBot)", inline=True)
        info_msg.set_author(name="Krew Bot Information",
        icon_url="https://lh3.googleusercontent.com/proxy/IE0HkL7sE5XsN81L0GNI8wakwUKCACIgRhLxQQcICPUNrc5rArnvjKO0BfweqzqM9tHpPYTaHhWRkSSpKFZO6NxB3AXTmnKOTlDEUtseNR2PaZQnmp4W7w")
        await ctx.send(embed=info_msg)

    @commands.command(name="uptime", aliases=['up'])
    async def get_uptime(self, ctx):
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


    @commands.command(name='invite')
    async def invite(self, ctx):
        inv_embed = discord.Embed(color=discord.Color.orange(), description='[Click Here!](https://discord.com/api/oauth2/authorize?client_id=752948048669442228&permissions=519367&scope=bot)')

        inv_embed.set_author(name="Invite the bot!",
        icon_url="https://lh3.googleusercontent.com/proxy/IE0HkL7sE5XsN81L0GNI8wakwUKCACIgRhLxQQcICPUNrc5rArnvjKO0BfweqzqM9tHpPYTaHhWRkSSpKFZO6NxB3AXTmnKOTlDEUtseNR2PaZQnmp4W7w")

        inv_embed.set_footer(text="Made by Emerald and Sh-wayz")
        await ctx.send(embed=inv_embed)





def setup(bot):
    bot.add_cog(Other(bot))
