import discord
from discord.ext import commands
from discord.utils import get
import classyjson as cj



class Config(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.get_cog("Krew")


    @commands.group(name='config')
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def config(self, ctx):
        if ctx.invoked_subcommand is None:
            help_embed = discord.Embed(color=discord.Color.orange())
            help_embed.set_author(
                name="Config Commands")

    @config.command(name='prefix')
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def prefix(self, ctx, prefix):
        with open('data/prefixes.json', 'r') as f:
            prefixes = cj.load(f)

        prefixes[str(ctx.guild.id)] = prefix

        with open('data/prefixes.json', 'w') as f:
            cj.dump(prefixes, f, indent=4)

        await ctx.send(embed=discord.Embed(color=discord.Color.orange(), description=f'Prefix has been updated!'))















def setup(bot):
    bot.add_cog(Config(bot))
