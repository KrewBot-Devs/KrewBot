import discord
from discord.ext import commands
from discord.utils import get



class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        bot.remove_command('help')

    @commands.group(name='help')
    async def help(self, ctx):
        if ctx.invoked_subcommand is None:
            help_embed = discord.Embed(color=discord.Color.orange())
            help_embed.set_author(
                name="Krew Bot Commands")

            help_embed.add_field(name="Admin", value=f"``{ctx.prefix}help admin``", inline=True)
            help_embed.add_field(name='Other', value=f"``{ctx.prefix}help other``", inline=True)
            help_embed.set_footer(text="Made by Emerald and Shwayz")
            await ctx.send(embed=help_embed)


    @help.command(name='admin')
    async def help_admin(self, ctx):

        help_embed = discord.Embed(color=discord.Color.orange())
        help_embed.set_author(
        name='Krew Bot Commands')

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

        help_embed = discord.Embed(color=discord.Color.orange())
        help_embed.set_author(
        name='Krew Bot Commands')

        help_embed.add_field(
        name='**Other Commands**',
        value=f'**{ctx.prefix}info** - Displays some info about the bot\n', inline=False)

        help_embed.set_footer(text="Need more help? DM @Emerald#8617 or @Sh-wayz#4749")

        await ctx.send(embed=help_embed)


def setup(bot):
    bot.add_cog(Help(bot))
