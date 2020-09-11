import discord
from discord.ext import commands
from discord.utils import get

bot = commands.Bot(command_prefix='!k ')

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        activity = discord.Game(name='Krew.io with emerald', type=3)
        await self.bot.change_presence(status=discord.Status.online, activity=activity)


    @commands.Cog.listener()
    async def on_message(self, message):
        if self.bot.user.mentioned_in(message):
            await message.channel.send(
            embed = discord.Embed(color=discord.Color.orange(), description='`Pls use !k to use a command.`'))
            await bot.process_commands(message)



    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = get(member.guild.channels, name="🚪front-door")
        await channel.send(f"Everyone welcome {member.mention} aboard!")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = get(member.guild.channels, name="🚪front-door")
        await channel.send(f"{member.mention} has abandoned ship.")






def setup(bot):
    bot.add_cog(Events(bot))
