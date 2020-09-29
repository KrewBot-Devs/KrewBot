from discord.ext import commands
import discord
import os


class Owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        

    @commands.command(name='load')
    @commands.is_owner()
    async def load_cog(self, ctx, cog):
        self.bot.load_extension('Cogs.' + cog)

    @commands.command(name='unload')
    @commands.is_owner()
    async def unload_cog(self, ctx, cog):
        self.bot.unload_extension('Cogs.' + cog)

    @commands.command(name='reload')
    @commands.is_owner()
    async def reload_cog(self, ctx, cog):
        self.bot.reload_extension('Cogs.' + cog)

    @commands.command(name='gitpull', aliases=['git_pull'])
    @commands.is_owner()
    async def git_pull(self, ctx):
        os.system('git pull > git_pull_log 2>&1')

        with open('git_pull_log', 'r') as log_file:
            await ctx.send(embed=discord.Embed(color=discord.Color.orange, description=f'```{log_file.read()}```'))

        os.remove('git_pull_log')


def setup(bot):
    bot.add_cog(Owner(bot))
