import discord
from discord.ext import commands
from discord.utils import get
class Config(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(name='config')
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def config(self, ctx):
        if ctx.invoked_subcommand is None:
            help_embed = discord.Embed(color=discord.Color.orange())
            help_embed.set_author(
                name="Config Commands")


    @config.command(name='disable')
    async def disable(self, ctx, *, command, pass_context=True):
        try:
            print('yee yee temp shit')
            bot.remove_command(command)

        except:
            await ctx.send(embed=discord.Embed(color=discord.Color.orange(), description="That's not a valid command!"))






def setup(bot):
    bot.add_cog(Config(bot))
