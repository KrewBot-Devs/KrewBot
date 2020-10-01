from discord.ext import commands
import discord
import os
import asyncio
import classyjson as cj

class Owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name='load')
    @commands.is_owner()
    async def load_cog(self, ctx, cog = 'all'):
        if cog == "all":
            print("Loaded all cogs")
            await ctx.send('Loaded all cogs')
            self.bot.load_extension('Cogs.Admin')
            self.bot.load_extension('Cogs.Config')
            self.bot.load_extension('Cogs.Events')
            self.bot.load_extension('Cogs.Help')
            self.bot.load_extension('Cogs.Krew')
            self.bot.load_extension('Cogs.Other')
        elif cog == "Admin" or cog == "Config" or cog == "Events" or cog == "Help" or cog == "Krew" or cog == "Other":
            self.bot.load_extension('Cogs.' + cog)
            print(f"Loaded {cog}")
            await ctx.send(f'Loaded {cog}')

    @commands.command(name='unload')
    @commands.is_owner()
    async def unload_cog(self, ctx, cog = "all"):
        if cog == "all":
            print("Unloaded all cogs")
            await ctx.send('Unloaded all cogs')
            self.bot.unload_extension('Cogs.Admin')
            self.bot.unload_extension('Cogs.Config')
            self.bot.unload_extension('Cogs.Events')
            self.bot.unload_extension('Cogs.Help')
            self.bot.unload_extension('Cogs.Krew')
            self.bot.unload_extension('Cogs.Other')
        elif cog == "Admin" or cog == "Config" or cog == "Events" or cog == "Help" or cog == "Krew" or cog == "Other":
            self.bot.unload_extension('Cogs.' + cog)
            print(f"Unloaded {cog}")
            await ctx.send(f'Unloaded {cog}')

    @commands.command(name='reload')
    @commands.is_owner()
    async def reload_cog(self, ctx, cog = "all"):
        if cog == 'all':
            print("reloaded all cogs")
            await ctx.send('Reloaded all cogs')
            self.bot.reload_extension('Cogs.Admin')
            self.bot.reload_extension('Cogs.Config')
            self.bot.reload_extension('Cogs.Events')
            self.bot.reload_extension('Cogs.Help')
            self.bot.reload_extension('Cogs.Krew')
            self.bot.reload_extension('Cogs.Other')
            self.bot.reload_extension('Cogs.Owner')
        elif cog == 'Admin' or cog == 'Config' or cog == 'Events' or cog == 'Help' or cog == 'Krew' or cog == 'Other' or cog == 'Owner':
            self.bot.reload_extension('Cogs.' + cog)
            print(f"reloaded {cog}")
            await ctx.send(f'Reloaded {cog}')

    @commands.command(name='gitpull')
    @commands.is_owner()
    async def git_pull(self, ctx):
        os.system('git pull > git_pull_log 2>&1')

        with open('git_pull_log', 'r') as log_file:
            await ctx.send(embed=discord.Embed(color=discord.Color.orange(), description=f'```{log_file.read()}```'))

        os.remove('git_pull_log')

    @commands.command(name='prefix')
    @commands.guild_only()
    @commands.is_owner()
    async def prefix(self, ctx, prefix):
        with open('data/prefixes.json', 'r') as f:
            prefixes = cj.load(f)

        prefixes[str(ctx.guild.id)] = prefix

        with open('data/prefixes.json', 'w') as f:
            cj.dump(prefixes, f, indent=4)

        await ctx.send(embed=discord.Embed(color=discord.Color.orange(), description=f'Prefix has been updated!'))


    @commands.group(name='ownerhelp')
    @commands.is_owner()
    async def ownerhelp(self, ctx):
        if ctx.invoked_subcommand is None:
            async with ctx.typing():
                await asyncio.sleep(1)
                help_embed = discord.Embed(color=discord.Color.orange())
                help_embed.set_author(
                    name="Krew Bot Owner cmds",
                    icon_url="https://lh3.googleusercontent.com/proxy/IE0HkL7sE5XsN81L0GNI8wakwUKCACIgRhLxQQcICPUNrc5rArnvjKO0BfweqzqM9tHpPYTaHhWRkSSpKFZO6NxB3AXTmnKOTlDEUtseNR2PaZQnmp4W7w")

                help_embed.add_field(name="Cogs", value=f"``{ctx.prefix}ownerhelp cogs``", inline=True)
                help_embed.add_field(name='Git', value=f"``{ctx.prefix}ownerhelp git``", inline=True)
                help_embed.add_field(name='Other', value=f"``{ctx.prefix}ownerhelp other``", inline=True)

                help_embed.set_footer(text="Made by the only people who can use this command.")
                await ctx.send(embed=help_embed)


    @ownerhelp.command(name='cogs')
    async def help_cogs(self, ctx):

        async with ctx.typing():
            await asyncio.sleep(1)

            help_embed = discord.Embed(color=discord.Color.orange())
            help_embed.set_author(
            name='Cog cmds',
            icon_url="https://lh3.googleusercontent.com/proxy/IE0HkL7sE5XsN81L0GNI8wakwUKCACIgRhLxQQcICPUNrc5rArnvjKO0BfweqzqM9tHpPYTaHhWRkSSpKFZO6NxB3AXTmnKOTlDEUtseNR2PaZQnmp4W7w")

            help_embed.add_field(
            name='**Cooooooogs**', value = f"**{ctx.prefix}load** *cog name* - loads cog lol what did you think.\n"
            f"**{ctx.prefix}unload** *cog name* - seems pretty obvious to me tbh.\n"
            f"**{ctx.prefix}reload** *cog name* - Reloads a cog, obviously.\n", inline=True)

            help_embed.set_footer(text="Need more help? You're an owner go fix it.")

            await ctx.send(embed=help_embed)


    @ownerhelp.command(name='git')
    async def help_git(self, ctx):

        async with ctx.typing():
            await asyncio.sleep(1)

            help_embed = discord.Embed(color=discord.Color.orange())
            help_embed.set_author(
            name='git cmds',
            icon_url="https://lh3.googleusercontent.com/proxy/IE0HkL7sE5XsN81L0GNI8wakwUKCACIgRhLxQQcICPUNrc5rArnvjKO0BfweqzqM9tHpPYTaHhWRkSSpKFZO6NxB3AXTmnKOTlDEUtseNR2PaZQnmp4W7w")

            help_embed.add_field(
            name='**git is the best**',
            value=f'**{ctx.prefix}gitpull** - <:megathonk:760543221246853120> whaddaya think.\n'
                , inline=False)

            help_embed.set_footer(text="Need more help? You're an owner go fix it.")
            await ctx.send(embed=help_embed)


    @ownerhelp.command(name='other')
    async def help_other(self, ctx):

        async with ctx.typing():
            await asyncio.sleep(1)

            help_embed = discord.Embed(color=discord.Color.orange())
            help_embed.set_author(
            name='other cmds',
            icon_url="https://lh3.googleusercontent.com/proxy/IE0HkL7sE5XsN81L0GNI8wakwUKCACIgRhLxQQcICPUNrc5rArnvjKO0BfweqzqM9tHpPYTaHhWRkSSpKFZO6NxB3AXTmnKOTlDEUtseNR2PaZQnmp4W7w")

            help_embed.add_field(
            name='**OwO whats this**',
            value=f'**{ctx.prefix}eval** <:megathonk:760543221246853120> i wonder.\n **{ctx.prefix}awaiteval** eval, but awaited\n'
                , inline=False)

            help_embed.set_footer(text="Need more help? You're an owner go fix it.")
            await ctx.send(embed=help_embed)
    @commands.command(name="eval")
    @commands.is_owner()
    async def eval_message(self, ctx, *, msg):
        await ctx.send(f"{eval(msg)}\uFEFF")

    @commands.command(name="awaiteval")
    @commands.is_owner()
    async def await_eval_message(self, ctx, *, msg):
        await ctx.send(f"{await eval(msg)}\uFEFF")


def setup(bot):
    bot.add_cog(Owner(bot))
