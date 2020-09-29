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
   @commands.group(name='ownerhelp')
   @commands.is_owner()
    async def ownerhelp(self, ctx):
        if ctx.invoked_subcommand is None:
            async with ctx.typing():
                await asyncio.sleep(1)
                help_embed = discord.Embed(color=discord.Color.orange())
                help_embed.set_author(
                    name="KrewBot Owner cmds",
                    icon_url="https://lh3.googleusercontent.com/proxy/IE0HkL7sE5XsN81L0GNI8wakwUKCACIgRhLxQQcICPUNrc5rArnvjKO0BfweqzqM9tHpPYTaHhWRkSSpKFZO6NxB3AXTmnKOTlDEUtseNR2PaZQnmp4W7w")

                help_embed.add_field(name="Cogs", value=f"``{ctx.prefix}ownerhelp cogs``", inline=True)
                help_embed.add_field(name='Git', value=f"``{ctx.prefix}ownerhelp git``", inline=True)
                help_embed.add_field(name='Other, value=f"``{ctx.prefix}ownerhelp other", inline=True)
            help_embed.set_footer(text="Made by the only people who can use this command.")
            await ctx.send(embed=help_embed)


    @ownerhelp.command(name='cogs')
    async def help_admin(self, ctx):

        async with ctx.typing():
            await asyncio.sleep(1)

            help_embed = discord.Embed(color=discord.Color.orange())
            help_embed.set_author(
            name='Cog cmds',
            icon_url="https://lh3.googleusercontent.com/proxy/IE0HkL7sE5XsN81L0GNI8wakwUKCACIgRhLxQQcICPUNrc5rArnvjKO0BfweqzqM9tHpPYTaHhWRkSSpKFZO6NxB3AXTmnKOTlDEUtseNR2PaZQnmp4W7w")

            help_embed.add_field(
            name='**Cooooooogs**',
            value=f'**{ctx.prefix}load** *\{cogname\}* - loads cog lol what did you think.\n'
            f'**{ctx.prefix}unload** *\{cog name\}* - seems pretty obvious to me tbh.\n'
            f'**{ctx.prefix}reload** *Number of messages.* - Remove set amount of messages.\n'
                , inline=False)

            help_embed.set_footer(text="Need more help? You're an owner go fix it.)

            await ctx.send(embed=help_embed)


    @ownerhelp.command(name='git')
    async def help_admin(self, ctx):

        async with ctx.typing():
            await asyncio.sleep(1)

            help_embed = discord.Embed(color=discord.Color.orange())
            help_embed.set_author(
            name='git cmds',
            icon_url="https://lh3.googleusercontent.com/proxy/IE0HkL7sE5XsN81L0GNI8wakwUKCACIgRhLxQQcICPUNrc5rArnvjKO0BfweqzqM9tHpPYTaHhWRkSSpKFZO6NxB3AXTmnKOTlDEUtseNR2PaZQnmp4W7w")

            help_embed.add_field(
            name='**git is the best**',
            value=f'**{ctx.prefix}gitpull** *\{cogname\}* - <:megathonk:683696698459029566> whaddaya think.\n'
                , inline=False)

            help_embed.set_footer(text="Need more help? You're an owner go fix it.)
            ctx.send(embed=help_embed)

      
    @ownerhelp.command(name='git')
    async def help_admin(self, ctx):

        async with ctx.typing():
            await asyncio.sleep(1)    
            await ctx.send('https://i.kym-cdn.com/entries/icons/original/000/027/081/wow.jpg)


def setup(bot):
    bot.add_cog(Owner(bot))
