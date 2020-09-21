import discord
from discord.ext import commands
from discord.utils import get

client = discord.Client()

bot = commands.Bot(command_prefix='!k ')

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name="clear", help=" - Remove set amount of messages", aliases=["c"])
    @commands.has_permissions(manage_messages=True)
    @commands.guild_only()
    async def clear(self, ctx, n: int):
        if n <= 9999:
            try:
                await ctx.channel.purge(limit=n+1)
            except Exception:
                error_embed = discord.Embed(
                    color=discord.Color.orange(),
                    description='''Make sure I'm allowed to do this.''')
                await ctx.send(embed=error_embed)
        else:
            limit_embed = discord.Embed(
                color=discord.Color.orange(),
                description='''Theres too many messages specified.''')
            await ctx.send(embed=limit_embed)
        if n <= -1:
            too_low = discord.Embed(color=discord.Color.orange(), description="You can't clear a negative amount of messages!")
            await ctx.send(embed=too_low)

    @commands.command(name="kick", help=' - throw someone overboard')
    @commands.guild_only()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, user: discord.Member, *, reason="No reason provided."):
        nickname = user.mention
        channel = get(user.guild.channels, name="whalecome")
        if ctx.author.id == user.id:
            await ctx.send(embed=discord.Embed(color=discord.Color.orange(), description="You can't just abandon your krew like that."))
            return
        if ctx.author.top_role.id == user.top_role.id and ctx.author.id != ctx.guild.owner.id:
            await ctx.send(embed=discord.Embed(color=discord.Color.orange(), description="You don't have captain's permission."))
            return
        await ctx.guild.kick(user, reason=reason)
        kick_embed = discord.Embed(
            color=discord.Color.orange(),
            description=f"Threw **{str(user)}** overboard.")
        await ctx.send(embed=kick_embed)


    @commands.command(name="ban", help=' - Banish someone from your krew', aliases=['b'])
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user: discord.Member, *, reason="No reason provided."):
        nickname = user.mention
        channel = get(user.guild.channels, name="whalecome")
        if ctx.author.id == user.id:
            await ctx.send(embed=discord.Embed(color=discord.Color.orange(), description="Now why wuld you want to banish yourself?"))
            return
        if ctx.author.top_role.id == user.top_role.id and ctx.author.id != ctx.guild.owner.id:
            await ctx.send(embed=discord.Embed(color=discord.Color.orange(), description="You don't have the captains permission."))
            return
        for entry in await ctx.guild.bans():
            if entry[1].id == user.id:
                already_banned_embed = discord.Embed(
                    color=discord.Color.orange(),
                    description="They have already been banished.")
                await ctx.send(embed=already_banned_embed)
                return

        await ctx.guild.ban(user, reason=reason, delete_message_days=0)
        banned_embed = discord.Embed(
            color=discord.Color.orange(),
            description=f"Banished **{str(user)}**.")
        await ctx.send(embed=banned_embed)


    @commands.command(name="pardon", help=' - Pardon people who were wrongfully banished')
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def pardon_user(self, ctx, user: discord.User, *, reason="No reason provided."):
        if ctx.author.id == user.id:
            await ctx.send(embed=discord.Embed(color=discord.Color.orange(), description="You need someone else to unban you."))
            return
        for entry in await ctx.guild.bans():
            if entry[1].id == user.id:
                await ctx.guild.unban(user, reason=reason)
                unban_embed = discord.Embed(
                    color=discord.Color.orange(),
                    description=f"Pardoned **{str(user)}**.")
                await ctx.send(embed=unban_embed)
                return

        not_banned_embed = discord.Embed(
            color=discord.Color.orange(),
            description="They haven't been banished before.")
        await ctx.send(embed=not_banned_embed)


def setup(bot):
    bot.add_cog(Admin(bot))
