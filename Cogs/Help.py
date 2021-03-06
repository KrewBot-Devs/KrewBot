import discord
from discord.ext import commands
from discord.utils import get
import asyncio



class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(name='help', aliases=['halp', 'fack', 'wat'])
    async def help(self, ctx):
        if ctx.invoked_subcommand is None:
            async with ctx.typing():
                await asyncio.sleep(1)
                help_embed = discord.Embed(color=discord.Color.orange())
                help_embed.set_author(
                    name="Krew Bot Commands",
                    icon_url="https://lh3.googleusercontent.com/proxy/IE0HkL7sE5XsN81L0GNI8wakwUKCACIgRhLxQQcICPUNrc5rArnvjKO0BfweqzqM9tHpPYTaHhWRkSSpKFZO6NxB3AXTmnKOTlDEUtseNR2PaZQnmp4W7w")

                help_embed.add_field(name="Admin", value=f"``{ctx.prefix}help admin``", inline=True)
                help_embed.add_field(name='Other', value=f"``{ctx.prefix}help other``", inline=True)
                help_embed.add_field(name='Krew', value=f"``{ctx.prefix}help krew``", inline=True)
                help_embed.add_field(name='Config', value=f"``{ctx.prefix}help config``", inline=True)
            help_embed.set_footer(text="Made by Emerald and Sh-wayz")
            await ctx.send(embed=help_embed)


    @help.command(name='admin')
    async def help_admin(self, ctx):

        async with ctx.typing():
            await asyncio.sleep(1)

            help_embed = discord.Embed(color=discord.Color.orange())
            help_embed.set_author(
            name='Krew Bot Commands',
            icon_url="https://lh3.googleusercontent.com/proxy/IE0HkL7sE5XsN81L0GNI8wakwUKCACIgRhLxQQcICPUNrc5rArnvjKO0BfweqzqM9tHpPYTaHhWRkSSpKFZO6NxB3AXTmnKOTlDEUtseNR2PaZQnmp4W7w")

            help_embed.add_field(
            name='**Admin Commands**',
            value=f'**{ctx.prefix}kick** *@user* *reason (optional)* - Throw someone overboard.\n'
            f'**{ctx.prefix}ban** *@user* *reason (optional)* - Banish someone from your Krew.\n'
            f'**{ctx.prefix}clear** *Number of messages.* - Remove set amount of messages.\n'
            f'**{ctx.prefix}pardon** *user ID* - Pardon people who were wrongfully banished.\n', inline=False)

            help_embed.set_footer(text="Need more help? DM @Emerald#8617 or @Sh-wayz#4749")

            await ctx.send(embed=help_embed)


    @help.command(name='other')
    async def help_other(self, ctx):
        async with ctx.typing():
            await asyncio.sleep(1)
            help_embed = discord.Embed(color=discord.Color.orange())
            help_embed.set_author(
            name='Krew Bot Commands',
            icon_url="https://lh3.googleusercontent.com/proxy/IE0HkL7sE5XsN81L0GNI8wakwUKCACIgRhLxQQcICPUNrc5rArnvjKO0BfweqzqM9tHpPYTaHhWRkSSpKFZO6NxB3AXTmnKOTlDEUtseNR2PaZQnmp4W7w")

            help_embed.add_field(
            name='**Other Commands**',
            value=f'**{ctx.prefix}info** - Displays some info about the bot.\n'
            f'**{ctx.prefix}uptime** - Show how long the bot has been running.\n'
            f'**{ctx.prefix}invite** - Invite the bot to your server.\n'
            f'**{ctx.prefix}guild** - Info about current server.\n'
            f'**{ctx.prefix}ping** - Get bot to API latency.', inline=False)

            help_embed.set_footer(text="Need more help? DM @Emerald#8617 or @Sh-wayz#4749")

            await ctx.send(embed=help_embed)

    @help.command(name='krew')
    async def help_krew(self, ctx):
        async with ctx.typing():
            await asyncio.sleep(1)
            help_embed = discord.Embed(color=discord.Color.orange())
            help_embed.set_author(
            name='Krew Bot Commands',
            icon_url="https://lh3.googleusercontent.com/proxy/IE0HkL7sE5XsN81L0GNI8wakwUKCACIgRhLxQQcICPUNrc5rArnvjKO0BfweqzqM9tHpPYTaHhWRkSSpKFZO6NxB3AXTmnKOTlDEUtseNR2PaZQnmp4W7w")

            help_embed.add_field(
            name='**Krew Related Commands**',
            value=f'**{ctx.prefix}goods** - Get all trade prices for goods\n'
            f'**{ctx.prefix}ships** - Get all prices for ships.\n'
            f'**{ctx.prefix}items** - Get prices for all items.\n', inline=True)

            help_embed.set_footer(text="Need more help? DM @Emerald#8617 or @Sh-wayz#4749")

            await ctx.send(embed=help_embed)

    @help.command(name='config')
    async def help_config(self, ctx):
        async with ctx.typing():
            await asyncio.sleep(1)
            help_embed = discord.Embed(color=discord.Color.orange())
            help_embed.set_author(
            name='Krew Bot Commands',
            icon_url="https://lh3.googleusercontent.com/proxy/IE0HkL7sE5XsN81L0GNI8wakwUKCACIgRhLxQQcICPUNrc5rArnvjKO0BfweqzqM9tHpPYTaHhWRkSSpKFZO6NxB3AXTmnKOTlDEUtseNR2PaZQnmp4W7w")

            help_embed.add_field(
            name='**Config Commands**',
            value=f"**{ctx.prefix}config prefix *new value*** - Set a new prefix for the respective server.\n", inline=True)

            help_embed.set_footer(text="Need more help? DM @Emerald#8617 or @Sh-wayz#4749")

            await ctx.send(embed=help_embed)

def setup(bot):
    bot.add_cog(Help(bot))
