import discord
from discord.ext import commands
from discord.utils import get
import arrow
import asyncio


bot = commands.Bot(command_prefix='!k ')



class Other(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.g = arrow.utcnow()
        self.db = self.bot.get_cog("Database")


    @commands.command(name="info", aliases=["information"])
    async def information(self, ctx):
        async with ctx.typing():
            await asyncio.sleep(1)
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




    @commands.command(name='invite')
    async def invite(self, ctx):
        async with ctx.typing():
            await asyncio.sleep(1)
            inv_embed = discord.Embed(color=discord.Color.orange(), description='[Click Here!](https://discord.com/api/oauth2/authorize?client_id=752948048669442228&permissions=519367&scope=bot)')

            inv_embed.set_author(name="Invite the bot!",
            icon_url="https://lh3.googleusercontent.com/proxy/IE0HkL7sE5XsN81L0GNI8wakwUKCACIgRhLxQQcICPUNrc5rArnvjKO0BfweqzqM9tHpPYTaHhWRkSSpKFZO6NxB3AXTmnKOTlDEUtseNR2PaZQnmp4W7w")

            inv_embed.set_footer(text="Made by Emerald and Sh-wayz")
            await ctx.send(embed=inv_embed)


    @commands.command(name="guild", aliases=["si", "server", "serverinfo", "guildinfo"])
    @commands.guild_only()
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def server_info(self, ctx, g: discord.Guild = None):
        async with ctx.typing():
            await asyncio.sleep(1)
            g = ctx.guild if g is None else g

            embed = discord.Embed(color=discord.Color.orange())

            embed.set_author(name=g.name, icon_url=g.icon_url_as(format="png"))

            embed.add_field(name="Owner", value=self.bot.get_user(g.owner_id).display_name)
            embed.add_field(name="Members", value=g.member_count)

            embed.add_field(name="Roles", value=len(g.roles))
            embed.add_field(name="Channels", value=len(g.channels))
            embed.add_field(name="Emojis", value=len(g.emojis))

            await ctx.send(embed=embed)

    @commands.command(name='ping')
    async def ping(self, ctx):
        await ctx.send(embed=discord.Embed(color=discord.Color.orange(),
                                           description=f"``{round(self.bot.latency * 1000, 2) - 1000} ms``"))


def setup(bot):
    bot.add_cog(Other(bot))
